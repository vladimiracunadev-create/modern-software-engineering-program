# Cambio silencioso

[↑ Glosario](../../README.md) · [← Cambio semántico](./cambio-semantico.md) · [Cambio sobre código existente →](./cambio-sobre-codigo-existente.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Diferencia entre versiones que produce un resultado distinto sin lanzar una excepción.

Definición de trabajo de [SE-522 — Migraciones de runtime, lenguaje y framework](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md).

## Por qué importa

En [SE-522 — Migraciones de runtime, lenguaje y framework](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md), el tema «Cambios silenciosos de semántica» importa porque alteran datos sin dejar rastro.

## Cómo funciona

Según [SE-522 — Migraciones de runtime, lenguaje y framework](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md):

Un cambio **ruidoso** se descubre al ejecutarlo: la llamada a una función eliminada lanza una excepción y la suite, si la ejercita, falla. Un cambio **silencioso** produce un resultado distinto sin excepción: el redondeo de empates, la división de enteros, el orden de un diccionario o un conjunto, la codificación por defecto al abrir un archivo. Los silenciosos son más peligrosos por dos razones: la suite solo los detecta si compara valores en los puntos exactos donde difieren, y el daño se acumula en los datos mientras nadie mira. Las sondas son el instrumento: se toman datos representativos, se aplica la operación con el comportamiento antiguo y con el nuevo y se cuenta cuántos resultados difieren.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-522 — Migraciones de runtime, lenguaje y framework](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo hace el catálogo de diferencias entre la versión actual y la objetivo y lo cruza con el código: encuentra 14 usos de `round`, 6 ordenamientos de nombres y un campo de 12 bytes. Ejecuta las sondas con las notas del último año: 38 de 760 resultados cambian de un décimo y 2 cruzan la frontera de aprobado.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La suite pasa y los datos cambian** — causa: cambio silencioso no ejercitado por las pruebas. Corrección: escribir sondas con datos reales y ampliar el maestro dorado. ([SE-522](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un cambio **silencioso** produce un resultado distinto sin excepción: el redondeo de empates, la división de enteros, el orden de un diccionario o un conjunto, la codificación por defecto al abrir un archivo. ([SE-522](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Excepción](../e/excepcion.md), [Resultado](../r/resultado.md), [Versión](../v/version.md), [Cambio ruidoso](./cambio-ruidoso.md), [Matriz de pruebas](../m/matriz-de-pruebas.md), [Reescritura por estructura](../r/reescritura-por-estructura.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-522 — Migraciones de runtime, lenguaje y framework](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: round (funciones integradas)](https://docs.python.org/3/library/functions.html) — redondeo de empates y representación de flotantes; autoridad: documentación de Python.
- [Python: Porting Python 2 Code to Python 3](https://docs.python.org/3/howto/pyporting.html) — estrategia de portado por pasos; autoridad: documentación de Python.
- [Python: What's New in Python 3.0](https://docs.python.org/3/whatsnew/3.0.html) — cambios de comportamiento entre versiones mayores; autoridad: documentación de Python.
- [Python: ast](https://docs.python.org/3/library/ast.html) — árbol sintáctico para reescrituras; autoridad: documentación de Python.
- [Unicode UAX #15](https://unicode.org/reports/tr15/) — normalización de texto; autoridad: Unicode Consortium.

---

[↑ Glosario](../../README.md) · [← Cambio semántico](./cambio-semantico.md) · [Cambio sobre código existente →](./cambio-sobre-codigo-existente.md)
