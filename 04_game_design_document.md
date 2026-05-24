# WarPrompts — Game Design Document (GDD)

> **Fase 3: Documento de diseño del juego**
> Versión 3.0 — Expansión: jerarquía Era→Civilización→Personajes, 9 categorías, Unidad Especial, estructuras de Obrero actualizadas

---

## 1. Historia y Narrativa

### 1.1 Contexto del mundo

En un futuro cercano, los conflictos militares ya no se deciden en el campo de batalla con fuerza bruta — se deciden con **inteligencia artificial**. Las potencias del mundo han desarrollado sistemas de IA capaces de comandar ejércitos enteros, con un límite crítico: la IA solo puede actuar sobre las instrucciones que recibe de su comandante humano.

El giro que nadie anticipó: la IA no solo puede coordinar ejércitos modernos. Puede interpretar, resucitar y desplegar **guerreros de cualquier era de la historia humana** — proyecciones tácticas reconstruidas a partir de los registros del pasado. En WarPrompts, un Legionario Romano puede pelear junto a un Sniper de la Segunda Guerra Mundial, y ambos obedecen al mismo comandante.

Quien mejor sepa comunicarse con su IA, gana la guerra. Y la historia completa de la humanidad es su arsenal.

### 1.2 Premisa narrativa

> *"Las armas más poderosas del mundo ahora son las palabras."*

WarPrompts se ambienta en un mundo donde cualquier comandante puede ensamblar un ejército a través del tiempo. La habilidad no está en el armamento — está en la inteligencia del comandante para construir el equipo correcto, posicionarlo con precisión y comunicar sus órdenes bajo presión.

El jugador asume el rol de un **Comandante de Voz** — el operativo humano que traduce la estrategia en órdenes para su IA de combate. Cada partida es irrepetible: los guerreros que llevas, el mapa que te toca, las decisiones que tomas.

### 1.3 Campaña de introducción

El modo campaña actúa como tutorial progresivo, no como historia lineal extensa. Consta de **6 misiones** que enseñan al jugador las mecánicas esenciales a través de situaciones narrativas:

| Misión | Mecánica enseñada | Contexto narrativo |
|---|---|---|
| 1 | Movimiento básico y control simple | Primer despliegue — zona de entrenamiento simulada |
| 2 | Combate y categorías de unidades | Primera escaramuza real con unidades de diferentes tipos |
| 3 | Control de zonas y recursos | Disputa por un nodo estratégico con Obreros |
| 4 | Prompts complejos (múltiples unidades) | Operación de flanqueo usando varias categorías a la vez |
| 5 | Evolución y sistema de potenciadores | Misión de alto riesgo: llevar unidades a nivel Legendario |
| 6 | Partida completa sin guía | Batalla decisiva — el jugador aplica todo lo aprendido |

Al completar la campaña, el jugador desbloquea el **modo competitivo** y recibe el título de *Comandante Certificado*.

---

## 2. Sistema de Personajes

### 2.1 Filosofía del sistema

WarPrompts no tiene facciones predefinidas. En su lugar, el jugador construye su propio ejército eligiendo personajes de su **colección personal**. El universo del juego se organiza en una jerarquía de tres niveles:

```
ERA (período histórico)
  └── CIVILIZACIÓN / TEMA (cultura o facción dentro de esa era)
         └── PERSONAJE / MÁQUINA (un guerrero por cada categoría táctica)
```

Cada jugador desarrolla su colección con el tiempo y diseña estrategias únicas para cada partida. No hay dos comandantes con el mismo ejército.

### 2.2 Categorías de personajes (9)

Todo personaje del juego pertenece a exactamente **una categoría táctica**. Existen **9 categorías estándar**. Cada categoría existe en todas las civilizaciones, adaptada al período y cultura correspondiente:

| Categoría | Rol | Característica principal |
|---|---|---|
| 🛡️ **Tanque** | Absorbe daño, ancla la línea frontal | Alta vida, lento, resistente a AOE |
| 🏹 **Distancia** | Daño sostenido desde lejos | Alto alcance, frágil, ideal en terreno elevado |
| 🗡️ **Asesino** | Elimina unidades prioritarias | Velocidad máxima, muy frágil, especializado en targets únicos |
| 🔮 **Mago** | Habilidades especiales y control de zona | Efectos AOE, control de estado, impredecible |
| ⚒️ **Obrero** | Economía y construcción | Recolecta recursos, construye estructuras de apoyo |
| 🔭 **Explorador** | Inteligencia y sigilo | Revela el mapa, difícil de detectar, no apto para combate directo |
| 🏇 **Caballería** | Alta movilidad y flanqueo | Velocidad elevada, daño de impacto, frágil en combate estático |
| 💣 **Artillería** | Daño masivo de área | Alcance extremo, lento o inmóvil al disparar, devastador en zonas abiertas |
| 💚 **Soporte** | Cura aliados y potencia el equipo | No combate directamente, multiplica la efectividad del equipo |

### 2.3 Eras y Civilizaciones

El universo del juego está organizado en **eras**. Dentro de cada era existen varias **civilizaciones o temas**, cada una con su paquete completo de 9 personajes (uno por categoría) y su propio **mapa**.

**4 eras en el lanzamiento, 3 civilizaciones cada una = 12 paquetes = 108 personajes base.**
Nuevas civilizaciones y eras se añaden como contenido live service (aprox. cada 6–8 semanas).

---

#### 🏛️ ERA ANTIGUA *(3000 a.C. – 500 d.C.)*

---

**Civilización: Imperio Romano**

*Disciplina militar, formaciones, ingeniería de campaña.*

