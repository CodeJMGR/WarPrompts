# WarPrompts — Concepto del Juego

> **Fase 2: Definición de los elementos principales**

---

## 1. Género

**Estrategia en tiempo real (RTS) competitivo 1 vs 1**

WarPrompts toma la estructura del RTS clásico — dos jugadores, un mapa, unidades en conflicto — pero reemplaza el control tradicional (clics, atajos de teclado) por **prompts de lenguaje natural enviados a un LLM**. El resultado es un género nuevo: RTS donde la habilidad del jugador se mide por su capacidad de comunicarse con una IA, no por su velocidad de mouse.

---

## 2. Plataforma

**📱 Móvil (iOS / Android) — Plataforma principal**

La decisión de priorizar móvil define toda la experiencia de diseño:

- **Interfaz táctil:** La caja de texto para escribir el prompt es nativa en móvil — el teclado virtual es el "controlador" del juego.
- **Sesiones cortas:** Las partidas deben diseñarse para completarse en 10–20 minutos, adecuadas al uso en movilidad.
- **Distribución:** App Store y Google Play como canales principales. Sin fricción de instalación para el jugador casual.
- **Viral por naturaleza:** Los jugadores pueden compartir sus prompts y jugadas directamente desde el dispositivo.

### Consideraciones técnicas para móvil
| Aspecto | Implicación |
|---|---|
| Latencia del LLM | Las respuestas deben llegar en <3 segundos para no romper el ritmo; se requiere optimización de API o modelo local |
| Pantalla pequeña | El mapa debe ser legible en 6"–7", con cámara rotable e zoom |
| Batería y datos | Minimizar llamadas al LLM; agrupar comandos cuando sea posible |
| Controles táctiles | Zoom con dos dedos, cámara arrastrable, UI con botones grandes |

---

## 3. Estilo Visual

**🎨 3D Semirealista**

WarPrompts apuesta por un look 3D con proporciones ligeramente estilizadas — cercano al realismo pero con suficiente carácter artístico para diferenciarse de simuladores militares genéricos.

### Referencias visuales de referencia
- **Clash of Clans / Clash Royale** — Vista isométrica 3D, unidades con personalidad clara, legibles en pantalla pequeña
- **Total War Mobile** — Mapas 3D con vegetación y terreno variado, ejércitos reconocibles
- **Into the Breach** (adaptado a 3D) — Claridad táctica visual, cada unidad ocupa un espacio definido en el mapa

### Elementos visuales clave
- **Mapa:** Terreno 3D con zonas diferenciadas (bosques, colinas, ríos, ciudades) desde vista aérea levemente inclinada (ángulo isométrico ~45°)
- **Unidades:** Modelos 3D con proporciones ligeramente heroicas — reconocibles de un vistazo desde arriba
- **Indicadores de prompt:** Cuando una unidad recibe una orden, aparece brevemente una burbuja de texto o ícono sobre ella para dar feedback visual
- **Paleta:** Dos equipos con colores claramente diferenciados (ej. azul vs rojo), con el mapa en tonos neutros verdes/grises
- **UI del prompt:** Caja de texto limpia en la parte inferior de la pantalla, con contador de caracteres visible

---

## 4. Mecánicas Principales

### 4.1 Sistema de Prompt como Control
El corazón del juego. El jugador escribe en lenguaje natural qué quiere que hagan sus unidades y lo envía al LLM:

```
"Mueve la infantería hacia el norte y rodea la colina por la izquierda.
 Que los arqueros cubran desde atrás."
```

El LLM interpreta la intención y traduce el texto en acciones concretas para las unidades (waypoints, objetivos de ataque, formaciones). La calidad de la interpretación depende de la claridad del prompt — los jugadores aprenden implícitamente a comunicarse mejor.

**Modo tiempo real libre:** El jugador puede enviar prompts en cualquier momento. No hay "turno" formal — las unidades ejecutan la última instrucción recibida mientras el juego avanza. Esto crea tensión: ¿mando otra orden ahora o dejo que la anterior se ejecute?

### 4.2 Tipos de Unidades
Tres categorías base con roles distintos:

| Unidad | Rol | Fortaleza | Debilidad |
|---|---|---|---|
| **Infantería** | Combate cuerpo a cuerpo, captura de zonas | Alta vida, buen en terreno urbano | Lenta, vulnerable a proyectiles |
| **Arqueros / Tiradores** | Daño a distancia, cobertura | Alto alcance, bajo costo | Frágiles en combate directo |
| **Caballería / Vehículos** | Movilidad y flanqueo | Muy rápida, alto impacto | Cara, difícil de controlar con precisión |

Cada tipo responde de forma diferente a la misma instrucción — "avanza" en infantería es lento y en caballería es una carga.

### 4.3 Control del Mapa
El mapa está dividido en **zonas** (aldeas, colinas, cruces de caminos). Controlar zonas genera puntos de territorio con el tiempo. Ganar por:
- **Dominio:** Tener más puntos de territorio acumulados al finalizar el tiempo
- **Eliminación:** Destruir todas las unidades enemigas

### 4.4 Sistema de Potenciadores
Se desbloquean al cumplir objetivos durante la partida:

| Potenciador | Cómo se gana | Efecto |
|---|---|---|
| 🔡 **Prompt extendido** | Controlar 3 zonas simultáneamente | +150 caracteres al límite del prompt |
| 🔍 **Espionaje** | Destruir una unidad de exploración enemiga | Ver el próximo prompt del rival sin que lo sepa |
| ⏳ **Reintento** | Defender una zona por 2 minutos seguidos | Reenviar el último prompt con resultado diferente |
| 🛡️ **Escudo de prompt** | Eliminar 5 unidades enemigas | El enemigo no puede espiarte durante 60 segundos |

### 4.5 Limitaciones del Prompt (Equilibrio)
Para mantener el juego balanceado, el prompt tiene restricciones iniciales:
- **Límite de caracteres:** 280 caracteres por defecto (ampliable con potenciadores)
- **Cooldown:** Mínimo 5 segundos entre prompts para evitar spam
- **Idioma libre:** El jugador puede escribir en cualquier idioma — el LLM lo interpreta igualmente

---

## 5. Resumen de Concepto

| Elemento | Definición |
|---|---|
| **Género** | RTS competitivo 1 vs 1 |
| **Plataforma** | Móvil (iOS / Android) |
| **Estilo visual** | 3D semirealista, vista isométrica |
| **Control** | Prompts de lenguaje natural → LLM → unidades |
| **Ritmo** | Tiempo real libre con cooldown de prompt |
| **Victoria** | Dominio del mapa o eliminación del ejército rival |
| **Diferenciador** | El prompt engineering es la habilidad del jugador |

---

## 6. Nota sobre complejidad técnica

La combinación **móvil + 3D + tiempo real + LLM** es ambiciosa para un proyecto indie. Se recomienda:

1. **Prototipo en 2D / web primero** para validar que la mecánica de prompts es divertida antes de invertir en el arte 3D y la optimización móvil.
2. **Evaluar modelos LLM locales** (ej. Gemma, Phi-3) para reducir latencia y costo por partida en dispositivos móviles modernos.
3. El arte 3D puede desarrollarse en paralelo al prototipo funcional.

---

*Documento creado: Fase 2 — Concepto del Juego*
*Siguiente paso: Fase 3 — Game Design Document (GDD)*
