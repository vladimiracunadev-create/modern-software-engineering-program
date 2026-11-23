# Árbol, raíz y subárbol

[↑ Glosario](../../README.md) · [← Árbol de utilidad](./arbol-de-utilidad.md) · [Archivo de bloqueo →](./archivo-de-bloqueo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

Un árbol conecta nodos sin ciclos mediante relación padre-hijo y ofrece un camino único desde la raíz.

Definición de trabajo de [SE-088 — Árboles, tries y estructuras jerárquicas](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md).

## Por qué importa

En [SE-088 — Árboles, tries y estructuras jerárquicas](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md), el tema «Árbol, raíz y subárbol» importa porque un árbol conecta nodos sin ciclos mediante relación padre-hijo y ofrece un camino único desde la raíz.

## Cómo funciona

Según [SE-088 — Árboles, tries y estructuras jerárquicas](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md), en la sección «Árbol, raíz y subárbol»:

Un árbol conecta nodos sin ciclos mediante relación padre-hijo y ofrece un camino único desde la raíz. Profundidad, altura y grado describen forma. Una jerarquía organizacional puede no ser árbol si un nodo tiene varios padres; forzarla pierde relaciones.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-088 — Árboles, tries y estructuras jerárquicas](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md):

En la biblioteca de estructuras y algoritmos, un caso conserva identidad, prioridad, dependencias, instante de llegada y estado de resolución. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-088 — Árboles, tries y estructuras jerárquicas](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md)) son:

- **Inserción lenta y `RecursionError` con datos ordenados** — causa: BST sin balanceo con entrada ordenada. Corrección: equilibrar, barajar o usar una lista ordenada; probar las tres entradas.
- **El trie consume más memoria que la lista de datos** — causa: un diccionario por carácter paga cabecera por nodo. Corrección: medir con `tracemalloc` y valorar bisect o un trie comprimido.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-088 — Árboles, tries y estructuras jerárquicas](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md)) son: Las definiciones son operativas para la biblioteca de estructuras y algoritmos. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Un árbol representa jerarquía, no dependencias arbitrarias o múltiples rutas. La siguiente clase generaliza a grafos y recorridos.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Árbol](./arbol.md), [Ciclo](../c/ciclo.md), [Raíz](../r/raiz.md), [Relación](../r/relacion.md), [Árbol de búsqueda](./arbol-de-busqueda.md), [Balance y rotaciones](../b/balance-y-rotaciones.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-088 — Árboles, tries y estructuras jerárquicas](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md) — [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md), Estructuras de datos y algoritmos.

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

[↑ Glosario](../../README.md) · [← Árbol de utilidad](./arbol-de-utilidad.md) · [Archivo de bloqueo →](./archivo-de-bloqueo.md)