| Categoría | Personaje | Descripción |
|---|---|---|
| 🛡️ Tanque | **Legionario** | Infantería pesada romana. Escudo testudo, gladius. Alta resistencia en formación. |
| 🏹 Distancia | **Velite** | Explorador ligero con jabalinas. Dispara y retrocede antes del combate cuerpo a cuerpo. |
| 🗡️ Asesino | **Gladiador** | Combatiente de arena. Elimina un objetivo y desaparece antes del contraataque. |
| 🔮 Mago | **Augur** | Sacerdote militar. Sus "presagios" otorgan visión del cuadrante enemigo y generan confusión táctica. |
| ⚒️ Obrero | **Ingeniero Romano** | Construye fortines y torres con velocidad excepcional. |
| 🔭 Explorador | **Explorador de Vanguardia** | Reconocimiento ligero. Invisible en terreno abierto. |
| 🏇 Caballería | **Caballería Romana** | Jinete de asalto. Rompe líneas enemigas con carga frontal. |
| 💣 Artillería | **Balista** | Catapulta de torsión. Daño masivo a distancia, inmóvil al disparar. |
| 💚 Soporte | **Médico de Legión** | Cura unidades cercanas; reduce el tiempo de recuperación tras recibir daño. |

*Mapa: **Coliseo del Imperio** — ruinas romanas, zonas de arena que aceleran unidades ligeras. Recurso del mapa: **Oro**.*
*Unidad Especial: ver Sección 2.5*

---

**Civilización: Egipto del Faraón**

*Misterio, monumentos, poderes del más allá.*

| Categoría | Personaje | Descripción |
|---|---|---|
| 🛡️ Tanque | **Guardián del Faraón** | Guerrero élite con escudo de bronce y khopesh. Protege a unidades adyacentes. |
| 🏹 Distancia | **Arquero del Nilo** | Arquero de élite entrenado desde la infancia. Alta cadencia de disparo. |
| 🗡️ Asesino | **Sacerdote de Anubis** | Mata en silencio. Invisible en zonas de sombra y arena. |
| 🔮 Mago | **Hechicero del Faraón** | Lanza maldiciones que reducen las estadísticas enemigas temporalmente. |
| ⚒️ Obrero | **Constructor de Pirámides** | Levanta estructuras masivas con alta resistencia. Sus construcciones duran el doble. |
| 🔭 Explorador | **Mensajero del Desierto** | Se mueve entre dunas sin ser detectado. Cubre grandes distancias. |
| 🏇 Caballería | **Carro de Guerra** | Carro tirado por dos caballos. Atropella unidades ligeras sin detenerse. |
| 💣 Artillería | **Catapulta Egipcia** | Lanza bloques de roca. Destruye estructuras enemigas eficientemente. |
| 💚 Soporte | **Sanador del Templo** | Cura mediante rituales. Lento pero cura múltiples unidades simultáneamente. |

*Mapa: **Valle del Nilo** — dunas que ralentizan, oasis con recursos concentrados. Recurso del mapa: **Oro**.*

---

**Civilización: Esparta**

*Combate feroz, resistencia extrema, sacrificio.*

| Categoría | Personaje | Descripción |
|---|---|---|
| 🛡️ Tanque | **Hoplita** | Guerrero espartano con aspis y doru. Cuando está al 20% de vida, gana +30% de daño. |
| 🏹 Distancia | **Arquero Helénico** | Arquero griego. Efectivo en colinas y formaciones defensivas. |
| 🗡️ Asesino | **Krypteia** | Espía espartano entrenado desde adolescente. Emboscadas devastadoras. |
| 🔮 Mago | **Oráculo de Delfos** | Predice y revela la zona donde el rival enviará su próxima unidad. |
| ⚒️ Obrero | **Esclavo Helota** | Trabaja más rápido que otros Obreros pero tiene menos vida. |
| 🔭 Explorador | **Perieco Rastreador** | Explorador de territorios fronterizos. Detecta emboscadas antes de que ocurran. |
| 🏇 Caballería | **Caballería Griega** | Jinetes espartanos de élite. Flanqueo rápido en terreno abierto. |
| 💣 Artillería | **Onagro** | Catapulta de contrapeso. Destruye agrupaciones de unidades enemigas. |
| 💚 Soporte | **Médico de Campo Griego** | Cura heridas en combate. Su presencia reduce la retirada de unidades dañadas. |

*Mapa: **Las Termópilas** — desfiladero estrecho, puntos de control en pasos de montaña. Recurso del mapa: **Hierro**.*

---

#### ⚔️ ERA MEDIEVAL *(500 – 1500 d.C.)*

---

**Civilización: Cruzados Europeos**

*Fe, armadura pesada, asedio de fortalezas.*

| Categoría | Personaje | Descripción |
|---|---|---|
| 🛡️ Tanque | **Caballero Templario** | Armadura completa, maza de guerra. La unidad más resistente de esta era. |
| 🏹 Distancia | **Arquero de Arco Largo** | Alcance superior en colinas. Puede disparar en arco por encima de obstáculos. |
| 🗡️ Asesino | **Asesino de Gremio** | Se oculta entre estructuras. Emboscada con daga envenenada. |
| 🔮 Mago | **Alquimista** | Proyectiles de fuego griego. Ralentiza zonas del mapa con humo. |
| ⚒️ Obrero | **Artesano de Asedio** | Construye torres de asedio y balistas de campaña. |
| 🔭 Explorador | **Heraldo** | Mensajero veloz a caballo. Revela el cuadrante enemigo y reduce el cooldown de prompt por 2 seg. |
| 🏇 Caballería | **Caballero a Caballo** | Carga devastadora. En terreno abierto, el primero en atacar inflige el doble de daño. |
| 💣 Artillería | **Trebuchet** | Catapulta de contrapeso. Mayor alcance del juego en esta era. |
| 💚 Soporte | **Fraile Médico** | Cura mediante hierbas. Aumenta la vida máxima de unidades adyacentes. |

*Mapa: **Tierra de Feudos** — castillos en los extremos, bosques centrales con cobertura. Recurso del mapa: **Madera**.*

