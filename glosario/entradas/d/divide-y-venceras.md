# Divide y vencerás

[↑ Glosario](../../README.md) · [← Divergencia](./divergencia.md) · [Divulgación coordinada →](./divulgacion-coordinada.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

Se divide en subproblemas independientes, se resuelven y combinan.

Definición de trabajo de [SE-092 — Backtracking, divide y vencerás](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md).

## Por qué importa

En [SE-092 — Backtracking, divide y vencerás](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md), el tema «Divide y vencerás» importa porque se divide en subproblemas independientes, se resuelven y combinan.

## Cómo funciona

Según [SE-092 — Backtracking, divide y vencerás](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md), en la sección «Divide y vencerás»:

Se divide en subproblemas independientes, se resuelven y combinan. La independencia y el costo de combinar determinan la recurrencia. Llamar divide-and-conquer a cualquier recursión oculta dependencias y resultados duplicados.

## Ejemplo

Caso medido en la sección «Divide y vencerás: profundidad, costo y cuándo no conviene» de [SE-092 — Backtracking, divide y vencerás](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md):

La ordenación por mezcla divide en mitades: con 1 000, 10 000 y 100 000 elementos usó 8 678, 120 398 y 1 536 147 comparaciones, cerca de `n·log₂ n` (9 966; 132 877; 1 660 964), con profundidad de recursión 10, 14 y 17. Si la división es desigual (quitar un elemento cada vez), la profundidad pasa a ser `n`: una recursión de ese tipo con 2 000 elementos agotó la pila con `RecursionError`. Dividir bien es parte de la corrección práctica del algoritmo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **`RecursionError` en divide y vencerás** — causa: partición desigual con profundidad `n`. Corrección: dividir por la mitad o usar iteración. ([SE-092](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md))
- **El esquema divide y vencerás es más lento que un bucle** — causa: constantes de la recursión y copias. Corrección: comparar con la solución lineal antes de adoptar el esquema. ([SE-092](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-092 — Backtracking, divide y vencerás](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md)) son: Las definiciones son operativas para la biblioteca de estructuras y algoritmos. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. La exploración exacta puede seguir siendo intratable. La siguiente clase presenta índices, estructuras probabilísticas y persistentes con garantías explícitas, no magia de rendimiento.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Backtracking](../b/backtracking.md), [Espacio de estados](../e/espacio-de-estados.md), [Poda segura](../p/poda-segura.md), [Recurrencias y umbral práctico](../r/recurrencias-y-umbral-practico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-092 — Backtracking, divide y vencerás](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md) — [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md), Estructuras de datos y algoritmos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-091](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-091-algoritmos-voraces-y-programacion-dinamica/README.md), [SE-093](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md).

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

[↑ Glosario](../../README.md) · [← Divergencia](./divergencia.md) · [Divulgación coordinada →](./divulgacion-coordinada.md)
