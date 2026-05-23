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

---

## 7. Primera Versión de Prueba (V0 — Proof of Concept)

Antes de comprometer recursos en el desarrollo móvil 3D completo, se propone una **versión de prueba mínima** con un único objetivo: validar que la mecánica de control por prompts es divertida, comprensible y justa.

### Filosofía de la V0
> "No importa que se vea bonito. Importa que la mecánica funcione."

La V0 no es el juego. Es el experimento que decide si el juego vale la pena construirse.

### Alcance de la V0

| Elemento | V0 (Prueba) | Versión final |
|---|---|---|
| **Plataforma** | Web (navegador, escritorio) | Móvil iOS/Android |
| **Gráficos** | 2D top-down, formas geométricas simples | 3D semirealista isométrico |
| **Unidades** | 1 tipo (infantería genérica) | 3 tipos con roles distintos |
| **Mapa** | Grid cuadriculado fijo, sin variación de terreno | Mapa 3D con zonas, obstáculos y terreno |
| **LLM** | API cloud (OpenAI/Anthropic vía clave temporal) | Híbrido: on-device + cloud fallback |
| **Modo de juego** | 1 vs IA sencilla (bot con lógica básica) | 1 vs 1 multijugador en tiempo real |
| **Potenciadores** | Ninguno — mecánica pura | Sistema completo de potenciadores |
| **UI** | Caja de texto, botón de enviar, log de acciones | Interfaz móvil completa con HUD |

### Preguntas que debe responder la V0

1. **¿Es la mecánica comprensible?** ¿Un jugador nuevo entiende que escribe un prompt y sus unidades se mueven?
2. **¿Genera decisiones interesantes?** ¿El jugador piensa en cómo redactar, no solo qué hacer?
3. **¿La latencia del LLM arruina el flujo?** ¿3 segundos de espera se sienten aceptables o frustrantes?
4. **¿Es predecible de forma justa?** ¿El mismo prompt produce resultados consistentes o demasiado aleatorios?
5. **¿Hay "momento wow"?** ¿Existe alguna jugada que haga que el jugador quiera contársela a alguien?

### Stack tecnológico sugerido para la V0

- **Frontend:** HTML5 + Canvas o React con una librería 2D ligera (Phaser.js)
- **LLM:** API de OpenAI (GPT-4o-mini) o Anthropic (Claude Haiku) — bajo costo por llamada
- **Backend mínimo:** Node.js o Python (FastAPI) para gestionar las llamadas al LLM y el estado de la partida
- **Tiempo estimado de desarrollo V0:** 3–5 semanas para un desarrollador con experiencia

### Criterio de éxito de la V0
Si al final de una sesión de prueba el jugador pregunta **"¿puedo jugar otra partida?"**, la mecánica está validada y se puede avanzar a producción.

---

## 8. Estudio de Mercado — Plataforma y Tecnologías

### 8.1 El mercado móvil como oportunidad

El mercado global de juegos móviles alcanzó **$143.96 mil millones en 2025** y proyecta crecer a $371.71 mil millones para 2035. Los juegos de estrategia representan solo el **4% de las descargas** pero generan el **21.4% de los ingresos totales** — la audiencia estratégica gasta significativamente más que el promedio.

Los juegos de estrategia más rentables en móvil en 2025:

| Juego | Ingresos 2025 | Género |
|---|---|---|
| Honor of Kings | ~$2.4B | MOBA/Estrategia |
| Last War: Survival | ~$1.5B+ | Estrategia/Supervivencia |
| Whiteout Survival | ~$1.4B | Estrategia/Supervivencia |
| Kingshot | Top 15 mundial | 4X Estrategia (nuevo) |

Esto confirma que **la audiencia dispuesta a pagar existe y es activa en móvil**.

### 8.2 iOS vs Android — ¿Cuál priorizar?

| Métrica | iOS | Android |
|---|---|---|
| Share de descargas | ~30% | ~70% |
| Share de ingresos | **~61–63%** | ~37–39% |
| Gasto promedio por usuario | Más alto | Más bajo |
| Fragmentación de dispositivos | Baja (controlada por Apple) | Alta (miles de modelos) |
| Ciclo de aprobación de app | 1–3 días | Horas |
| Modelo de monetización favorito | IAP + Suscripciones | IAP + Anuncios |

**Recomendación:** Lanzar primero en **iOS**. A pesar de tener menos descargas, genera el doble de ingresos por usuario. La menor fragmentación de hardware también simplifica la optimización del motor 3D y la inferencia del LLM. Android en segunda fase.

