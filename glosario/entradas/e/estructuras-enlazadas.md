# Estructuras enlazadas

[↑ Glosario](../../README.md) · [← Estructura del paquete](./estructura-del-paquete.md) · [Estructuras persistentes →](./estructuras-persistentes.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

Los nodos enlazados insertan localmente cuando ya se posee el nodo, pero localizar una posición sigue siendo lineal.

Definición de trabajo de [SE-085 — Arreglos, listas y secuencias](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md).

## Por qué importa

En [SE-085 — Arreglos, listas y secuencias](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md), el tema «Estructuras enlazadas» importa porque los nodos enlazados insertan localmente cuando ya se posee el nodo, pero localizar una posición sigue siendo lineal.

## Cómo funciona

Según [SE-085 — Arreglos, listas y secuencias](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md), en la sección «Estructuras enlazadas»:

Los nodos enlazados insertan localmente cuando ya se posee el nodo, pero localizar una posición sigue siendo lineal. Punteros, asignaciones y mala localidad pueden superar la ventaja teórica. En Python, la lista incorporada no es una linked list.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-085 — Arreglos, listas y secuencias](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md):

En la biblioteca de estructuras y algoritmos, un caso conserva identidad, prioridad, dependencias, instante de llegada y estado de resolución. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-085 — Arreglos, listas y secuencias](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md)) son:

- **Vaciar una cola de 80 000 elementos tarda casi un segundo** — causa: se usa `lista.pop(0)` como operación dominante. Corrección: cambiar a `deque.popleft()` y repetir la medición con la misma carga.
- **Tres filas de una cuadrícula cambian a la vez** — causa: `[[0]] * 3` repite la misma lista interna. Corrección: construir con `[[0] for _ in range(3)]` y probar una escritura aislada.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La estructura enlazada insertaría en `O(1)` si ya tuviéramos el nodo, pero localizar una posición sigue siendo lineal y cada salto de puntero es un acceso a memoria que la caché no puede anticipar. ([SE-085](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Arreglo contiguo y localidad](../a/arreglo-contiguo-y-localidad.md), [Interfaz de secuencia](../i/interfaz-de-secuencia.md), [Lista dinámica y capacidad](../l/lista-dinamica-y-capacidad.md), [Slicing, vistas y copias](../s/slicing-vistas-y-copias.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-085 — Arreglos, listas y secuencias](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md) — [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md), Estructuras de datos y algoritmos.

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

[↑ Glosario](../../README.md) · [← Estructura del paquete](./estructura-del-paquete.md) · [Estructuras persistentes →](./estructuras-persistentes.md)
