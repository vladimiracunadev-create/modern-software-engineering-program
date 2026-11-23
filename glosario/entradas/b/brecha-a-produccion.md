# Brecha a producción

[↑ Glosario](../../README.md) · [← Brecha](./brecha.md) · [Brecha entre segmentos →](./brecha-entre-segmentos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Conjunto de atributos que un prototipo no tiene y producción exige.

Definición de trabajo de [SE-557 — Prototipado, scaffolding y exploración de alternativas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md).

## Por qué importa

En [SE-557 — Prototipado, scaffolding y exploración de alternativas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md), el tema «Brecha a producción» importa porque convierte «ya funciona» en una lista de trabajo

## Cómo funciona

Según [SE-557 — Prototipado, scaffolding y exploración de alternativas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones necesita una exportación. Antes de generar nada escribe cuatro criterios: error claro ante nota ausente, salida idéntica para la misma entrada, pruebas sin base de datos y menos de 200 líneas. Pide al asistente cuatro alternativas realmente distintas, cada una con supuestos y desventajas. Las evalúa ejecutando el mismo conjunto de 12 casos reales anonimizados, incluidos tres de nota ausente. Dos fallan en la nota ausente, una pasa pero requiere la base de datos y una pasa todo. Elige esta, la declara **evolutiva** y anota las tres descartadas con su razón. Calcula la brecha a producción: faltan validación de entradas, registro y límites de tamaño, 18 puntos.

Según [SE-557 — Prototipado, scaffolding y exploración de alternativas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md):

Traslada el análisis a otro dominio (por ejemplo, el módulo de presupuestos de un taller mecánico): cambia los criterios y las alternativas y conserva el procedimiento de fijar criterios previos, comprobar la elegida con un conjunto aparte, contar generado y usado y listar la brecha a producción. La transferencia está lograda cuando puedes decir qué alternativas de ese dominio descartarías y con qué dato, no cuando la tabla se parece a la del módulo de calificaciones.

## Ejemplo

Ejemplo de [SE-557 — Prototipado, scaffolding y exploración de alternativas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones necesita una exportación. Antes de generar nada escribe cuatro criterios: error claro ante nota ausente, salida idéntica para la misma entrada, pruebas sin base de datos y menos de 200 líneas. Pide al asistente cuatro alternativas realmente distintas, cada una con supuestos y desventajas. Las evalúa ejecutando el mismo conjunto de 12 casos reales anonimizados, incluidos tres de nota ausente. Dos fallan en la nota ausente, una pasa pero requiere la base de datos y una pasa todo. Elige esta, la declara **evolutiva** y anota las tres descartadas con su razón.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **«Ya casi está» durante meses** — causa: no se listó la brecha a producción. Corrección: enumerar atributos pendientes y estimarlos. ([SE-557](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-557 — Prototipado, scaffolding y exploración de alternativas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: una simulación de selección con ruido, un análisis real con `ast` sobre un andamiaje de plantilla y una simulación de brecha a producción. No se evaluó ningún generador, ningún asistente ni ningún equipo; las distribuciones de calidad y ruido, la plantilla, las cuatro funciones usadas y las probabilidades de los atributos son construcciones del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-556](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Atributo](../a/atributo.md), [Conjunto](../c/conjunto.md), [Producción](../p/produccion.md), [Prototipo](../p/prototipo.md), [Andamiaje](../a/andamiaje.md), [Maldición del optimizador](../m/maldicion-del-optimizador.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-557 — Prototipado, scaffolding y exploración de alternativas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

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

[↑ Glosario](../../README.md) · [← Brecha](./brecha.md) · [Brecha entre segmentos →](./brecha-entre-segmentos.md)