---

**Civilización: Japón Feudal**

*Sigilo, honor, precisión milimétrica.*

| Categoría | Personaje | Descripción |
|---|---|---|
| 🛡️ Tanque | **Samurái** | Armadura Ō-yoroi. Equilibrio entre daño y resistencia. Contraataca automáticamente cuando recibe daño. |
| 🏹 Distancia | **Arquero Yumi** | Arquero a caballo. Dispara en movimiento sin penalización de precisión. |
| 🗡️ Asesino | **Shinobi** | Invisible en zonas de bosque y sombra. Mata en un golpe a unidades dañadas. |
| 🔮 Mago | **Monje Onmyoji** | Invoca sellos que bloquean el avance de unidades enemigas. |
| ⚒️ Obrero | **Constructor de Castillo** | Sus estructuras defensivas duran el doble. Puede reparar construcciones aliadas. |
| 🔭 Explorador | **Kunoichi** | Espía infiltrada. Puede moverse entre unidades enemigas sin ser detectada brevemente. |
| 🏇 Caballería | **Samurái a Caballo** | Jinete de élite. Carga en línea recta ignorando el terreno. |
| 💣 Artillería | **Fusilero Teppo** | Arcabuz primitivo. Perfora armaduras. Alto daño, recarga lenta. |
| 💚 Soporte | **Monje Zen** | Ralentiza el consumo de recursos aliados. Reduce el daño recibido por unidades cercanas en 15%. |

*Mapa: **Santuario de las Tres Colinas** — cerezos que bloquean la visión, ríos que ralentizan unidades pesadas. Recurso del mapa: **Madera**.*

---

**Civilización: Imperio Otomano**

*Expansión territorial, diplomacia, pólvora temprana.*

| Categoría | Personaje | Descripción |
|---|---|---|
| 🛡️ Tanque | **Jenízaro** | Infantería élite del sultán. Alta disciplina, no huye ante bajas enemigas. |
| 🏹 Distancia | **Arquero Sipahi** | Arquero a caballo ligero. Cubre grandes distancias mientras dispara. |
| 🗡️ Asesino | **Agente del Diván** | Espía otomano. Puede disfrazarse de unidad neutral durante 8 segundos. |
| 🔮 Mago | **Visir de Batalla** | Coordina tropas con órdenes estratégicas. Reduce el cooldown de prompt en 2 seg para todas las unidades. |
| ⚒️ Obrero | **Ingeniero de Asedio** | Especialista en cañones y torres. Sus Extractores generan recursos un 20% más rápido. |
| 🔭 Explorador | **Explorador de Akıncı** | Caballería ligera de reconocimiento. Mapea rápidamente zonas enemigas. |
| 🏇 Caballería | **Sipahi de Línea** | Caballería pesada otomana. Rompe formaciones enemigas con carga coordinada. |
| 💣 Artillería | **Cañón Otomano** | Primer uso masivo de pólvora en el juego. Destruye estructuras enemigas con un disparo. |
| 💚 Soporte | **Médico de Campaña Otomano** | Cura en la línea de combate. Puede curar mientras se mueve. |

*Mapa: **Murallas de Constantinopla** — muros que delimitan zonas, puertas como puntos de control críticos. Recurso del mapa: **Hierro**.*

---

#### 💣 ERA INDUSTRIAL *(1850 – 1945)*

---

**Civilización: Segunda Guerra Mundial**

*Coordinación táctica, tecnología de masas, fuego combinado.*

| Categoría | Personaje | Descripción |
|---|---|---|
| 🛡️ Tanque | **Soldado de Trinchera** | Infantería blindada. Efectivo en zonas urbanas y trincheras. |
| 🏹 Distancia | **Francotirador** | Alcance máximo de su era. Inmóvil al disparar; si se mueve, pierde precisión por 3 seg. |
| 🗡️ Asesino | **Espía de Guerra** | Se disfraza de unidad neutral. Sabotea estructuras enemigas desde dentro. |
| 🔮 Mago | **Operador de Radio** | Coordina ataques de artillería a distancia. Llama refuerzos de zona con demora. |
| ⚒️ Obrero | **Ingeniero de Campo** | Instala búnkeres y torretas. Sus estructuras pueden ser reparadas bajo fuego. |
| 🔭 Explorador | **Aviador de Reconocimiento** | Sobrevolada que revela todo el mapa durante 15 segundos. |
| 🏇 Caballería | **Motociclista de Asalto** | Alta velocidad. Ideal para capturar zonas distantes rápidamente. |
| 💣 Artillería | **Cañón Howitzer** | Bombardeo de área con alta demora. Daño masivo y destruye estructuras. |
| 💚 Soporte | **Enfermero de Combate** | Cura heridos críticos instantáneamente. Solo puede curar 1 unidad a la vez. |

*Mapa: **Campo de Batalla Europeo** — trincheras como cobertura, zonas de bombardeo aleatorio. Recurso del mapa: **Carbón**.*

---

**Civilización: Era Victoriana / Steampunk**

*Ingenio mecánico, vapor, inventos inéditos.*

| Categoría | Personaje | Descripción |
|---|---|---|
| 🛡️ Tanque | **Guardia de Hierro** | Soldado con armadura de vapor. Lento pero prácticamente imparable en línea recta. |
| 🏹 Distancia | **Tirador de Émbolo** | Rifle de precisión de repetición. Alta cadencia para su época. |
| 🗡️ Asesino | **Ladrón de Guante Blanco** | Especialista en sabotaje. Roba recursos del rival en lugar de matar. |
| 🔮 Mago | **Inventor Loco** | Despliega artilugios experimentales: minas de vapor, granadas de gas, señuelos mecánicos. |
| ⚒️ Obrero | **Mecánico de Campo** | Repara estructuras y unidades mecánicas. Puede mejorar una Torre Vigía a versión blindada. |
| 🔭 Explorador | **Piloto de Globo** | Reconocimiento aéreo. No puede ser atacado por unidades terrestres. |
| 🏇 Caballería | **Jinete de Velocípedo** | Bicicleta de asalto blindada. Más silenciosa que caballería tradicional — no activa exploración enemiga. |
| 💣 Artillería | **Cañón de Vapor** | Disparo potenciado a vapor. Alcance variable controlable por el jugador. |
| 💚 Soporte | **Médico Victoriano** | Usa instrumental quirúrgico avanzado. Puede curar a distancia con una "pistola de suero". |

