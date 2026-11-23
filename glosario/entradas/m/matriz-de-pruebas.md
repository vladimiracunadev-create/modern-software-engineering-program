# Matriz de pruebas

[↑ Glosario](../../README.md) · [← Matriz de decisión](./matriz-de-decision.md) · [Matriz de soporte →](./matriz-de-soporte.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Ejecución de la misma suite en varias versiones de la plataforma.

Definición de trabajo de [SE-522 — Migraciones de runtime, lenguaje y framework](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md).

## Por qué importa

La clase donde se define, [SE-522 — Migraciones de runtime, lenguaje y framework](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md), existe con este propósito: la clase existe para que puedas mover un sistema a otra versión del lenguaje, del runtime o del framework sin que el cambio falle de la forma más peligrosa: sin hacer ruido.

## Cómo funciona

Según [SE-522 — Migraciones de runtime, lenguaje y framework](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md):

La estrategia que más reduce el riesgo es hacer que el código funcione **en la versión actual y en la nueva** antes de cambiar la de producción. Se hace en pasos: se ejecutan las pruebas en las dos versiones (una matriz de pruebas), se reescribe lo que difiere de manera que dé el mismo resultado en ambas, se retiran las dependencias que no soportan la nueva y, solo entonces, se cambia la versión en producción, con el interruptor de volver a la anterior disponible mientras dura un periodo de observación. El código compatible con ambas versiones es provisional y se limpia después. La alternativa, reescribir y cambiar de versión a la vez, mezcla dos fuentes de fallo y hace imposible saber cuál causó un problema.

Según [SE-522 — Migraciones de runtime, lenguaje y framework](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo hace el catálogo de diferencias entre la versión actual y la objetivo y lo cruza con el código: encuentra 14 usos de `round`, 6 ordenamientos de nombres y un campo de 12 bytes. Ejecuta las sondas con las notas del último año: 38 de 760 resultados cambian de un décimo y 2 cruzan la frontera de aprobado. Decide conservar el comportamiento antiguo en el cálculo (una función explícita de redondeo, con la regla escrita y probada) y aceptar el orden con plegado de acentos, con aviso al área académica. Para la llamada obsoleta que aparece 148 veces escribe un script con `ast`, lo prueba con el conjunto de 400 fragmentos y revisa el diff completo.

## Ejemplo

Ejemplo de [SE-522 — Migraciones de runtime, lenguaje y framework](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo hace el catálogo de diferencias entre la versión actual y la objetivo y lo cruza con el código: encuentra 14 usos de `round`, 6 ordenamientos de nombres y un campo de 12 bytes. Ejecuta las sondas con las notas del último año: 38 de 760 resultados cambian de un décimo y 2 cruzan la frontera de aprobado. Decide conservar el comportamiento antiguo en el cálculo (una función explícita de redondeo, con la regla escrita y probada) y aceptar el orden con plegado de acentos, con aviso al área académica.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-522 — Migraciones de runtime, lenguaje y framework](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md)) son:

- **La suite pasa y los datos cambian** — causa: cambio silencioso no ejercitado por las pruebas. Corrección: escribir sondas con datos reales y ampliar el maestro dorado.
- **El script de reescritura cambió comentarios y textos** — causa: sustitución de texto o expresión regular. Corrección: reescribir por árbol sintáctico y revisar el diff.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-522 — Migraciones de runtime, lenguaje y framework](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con cifras idénticas. Las sondas ejercitan CPython de verdad, pero con datos sintéticos; no se migró ningún sistema real, no se probó otro lenguaje ni un framework, y el calendario de un año con tres años de soporte, la duración de las migraciones y el 30 % de las pequeñas son construcciones del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Plataforma](../p/plataforma.md), [Versión](../v/version.md), [Cambio ruidoso](../c/cambio-ruidoso.md), [Cambio silencioso](../c/cambio-silencioso.md), [Reescritura por estructura](../r/reescritura-por-estructura.md), [Sonda](../s/sonda.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-522 — Migraciones de runtime, lenguaje y framework](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-240](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md), [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md), [SE-176](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md), [SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md), [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md).

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

[↑ Glosario](../../README.md) · [← Matriz de decisión](./matriz-de-decision.md) · [Matriz de soporte →](./matriz-de-soporte.md)
