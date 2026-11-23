# Rebanada

[↑ Glosario](../../README.md) · [← README](./readme.md) · [Rebase →](./rebase.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Unidad de funcionalidad migrable y reversible de forma independiente.

Definición de trabajo de [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md).

## Por qué importa

En [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md), el tema «Estrangulamiento y rebanadas» importa porque reduce el daño por paso y permite revertir.

## Cómo funciona

Según [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md):

El nombre viene de las higueras estranguladoras, que crecen alrededor de un árbol hasta sustituirlo. El patrón coloca una **fachada** (un enrutador, un proxy o una capa en el propio código) delante del sistema antiguo; al principio todo pasa por el antiguo, y se va desviando hacia el nuevo, **rebanada** por rebanada, la funcionalidad migrada. Cada rebanada debe ser lo bastante pequeña para migrarse y revertirse rápido, y lo bastante independiente para que migrarla no obligue a migrar otra. Los criterios para cortar son tres: por **ruta o capacidad** (calcular nota, cerrar acta, exportar), por **datos** (los cursos de un año) o por **tipo de cliente**.

Según [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo divide el módulo en cuatro rebanadas: consulta de nota (poco tráfico, lectura), cálculo de nota, cierre de acta y exportación. Empieza por la consulta: la fachada la envía al sistema nuevo al 5 % y copia el 100 % en sombra al antiguo para comparar; la regla de equivalencia compara la nota al décimo y estado traducido, e ignora la marca de tiempo. Antes de subir a 25 % exige 3 000 comparaciones sin diferencias, calculadas para detectar una tasa del 0,1 %. Para el cálculo de nota, identifica en el calendario las dos semanas de cierre y no sube más allá del 25 % hasta haber reproducido tráfico grabado de la última de esas semanas.

## Ejemplo

Ejemplo de [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo divide el módulo en cuatro rebanadas: consulta de nota (poco tráfico, lectura), cálculo de nota, cierre de acta y exportación. Empieza por la consulta: la fachada la envía al sistema nuevo al 5 % y copia el 100 % en sombra al antiguo para comparar; la regla de equivalencia compara la nota al décimo y estado traducido, e ignora la marca de tiempo. Antes de subir a 25 % exige 3 000 comparaciones sin diferencias, calculadas para detectar una tasa del 0,1 %.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El corte se pospone una y otra vez** — causa: el paso es demasiado grande para verificarse. Corrección: dividir en rebanadas con retroceso independiente. ([SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cada rebanada debe ser lo bastante pequeña para migrarse y revertirse rápido, y lo bastante independiente para que migrarla no obligue a migrar otra. ([SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capa anticorrupción](../c/capa-anticorrupcion.md), [Comparación en sombra](../c/comparacion-en-sombra.md), [Estrangulamiento](../e/estrangulamiento.md), [Rama por abstracción](./rama-por-abstraccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-521 — Strangler, branch by abstraction y anticorruption](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-085](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md), [SE-526](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md), [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md), [SE-522](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md), [SE-528](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «StranglerFigApplication»](https://martinfowler.com/bliki/StranglerFigApplication.html) — el patrón de estrangulamiento; autoridad: autor del texto.
- [Microsoft Azure Architecture Center: Strangler Fig](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig) — fachada y migración incremental; autoridad: documentación de Microsoft.
- [Microsoft Azure Architecture Center: Anti-corruption Layer](https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer) — traducción entre modelos; autoridad: documentación de Microsoft.
- [Fowler, «DarkLaunching»](https://martinfowler.com/bliki/DarkLaunching.html) — ejecutar con tráfico real sin exponer el resultado; autoridad: autor del texto.
- [Fowler, «FeatureToggle»](https://martinfowler.com/bliki/FeatureToggle.html) — banderas de funcionalidad y su costo; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← README](./readme.md) · [Rebase →](./rebase.md)
