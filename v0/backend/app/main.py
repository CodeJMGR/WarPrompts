"""FastAPI backend de la V0 de WarPrompts: 1 jugador vs bot, control por prompts."""
from __future__ import annotations

import asyncio
import logging
import time
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from .bot import BOT_DECISION_INTERVAL_S, bot_decide
from .engine import tick
from .llm import LLMError, interpret_prompt
from .state import PROMPT_COOLDOWN_S, PROMPT_MAX_CHARS, TICK_INTERVAL_S, GameState, new_game

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("warprompts")

app = FastAPI(title="WarPrompts V0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

gs: GameState = new_game()
gs_lock = asyncio.Lock()


class PromptRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=PROMPT_MAX_CHARS)


@app.on_event("startup")
async def start_game_loop() -> None:
    asyncio.create_task(_game_loop())


async def _game_loop() -> None:
    time_since_bot_decision = 0.0
    while True:
        await asyncio.sleep(TICK_INTERVAL_S)
        async with gs_lock:
            tick(gs)
            time_since_bot_decision += TICK_INTERVAL_S
            if time_since_bot_decision >= BOT_DECISION_INTERVAL_S:
                bot_decide(gs)
                time_since_bot_decision = 0.0


@app.post("/api/game/new")
async def api_new_game() -> dict:
    global gs
    async with gs_lock:
        gs = new_game()
        return gs.to_dict()


@app.get("/api/game/state")
async def api_state() -> dict:
    async with gs_lock:
        return gs.to_dict()


@app.post("/api/game/prompt")
async def api_prompt(body: PromptRequest) -> dict:
    async with gs_lock:
        if gs.status != "playing":
            raise HTTPException(status_code=409, detail="La partida ya terminó.")
        now = time.time()
        if now < gs.prompt_ready_at:
            raise HTTPException(
                status_code=429,
                detail=f"Cooldown activo, espera {gs.prompt_ready_at - now:.1f}s.",
            )
        state_snapshot = gs

    try:
        commands, summary = await interpret_prompt(state_snapshot, "blue", body.prompt)
    except LLMError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc

    async with gs_lock:
        for cmd in commands:
            unit = gs.units.get(cmd["unit_id"])
            if unit is None:
                continue
            action = cmd["action"]
            if action == "move":
                unit.target_x = cmd["target_x"]
                unit.target_y = cmd["target_y"]
                unit.target_unit_id = None
            elif action == "attack":
                unit.target_unit_id = cmd["target_unit_id"]
                unit.target_x = unit.target_y = None
            elif action == "stop":
                unit.target_x = unit.target_y = None
                unit.target_unit_id = None

        gs.prompt_ready_at = time.time() + PROMPT_COOLDOWN_S
        gs.add_log("blue", f'"{body.prompt}" → {summary}')
        return {"state": gs.to_dict(), "summary": summary, "commands_applied": len(commands)}


frontend_dir = Path(__file__).resolve().parents[2] / "frontend"
if frontend_dir.exists():
    app.mount("/", StaticFiles(directory=str(frontend_dir), html=True), name="frontend")
