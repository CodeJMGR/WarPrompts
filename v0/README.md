# WarPrompts — V0 (prueba de concepto)

🌐 Dominio oficial del proyecto: [warpromptsgame.com](https://warpromptsgame.com)

Implementación de la V0 descrita en [`03_concepto_del_juego.md`](../03_concepto_del_juego.md) (sección 7):
web, 2D simple, un tipo de unidad, control **únicamente** por prompts a un LLM, 1 jugador (azul) vs bot sencillo (rojo).

Objetivo: validar si la mecánica de "escribir órdenes en lenguaje natural para mover un ejército" es
comprensible, divertida y justa — no busca verse bien ni ser el juego final.

## Cómo se juega

- Escribes una orden en lenguaje natural (máx. 280 caracteres) para tus unidades azules.
- Un LLM (GPT-4o-mini) interpreta la orden y genera comandos de movimiento/ataque para las unidades que menciones.
- Cooldown de 6 segundos entre órdenes.
- El bot rojo juega solo (heurística fija, sin LLM): persigue enemigos cercanos o avanza hacia la zona de control.
- Victoria: 60 puntos de control de zona, eliminar todas las unidades enemigas, o más puntos al llegar a los 5 minutos.

## Arquitectura

```
v0/
  backend/    FastAPI (Python) — estado de partida, loop de simulación, bot, llamada al LLM
  frontend/   HTML + Phaser.js (vía CDN) — tablero, HUD, caja de prompt
```

El backend sirve también los archivos estáticos del frontend, así que solo necesitas correr un proceso.

## Puesta en marcha

1. Backend

   ```bash
   cd v0/backend
   python3 -m venv .venv
   .venv/bin/pip install -r requirements.txt
   cp .env.example .env
   # Edita .env y pon tu clave: OPENAI_API_KEY=sk-...
   .venv/bin/uvicorn app.main:app --reload --port 8420
   ```

2. Abre `http://127.0.0.1:8420` en el navegador. No hace falta levantar el frontend por separado.

## Log de llamadas al LLM

Cada llamado al LLM (éxito o error) se registra como una línea JSON en `v0/logs/llm_calls.jsonl`
(se crea automáticamente, y está excluido de git). Cada entrada incluye: timestamp, equipo, prompt
del jugador, el contenido exacto enviado al modelo, la respuesta cruda, los comandos parseados vs.
los efectivamente aplicados (tras validación), el resumen generado, la latencia en ms, el consumo de
tokens y el error si lo hubo. Útil para depurar interpretaciones raras y medir latencia real.

## Notas de diseño (V0, según el documento)

- Sin potenciadores, sin evolución de unidades, sin zonas de recursos: mecánica de prompts "pura".
- Sin control rápido por click (eso es parte de la versión final, no de esta V0).
- Un único tipo de unidad ("infantería genérica") para ambos equipos.
- Grid fijo 20x12, sin terreno ni obstáculos.

## Qué probar

Las 5 preguntas que la V0 debe responder (ver `03_concepto_del_juego.md`):
comprensibilidad, decisiones interesantes, tolerancia a la latencia del LLM, consistencia de resultados
ante el mismo prompt, y si aparece algún "momento wow". Anota impresiones de partidas reales para decidir
si se avanza a producción (Unity + móvil, según seción 8 del documento).
