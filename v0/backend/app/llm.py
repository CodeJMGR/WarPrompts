"""Interpretación de prompts en lenguaje natural -> comandos de unidades.

Usa la Structured Outputs de la API de OpenAI (gpt-4o-mini) para forzar
una respuesta JSON con el esquema esperado por el motor del juego.
"""
from __future__ import annotations

import asyncio
import json
import logging
import os
import time
from datetime import datetime, timezone
from pathlib import Path

from openai import AsyncOpenAI, OpenAIError

from .state import GRID_H, GRID_W, GameState, Team

logger = logging.getLogger("warprompts.llm")

MODEL = "gpt-4o-mini"

LOG_DIR = Path(__file__).resolve().parents[2] / "logs"
LOG_FILE = LOG_DIR / "llm_calls.jsonl"
_log_lock = asyncio.Lock()


async def _log_call(entry: dict) -> None:
    """Añade una línea JSON al log de llamadas al LLM (una por llamado)."""
    entry = {"ts": datetime.now(timezone.utc).isoformat(), **entry}
    line = json.dumps(entry, ensure_ascii=False)
    async with _log_lock:
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        with LOG_FILE.open("a", encoding="utf-8") as f:
            f.write(line + "\n")

RESPONSE_SCHEMA = {
    "name": "unit_commands",
    "strict": True,
    "schema": {
        "type": "object",
        "properties": {
            "commands": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "unit_id": {"type": "string"},
                        "action": {"type": "string", "enum": ["move", "attack", "stop"]},
                        "target_x": {"type": ["number", "null"]},
                        "target_y": {"type": ["number", "null"]},
                        "target_unit_id": {"type": ["string", "null"]},
                    },
                    "required": ["unit_id", "action", "target_x", "target_y", "target_unit_id"],
                    "additionalProperties": False,
                },
            },
            "summary": {
                "type": "string",
                "description": "Resumen breve en español de cómo interpretaste la orden.",
            },
        },
        "required": ["commands", "summary"],
        "additionalProperties": False,
    },
}

SYSTEM_PROMPT = f"""Eres el árbitro de movimientos de WarPrompts, un juego de estrategia.
Traduces la orden en lenguaje natural de un jugador en comandos concretos para SUS unidades.

Reglas:
- El grid mide {GRID_W}x{GRID_H} celdas (x: 0-{GRID_W - 1}, y: 0-{GRID_H - 1}).
- Solo puedes dar órdenes a las unidades del equipo del jugador que están listadas.
- Si el jugador no menciona una unidad, no la muevas (no incluyas comando para ella).
- "move": requiere target_x y target_y (coordenadas dentro del grid). target_unit_id debe ser null.
- "attack": requiere target_unit_id (id de una unidad enemiga listada). target_x/target_y deben ser null.
- "stop": no requiere target_x, target_y ni target_unit_id (todos null).
- Si la orden es ambigua, interpreta la intención más razonable; nunca inventes ids de unidades que no existen.
- El campo summary debe describir en una frase corta qué hará el ejército.
"""


class LLMError(Exception):
    pass


def _client() -> AsyncOpenAI:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise LLMError("OPENAI_API_KEY no está configurada en el entorno del backend.")
    return AsyncOpenAI(api_key=api_key)


def _build_user_prompt(gs: GameState, team: Team, prompt: str) -> str:
    own_units = [
        {"id": u.id, "x": round(u.x, 1), "y": round(u.y, 1), "hp": round(u.hp)}
        for u in gs.units_by_team(team)
    ]
    enemy_team: Team = "red" if team == "blue" else "blue"
    enemy_units = [
        {"id": u.id, "x": round(u.x, 1), "y": round(u.y, 1), "hp": round(u.hp)}
        for u in gs.units_by_team(enemy_team)
    ]
    zone = gs.to_dict()["zone"]
    payload = {
        "your_team": team,
        "your_units": own_units,
        "enemy_units": enemy_units,
        "control_zone": zone,
        "order": prompt,
    }
    return json.dumps(payload, ensure_ascii=False)


async def interpret_prompt(gs: GameState, team: Team, prompt: str) -> tuple[list[dict], str]:
    client = _client()
    user_content = _build_user_prompt(gs, team, prompt)
    started = time.monotonic()

    try:
        response = await client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_content},
            ],
            response_format={"type": "json_schema", "json_schema": RESPONSE_SCHEMA},
            temperature=0.2,
            timeout=8.0,
        )
    except OpenAIError as exc:
        logger.warning("Fallo llamada a OpenAI: %s", exc)
        await _log_call(
            {
                "team": team,
                "prompt": prompt,
                "request_user_content": user_content,
                "latency_ms": round((time.monotonic() - started) * 1000, 1),
                "error": str(exc),
            }
        )
        raise LLMError(f"La IA no pudo interpretar la orden ({exc}).") from exc

    latency_ms = round((time.monotonic() - started) * 1000, 1)
    content = response.choices[0].message.content

    try:
        data = json.loads(content)
    except (TypeError, json.JSONDecodeError) as exc:
        await _log_call(
            {
                "team": team,
                "prompt": prompt,
                "request_user_content": user_content,
                "response_raw": content,
                "latency_ms": latency_ms,
                "error": "respuesta con formato inválido",
            }
        )
        raise LLMError("La IA devolvió una respuesta con formato inválido.") from exc

    own_ids = {u.id for u in gs.units_by_team(team)}
    enemy_ids = {u.id for u in gs.units_by_team("red" if team == "blue" else "blue")}
    commands: list[dict] = []
    for cmd in data.get("commands", []):
        if cmd.get("unit_id") not in own_ids:
            continue
        action = cmd.get("action")
        if action == "move":
            tx, ty = cmd.get("target_x"), cmd.get("target_y")
            if tx is None or ty is None:
                continue
            cmd["target_x"] = max(0, min(GRID_W - 1, float(tx)))
            cmd["target_y"] = max(0, min(GRID_H - 1, float(ty)))
        elif action == "attack":
            if cmd.get("target_unit_id") not in enemy_ids:
                continue
        elif action != "stop":
            continue
        commands.append(cmd)

    summary = data.get("summary", "").strip() or "La IA no proporcionó un resumen."

    await _log_call(
        {
            "team": team,
            "prompt": prompt,
            "request_user_content": user_content,
            "response_raw": content,
            "commands_raw": data.get("commands", []),
            "commands_applied": commands,
            "summary": summary,
            "latency_ms": latency_ms,
            "usage": response.usage.model_dump() if response.usage else None,
            "error": None,
        }
    )

    return commands, summary
