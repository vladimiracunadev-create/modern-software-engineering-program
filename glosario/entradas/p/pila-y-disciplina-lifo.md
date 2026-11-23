# Pila y disciplina lifo

[↑ Glosario](../../README.md) · [← Pila de PR](./pila-de-pr.md) · [Pipeline →](./pipeline.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

Una pila expone `push`, `pop` y `peek`; el último elemento entra primero en salir.

Definición de trabajo de [SE-086 — Pilas, colas, deques y prioridades](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-086-pilas-colas-deques-y-prioridades/README.md).

## Por qué importa

En [SE-086 — Pilas, colas, deques y prioridades](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-086-pilas-colas-deques-y-prioridades/README.md), el tema «Pila y disciplina LIFO» importa porque una pila expone `push`, `pop` y `peek`; el último elemento entra primero en salir.

## Cómo funciona

Según [SE-086 — Pilas, colas, deques y prioridades](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-086-pilas-colas-deques-y-prioridades/README.md), en la sección «Pila y disciplina LIFO»:

Una pila expone `push`, `pop` y `peek`; el último elemento entra primero en salir. Modela deshacer, marcos y exploración en profundidad. Buscar arbitrariamente dentro rompe la abstracción y suele indicar que la carga necesita otra estructura.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-086 — Pilas, colas, deques y prioridades](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-086-pilas-colas-deques-y-prioridades/README.md):

En la biblioteca de estructuras y algoritmos, un caso conserva identidad, prioridad, dependencias, instante de llegada y estado de resolución. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-086 — Pilas, colas, deques y prioridades](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-086-pilas-colas-deques-y-prioridades/README.md)) son:

- **Dos tareas con igual prioridad salen en orden alfabético** — causa: el desempate recae en el texto de la carga útil. Corrección: añadir un contador monótono como segundo elemento de la tupla.
- **`TypeError` solo cuando dos prioridades coinciden** — causa: la comparación llega a cargas útiles no ordenables. Corrección: hacer que la tupla sea totalmente ordenable (prioridad, contador, carga).

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-086 — Pilas, colas, deques y prioridades](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-086-pilas-colas-deques-y-prioridades/README.md)) son: Las definiciones son operativas para la biblioteca de estructuras y algoritmos. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Una cola responde cuál sale después, no cómo encontrar identidad ni evitar duplicados. La siguiente clase añade mapas y conjuntos con contratos de igualdad y hash.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Cola y disciplina fifo](../c/cola-y-disciplina-fifo.md), [Deque y ventanas](../d/deque-y-ventanas.md), [Heap y prioridad parcial](../h/heap-y-prioridad-parcial.md), [Starvation y envejecimiento](../s/starvation-y-envejecimiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-086 — Pilas, colas, deques y prioridades](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-086-pilas-colas-deques-y-prioridades/README.md) — [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md), Estructuras de datos y algoritmos.

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

[↑ Glosario](../../README.md) · [← Pila de PR](./pila-de-pr.md) · [Pipeline →](./pipeline.md)