*Mapa: **Ciudad Industrial Humeante** — fábricas que generan niebla, vías de tren como corredores de movimiento rápido. Recurso del mapa: **Carbón**.*

---

**Civilización: Revolución / Guerrilla**

*Pocos recursos, máxima movilidad, astucia sobre fuerza.*

| Categoría | Personaje | Descripción |
|---|---|---|
| 🛡️ Tanque | **Miliciano Resistente** | Poca armadura pero se regenera lentamente en zonas de bosque. |
| 🏹 Distancia | **Francotirador Guerrillero** | Activo solo en zonas de bosque y colina. Invisible mientras no dispara. |
| 🗡️ Asesino | **Saboteador** | Destruye estructuras enemigas con explosivos. No combate unidades directamente. |
| 🔮 Mago | **Propagandista** | Reduce la moral enemiga: las unidades rivales atacadas reducen su daño un 20% por 10 seg. |
| ⚒️ Obrero | **Campesino Organizado** | Recolecta recursos el doble de rápido pero no puede construir estructuras defensivas. |
| 🔭 Explorador | **Mensajero Clandestino** | Transmite información de posiciones enemigas al instante. Revela las unidades detrás de estructuras. |
| 🏇 Caballería | **Jinete de Emboscada** | Aparece desde zonas de bosque con daño 2× si el enemigo no lo detectó previamente. |
| 💣 Artillería | **Morterete de Campaña** | Ligero y portátil. Puede moverse entre disparos con penalización de precisión. |
| 💚 Soporte | **Enfermera de Campo** | Cura usando recursos disponibles. Sin recursos, no puede curar — mecánica de escasez. |

*Mapa: **Bosques de la Resistencia** — denso follaje, caminos estrechos, cuevas como puntos de ocultamiento. Recurso del mapa: **Madera**.*

---

#### 🤖 ERA FUTURA *(2100+)*

---

**Civilización: Mechs Corporativos**

*Fuerza bruta, armadura masiva, superioridad tecnológica aplastante.*

| Categoría | Personaje | Descripción |
|---|---|---|
| 🛡️ Tanque | **Mech de Combate** | Androide de guerra pesado. Inmune a efectos de estado. |
| 🏹 Distancia | **Francotirador Láser** | Daño instantáneo a distancia máxima. Sin caída de proyectil ni curva balística. |
| 🗡️ Asesino | **Infiltrador Nano** | Se vuelve invisible durante 5 seg entre ataques. Mata instantáneamente a unidades bajo 20% de vida. |
| 🔮 Mago | **IA de Combate** | Analiza patrones de prompts. Predice con 30% de precisión la próxima acción enemiga y contraataca. |
| ⚒️ Obrero | **Ingeniero Nano** | Construye estructuras instantáneamente usando nanobots. Sus construcciones se reparan solas (lentamente). |
| 🔭 Explorador | **Dron de Enjambre** | Red de microdrones. Cubre todo el mapa simultáneamente pero es vulnerable a ataques de área. |
| 🏇 Caballería | **Moto de Combate** | Hoverbike que ignora el terreno. Puede atravesar zonas de bosque sin penalización. |
| 💣 Artillería | **Lanzador Orbital** | Solicita un strike orbital con 20 segundos de demora. El impacto más poderoso del juego. |
| 💚 Soporte | **Nano-Médico** | Inyecta nanobots que regeneran vida de forma continua por 30 segundos. |

*Mapa: **Metrópolis Fracturada** — plataformas flotantes, zonas de energía que potencian mechs. Recurso del mapa: **Nano-cristales**.*

---

**Civilización: Hackers / Resistencia**

*Sabotaje digital, guerrilla tecnológica, información como arma.*

| Categoría | Personaje | Descripción |
|---|---|---|
| 🛡️ Tanque | **Operativo Blindado** | Traje de combate ligero con escudo energético. Más móvil que los mechs. |
| 🏹 Distancia | **Tirador de Pulso** | Rifle de pulso electromagnético. Deshabilita estructuras enemigas por 5 seg al impactar. |
| 🗡️ Asesino | **Ghost Digital** | Se camufla en el entorno visual. Solo detectable por Exploradores. |
| 🔮 Mago | **Hacker de Campo** | Toma control temporal de una estructura enemiga (Torre Vigía o Extractor) por 15 seg. |
| ⚒️ Obrero | **Técnico de Resistencia** | No puede construir Cuarteles pero sus Extractores son invisibles para el rival. |
| 🔭 Explorador | **Infiltrador de Red** | Hackea los drones rivales para usarlos como cámara durante 10 seg. |
| 🏇 Caballería | **Motorista Fantasma** | Moto silenciosa. Se mueve sin ser detectado por Exploradores. |
| 💣 Artillería | **Cañón EMP** | Emite un pulso que deshabilita todas las estructuras enemigas en radio por 20 seg. Sin daño directo a unidades. |
| 💚 Soporte | **Médico Callejero** | Cura unidades y puede "reconstruir" una unidad aliada destruida (1 vez por partida). |

*Mapa: **Ciudad Roja** — rascacielos como cobertura, nodos de red como puntos de control que amplifican el cooldown del LLM enemigo. Recurso del mapa: **Energía**.*

---

