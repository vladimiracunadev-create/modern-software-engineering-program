# Estructuras persistentes

[↑ Glosario](../../README.md) · [← Estructuras enlazadas](./estructuras-enlazadas.md) · [ETag →](./etag.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

Una actualización produce nueva versión compartiendo partes inmutables con la anterior.

Definición de trabajo de [SE-093 — Índices, probabilísticas y estructuras persistentes](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md).

## Por qué importa

En [SE-093 — Índices, probabilísticas y estructuras persistentes](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md), el tema «Estructuras persistentes» importa porque una actualización produce nueva versión compartiendo partes inmutables con la anterior.

## Cómo funciona

Según [SE-093 — Índices, probabilísticas y estructuras persistentes](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md), en la sección «Estructuras persistentes»:

Una actualización produce nueva versión compartiendo partes inmutables con la anterior. Persistente aquí significa conservar versiones, no necesariamente guardar en disco. Compartir reduce copia pero retiene memoria mientras haya referencias a raíces antiguas.

## Ejemplo

Caso medido en la sección «Estructuras persistentes: compartir en vez de copiar» de [SE-093 — Índices, probabilísticas y estructuras persistentes](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md):

Una estructura persistente conserva versiones anteriores sin mutarlas. Construimos un árbol binario balanceado de 4 095 nodos e insertamos una clave copiando solo el camino desde la raíz: se crearon 13 nodos nuevos y 4 083 nodos quedaron compartidos entre las dos versiones; en memoria existen 4 108 nodos distintos, no 8 190. Copiar la lista completa de 4 095 referencias (un `memcpy`) tardó entre 13,6 y 19,0 µs y copiar el camino entre 6,6 y 16,0 µs: el tiempo fue parecido, la ganancia es de memoria y de poder conservar ambas versiones.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-093 — Índices, probabilísticas y estructuras persistentes](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md)) son:

- **La consulta sigue lenta tras crear el índice** — causa: poca selectividad o el planificador no lo usa. Corrección: leer `EXPLAIN QUERY PLAN` y medir con y sin índice.
- **Un filtro de Bloom reporta «posiblemente» demasiado a menudo** — causa: pocos bits por elemento o demasiadas inserciones. Corrección: dimensionar `m` y `k` según el error objetivo y verificar con ausentes.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una estructura persistente conserva versiones anteriores sin mutarlas. ([SE-093](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Versión](../v/version.md), [Bloom filter](../b/bloom-filter.md), [Índice como proyección](../i/indice-como-proyeccion.md), [Índices ordenados y consultas de rango](../i/indices-ordenados-y-consultas-de-rango.md), [Sketches y aproximación](../s/sketches-y-aproximacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-093 — Índices, probabilísticas y estructuras persistentes](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md) — [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md), Estructuras de datos y algoritmos.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-076](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md), [SE-092](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md), [SE-094](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-094-complejidad-empirica-benchmarks-y-perfiles/README.md).

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

[↑ Glosario](../../README.md) · [← Estructuras enlazadas](./estructuras-enlazadas.md) · [ETag →](./etag.md)
