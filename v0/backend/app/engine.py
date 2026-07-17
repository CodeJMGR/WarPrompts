"""Loop de simulación: movimiento, combate, control de zona y condiciones de victoria."""
from __future__ import annotations

from .state import (
    ATTACK_RANGE,
    DETECT_RANGE,
    GameState,
    TICK_INTERVAL_S,
    TIME_LIMIT_S,
    UNIT_DPS,
    UNIT_SPEED,
    WIN_SCORE,
    ZONE_POINTS_PER_SEC,
    ZONE_X0,
    ZONE_X1,
    ZONE_Y0,
    ZONE_Y1,
    clamp,
    distance,
    nearest_enemy,
)


def _move_towards(unit, tx: float, ty: float, dt: float) -> None:
    dx, dy = tx - unit.x, ty - unit.y
    dist = (dx**2 + dy**2) ** 0.5
    step = UNIT_SPEED * dt
    if dist <= step or dist == 0:
        unit.x, unit.y = tx, ty
    else:
        unit.x += dx / dist * step
        unit.y += dy / dist * step
    unit.x = clamp(unit.x, 0, 19.99)
    unit.y = clamp(unit.y, 0, 11.99)


def _in_zone(unit) -> bool:
    return ZONE_X0 <= unit.x <= ZONE_X1 and ZONE_Y0 <= unit.y <= ZONE_Y1


def tick(gs: GameState) -> None:
    if gs.status != "playing":
        return

    dt = TICK_INTERVAL_S

    for unit in list(gs.units.values()):
        if not unit.alive:
            continue

        enemy = nearest_enemy(gs, unit, within=ATTACK_RANGE)
        if enemy is None and unit.target_unit_id:
            target = gs.units.get(unit.target_unit_id)
            if target and target.alive:
                enemy = target if distance(unit, target) <= ATTACK_RANGE else None
        if enemy is None:
            auto_engage = nearest_enemy(gs, unit, within=DETECT_RANGE)
            if auto_engage and unit.target_x is None:
                enemy = auto_engage if distance(unit, auto_engage) <= ATTACK_RANGE else None

        if enemy is not None:
            enemy.hp -= UNIT_DPS * dt
            if enemy.hp <= 0:
                enemy.hp = 0
                gs.add_log(unit.team, f"{unit.id} eliminó a {enemy.id}.")
            continue

        # Perseguir unidad objetivo si la tiene asignada
        if unit.target_unit_id:
            target = gs.units.get(unit.target_unit_id)
            if target and target.alive:
                _move_towards(unit, target.x, target.y, dt)
                continue
            else:
                unit.target_unit_id = None

        if unit.target_x is not None and unit.target_y is not None:
            _move_towards(unit, unit.target_x, unit.target_y, dt)
            if abs(unit.x - unit.target_x) < 0.05 and abs(unit.y - unit.target_y) < 0.05:
                unit.target_x = unit.target_y = None

    for dead_id in [uid for uid, u in gs.units.items() if not u.alive]:
        gs.units.pop(dead_id, None)

    blue_in_zone = sum(1 for u in gs.units_by_team("blue") if _in_zone(u))
    red_in_zone = sum(1 for u in gs.units_by_team("red") if _in_zone(u))
    if blue_in_zone > red_in_zone:
        gs.score["blue"] += ZONE_POINTS_PER_SEC * dt
    elif red_in_zone > blue_in_zone:
        gs.score["red"] += ZONE_POINTS_PER_SEC * dt

    _check_victory(gs)


def _check_victory(gs: GameState) -> None:
    blue_alive = bool(gs.units_by_team("blue"))
    red_alive = bool(gs.units_by_team("red"))

    if not blue_alive and not red_alive:
        gs.status = "draw"
    elif not blue_alive:
        gs.status = "red_win"
    elif not red_alive:
        gs.status = "blue_win"
    elif gs.score["blue"] >= WIN_SCORE:
        gs.status = "blue_win"
    elif gs.score["red"] >= WIN_SCORE:
        gs.status = "red_win"
    elif gs.elapsed() >= TIME_LIMIT_S:
        if gs.score["blue"] > gs.score["red"]:
            gs.status = "blue_win"
        elif gs.score["red"] > gs.score["blue"]:
            gs.status = "red_win"
        else:
            gs.status = "draw"

    if gs.status != "playing" and gs.log[-1].text != "Partida terminada.":
        gs.add_log("blue" if gs.status == "blue_win" else "red", "Partida terminada.")
