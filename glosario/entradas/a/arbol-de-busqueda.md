# Árbol de búsqueda

[↑ Glosario](../../README.md) · [← Árbol de accesibilidad](./arbol-de-accesibilidad.md) · [Árbol de métricas →](./arbol-de-metricas.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

En un bst, claves menores y mayores se separan por subárbol.

Definición de trabajo de [SE-088 — Árboles, tries y estructuras jerárquicas](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md).

## Por qué importa

En [SE-088 — Árboles, tries y estructuras jerárquicas](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md), el tema «Árbol de búsqueda» importa porque en un BST, claves menores y mayores se separan por subárbol.

## Cómo funciona

Según [SE-088 — Árboles, tries y estructuras jerárquicas](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md), en la sección «Árbol de búsqueda»:

En un BST, claves menores y mayores se separan por subárbol. La búsqueda sigue una rama, pero cuesta proporcional a altura. Sin balance, inserciones ordenadas degeneran a lista y convierten el caso esperado logarítmico en lineal.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-088 — Árboles, tries y estructuras jerárquicas](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md):

En la biblioteca de estructuras y algoritmos, un caso conserva identidad, prioridad, dependencias, instante de llegada y estado de resolución. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-088 — Árboles, tries y estructuras jerárquicas](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md)) son:

- **Inserción lenta y `RecursionError` con datos ordenados** — causa: BST sin balanceo con entrada ordenada. Corrección: equilibrar, barajar o usar una lista ordenada; probar las tres entradas.
- **El trie consume más memoria que la lista de datos** — causa: un diccionario por carácter paga cabecera por nodo. Corrección: medir con `tracemalloc` y valorar bisect o un trie comprimido.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-088 — Árboles, tries y estructuras jerárquicas](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md)) son: Las definiciones son operativas para la biblioteca de estructuras y algoritmos. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Un árbol representa jerarquía, no dependencias arbitrarias o múltiples rutas. La siguiente clase generaliza a grafos y recorridos.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Árbol, raíz y subárbol](./arbol-raiz-y-subarbol.md), [Balance y rotaciones](../b/balance-y-rotaciones.md), [Recorridos y serialización](../r/recorridos-y-serializacion.md), [Trie y prefijos](../t/trie-y-prefijos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-088 — Árboles, tries y estructuras jerárquicas](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md) — [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md), Estructuras de datos y algoritmos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-092](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md), [SE-078](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md).

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

[↑ Glosario](../../README.md) · [← Árbol de accesibilidad](./arbol-de-accesibilidad.md) · [Árbol de métricas →](./arbol-de-metricas.md)
