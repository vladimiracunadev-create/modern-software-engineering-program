# Selección parcial

[↑ Glosario](../../README.md) · [← Selección de campos](./seleccion-de-campos.md) · [Selección por cliente →](./seleccion-por-cliente.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

Para top-k, un heap de tamaño `k` evita ordenar todo y usa espacio acotado.

Definición de trabajo de [SE-090 — Búsqueda, ordenamiento y selección](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md).

## Por qué importa

En [SE-090 — Búsqueda, ordenamiento y selección](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md), el tema «Selección parcial» importa porque para top-k, un heap de tamaño `k` evita ordenar todo y usa espacio acotado.

## Cómo funciona

Según [SE-090 — Búsqueda, ordenamiento y selección](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md), en la sección «Selección parcial»:

Para top-k, un heap de tamaño `k` evita ordenar todo y usa espacio acotado. Quickselect ofrece selección esperada lineal bajo pivotes adecuados. La mejor opción depende de si llegan datos en streaming, si k cambia y si se necesita salida ordenada.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-090 — Búsqueda, ordenamiento y selección](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md):

En la biblioteca de estructuras y algoritmos, un caso conserva identidad, prioridad, dependencias, instante de llegada y estado de resolución. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-090 — Búsqueda, ordenamiento y selección](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md)) son:

- **El ordenamiento propio es lento con datos casi ordenados** — causa: pivote fijo en un quicksort ingenuo. Corrección: usar `sorted` o un pivote aleatorio; probar con entrada ordenada.
- **El resultado «ordenado» no está ordenado** — causa: hay NaN o un comparador no transitivo. Corrección: normalizar el criterio y verificar con una prueba de orden total.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-090 — Búsqueda, ordenamiento y selección](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md)) son: Las definiciones son operativas para la biblioteca de estructuras y algoritmos. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Elegir top-k no resuelve decisiones secuenciales con subproblemas o restricciones. La siguiente clase compara estrategias voraces y programación dinámica.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Heap](../h/heap.md), [Búsqueda lineal y binaria](../b/busqueda-lineal-y-binaria.md), [Contrato de comparación](../c/contrato-de-comparacion.md), [Estabilidad](../e/estabilidad.md), [Familias de ordenamiento](../f/familias-de-ordenamiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-090 — Búsqueda, ordenamiento y selección](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md) — [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md), Estructuras de datos y algoritmos.

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

[↑ Glosario](../../README.md) · [← Selección de campos](./seleccion-de-campos.md) · [Selección por cliente →](./seleccion-por-cliente.md)