**Civilización: Soldados Aumentados**

*Biología + tecnología. Velocidad extrema, adaptación, superhumanos.*

| Categoría | Personaje | Descripción |
|---|---|---|
| 🛡️ Tanque | **Berserker Aumentado** | Exoesqueleto orgánico-metálico. A menor vida, más daño inflige. |
| 🏹 Distancia | **Francotirador Implantado** | Visión de largo alcance quirúrgica. Ve a través de obstáculos menores. |
| 🗡️ Asesino | **Clon de Combate** | Puede dividirse en dos instancias por 8 seg. Confunde al rival sobre qué objetivo atacar. |
| 🔮 Mago | **Psiónico** | Habilidades mentales. Invierte brevemente las órdenes de una unidad enemiga. |
| ⚒️ Obrero | **Bio-Constructor** | Hace crecer estructuras orgánicas. Más baratas pero se degradan solas con el tiempo. |
| 🔭 Explorador | **Rastreador Neural** | Conectado neuralmente al mapa. Detecta automáticamente cualquier movimiento enemigo cercano. |
| 🏇 Caballería | **Saltador de Combate** | Exotraje de salto. Atraviesa obstáculos verticalmente y aterriza con daño de área. |
| 💣 Artillería | **Cañón Bioquímico** | Lanza cápsulas de gas que reducen estadísticas enemigas en zona durante 15 seg. |
| 💚 Soporte | **Médico Genético** | Cura unidades y puede otorgar temporalmente resistencia al daño de área. |

*Mapa: **Laboratorio Extendido** — corredores de laboratorio, zonas de mejora que evolucionan unidades al 50% del costo normal. Recurso del mapa: **Energía**.*

---

### 2.4 Bono de civilización por mapa

Cuando el mapa seleccionado aleatoriamente pertenece a una civilización específica, las unidades de ese origen reciben un bono de estadísticas:

| Coincidencia | Bono |
|---|---|
| **Misma civilización** que el mapa | +25% a todas las estadísticas base |
| **Misma era**, diferente civilización | +10% a todas las estadísticas base |
| Era diferente | Sin bono |

Dado que el mapa se revela solo al iniciar la partida, este bono es un factor de riesgo/recompensa. Los jugadores que especializan su colección en pocas civilizaciones apuestan a obtener el bono máximo; los que diversifican juegan de forma más predecible pero con mayor consistencia.

### 2.5 Unidad Especial

Cada civilización cuenta con **1 Unidad Especial** — la figura histórica más emblemática o el símbolo máximo de esa facción. Estas unidades son el **"héroe"** del equipo y ocupan el **quinto slot obligatorio** de la selección pre-partida.

**Características de las Unidades Especiales:**
- Stats superiores a cualquier unidad estándar del mismo nivel de evolución
- **1 habilidad pasiva** (siempre activa durante toda la partida)
- **1 habilidad activa** exclusiva (invocable mediante prompt o botón dedicado en el menú contextual)
- Visible y distinguible del resto del equipo — mayor tamaño visual, efectos únicos

**Desbloqueo de Unidades Especiales:**
Las Unidades Especiales **no se obtienen en cofres**. Cada una tiene un requisito de desbloqueo específico basado en progreso real:

| Civilización | Unidad Especial | Requisito de desbloqueo | Habilidad activa |
|---|---|---|---|
| Imperio Romano | **César** | Nivel 20 + 10 victorias con Romano | *Discurso de Marte* — ignora cooldown de prompt por 8 seg |
| Egipto del Faraón | **Ramses II** | Tener desbloqueados los 9 personajes Egipcios | *Voluntad del Faraón* — construye una pirámide que bloquea proyectiles |
| Esparta | **Leónidas** | 50 kills totales con unidades espartanas | *300* — el Tanque más cercano es invulnerable 5 seg |
| Cruzados | **Ricardo Corazón de León** | Alcanzar liga Plata con Cruzados | *Por la Fe* — todas las unidades aliadas se regeneran vida por 10 seg |
| Japón Feudal | **Oda Nobunaga** | Ganar 5 partidas con equipos mixtos de eras distintas | *Estrategia Decisiva* — revela el prompt actual del rival |
| Imperio Otomano | **Solimán el Magnífico** | Construir 100 estructuras con Obreros Otomanos | *Imperio en Expansión* — captura la zona más cercana instantáneamente |
| WW2 | **General Fantasma** | 10 partidas ganadas con más kills que el rival | *Maniobra Envolvente* — reposiciona todas las unidades aliadas simultáneamente |
| Steampunk | **Gran Inventor** | Construir todos los tipos de estructura en una partida | *Prototipo Definitivo* — convierte la Torre Vigía más cercana en versión mejorada |
| Guerrilla | **El Comandante** | Ganar una partida sin perder ninguna unidad | *Resistencia* — las unidades aliadas no pueden morir por 4 seg |
| Mechs Corp. | **UNIT-ZERO** | Evolucionar 3 unidades a Legendario en una sola partida | *Protocolo Omega* — evoluciona instantáneamente a Legendario |
| Hackers | **Ghost Root** | Hackear 20 estructuras enemigas con el Hacker de Campo | *Blackout Total* — deshabilita todas las estructuras enemigas por 10 seg |
| Soldados Aumentados | **Prototipo ALPHA** | Llegar a liga Diamante | *Singularidad* — duplica todos los stats durante 6 seg |

### 2.6 Sistema de desbloqueo de personajes estándar

Los personajes estándar se desbloquean mediante:

- **Monedas de partida** — Se ganan al finalizar cada partida. Ganar otorga 1.5× monedas. Se usan para compra directa de personajes o cofres.
- **Cofres** — Gratuitos cada 4 horas; de pago con monedas premium. Contienen personajes aleatorios según rareza.
- **Pase de batalla** — Incluye 1 personaje exclusivo de temporada en sus niveles premium.
- **Live service** — Nuevos personajes (y eventualmente nuevas civilizaciones) añadidos periódicamente.

