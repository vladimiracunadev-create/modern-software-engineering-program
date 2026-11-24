# Puntuación de mutación

[↑ Glosario](../../README.md) · [← Puntuación de Brier](./puntuacion-de-brier.md) · [QA / Test Automation Engineer →](../q/qa-test-automation-engineer.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

La **puntuación de mutación** es la fracción de mutantes no equivalentes que alguna prueba mata ([SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md)). [SE-307](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md) la usa en el mismo sentido: la fracción de mutantes no equivalentes que una batería detecta. Mide la capacidad de una batería de pruebas para notar cambios en el código.

## Por qué importa

La cobertura de líneas dice qué se ejecutó, no qué se comprobó. Una batería puede ejecutar todo y afirmar casi nada. La puntuación de mutación responde a otra pregunta: si esta línea cambia, ¿falla algo? La decisión que cambia es cómo se valora una batería de pruebas: por lo que detecta, no por lo que recorre.

## Cómo funciona

Un **mutante** es una copia del programa con un cambio pequeño y deliberado (invertir una comparación, cambiar un `<` por `<=`). Si alguna prueba falla con el mutante, está **muerto**; si todas pasan, sobrevive. Algunos mutantes son **equivalentes**: se comportan igual que el original y ninguna prueba puede distinguirlos; se excluyen del cálculo. La puntuación es:

mutantes muertos ÷ mutantes no equivalentes.

[SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md) explica por qué difiere de la cobertura. Para una batería con aserciones débiles, la diferencia es grande: ejecutar todas las líneas y no comprobar casi ningún valor da cobertura alta y puntuación baja. Por eso añadir casos que ejecutan líneas sin afirmar fronteras sube la cobertura pero no la cantidad de mutantes muertos; la corrección es medir la puntuación al añadir casos.

La clase aclara su sentido: la puntuación no es una probabilidad de detectar defectos reales; es una **comparación entre baterías sobre el mismo conjunto de mutantes**. [SE-307](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md) la usa como red de seguridad antes de refactorizar: si la puntuación es baja, la batería no detectaría un cambio de comportamiento.

## Ejemplo

El módulo sintético de [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md) tiene 21 líneas, 18 mutantes y cuatro defectos escritos por el autor. Una batería recorre todas las líneas (cobertura del 100 %) pero solo mata una parte de los mutantes, porque casi no comprueba valores de frontera. Al añadir casos que afirman los bordes, la puntuación sube. Un mutante que cambia `<` por `<=` sobrevive hasta que un caso lo prueba en el valor exacto.

## Errores y confusiones comunes

- **La cobertura sube y los mutantes muertos no**: se añadieron casos que ejecutan líneas sin afirmar fronteras; se corrige midiendo la puntuación de mutación.
- **Tratarla como probabilidad de hallar defectos reales**.
- **Contar los equivalentes** como supervivientes: falsean la puntuación a la baja.
- **Perseguir el 100 %**: el último tramo suele ser equivalentes o de poco valor.

## Límites y cuándo no aplica

[SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md) precisa que usó un módulo sintético de 21 líneas, 18 mutantes y cuatro defectos del autor, sin herramienta de mutación ni fuzzer real; los generadores contienen valores que el autor sabía que importaban, y la equivalencia se decidió con una rejilla finita. Decidir si un mutante es equivalente puede ser indecidible en general. Generar y ejecutar mutantes cuesta tiempo, lo que obliga a acotar el alcance en bases de código grandes.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-306](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Variante defectuosa](../v/variante-defectuosa.md), [Corpus](../c/corpus.md), [Fuzzing](../f/fuzzing.md), [Mutante equivalente](../m/mutante-equivalente.md), [Red de pruebas](../r/red-de-pruebas.md), [Refactorización](../r/refactorizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-307 — Refactorización segura apoyada por pruebas](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-426 — Mutación, fuzzing y generación de casos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md), [SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [DeMillo, Lipton y Sayward, «Hints on test data selection»](https://doi.org/10.1109/C-M.1978.218136) — origen del análisis de mutantes; autoridad: artículo original de 1978.
- [Jia y Harman, «An analysis and survey of the development of mutation testing»](https://doi.org/10.1109/TSE.2010.62) — panorama de la prueba de mutación; autoridad: artículo revisado de IEEE TSE.
- [Petrović e Ivanković, «State of Mutation Testing at Google»](https://research.google/pubs/state-of-mutation-testing-at-google/) — mutación a gran escala; autoridad: Google Research.
- [Inozemtseva y Holmes, «Coverage is not strongly correlated with test suite effectiveness»](https://doi.org/10.1145/2568225.2568271) — cobertura y eficacia; autoridad: artículo revisado de ICSE 2014.
- [Miller et al., «An empirical study of the reliability of UNIX utilities»](https://doi.org/10.1145/96267.96279) — origen del fuzzing; autoridad: artículo original de Communications of the ACM.

---

[↑ Glosario](../../README.md) · [← Puntuación de Brier](./puntuacion-de-brier.md) · [QA / Test Automation Engineer →](../q/qa-test-automation-engineer.md)
