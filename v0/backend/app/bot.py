"""IA sencilla del rival (equipo rojo) para la V0. Sin LLM: heurística fija."""
from __future__ import annotations

from .state import GameState, ZONE_X0, ZONE_X1, ZONE_Y0, ZONE_Y1, nearest_enemy

BOT_DECISION_INTERVAL_S = 4.0
CHASE_RANGE = 6.0

_ZONE_SPOTS = [
    ((ZONE_X0 + ZONE_X1) / 2, (ZONE_Y0 + ZONE_Y1) / 2),
    (ZONE_X0, ZONE_Y0),
    (ZONE_X1, ZONE_Y1),
]


def bot_decide(gs: GameState) -> None:
    if gs.status != "playing":
        return

    for i, unit in enumerate(gs.units_by_team("red")):
        enemy = nearest_enemy(gs, unit, within=CHASE_RANGE)
        if enemy is not None:
            unit.target_unit_id = enemy.id
            unit.target_x = unit.target_y = None
            continue

        unit.target_unit_id = None
        spot = _ZONE_SPOTS[i % len(_ZONE_SPOTS)]
        unit.target_x, unit.target_y = spot
