const CELL = 40;
const POLL_MS = 400;

let scene = null;
let gridDrawn = false;
const unitSprites = {};

const el = (id) => document.getElementById(id);

function statusClass(status) {
  if (status === "blue_win") return "win";
  if (status === "red_win") return "lose";
  if (status === "draw") return "draw";
  return "";
}

function statusText(status) {
  return {
    blue_win: "🔵 ¡Victoria azul!",
    red_win: "🔴 Gana el rival.",
    draw: "Empate.",
  }[status] || "";
}

function formatTime(seconds) {
  const m = Math.floor(seconds / 60);
  const s = Math.floor(seconds % 60);
  return `${m}:${String(s).padStart(2, "0")}`;
}

function ensureGrid(state) {
  if (gridDrawn) return;
  const { w, h } = state.grid;

  const g = scene.add.graphics();
  g.lineStyle(1, 0x2a3550, 1);
  for (let x = 0; x <= w; x++) g.lineBetween(x * CELL, 0, x * CELL, h * CELL);
  for (let y = 0; y <= h; y++) g.lineBetween(0, y * CELL, w * CELL, y * CELL);

  const z = state.zone;
  scene.add
    .rectangle(
      ((z.x0 + z.x1 + 1) / 2) * CELL,
      ((z.y0 + z.y1 + 1) / 2) * CELL,
      (z.x1 - z.x0 + 1) * CELL,
      (z.y1 - z.y0 + 1) * CELL,
      0xf59e0b,
      0.15
    )
    .setStrokeStyle(2, 0xf59e0b, 0.6);

  gridDrawn = true;
}

function syncUnits(state) {
  const seen = new Set();
  for (const u of state.units) {
    seen.add(u.id);
    const px = (u.x + 0.5) * CELL;
    const py = (u.y + 0.5) * CELL;
    const color = u.team === "blue" ? 0x3b82f6 : 0xef4444;

    let obj = unitSprites[u.id];
    if (!obj) {
      const circle = scene.add.circle(px, py, 14, color).setStrokeStyle(2, 0xffffff, 0.8);
      const hpBg = scene.add.rectangle(px, py - 22, 28, 5, 0x000000, 0.5);
      const hpFill = scene.add.rectangle(px - 14, py - 22, 28, 5, 0x22c55e).setOrigin(0, 0.5);
      obj = { circle, hpBg, hpFill };
      unitSprites[u.id] = obj;
    }

    obj.circle.setPosition(px, py);
    obj.hpBg.setPosition(px, py - 22);
    const pct = Math.max(0, u.hp / u.max_hp);
    obj.hpFill.setPosition(px - 14, py - 22);
    obj.hpFill.width = 28 * pct;
    obj.hpFill.fillColor = pct > 0.5 ? 0x22c55e : pct > 0.25 ? 0xf59e0b : 0xef4444;
  }

  for (const id of Object.keys(unitSprites)) {
    if (!seen.has(id)) {
      unitSprites[id].circle.destroy();
      unitSprites[id].hpBg.destroy();
      unitSprites[id].hpFill.destroy();
      delete unitSprites[id];
    }
  }
}

let lastLogTs = 0;
function renderLog(log) {
  const list = el("log-list");
  for (const entry of log) {
    if (entry.ts <= lastLogTs) continue;
    const li = document.createElement("li");
    li.className = entry.team;
    li.textContent = entry.text;
    list.appendChild(li);
  }
  if (log.length) lastLogTs = log[log.length - 1].ts;
  list.scrollTop = list.scrollHeight;
}

function renderHud(state) {
  el("score-blue").textContent = Math.floor(state.score.blue);
  el("score-red").textContent = Math.floor(state.score.red);
  el("timer").textContent = formatTime(Math.max(0, state.time_limit - state.elapsed));

  const banner = el("status-banner");
  if (state.status === "playing") {
    banner.classList.add("hidden");
  } else {
    banner.classList.remove("hidden");
    banner.className = `status-banner ${statusClass(state.status)}`;
    banner.id = "status-banner";
    banner.textContent = statusText(state.status);
  }
}

function renderCooldown(state) {
  const remaining = state.prompt_ready_at - Date.now() / 1000;
  const btn = el("send-btn");
  const fill = el("cooldown-fill");
  const label = el("cooldown-label");

  const gameOver = state.status !== "playing";
  if (remaining > 0 && !gameOver) {
    btn.disabled = true;
    const pct = Math.min(100, (remaining / state.prompt_cooldown_s) * 100);
    fill.style.width = `${pct}%`;
    label.textContent = `Cooldown: ${remaining.toFixed(1)}s`;
  } else {
    btn.disabled = gameOver || sending;
    fill.style.width = "0%";
    label.textContent = gameOver ? "Partida terminada" : "";
  }
}

let latestState = null;

async function pollState() {
  try {
    const res = await fetch("/api/game/state");
    const state = await res.json();
    latestState = state;
    ensureGrid(state);
    syncUnits(state);
    renderHud(state);
    renderLog(state.log);
    renderCooldown(state);
  } catch (err) {
    console.error("Error al obtener el estado:", err);
  }
}

function showError(msg) {
  const p = el("form-error");
  p.textContent = msg;
  p.classList.remove("hidden");
  setTimeout(() => p.classList.add("hidden"), 5000);
}

let sending = false;

async function submitPrompt(evt) {
  evt.preventDefault();
  const input = el("prompt-input");
  const prompt = input.value.trim();
  if (!prompt || sending) return;

  sending = true;
  el("send-btn").disabled = true;

  try {
    const res = await fetch("/api/game/prompt", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt }),
    });
    const data = await res.json();
    if (!res.ok) {
      showError(data.detail || "Error al enviar la orden.");
    } else {
      input.value = "";
      el("char-counter").textContent = "0 / 280";
    }
  } catch (err) {
    showError("No se pudo conectar con el backend.");
  } finally {
    sending = false;
    await pollState();
  }
}

async function newGame() {
  await fetch("/api/game/new", { method: "POST" });
  lastLogTs = 0;
  el("log-list").innerHTML = "";
  await pollState();
}

function initUi() {
  el("prompt-input").addEventListener("input", (e) => {
    el("char-counter").textContent = `${e.target.value.length} / 280`;
  });
  el("prompt-form").addEventListener("submit", submitPrompt);
  el("new-game-btn").addEventListener("click", newGame);
}

const config = {
  type: Phaser.AUTO,
  width: 800,
  height: 480,
  parent: "game-container",
  backgroundColor: "#16213e",
  scene: {
    create() {
      scene = this;
    },
  },
};

new Phaser.Game(config);

initUi();
pollState();
setInterval(pollState, POLL_MS);
setInterval(() => {
  if (latestState) renderCooldown(latestState);
}, 100);