**Política de cofres (transparencia):**
- Las probabilidades de cada rareza son siempre visibles antes de abrir.
- Sistema de *pity*: tras 40 cofres consecutivos sin obtener un personaje épico o superior, el siguiente lo garantiza.
- Los personajes duplicados otorgan **fragmentos** que permiten comprar directamente cualquier personaje sin depender de la aleatoriedad.

### 2.7 Personaje guía de campaña

Durante las 6 misiones del tutorial, el jugador es asistido por **VANE** — una IA de voz neutral con personalidad adaptativa. VANE analiza el estilo del jugador y ajusta sus sugerencias: más directa con quienes prefieren prompts cortos, más creativa con quienes experimentan.

> *"Interesante elección de prompt. No era la óptima, pero funcionó. Anoto eso."* — VANE

---

## 3. Flujo Pre-Partida y Selección de Equipo

### 3.1 Flujo completo antes de una partida

```
[Colección del jugador]
        ↓
[Seleccionar 4 categorías estándar (de las 9 disponibles) — 1 personaje por categoría]
        ↓
[Seleccionar 1 Unidad Especial (de las que tenga desbloqueadas)]
        ↓
[Equipo confirmado: 5 unidades totales]
        ↓
[Entrar a matchmaking]
        ↓
[Partida inicia — el mapa y la civilización beneficiada se revelan en este momento]
        ↓
[Despliegue inicial y comienzo del combate]
```

### 3.2 Reglas de selección

- El jugador elige **4 categorías estándar** de las 9 disponibles (1 personaje por categoría elegida).
- Más **1 Unidad Especial** de cualquier civilización desbloqueada.
- Total: **5 unidades por partida**.
- Las 5 categorías estándar no elegidas son los puntos débiles del jugador para esa partida.
- La combinación de categorías elegidas define el "arquetipo" del equipo (agresivo, económico, reconocimiento, etc.).

### 3.3 El mapa es desconocido

El mapa — y por tanto qué civilización recibe bono — **no se conoce hasta que la partida comienza**. Esto fuerza a los jugadores a construir equipos versátiles o asumir el riesgo de especializarse.

---

## 4. Niveles y Escenarios

### 4.1 Estructura del mapa

Cada mapa es un terreno **3D semirealista de tamaño fijo** dividido en **zonas de control** capturables. El tamaño estándar es de **9 zonas** en una cuadrícula 3×3 con variaciones de terreno.

**Tipos de zona:**

| Tipo | Descripción | Bonus |
|---|---|---|
| 🏙️ **Ciudad / Estructura** | Edificios según la era del mapa | +20% defensa para unidades en zona |
| 🌲 **Terreno Natural** | Bosque, desierto, nieve — según era | Unidades no visibles hasta 2 tiles de distancia |
| ⛰️ **Colina / Altura** | Terreno elevado de cualquier tipo | +30% alcance para unidades a distancia |
| ⛏️ **Zona de recursos** | Nodo del recurso específico del mapa | Obreros recolectan aquí; nodo agotable |
| 🚩 **Nexo** | Zona central estratégica | Controlarla otorga +2 puntos de territorio por segundo |

### 4.2 Mapas del lanzamiento (V1)

**12 mapas** en el lanzamiento — uno por civilización:

| Mapa | Civilización | Recurso | Característica especial |
|---|---|---|---|
| **Coliseo del Imperio** | Romano | Oro | Zonas de arena aceleran unidades ligeras |
| **Valle del Nilo** | Egipcio | Oro | Oasis concentran recursos en puntos clave |
| **Las Termópilas** | Espartano | Hierro | Desfiladero estrecho — cuellos de botella extremos |
| **Tierra de Feudos** | Cruzados | Madera | Castillos en extremos del mapa |
| **Santuario de las Tres Colinas** | Japón Feudal | Madera | Ríos ralentizan; cerezos bloquean visión |
| **Murallas de Constantinopla** | Otomano | Hierro | Puertas como puntos de control críticos |
| **Campo de Batalla Europeo** | WW2 | Carbón | Trincheras y zonas de bombardeo aleatorio |
| **Ciudad Industrial Humeante** | Steampunk | Carbón | Niebla de fábrica, vías de tren como corredores rápidos |
| **Bosques de la Resistencia** | Guerrilla | Madera | Cobertura densa, cuevas como puntos ocultos |
| **Metrópolis Fracturada** | Mechs | Nano-cristales | Plataformas flotantes, zonas de energía |
| **Ciudad Roja** | Hackers | Energía | Nodos de red amplifican cooldown del LLM rival |
| **Laboratorio Extendido** | Soldados Aum. | Energía | Zonas de mejora aceleran evolución de unidades |

### 4.3 Mapas en campaña

Las 6 misiones del tutorial se juegan en versiones modificadas de los mapas anteriores con condiciones especiales: tiempo límite, unidades predefinidas, restricciones de prompt o recursos limitados.

---

## 5. Reglas del Juego

### 5.1 Estructura de una partida

1. **Selección pre-partida:** 4 categorías estándar + 1 Unidad Especial por jugador.
2. **Matchmaking:** El sistema empareja jugadores de rango similar.
3. **Despliegue inicial:** Cada jugador parte con sus 5 unidades en su esquina del mapa.
4. **Revelación del mapa:** El mapa y la civilización con bono se muestran al iniciar.
5. **Fase de combate (tiempo real):** Los jugadores envían prompts en cualquier momento. No hay turnos.
6. **Victoria:** La partida termina cuando se cumple una condición de victoria.

### 5.2 Condiciones de victoria

| Condición | Descripción |
|---|---|
| **Dominio** | Acumular 100 puntos de territorio antes que el rival |
| **Eliminación** | Destruir todas las unidades enemigas |
| **Tiempo** | Al llegar al tiempo límite (15 min), gana quien tenga más puntos de territorio |

