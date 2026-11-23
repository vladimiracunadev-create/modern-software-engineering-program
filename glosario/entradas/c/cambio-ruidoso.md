# Cambio ruidoso

[↑ Glosario](../../README.md) · [← Cambio rompedor](./cambio-rompedor.md) · [Cambio semántico →](./cambio-semantico.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Diferencia entre versiones que lanza una excepción al ejecutarse.

Definición de trabajo de [SE-522 — Migraciones de runtime, lenguaje y framework](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md).

## Por qué importa

La clase donde se define, [SE-522 — Migraciones de runtime, lenguaje y framework](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md), existe con este propósito: la clase existe para que puedas mover un sistema a otra versión del lenguaje, del runtime o del framework sin que el cambio falle de la forma más peligrosa: sin hacer ruido.

## Cómo funciona

Según [SE-522 — Migraciones de runtime, lenguaje y framework](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md):

Un cambio **ruidoso** se descubre al ejecutarlo: la llamada a una función eliminada lanza una excepción y la suite, si la ejercita, falla. Un cambio **silencioso** produce un resultado distinto sin excepción: el redondeo de empates, la división de enteros, el orden de un diccionario o un conjunto, la codificación por defecto al abrir un archivo. Los silenciosos son más peligrosos por dos razones: la suite solo los detecta si compara valores en los puntos exactos donde difieren, y el daño se acumula en los datos mientras nadie mira. Las sondas son el instrumento: se toman datos representativos, se aplica la operación con el comportamiento antiguo y con el nuevo y se cuenta cuántos resultados difieren.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-522 — Migraciones de runtime, lenguaje y framework](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo hace el catálogo de diferencias entre la versión actual y la objetivo y lo cruza con el código: encuentra 14 usos de `round`, 6 ordenamientos de nombres y un campo de 12 bytes. Ejecuta las sondas con las notas del último año: 38 de 760 resultados cambian de un décimo y 2 cruzan la frontera de aprobado.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-522 — Migraciones de runtime, lenguaje y framework](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md)) son:

- **La suite pasa y los datos cambian** — causa: cambio silencioso no ejercitado por las pruebas. Corrección: escribir sondas con datos reales y ampliar el maestro dorado.
- **El script de reescritura cambió comentarios y textos** — causa: sustitución de texto o expresión regular. Corrección: reescribir por árbol sintáctico y revisar el diff.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-522 — Migraciones de runtime, lenguaje y framework](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con cifras idénticas. Las sondas ejercitan CPython de verdad, pero con datos sintéticos; no se migró ningún sistema real, no se probó otro lenguaje ni un framework, y el calendario de un año con tres años de soporte, la duración de las migraciones y el 30 % de las pequeñas son construcciones del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Excepción](../e/excepcion.md), [Versión](../v/version.md), [Cambio silencioso](./cambio-silencioso.md), [Matriz de pruebas](../m/matriz-de-pruebas.md), [Reescritura por estructura](../r/reescritura-por-estructura.md), [Sonda](../s/sonda.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-522 — Migraciones de runtime, lenguaje y framework](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

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

[↑ Glosario](../../README.md) · [← Cambio rompedor](./cambio-rompedor.md) · [Cambio semántico →](./cambio-semantico.md)
