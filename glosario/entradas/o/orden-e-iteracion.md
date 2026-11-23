# Orden e iteración

[↑ Glosario](../../README.md) · [← Orden de resolución de métodos](./orden-de-resolucion-de-metodos.md) · [Orden global de adquisición →](./orden-global-de-adquisicion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

Python garantiza orden de inserción en `dict`, pero `set` no promete orden estable entre ejecuciones.

Definición de trabajo de [SE-087 — Tablas hash, mapas y conjuntos](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-087-tablas-hash-mapas-y-conjuntos/README.md).

## Por qué importa

En [SE-087 — Tablas hash, mapas y conjuntos](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-087-tablas-hash-mapas-y-conjuntos/README.md), el tema «Orden e iteración» importa porque python garantiza orden de inserción en `dict`, pero `set` no promete orden estable entre ejecuciones.

## Cómo funciona

Según [SE-087 — Tablas hash, mapas y conjuntos](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-087-tablas-hash-mapas-y-conjuntos/README.md), en la sección «Orden e iteración»:

Python garantiza orden de inserción en `dict`, pero `set` no promete orden estable entre ejecuciones. Usar el orden observado de un conjunto como desempate crea pruebas frágiles. Si el orden importa, debe representarse explícitamente.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-087 — Tablas hash, mapas y conjuntos](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-087-tablas-hash-mapas-y-conjuntos/README.md):

En la biblioteca de estructuras y algoritmos, un caso conserva identidad, prioridad, dependencias, instante de llegada y estado de resolución. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-087 — Tablas hash, mapas y conjuntos](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-087-tablas-hash-mapas-y-conjuntos/README.md)) son:

- **Una búsqueda en un `dict` falla para una clave que «seguro» se insertó** — causa: la clave se mutó después de insertarla. Corrección: usar claves inmutables o un identificador estable; añadir una prueba que mute y busque.
- **El orden de salida cambia entre ejecuciones** — causa: se itera un `set` de cadenas con hash aleatorizado. Corrección: ordenar explícitamente antes de producir resultados.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-087 — Tablas hash, mapas y conjuntos](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-087-tablas-hash-mapas-y-conjuntos/README.md)) son: Las definiciones son operativas para la biblioteca de estructuras y algoritmos. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Las tablas hash no mantienen rangos ni prefijos ordenados. La siguiente clase estudia árboles, tries y jerarquías con invariantes estructurales.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Factor de carga y crecimiento](../f/factor-de-carga-y-crecimiento.md), [Función hash y buckets](../f/funcion-hash-y-buckets.md), [Igualdad y estabilidad](../i/igualdad-y-estabilidad.md), [Mapa y conjunto](../m/mapa-y-conjunto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-087 — Tablas hash, mapas y conjuntos](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-087-tablas-hash-mapas-y-conjuntos/README.md) — [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md), Estructuras de datos y algoritmos.

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

[↑ Glosario](../../README.md) · [← Orden de resolución de métodos](./orden-de-resolucion-de-metodos.md) · [Orden global de adquisición →](./orden-global-de-adquisicion.md)