### 5.3 Sistema de control dual

El jugador tiene dos formas de controlar sus unidades:

**Modo movimiento rápido (sin prompt):**
1. Toque en una unidad → se abre el menú contextual
2. Toque en un punto del mapa o minimapa → la unidad se mueve a esa posición

Ejecuta la acción de inmediato, sin cooldown, pero solo permite movimiento básico a una sola unidad.

**Modo prompt (control avanzado):**
1. Toque en una unidad → se abre el menú contextual
2. Toque en el botón central del menú → se abre la caja de texto
3. El jugador escribe la orden en lenguaje natural → toca "Enviar"
4. El LLM interpreta el prompt y ejecuta acciones complejas sobre múltiples unidades

Tiene **cooldown de 6 segundos** entre prompts. Permite coordinar todo el ejército con una sola instrucción.

**Menú contextual (diseño):**
```
         [ℹ️ Info]
    [↩️ Retroceder]  [💬 Prompt]  [⚔️ Atacar zona]
         [🚶 Mover]      [★ Habilidad Especial]  ← solo en Unidad Especial
```

**Parámetros del sistema de prompt:**
- **Límite base:** 280 caracteres por prompt
- **Cooldown base:** 6 segundos entre prompts
- El jugador puede referirse a unidades por categoría, civilización, o nombre propio asignado

**Ejemplos de prompts válidos:**
```
"Manda al Legionario y al Caballero al Nexo. Que el Shinobi los cubra desde el bosque."
"El Obrero que construya una Torre Vigía en la colina norte con los recursos disponibles."
"Todos los Exploradores al cuadrante sur. El Asesino que espere en el bosque este."
"Rodea la ciudad con las unidades rápidas, ataca cuando el Tanque llegue al centro."
"Usa la habilidad de César ahora que el rival está reagrupando sus tropas."
```

### 5.4 Sistema de evolución de unidades

Las unidades evolucionan a versiones más poderosas al cumplir **ambas condiciones simultáneamente**: kills acumuladas + recursos gastados.

| Nivel | Nombre | Kills acumuladas | Recursos gastados | Mejora |
|---|---|---|---|---|
| 1 | **Base** | — | — | Estadísticas base |
| 2 | **Elite** | 3 kills | 50 recursos | +25% todas las estadísticas |
| 3 | **Legendario** | 6 kills | 120 recursos | +50% estadísticas + habilidad especial de personaje |

La evolución ocurre automáticamente al cumplir ambas condiciones. La habilidad especial de nivel Legendario es única por personaje.

### 5.5 Sistema de recursos y construcciones

Los **Obreros** son el motor económico de la partida. Recolectan el recurso específico del mapa en las zonas de recursos.

**Flujo de recursos:**
- El Obrero debe desplazarse a una zona de recursos y permanecer en ella para recolectar.
- Genera ~10 recursos cada 5 segundos mientras está en la zona.
- Los nodos de recursos se agotan con el tiempo y se regeneran lentamente.

**Recurso cosmético por era** (mecánicamente idéntico, visualmente temático):

| Era | Recurso | Apariencia del Extractor |
|---|---|---|
| Antigua | Oro | Mina de gemas / Escombros de pirámide |
| Medieval | Madera / Hierro | Serrería / Fragua |
| Industrial | Carbón / Acero | Mina de carbón / Alto horno |
| Futura | Energía / Nano-cristales | Reactor de plasma / Extractor nano |

**Construcciones disponibles para Obreros:**

| Estructura | Efecto | Costo | Tiempo |
|---|---|---|---|
| ⛏️ **Extractor [Recurso de Era]** | Genera recursos pasivamente sin necesidad del Obrero presente | 40 | 8 seg |
| 🗼 **Torre Vigía** | Ataca unidades enemigas en rango; otorga visión del área | 60 | 10 seg |
| 🏕️ **Base Secundaria** | Punto de spawn alternativo para unidades existentes; produce nuevos Obreros periódicamente | 80 | 12 seg |
| 🏕️ **Cuartel** | Permite desplegar una unidad de combate adicional desde la reserva | 100 | 15 seg |

Las estructuras pueden ser destruidas por el rival. Los Obreros pueden demoler sus propias construcciones recuperando el 50% de recursos.

### 5.6 Sistema de potenciadores

Los potenciadores se ganan al cumplir objetivos durante la partida:

| Potenciador | Cómo se gana | Efecto | Duración |
|---|---|---|---|
| 🔡 **Prompt+** | Controlar 3 zonas a la vez | +150 caracteres al límite | Permanente en la partida |
| 🔍 **Espionaje** | Destruir una unidad exploradora enemiga | Ver el próximo prompt del rival | 1 uso |
| ⏳ **Reintento** | Defender una zona por 2 min seguidos | Reenviar el último prompt con nuevo resultado | 1 uso |
| 🛡️ **Escudo** | Eliminar 5 unidades enemigas | Bloquea el espionaje enemigo por 60s | 60 segundos |

---

## 6. Controles

### 6.1 Controles móviles (versión final)

| Acción | Gesto |
|---|---|
| Mover cámara | Arrastrar con un dedo |
| Zoom | Pellizcar con dos dedos |
| Seleccionar unidad | Toque sobre la unidad → abre menú contextual |
| Mover unidad (rápido) | Toque en unidad → toque en destino en el mapa o minimapa |
| Abrir prompt de unidad | Toque en unidad → botón central del menú contextual |
| Usar habilidad especial | Toque en Unidad Especial → botón ★ del menú contextual |
| Enviar prompt | Botón "Enviar" o Enter en teclado |
| Ver estado de unidad | Toque largo sobre una unidad |
| Acceder a potenciadores | Panel lateral izquierdo |
| Ver mapa completo | Botón minimapa (esquina inferior derecha) |

