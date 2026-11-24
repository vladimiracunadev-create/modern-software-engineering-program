# Árbol de búsqueda

[↑ Glosario](../../README.md) · [← Árbol de accesibilidad](./arbol-de-accesibilidad.md) · [Árbol de métricas →](./arbol-de-metricas.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

Un **árbol de búsqueda** (en [SE-088](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md), el árbol binario de búsqueda o BST) es un árbol donde cada nodo guarda una clave y separa las demás por subárbol: las menores quedan a un lado y las mayores al otro. La propiedad de orden permite buscar, insertar y borrar siguiendo **una sola rama** desde la raíz. El programa lo enseña como la estructura que muestra, con números, que una garantía asintótica depende de una condición: que el árbol esté equilibrado.

## Por qué importa

La promesa de `O(log n)` para búsqueda es lo que justifica elegir un árbol sobre una lista. Pero esa promesa describe un árbol de altura logarítmica, no cualquier árbol. La decisión profesional que cambia es si se acepta la estructura sin comprobar cómo llegan los datos: un BST sin balance alimentado con claves ordenadas, algo muy común (identificadores crecientes, marcas de tiempo, archivos ordenados), se convierte en una lista enlazada con costo lineal y con riesgo de agotar la pila de recursión.

## Cómo funciona

Para buscar una clave, se compara con el nodo actual: si es menor se baja por el subárbol izquierdo, si es mayor por el derecho, si es igual se termina. El costo es proporcional a la **altura** *h* del árbol, no a *n*. Insertar sigue el mismo camino hasta una posición vacía.

La altura depende del **orden de inserción**. Si las claves llegan barajadas, cada una cae a ambos lados con probabilidad parecida y la altura crece como `log n`. Si llegan ordenadas, cada nueva clave es mayor que todas y se cuelga siempre a la derecha: la altura es *n*. Los árboles balanceados (AVL, rojo-negro) añaden rotaciones tras insertar o borrar para acotar la altura; tienen su propia entrada y clase ([SE-088](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md)). El recorrido en orden de un BST entrega las claves ordenadas, lo que explica su uso en consultas de rango.

## Ejemplo

[SE-088](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md) mide la altura y las comparaciones acumuladas con tres tamaños. Insertando 255, 1 000 y 4 000 claves **en orden**, la altura fue 255, 1 000 y 4 000, y las comparaciones sumaron 32 385, 499 500 y 7 998 000: una lista enlazada disfrazada. Con las mismas claves **barajadas**, la altura fue 17, 26 y 30 y las comparaciones 2 104, 11 562 y 56 801. Con 4 000 claves, la diferencia es de unas 140 veces en comparaciones. La mínima prueba defensiva es insertar las mismas claves en tres órdenes (ascendente, descendente, aleatorio) y comparar altura:

```python
def altura(nodo):
    return 0 if nodo is None else 1 + max(altura(nodo.izq), altura(nodo.der))
```

Con datos ordenados, esta función recursiva además supera el límite de recursión de Python, que es el `RecursionError` que [SE-088](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md) menciona.

## Errores y confusiones comunes

- **Dar por logarítmico un BST sin balanceo.** Es logarítmico en el caso esperado con orden aleatorio, no en el peor caso.
- **Probar solo con datos barajados.** El defecto aparece con entrada ordenada; [SE-088](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md) pide probar las tres entradas.
- **Confundir árbol de búsqueda con árbol cualquiera.** Un árbol jerárquico de carpetas no cumple la propiedad de orden y no se busca en `O(h)`.
- **Olvidar el costo constante.** Un nodo con punteros ocupa más memoria que una celda de arreglo y tiene peor localidad.

## Límites y cuándo no aplica

Un árbol representa jerarquía u orden, no dependencias arbitrarias ni varias rutas entre nodos; para eso la clase siguiente generaliza a grafos. En memoria, un arreglo ordenado con búsqueda binaria suele ser más rápido en la práctica para datos casi estáticos, porque recorre memoria contigua. Y si las claves son cadenas con prefijos comunes, un trie puede convenir más; cada estructura se justifica con medición, no por su cota teórica.

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
