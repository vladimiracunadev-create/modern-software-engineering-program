# Dfs, ciclos y orden

[↑ Glosario](../../README.md) · [← DevOps Engineer](./devops-engineer.md) · [Día de práctica →](./dia-de-practica.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

Dfs usa pila implícita o explícita y profundiza antes de retroceder.

Definición de trabajo de [SE-089 — Grafos y recorridos](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-089-grafos-y-recorridos/README.md).

## Por qué importa

En [SE-089 — Grafos y recorridos](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-089-grafos-y-recorridos/README.md), el tema «DFS, ciclos y orden» importa porque DFS usa pila implícita o explícita y profundiza antes de retroceder.

## Cómo funciona

Según [SE-089 — Grafos y recorridos](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-089-grafos-y-recorridos/README.md), en la sección «DFS, ciclos y orden»:

DFS usa pila implícita o explícita y profundiza antes de retroceder. Colores o estados distinguen no visto, activo y terminado para detectar ciclos dirigidos. Un conjunto visitado simple puede perder la diferencia necesaria para explicar un back edge.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-089 — Grafos y recorridos](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-089-grafos-y-recorridos/README.md):

En la biblioteca de estructuras y algoritmos, un caso conserva identidad, prioridad, dependencias, instante de llegada y estado de resolución. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-089 — Grafos y recorridos](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-089-grafos-y-recorridos/README.md)) son:

- **El «camino más corto» devuelto es largo** — causa: se usó DFS donde se necesitaba BFS. Corrección: usar BFS (sin pesos) y comprobarlo contra una fórmula conocida en rejillas.
- **El recorrido no termina o repite nodos** — causa: falta el conjunto de visitados. Corrección: marcar al encolar y probar un ciclo mínimo.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-089 — Grafos y recorridos](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-089-grafos-y-recorridos/README.md)) son: Las definiciones son operativas para la biblioteca de estructuras y algoritmos. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. BFS no resuelve pesos negativos ni toda forma de optimización de caminos. La siguiente clase contrasta búsqueda, ordenamiento y selección bajo contratos precisos.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Bfs y distancia no ponderada](../b/bfs-y-distancia-no-ponderada.md), [Componentes y alcanzabilidad](../c/componentes-y-alcanzabilidad.md), [Lista y matriz de adyacencia](../l/lista-y-matriz-de-adyacencia.md), [Vértices, aristas y dirección](../v/vertices-aristas-y-direccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-089 — Grafos y recorridos](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-089-grafos-y-recorridos/README.md) — [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md), Estructuras de datos y algoritmos.

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

[↑ Glosario](../../README.md) · [← DevOps Engineer](./devops-engineer.md) · [Día de práctica →](./dia-de-practica.md)