### 6.2 Controles web / V0 (teclado + mouse)

| Acción | Control |
|---|---|
| Mover cámara | WASD o arrastrar con click derecho |
| Zoom | Rueda del mouse |
| Seleccionar unidad | Click izquierdo |
| Mover unidad (rápido) | Seleccionar → click derecho en destino |
| Abrir prompt | Seleccionar → tecla [P] o botón de prompt |
| Usar habilidad especial | Tecla [Q] con Unidad Especial seleccionada |
| Enviar prompt | Enter |
| Activar potenciador | Teclas 1, 2, 3, 4 |

### 6.3 Diseño de la UI principal (móvil)

```
┌─────────────────────────────────┐
│  [Minimap]  [Civilización 🗺️] [Pts 🚩] │  ← HUD superior
│                                 │
│         MAPA 3D                 │  ← Vista de juego
│                                 │
│  ╔══════════════╗               │
│  ║  [ℹ️]  [💬]  ║  ← Menú contextual (al tocar una unidad)
│  ║  [🚶] [⚔️][★]║
│  ╚══════════════╝               │
│  [⚡][🔍][🛡️]  [━━━━━━] 280     │  ← Potenciadores + cooldown
└─────────────────────────────────┘
```

---

## 7. Sistema de Puntos, Progresión y Monetización

### 7.1 Sistema de puntos en partida

- **Puntos de territorio:** +1 por segundo por zona controlada; +2 por segundo si se controla el Nexo
- **Puntos de combate:** +5 por unidad enemiga eliminada (no afectan la victoria, sí el ranking)
- **Puntos de eficiencia:** Bonus al final de la partida por ganar con prompts cortos

### 7.2 Sistema de progresión de cuenta

| Nivel | Nombre | Desbloqueo |
|---|---|---|
| 1–5 | Recluta | Tutorial, 2 personajes iniciales (1 Romano, 1 WW2) |
| 6–15 | Operativo | Modo clasificatorio, cofres estándar, skins base |
| 16–30 | Veterano | Efectos visuales de evolución, títulos personalizados |
| 31–50 | Élite | Animaciones especiales de Legendario, íconos de perfil exclusivos |
| 51+ | Comandante | Acceso a torneos, insignia de temporada, cofres de élite |

La XP se gana en cada partida. Ganar otorga 1.5× XP.

### 7.3 Monetización — Modelo Free to Play

**Gratuito siempre:**
- Modo competitivo completo
- 2 personajes iniciales al crear cuenta
- Todos los 12 mapas del lanzamiento
- Partidas ilimitadas
- Cofre gratuito cada 4 horas

**Cuatro fuentes de ingresos:**

**A) Cofres de personajes**
- Probabilidades visibles siempre antes de abrir
- Sistema de pity garantizado (épico o superior cada 40 cofres máximo)
- Duplicados = fragmentos para compra directa
- Precio: $0.99 – $2.99 equivalente en monedas premium por cofre

**B) Cosméticos (tienda)**
Nunca afectan el gameplay:
- Skins de evolución (aspecto alternativo para nivel Elite o Legendario)
- Efectos de victoria, avatares, marcos de perfil
- Efectos de prompt (animación al enviar órdenes)
- Precio: $1.99 – $9.99 por ítem

**C) Pase de batalla (seasonal)**
- Duración: 2 meses
- Precio: $4.99
- Incluye: 50 niveles de recompensas, 1 personaje exclusivo de temporada, XP acelerado
- Versión gratuita del pase: recompensas reducidas, sin personaje exclusivo

**D) Publicidad opcional**
- Ver video de 30 seg para obtener: cofre básico adicional, +50% XP por 1 hora, o 2 horas sin anuncios
- Los anuncios nunca interrumpen una partida activa

**Tabla resumen:**

| Fuente | Tipo | Impacto en gameplay |
|---|---|---|
| Cofres | Compra con monedas | Más personajes = más opciones estratégicas |
| Cosméticos | Compra única | Ninguno |
| Pase de batalla | Suscripción temporal | 1 personaje exclusivo de temporada |
| Ver anuncio | Opcional | Cofre extra o XP bonus |

> **Nota de diseño:** Los jugadores con más personajes tienen más variedad táctica, pero no mayor poder — todos los personajes del mismo nivel de evolución tienen estadísticas balanceadas. Un jugador F2P con horas suficientes puede tener la misma colección que uno que paga.

---

## 8. Sistemas adicionales

### 8.1 Sistema de ranking competitivo

| Liga | Requisito |
|---|---|
| 🔩 Hierro | Partidas de placement (primeras 10) |
| ⚙️ Bronce | Ranking 0–999 |
| 🥈 Plata | Ranking 1000–2499 |
| 🥇 Oro | Ranking 2500–4999 |
| 💎 Diamante | Ranking 5000–7999 |
| 👁️ Comandante | Top 500 mundial |

La liga *Comandante* recibe cofres de élite y la insignia exclusiva de cada temporada.

### 8.2 Sistema social

- **Perfil público:** Colección, civilización favorita, estadísticas de prompts (longitud promedio, win rate), era más jugada
- **Replay de partidas:** Log completo de prompts y acciones de ambos jugadores al terminar una partida
- **Compartir jugadas:** Exportar el "prompt más creativo de la partida" como imagen o clip para redes
- **Clanes:** Grupos de hasta 30 jugadores, torneos internos, chat propio

---

*Documento creado: Fase 3 — Game Design Document*
*Versión 3.0 — Expansión mayor: 4 eras, 12 civilizaciones, 9 categorías, Unidad Especial, estructuras actualizadas*
*Versiones anteriores: v1.0 (facciones AXIOM/VANTIS), v2.0 (primer rediseño)*
*Siguiente paso: Fase 4 — Prototipo*
