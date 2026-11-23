# Índices ordenados y consultas de rango

[↑ Glosario](../../README.md) · [← Índice secundario](./indice-secundario.md) · [Inferencia →](./inferencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

Un índice ordenado localiza fronteras y recorre un intervalo sin escanear todo.

Definición de trabajo de [SE-093 — Índices, probabilísticas y estructuras persistentes](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md).

## Por qué importa

En [SE-093 — Índices, probabilísticas y estructuras persistentes](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md), el tema «Índices ordenados y consultas de rango» importa porque un índice ordenado localiza fronteras y recorre un intervalo sin escanear todo.

## Cómo funciona

Según [SE-093 — Índices, probabilísticas y estructuras persistentes](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md), en la sección «Índices ordenados y consultas de rango»:

Un índice ordenado localiza fronteras y recorre un intervalo sin escanear todo. Mantenerlo encarece escritura y requiere coherencia con la fuente. `bisect` encuentra posición logarítmica en una lista, pero insertar sigue siendo lineal por desplazamiento.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-093 — Índices, probabilísticas y estructuras persistentes](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md):

En la biblioteca de estructuras y algoritmos, un caso conserva identidad, prioridad, dependencias, instante de llegada y estado de resolución. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-093 — Índices, probabilísticas y estructuras persistentes](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md)) son:

- **La consulta sigue lenta tras crear el índice** — causa: poca selectividad o el planificador no lo usa. Corrección: leer `EXPLAIN QUERY PLAN` y medir con y sin índice.
- **Un filtro de Bloom reporta «posiblemente» demasiado a menudo** — causa: pocos bits por elemento o demasiadas inserciones. Corrección: dimensionar `m` y `k` según el error objetivo y verificar con ausentes.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-093 — Índices, probabilísticas y estructuras persistentes](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md)) son: Las definiciones son operativas para la biblioteca de estructuras y algoritmos. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Una garantía teórica no predice constantes, asignaciones ni distribución real. La siguiente clase diseña medición empírica y perfilado sin sesgos obvios.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Frontera](../f/frontera.md), [Índice](./indice.md), [Intervalo](./intervalo.md), [Bloom filter](../b/bloom-filter.md), [Estructuras persistentes](../e/estructuras-persistentes.md), [Índice como proyección](./indice-como-proyeccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-093 — Índices, probabilísticas y estructuras persistentes](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md) — [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md), Estructuras de datos y algoritmos.

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

[↑ Glosario](../../README.md) · [← Índice secundario](./indice-secundario.md) · [Inferencia →](./inferencia.md)
