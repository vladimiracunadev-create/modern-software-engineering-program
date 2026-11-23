# Recomendación condicionada

[↑ Glosario](../../README.md) · [← Rechazo implícito](./rechazo-implicito.md) · [Recomposición →](./recomposicion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

La conclusión usa forma `si carga y garantía, entonces opción; si cambia umbral, revisar`.

Definición de trabajo de [SE-095 — Taller: elegir por carga y no por costumbre](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-095-taller-elegir-por-carga-y-no-por-costumbre/README.md).

## Por qué importa

En [SE-095 — Taller: elegir por carga y no por costumbre](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-095-taller-elegir-por-carga-y-no-por-costumbre/README.md), el tema «Recomendación condicionada» importa porque la conclusión usa forma `si carga y garantía, entonces opción; si cambia umbral, revisar`.

## Cómo funciona

Según [SE-095 — Taller: elegir por carga y no por costumbre](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-095-taller-elegir-por-carga-y-no-por-costumbre/README.md), en la sección «Recomendación condicionada»:

La conclusión usa forma `si carga y garantía, entonces opción; si cambia umbral, revisar`. Declarar condiciones evita convertir un benchmark del taller en estándar universal. Los datos y scripts quedan junto al informe.

## Ejemplo

Ejemplo de [SE-095 — Taller: elegir por carga y no por costumbre](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-095-taller-elegir-por-carga-y-no-por-costumbre/README.md) (sección «Preguntas frecuentes»):

Un perfil de operaciones, una matriz de compromisos con mediciones y una recomendación condicionada con la medición que la invalidaría.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-095 — Taller: elegir por carga y no por costumbre](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-095-taller-elegir-por-carga-y-no-por-costumbre/README.md)) son:

- **La recomendación no convence a otro equipo** — causa: no declara la carga ni el tamaño. Corrección: escribir perfil de operaciones y tamaños antes de medir.
- **Se elige `set` para todo** — causa: se ignoró el costo de construirlo y la memoria. Corrección: calcular el umbral de reutilización y la memoria.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-095 — Taller: elegir por carga y no por costumbre](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-095-taller-elegir-por-carga-y-no-por-costumbre/README.md)) son: Las definiciones son operativas para la biblioteca de estructuras y algoritmos. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. El taller cubre cargas sintéticas y una plataforma. El proyecto siguiente empaqueta alternativas, propiedades y benchmarks para revisión reproducible.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Garantía](../g/garantia.md), [Opción](../o/opcion.md), [Candidatos equivalentes](../c/candidatos-equivalentes.md), [Cargas adversarias](../c/cargas-adversarias.md), [Matriz de compromisos](../m/matriz-de-compromisos.md), [Perfil de operaciones](../p/perfil-de-operaciones.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-095 — Taller: elegir por carga y no por costumbre](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-095-taller-elegir-por-carga-y-no-por-costumbre/README.md) — [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md), Estructuras de datos y algoritmos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MIT 6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — Estructuras, algoritmos, corrección y análisis de complejidad; autoridad: MIT OpenCourseWare.
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html) — Semántica de secuencias, conjuntos, mappings, igualdad y hash; autoridad: Python Software Foundation.
- [Python Standard Library](https://docs.python.org/3/library/index.html) — Deque, heapq, bisect, graphlib y contenedores disponibles; autoridad: Python Software Foundation.
- [Python Debugging and Profiling](https://docs.python.org/3/library/debug.html) — Timeit, cprofile y tracemalloc con sus límites; autoridad: Python Software Foundation.
- [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — Inducción, grafos, conteo y razonamiento discreto; autoridad: MIT OpenCourseWare.

---

[↑ Glosario](../../README.md) · [← Rechazo implícito](./rechazo-implicito.md) · [Recomposición →](./recomposicion.md)
