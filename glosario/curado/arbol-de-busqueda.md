# Árbol de búsqueda

## Definición

Un **árbol de búsqueda** (en `SE-088`, el árbol binario de búsqueda o BST) es un árbol donde cada nodo guarda una clave y separa las demás por subárbol: las menores quedan a un lado y las mayores al otro. La propiedad de orden permite buscar, insertar y borrar siguiendo **una sola rama** desde la raíz. El programa lo enseña como la estructura que muestra, con números, que una garantía asintótica depende de una condición: que el árbol esté equilibrado.

## Por qué importa

La promesa de `O(log n)` para búsqueda es lo que justifica elegir un árbol sobre una lista. Pero esa promesa describe un árbol de altura logarítmica, no cualquier árbol. La decisión profesional que cambia es si se acepta la estructura sin comprobar cómo llegan los datos: un BST sin balance alimentado con claves ordenadas, algo muy común (identificadores crecientes, marcas de tiempo, archivos ordenados), se convierte en una lista enlazada con costo lineal y con riesgo de agotar la pila de recursión.

## Cómo funciona

Para buscar una clave, se compara con el nodo actual: si es menor se baja por el subárbol izquierdo, si es mayor por el derecho, si es igual se termina. El costo es proporcional a la **altura** *h* del árbol, no a *n*. Insertar sigue el mismo camino hasta una posición vacía.

La altura depende del **orden de inserción**. Si las claves llegan barajadas, cada una cae a ambos lados con probabilidad parecida y la altura crece como `log n`. Si llegan ordenadas, cada nueva clave es mayor que todas y se cuelga siempre a la derecha: la altura es *n*. Los árboles balanceados (AVL, rojo-negro) añaden rotaciones tras insertar o borrar para acotar la altura; tienen su propia entrada y clase (`SE-088`). El recorrido en orden de un BST entrega las claves ordenadas, lo que explica su uso en consultas de rango.

## Ejemplo

`SE-088` mide la altura y las comparaciones acumuladas con tres tamaños. Insertando 255, 1 000 y 4 000 claves **en orden**, la altura fue 255, 1 000 y 4 000, y las comparaciones sumaron 32 385, 499 500 y 7 998 000: una lista enlazada disfrazada. Con las mismas claves **barajadas**, la altura fue 17, 26 y 30 y las comparaciones 2 104, 11 562 y 56 801. Con 4 000 claves, la diferencia es de unas 140 veces en comparaciones. La mínima prueba defensiva es insertar las mismas claves en tres órdenes (ascendente, descendente, aleatorio) y comparar altura:

```python
def altura(nodo):
    return 0 if nodo is None else 1 + max(altura(nodo.izq), altura(nodo.der))
```

Con datos ordenados, esta función recursiva además supera el límite de recursión de Python, que es el `RecursionError` que `SE-088` menciona.

## Errores y confusiones comunes

- **Dar por logarítmico un BST sin balanceo.** Es logarítmico en el caso esperado con orden aleatorio, no en el peor caso.
- **Probar solo con datos barajados.** El defecto aparece con entrada ordenada; `SE-088` pide probar las tres entradas.
- **Confundir árbol de búsqueda con árbol cualquiera.** Un árbol jerárquico de carpetas no cumple la propiedad de orden y no se busca en `O(h)`.
- **Olvidar el costo constante.** Un nodo con punteros ocupa más memoria que una celda de arreglo y tiene peor localidad.

## Límites y cuándo no aplica

Un árbol representa jerarquía u orden, no dependencias arbitrarias ni varias rutas entre nodos; para eso la clase siguiente generaliza a grafos. En memoria, un arreglo ordenado con búsqueda binaria suele ser más rápido en la práctica para datos casi estáticos, porque recorre memoria contigua. Y si las claves son cadenas con prefijos comunes, un trie puede convenir más; cada estructura se justifica con medición, no por su cota teórica.
