# Olor de código

[↑ Glosario](../../README.md) · [← Offline-first](./offline-first.md) · [Olvido catastrófico →](./olvido-catastrofico.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Característica de la estructura que sugiere un problema más profundo, sin demostrarlo.

Definición de trabajo de [SE-306 — Code smells y diagnóstico contextual](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-322 — Antipatrones y deuda de diseño](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md): Señal superficial que merece investigarse.

## Por qué importa

La clase donde se define, [SE-306 — Code smells y diagnóstico contextual](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md), existe con este propósito: la clase existe para que trates un olor de código como una sospecha que se confirma o se descarta con contexto, y no como un defecto que un umbral declara: sabrás qué señala cada medida, qué falsas alarmas produce y qué pregunta hacer antes de refactorizar.

## Cómo funciona

Según [SE-306 — Code smells y diagnóstico contextual](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md):

Un olor de código es una característica de la estructura que sugiere un problema más profundo sin demostrarlo. Una función larga, una lista larga de parámetros, anidamiento profundo, código repetido o una clase que accede más a datos ajenos que a los propios son olores clásicos. No fallan en una prueba: encarecen el cambio. Por eso se diagnostican con preguntas (¿cambia a menudo? ¿se entiende? ¿quién lo toca?), no con un aprobado o suspendido.

Según [SE-322 — Antipatrones y deuda de diseño](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md):

Un **antipatrón** es una estructura recurrente con un daño conocido (la «bola de barro» de Foote y Yoder, la clase de dios). Un **olor de código** es una señal superficial que a menudo corresponde a un problema más profundo, y a veces no (Fowler lo describe así: una indicación que merece investigarse). Una **incomodidad** es algo que molesta a quien lo lee sin costo medido. Distinguirlos importa porque piden respuestas distintas: el antipatrón se corrige con un refactor planificado, el olor se investiga con una medida, la incomodidad se deja o se arregla cuando se pasa cerca. Llamar «antipatrón» a toda incomodidad es la forma habitual de gastar tiempo de refactor sin retorno.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-306 — Code smells y diagnóstico contextual](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md):

El equipo no reduce el reporte a cero: lo clasifica. Para cada una de las doce funciones señaladas anota tres cosas en una tabla: si es lógica o datos, cuántas veces cambió en el último año según `git log` y quién la toca.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-306 — Code smells y diagnóstico contextual](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md)) son:

- **El tablero baja a cero y el código no mejora** — causa: se optimizó la métrica y no el costo del cambio. Corrección: priorizar por historia de cambios y contexto.
- **Una plantilla o tabla de datos se parte en trozos** — causa: la regla de largo no distingue datos de lógica. Corrección: excluir literales de datos de la regla.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un olor de código es una característica de la estructura que sugiere un problema más profundo sin demostrarlo. ([SE-306](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md))
- Un **olor de código** es una señal superficial que a menudo corresponde a un problema más profundo, y a veces no (Fowler lo describe así: una indicación que merece investigarse). ([SE-322](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md), [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md), [SE-305](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Característica](../c/caracteristica.md), [Estructura](../e/estructura.md), [Problemas](../p/problemas.md), [Señal](../s/senal.md), [Antipatrón](../a/antipatron.md), [Ciclo de dependencias](../c/ciclo-de-dependencias.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-306 — Code smells y diagnóstico contextual](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-322 — Antipatrones y deuda de diseño](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-305](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «CodeSmell»](https://martinfowler.com/bliki/CodeSmell.html) — qué es un olor de código; autoridad: Martin Fowler.
- [Fowler, «Refactoring»](https://martinfowler.com/books/refactoring.html) — catálogo de olores y de refactorizaciones; autoridad: Martin Fowler.
- [Sjøberg et al. (IEEE TSE, 2013)](https://doi.org/10.1109/TSE.2012.89) — olores y esfuerzo de mantenimiento; autoridad: IEEE Transactions on Software Engineering.
- [Yamashita y Moonen, «Do code smells reflect important maintainability aspects?» (ICSM, 2012)](https://doi.org/10.1109/ICSM.2012.6405287) — olores y aspectos de mantenibilidad percibidos; autoridad: IEEE ICSM.
- [McCabe, «A Complexity Measure» (IEEE TSE, 1976)](https://doi.org/10.1109/TSE.1976.233837) — complejidad ciclomática; autoridad: IEEE Transactions on Software Engineering.

---

[↑ Glosario](../../README.md) · [← Offline-first](./offline-first.md) · [Olvido catastrófico →](./olvido-catastrofico.md)
