# Problema del oráculo

[↑ Glosario](../../README.md) · [← Probe](./probe.md) · [Problemas →](./problemas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Dificultad de decidir si la salida de un programa es correcta sin una fuente de verdad distinta del programa.

Definición de trabajo de [SE-558 — Generación de pruebas, documentación y migraciones](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md).

## Por qué importa

La clase donde se define, [SE-558 — Generación de pruebas, documentación y migraciones](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md), existe con este propósito: la clase existe para que veas que las pruebas, la documentación y las migraciones comparten una propiedad peligrosa cuando las genera un asistente: su resultado tiene aspecto de verificación o de información fiable sin serlo.

## Cómo funciona

Según [SE-558 — Generación de pruebas, documentación y migraciones](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md):

Una prueba compara el resultado de ejecutar el código con un resultado esperado, y de dónde sale ese resultado esperado es la cuestión central. Barr y sus coautores llaman a esto el problema del oráculo: decidir si una salida es correcta exige una fuente de verdad distinta del programa mismo. Cuando el esperado se obtiene ejecutando el código, la prueba no comprueba nada, solo congela el comportamiento actual. Congelar tiene un uso legítimo: una **prueba de caracterización** (`SE-519`) fija lo que el sistema hace antes de modificarlo, a sabiendas de que puede ser incorrecto. Pero llamarla prueba de corrección es un error.

## Ejemplo

Caso medido en la sección «El problema del oráculo» de [SE-558 — Generación de pruebas, documentación y migraciones](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md):

Una prueba compara el resultado de ejecutar el código con un resultado esperado, y de dónde sale ese resultado esperado es la cuestión central. Barr y sus coautores llaman a esto el problema del oráculo: decidir si una salida es correcta exige una fuente de verdad distinta del programa mismo. Cuando el esperado se obtiene ejecutando el código, la prueba no comprueba nada, solo congela el comportamiento actual. Congelar tiene un uso legítimo: una **prueba de caracterización** (`SE-519`) fija lo que el sistema hace antes de modificarlo, a sabiendas de que puede ser incorrecto.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-558 — Generación de pruebas, documentación y migraciones](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md)) son:

- **Todas las pruebas pasan y un cambio de comportamiento pasa inadvertido** — causa: esperados copiados del código. Corrección: esperados calculados a mano desde la especificación.
- **Cobertura del 100 % y defectos sin detectar** — causa: se midió ejecución, no detección. Corrección: medir con mutantes.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-558 — Generación de pruebas, documentación y migraciones](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: ocho mutantes ejecutados contra dos suites, `doctest` real sobre módulos generados y una migración real en SQLite en memoria.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-557](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Fuente de verdad](../f/fuente-de-verdad.md), [Cuarentena](../c/cuarentena.md), [Documentación ejecutable](../d/documentacion-ejecutable.md), [Migración](../m/migracion.md), [Prueba de caracterización](./prueba-de-caracterizacion.md), [Variante defectuosa](../v/variante-defectuosa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-558 — Generación de pruebas, documentación y migraciones](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-559](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Barr et al., «The Oracle Problem in Software Testing: A Survey»](https://doi.org/10.1109/TSE.2014.2372785) — el problema del oráculo; autoridad: IEEE Transactions on Software Engineering.
- [Jia y Harman, «An Analysis and Survey of the Development of Mutation Testing»](https://doi.org/10.1109/TSE.2010.62) — pruebas de mutación; autoridad: IEEE Transactions on Software Engineering.
- [Python: doctest](https://docs.python.org/3/library/doctest.html) — ejecución de ejemplos en docstrings; autoridad: documentación de Python.
- [SQLite: datatypes](https://www.sqlite.org/datatype3.html) — tipificación y afinidad; autoridad: documentación de SQLite.
- [SQLite: expresiones y CAST](https://www.sqlite.org/lang_expr.html) — conversiones con CAST; autoridad: documentación de SQLite.

---

[↑ Glosario](../../README.md) · [← Probe](./probe.md) · [Problemas →](./problemas.md)
