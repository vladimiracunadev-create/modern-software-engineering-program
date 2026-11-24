# Estructuras persistentes

[↑ Glosario](../../README.md) · [← Estructuras enlazadas](./estructuras-enlazadas.md) · [ETag →](./etag.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

Una **estructura persistente** es una estructura de datos en la que **una actualización produce una nueva versión que comparte partes inmutables con la anterior**, de modo que las versiones previas siguen disponibles sin haber sido modificadas ([SE-093](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md)). La palabra «persistente» designa aquí **conservar versiones**, no necesariamente guardar en disco: una estructura persistente puede vivir solo en memoria. Es un uso técnico distinto del coloquial «persistencia» de datos en una base de datos.

## Por qué importa

Cuando se necesita conservar el estado anterior (para deshacer, para auditar, para razonar sobre versiones o para compartir datos entre hilos sin bloquear), copiar la estructura completa en cada cambio es caro. Una estructura persistente ofrece versiones baratas porque **comparte** lo que no cambió. La decisión que cambia es cómo se maneja el historial: en lugar de mutar y perder el pasado, se produce un valor nuevo y se conservan ambos. Al ser inmutables, las versiones antiguas pueden leerse concurrentemente sin riesgo.

## Cómo funciona

El mecanismo más sencillo es la **copia del camino** (*path copying*) en un árbol: para «cambiar» una hoja se crean copias solo de los nodos desde la raíz hasta esa hoja; el resto de los nodos se comparte entre la versión vieja y la nueva. La nueva raíz es la nueva versión; la raíz antigua sigue válida. Como ningún nodo compartido se modifica, la versión anterior permanece intacta.

Esto tiene un costo y un beneficio medibles. El costo de una actualización es proporcional a la altura del árbol (`O(log n)` si está equilibrado). El beneficio es memoria: se almacenan los nodos copiados, no la estructura completa. El costo oculto, que [SE-093](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md) advierte, es que **compartir retiene memoria mientras haya referencias a raíces antiguas**: una versión vieja que sigue referenciada mantiene vivos todos sus nodos, incluidos los que la versión nueva ya no usa.

## Ejemplo

[SE-093](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md) mide esto con un árbol binario equilibrado de 4 095 nodos. Al insertar una clave copiando solo el camino desde la raíz, se crearon **13 nodos nuevos** y **4 083 quedaron compartidos** entre las dos versiones; en memoria existen 4 108 nodos distintos, no 8 190 (el doble). Copiar la lista completa de 4 095 referencias tardó entre 13,6 y 19,0 µs y copiar el camino entre 6,6 y 16,0 µs: el **tiempo fue parecido**; la ganancia es de memoria y de poder conservar ambas versiones.

```python
class Nodo:
    __slots__ = ("clave", "izq", "der")
    def __init__(self, clave, izq=None, der=None):
        self.clave, self.izq, self.der = clave, izq, der

def insertar(n, k):           # devuelve una raíz nueva; no muta n
    if n is None: return Nodo(k)
    if k < n.clave: return Nodo(n.clave, insertar(n.izq, k), n.der)
    return Nodo(n.clave, n.izq, insertar(n.der, k))
```

Solo se copian los nodos del camino; los subárboles no visitados se comparten.

## Errores y confusiones comunes

- **Confundir persistente con guardado en disco.** El término habla de versiones, no de almacenamiento.
- **Esperar que sea más rápida.** En la medición, el tiempo fue parecido; lo que se gana es memoria y versiones.
- **Olvidar que las raíces antiguas retienen memoria.** Una referencia olvidada a una versión vieja evita liberar sus nodos.
- **Mutar un nodo compartido.** Rompe la garantía para todas las versiones que lo comparten.

## Límites y cuándo no aplica

Si no hace falta conservar versiones, una estructura mutable es más simple y suele ser más rápida en constantes. Las estructuras persistentes añaden asignaciones y punteros y empeoran la localidad frente a un arreglo. Y el ahorro de memoria depende de que los cambios sean pequeños respecto del total: si cada actualización toca casi todo, no hay nada que compartir. La clase advierte que una garantía teórica no predice constantes ni la distribución real; se mide.

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
