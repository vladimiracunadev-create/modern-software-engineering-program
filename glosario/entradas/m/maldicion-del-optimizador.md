# Maldición del optimizador

[↑ Glosario](../../README.md) · [← Maestro dorado](./maestro-dorado.md) · [Malla de servicios →](./malla-de-servicios.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Sesgo por el cual la alternativa elegida por su mejor estimación vale en promedio menos que esa estimación.

Definición de trabajo de [SE-557 — Prototipado, scaffolding y exploración de alternativas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md).

## Por qué importa

La clase donde se define, [SE-557 — Prototipado, scaffolding y exploración de alternativas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md), existe con este propósito: la clase existe para que aproveches lo que un asistente hace mejor y más barato, generar muchas variantes de algo desechable, sin confundir esa abundancia con progreso.

## Cómo funciona

Según [SE-557 — Prototipado, scaffolding y exploración de alternativas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md):

Si estimas la calidad de cada alternativa con error y eliges la de mayor valor estimado, el valor real de la elegida es, en promedio, menor que su estimación. Smith y Winkler lo llaman la maldición del optimizador: la selección favorece a quien el error benefició. Cuantas más alternativas y más ruido, mayor es la distancia entre lo medido y lo real. No es un defecto de la herramienta sino de la estadística de elegir el máximo. Las consecuencias prácticas son tres. Hay que medir con el menor ruido posible (pruebas ejecutables sobre casos reales, no impresión visual). Hay que desconfiar de la ventaja de una ganadora que gana por poco.

## Ejemplo

Ejemplo de [SE-557 — Prototipado, scaffolding y exploración de alternativas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md) (sección «Ejemplo mínimo»):

El fragmento muestra la maldición del optimizador con cinco alternativas. Antes de ejecutarlo, predice si la media de lo medido en la ganadora es mayor o menor que la de su calidad real.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-557 — Prototipado, scaffolding y exploración de alternativas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md)) son:

- **El prototipo acaba en producción sin pruebas** — causa: no se declaró su destino. Corrección: declarar destino y fecha de revisión al generarlo.
- **Se elige la alternativa «más limpia» y falla** — causa: no hay criterios previos. Corrección: escribir criterios verificables antes de generar.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-557 — Prototipado, scaffolding y exploración de alternativas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: una simulación de selección con ruido, un análisis real con `ast` sobre un andamiaje de plantilla y una simulación de brecha a producción. No se evaluó ningún generador, ningún asistente ni ningún equipo; las distribuciones de calidad y ruido, la plantilla, las cuatro funciones usadas y las probabilidades de los atributos son construcciones del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-556](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-556-autocompletado-chat-edicion-y-generacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Andamiaje](../a/andamiaje.md), [Brecha a producción](../b/brecha-a-produccion.md), [Prototipo desechable](../p/prototipo-desechable.md), [Prototipo evolutivo](../p/prototipo-evolutivo.md), [Registro de decisiones](../r/registro-de-decisiones.md).
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

[↑ Glosario](../../README.md) · [← Maestro dorado](./maestro-dorado.md) · [Malla de servicios →](./malla-de-servicios.md)
