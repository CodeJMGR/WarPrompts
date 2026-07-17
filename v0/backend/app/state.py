"""Estado de la partida para la V0 de WarPrompts.

Grid simple, un tipo de unidad, una zona de control central.
Ver 03_concepto_del_juego.md sección 7 para el alcance de esta V0.
"""
from __future__ import annotations

import math
import time
import uuid
from dataclasses import dataclass, field
from typing import Literal

Team = Literal["blue", "red"]

GRID_W = 20
GRID_H = 12

ZONE_X0, ZONE_X1 = 8, 11
ZONE_Y0, ZONE_Y1 = 4, 7

UNIT_MAX_HP = 100
UNIT_SPEED = 3.0  # celdas por segundo
UNIT_DPS = 18.0  # daño por segundo cuando ataca
ATTACK_RANGE = 1.5  # celdas (permite adyacencia diagonal)
DETECT_RANGE = 3.0  # celdas: distancia a la que una unidad se defiende sola

PROMPT_COOLDOWN_S = 6.0
PROMPT_MAX_CHARS = 280

WIN_SCORE = 60.0
ZONE_POINTS_PER_SEC = 1.0
TIME_LIMIT_S = 5 * 60.0

TICK_INTERVAL_S = 0.2


@dataclass
class Unit:
    id: str
    team: Team
    x: float
    y: float
    hp: float = UNIT_MAX_HP
    target_x: float | None = None
    target_y: float | None = None
    target_unit_id: str | None = None

    @property
    def alive(self) -> bool:
        return self.hp > 0

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "team": self.team,
            "x": round(self.x, 2),
            "y": round(self.y, 2),
            "hp": round(self.hp, 1),
            "max_hp": UNIT_MAX_HP,
        }


@dataclass
class LogEntry:
    ts: float
    team: Team
    text: str

    def to_dict(self) -> dict:
        return {"ts": self.ts, "team": self.team, "text": self.text}


@dataclass
class GameState:
    units: dict[str, Unit] = field(default_factory=dict)
    score: dict[str, float] = field(default_factory=lambda: {"blue": 0.0, "red": 0.0})
    started_at: float = field(default_factory=time.time)
    status: str = "playing"  # playing | blue_win | red_win | draw
    log: list[LogEntry] = field(default_factory=list)
    prompt_ready_at: float = 0.0
    lock_reason: str | None = None

    def add_log(self, team: Team, text: str) -> None:
        self.log.append(LogEntry(ts=time.time(), team=team, text=text))
        self.log = self.log[-30:]

    def elapsed(self) -> float:
        return time.time() - self.started_at

    def units_by_team(self, team: Team) -> list[Unit]:
        return [u for u in self.units.values() if u.team == team and u.alive]

    def to_dict(self) -> dict:
        return {
            "units": [u.to_dict() for u in self.units.values() if u.alive],
            "score": self.score,
            "elapsed": round(self.elapsed(), 1),
            "time_limit": TIME_LIMIT_S,
            "win_score": WIN_SCORE,
            "status": self.status,
            "log": [e.to_dict() for e in self.log[-15:]],
            "prompt_ready_at": self.prompt_ready_at,
            "prompt_cooldown_s": PROMPT_COOLDOWN_S,
            "prompt_max_chars": PROMPT_MAX_CHARS,
            "zone": {"x0": ZONE_X0, "x1": ZONE_X1, "y0": ZONE_Y0, "y1": ZONE_Y1},
            "grid": {"w": GRID_W, "h": GRID_H},
        }


def new_game() -> GameState:
    gs = GameState()
    blue_ys = [3, 6, 9]
    red_ys = [3, 6, 9]
    for i, y in enumerate(blue_ys):
        uid = f"blue-{i + 1}"
        gs.units[uid] = Unit(id=uid, team="blue", x=1.0, y=float(y))
    for i, y in enumerate(red_ys):
        uid = f"red-{i + 1}"
        gs.units[uid] = Unit(id=uid, team="red", x=GRID_W - 2.0, y=float(y))
    gs.add_log("blue", "Partida iniciada.")
    return gs


def distance(a: Unit, b: Unit) -> float:
    return math.hypot(a.x - b.x, a.y - b.y)


def nearest_enemy(gs: GameState, unit: Unit, within: float | None = None) -> Unit | None:
    enemy_team: Team = "red" if unit.team == "blue" else "blue"
    best: Unit | None = None
    best_d = math.inf
    for other in gs.units_by_team(enemy_team):
        d = distance(unit, other)
        if d < best_d and (within is None or d <= within):
            best_d = d
            best = other
    return best


def clamp(value: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, value))


def new_id(team: Team) -> str:
    return f"{team}-{uuid.uuid4().hex[:6]}"
