# Prototipo desechable

[↑ Glosario](../../README.md) · [← Prototipo](./prototipo.md) · [Prototipo evolutivo →](./prototipo-evolutivo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Pieza escrita para aprender que se descarta al responder su pregunta.

Definición de trabajo de [SE-557 — Prototipado, scaffolding y exploración de alternativas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md).

## Por qué importa

En [SE-557 — Prototipado, scaffolding y exploración de alternativas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md), el tema «Prototipos: desechable, evolutivo, producto» importa porque evita que un experimento herede obligaciones de un producto

## Cómo funciona

Según [SE-557 — Prototipado, scaffolding y exploración de alternativas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md):

Un prototipo **desechable** existe para aprender: se escribe rápido, sin pretensiones de calidad, y se tira cuando respondió su pregunta. Uno **evolutivo** se construye con la intención de endurecerlo y convertirlo en producto, y por eso desde el inicio lleva estructura, pruebas y estándares. El **producto** cumple las obligaciones de mantenimiento, seguridad y soporte. La generación con asistentes facilita el primero hasta el punto de abaratar tanto el experimento que los equipos generan más, y por eso la decisión de destino importa más que antes. El fallo clásico es el prototipo desechable que no se tira: funciona, alguien depende de él y el equipo hereda una pieza sin pruebas, sin manejo de errores y con supuestos que nadie recuerda.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-557 — Prototipado, scaffolding y exploración de alternativas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones necesita una exportación. Antes de generar nada escribe cuatro criterios: error claro ante nota ausente, salida idéntica para la misma entrada, pruebas sin base de datos y menos de 200 líneas. Pide al asistente cuatro alternativas realmente distintas, cada una con supuestos y desventajas. Las evalúa ejecutando el mismo conjunto de 12 casos reales anonimizados, incluidos tres de nota ausente.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-557 — Prototipado, scaffolding y exploración de alternativas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md)) son:

- **El prototipo acaba en producción sin pruebas** — causa: no se declaró su destino. Corrección: declarar destino y fecha de revisión al generarlo.
- **Se elige la alternativa «más limpia» y falla** — causa: no hay criterios previos. Corrección: escribir criterios verificables antes de generar.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un prototipo **desechable** existe para aprender: se escribe rápido, sin pretensiones de calidad, y se tira cuando respondió su pregunta. ([SE-557](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-556](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Andamiaje](../a/andamiaje.md), [Brecha a producción](../b/brecha-a-produccion.md), [Maldición del optimizador](../m/maldicion-del-optimizador.md), [Prototipo evolutivo](./prototipo-evolutivo.md), [Registro de decisiones](../r/registro-de-decisiones.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-557 — Prototipado, scaffolding y exploración de alternativas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-586](../../../classes/part-48-harness-y-agentic-engineering/se-586-ai-dlc-gobierno-y-vibe-coding-frente-a-agentic-engineering/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Brooks, «No Silver Bullet»](https://doi.org/10.1109/MC.1987.1663532) — complejidad esencial y accidental; autoridad: IEEE Computer, 1987.
- [Smith y Winkler, «The Optimizer's Curse»](https://doi.org/10.1287/mnsc.1050.0451) — sesgo al elegir por la mejor estimación; autoridad: Management Science.
- [Chen et al., «Evaluating Large Language Models Trained on Code»](https://arxiv.org/abs/2107.03374) — muestreo de varias soluciones filtradas por pruebas; autoridad: preprint de OpenAI.
- [Fowler, «Exploring Generative AI»](https://martinfowler.com/articles/exploring-gen-ai.html) — experiencias de uso en el desarrollo; autoridad: autor del texto.
- [Nygard, «Documenting Architecture Decisions»](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — registro de decisiones; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Prototipo](./prototipo.md) · [Prototipo evolutivo →](./prototipo-evolutivo.md)
