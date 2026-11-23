# Puntuación de mutación

[↑ Glosario](../../README.md) · [← Puntuación de Brier](./puntuacion-de-brier.md) · [QA / Test Automation Engineer →](../q/qa-test-automation-engineer.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Fracción de mutantes no equivalentes que alguna prueba mata.

Definición de trabajo de [SE-426 — Mutación, fuzzing y generación de casos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-307 — Refactorización segura apoyada por pruebas](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md): Fracción de mutantes no equivalentes que una suite detecta.

## Por qué importa

En [SE-426 — Mutación, fuzzing y generación de casos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), el tema «Puntuación de mutación» importa porque mide detección, no ejecución.

## Cómo funciona

Según [SE-426 — Mutación, fuzzing y generación de casos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), en la sección «Puntuación de mutación»:

Es la fracción de mutantes no equivalentes que alguna prueba mata. Responde a una pregunta distinta de la cobertura: no «¿se ejecutó esta línea?» sino «si esta línea cambia, ¿falla algo?». Para una batería con aserciones débiles, la diferencia es grande: ejecutar todas las líneas y no comprobar casi ningún valor da cobertura alta y puntuación baja. La puntuación no es una probabilidad de detectar defectos reales; es una comparación entre baterías sobre el mismo conjunto de mutantes.

## Ejemplo

Ejemplo de [SE-307 — Refactorización segura apoyada por pruebas](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md) (sección «Caso conductor»):

El componente `tarifas` conserva el diagnóstico de `SE-306` y gana una red de pruebas con una puntuación de mutación medida, valores de borde derivados del código y una comparación con la versión anterior. `SE-308` examinará cómo diseñar para el cambio, la prueba y la operación desde el principio. Cambia después una sola decisión, el tamaño del paso, y observa cuántos sospechosos tiene el primer fallo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La cobertura sube y los mutantes muertos no** — causa: se añadieron casos que ejecutan líneas sin afirmar fronteras. Corrección: medir la puntuación de mutación al añadir casos. ([SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-426 — Mutación, fuzzing y generación de casos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con un módulo sintético de 21 líneas, 18 mutantes y cuatro defectos escritos por el autor, en Windows y Ubuntu (WSL2), con salidas idénticas. No se usó una herramienta de mutación ni un fuzzer real, y los generadores estructurado y guiado contienen valores que el autor sabía que importaban. La equivalencia se decidió con una rejilla finita.

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