### 8.3 Motor de juego — Comparativa

| Motor | Ventajas para WarPrompts | Desventajas | Costo |
|---|---|---|---|
| **Unity** | 70%+ del market share móvil, mejor soporte iOS/Android, enorme ecosistema de assets 3D y plugins de IA, documentación extensa | Cambios de licencia en 2023 generaron controversia; puede ser pesado para indie | Gratis hasta $200K ingresos/año |
| **Godot 4** | Completamente gratuito y open-source, buenas capacidades 3D desde v4, comunidad creciente, ligero | Menor ecosistema de assets 3D, soporte móvil menos maduro que Unity | Gratis (sin royalties) |
| **Unreal Engine 5** | Los mejores gráficos 3D del mercado, Nanite + Lumen para semirealismo impresionante | Muy pesado para móvil, curva de aprendizaje alta, 5% royalties tras $1M | Gratis + 5% royalties |

**Recomendación:** **Unity** para producción final — es el estándar de facto en mobile gaming y tiene el mejor soporte para el stack 3D semirealista en iOS/Android. **Godot** para la V0/prototipo si se prefiere evitar restricciones de licencia durante la fase experimental.

### 8.4 Integración del LLM — Opciones y latencia

Este es el componente más crítico técnicamente. Hay tres arquitecturas posibles:

**Opción A — Cloud API (más sencilla)**
- Usar OpenAI (GPT-4o-mini) o Anthropic (Claude Haiku) vía API REST
- Latencia: 200–800ms según conexión de red
- Costo: ~$0.0001–$0.001 por llamada (muy bajo por partida)
- Ideal para: V0 y fases tempranas de desarrollo
- Riesgo: Requiere conexión a internet; costo escala con usuarios

**Opción B — On-Device LLM (más avanzada)**
- Frameworks: **Cactus SDK** (sub-50ms, cross-platform iOS/Android) o **Google LiteRT** (NPU unificado para Qualcomm/MediaTek/Tensor)
- Latencia: <50ms — prácticamente imperceptible
- Costo: Cero por inferencia tras descarga del modelo
- Modelos compatibles: Gemma 2B/3B, Phi-3 Mini, Llama 3.2 1B/3B
- Riesgo: Requiere dispositivo de gama media-alta; modelo limitado en capacidad

**Opción C — Arquitectura Híbrida (recomendada para producción)**
- On-device para comandos simples y frecuentes (baja latencia)
- Cloud API como fallback para dispositivos sin NPU o comandos complejos
- Detecta automáticamente las capacidades del dispositivo
- Mejor experiencia para todos los segmentos de hardware

### 8.5 Resumen de stack tecnológico recomendado

| Fase | Motor | LLM | Backend | Plataforma |
|---|---|---|---|---|
| **V0 (prueba)** | Phaser.js / HTML5 | OpenAI API (GPT-4o-mini) | Node.js / FastAPI | Web (navegador) |
| **V1 (producción)** | Unity 6 | Cactus SDK + Cloud fallback | Node.js + WebSocket | iOS primero, Android después |

---

### Fuentes

- [Best Game Engines Mobile 2026 — Sunstrike Studios](https://sunstrikestudios.com/en/blog/the_best_mobile_game_engines_in_2025/)
- [Unity vs Unreal vs Godot 2025 — DEV Community](https://dev.to/philipjohnbasile/unity-vs-unreal-vs-godot-finding-your-perfect-game-engine-in-2025-4ecg)
- [Mobile Gaming Market Size 2035 — Precedence Research](https://www.precedenceresearch.com/mobile-gaming-market)
- [Top Grossing Mobile Games 2025 — MobileGamer.biz](https://mobilegamer.biz/the-top-grossing-mobile-games-of-2025/)
- [200+ Mobile Gaming Statistics 2026 — Udonis](https://www.blog.udonis.co/mobile-marketing/mobile-games/mobile-gaming-statistics)
- [Cactus SDK On-Device LLM — InfoQ](https://www.infoq.com/news/2025/12/cactus-on-device-inference/)
- [LLM Integration in Mobile Apps — Studio Ubique](https://www.studioubique.com/llm-integration-in-mobile-app/)
- [Building LLM Games — GladeCore](https://www.gladecore.com/blog/llms-in-games)
- [On-Device LLMs State of the Union 2026](https://v-chandra.github.io/on-device-llms/)
