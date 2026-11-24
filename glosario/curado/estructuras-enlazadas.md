# Estructuras enlazadas

## Definición

Una **estructura enlazada** guarda sus elementos en **nodos** independientes que se conectan mediante referencias (punteros): cada nodo contiene un valor y una referencia al siguiente (en las listas enlazadas, también al anterior). En `SE-085` se contrasta con los arreglos: los nodos enlazados **insertan localmente cuando ya se posee el nodo**, pero **localizar una posición sigue siendo lineal**. La clase añade un aviso específico de Python: la lista incorporada (`list`) **no es** una lista enlazada, sino un arreglo dinámico de referencias.

## Por qué importa

La teoría enseña que insertar en una lista enlazada es `O(1)` y en un arreglo `O(n)`. Esa cifra es verdadera pero incompleta, y elegir con ella lleva a decisiones erróneas. La decisión que cambia es en qué se confía al elegir una estructura: no en la cota aislada, sino en la operación **dominante** de la carga real y en el costo constante de la máquina. En la práctica, las estructuras enlazadas pierden con frecuencia frente a los arreglos por motivos que la cota no recoge.

## Cómo funciona

Insertar o borrar en una lista enlazada solo reasigna referencias: si ya se tiene el nodo (o el anterior), el costo es constante. Pero para llegar a una posición hay que **recorrer** nodos uno a uno desde el inicio: `O(n)`. Así, «insertar en medio» cuesta `O(n)` en ambas estructuras si primero hay que buscar la posición; la ventaja enlazada solo existe si se conserva la referencia al nodo.

Además, hay costos que la notación asintótica oculta (`SE-085`):

- **Memoria por nodo:** cada elemento paga la cabecera del objeto y la referencia extra.
- **Asignaciones:** crear cada nodo es una asignación aparte.
- **Localidad:** los nodos pueden estar dispersos en memoria. Cada salto de puntero es un acceso que la **caché** no puede anticipar, mientras que un arreglo contiguo se recorre con lecturas previsibles.

Por eso la ventaja teórica puede ser superada por el arreglo hasta en tamaños grandes. Existen estructuras que combinan lo mejor de ambos mundos para casos específicos: `collections.deque` ofrece inserción y extracción eficientes en ambos extremos.

## Ejemplo

`SE-085` documenta dos errores relacionados. El primero: vaciar una cola de 80 000 elementos tarda casi un segundo porque se usa `lista.pop(0)` como operación dominante, que desplaza todos los elementos restantes en cada llamada (`O(n)`). La corrección es `deque.popleft()`, que es `O(1)`, y repetir la medición con la misma carga:

```python
from collections import deque
cola = deque(range(80_000))
while cola:
    cola.popleft()      # O(1); lista.pop(0) sería O(n) por llamada
```

El segundo: tres filas de una cuadrícula cambian a la vez porque `[[0]] * 3` repite la **misma** lista interna; se corrige con `[[0] for _ in range(3)]` y se prueba una escritura aislada.

## Errores y confusiones comunes

- **Creer que `list` de Python es una lista enlazada.** Es un arreglo dinámico; `insert(0, x)` y `pop(0)` son lineales.
- **Citar `O(1)` sin la búsqueda previa.** Ubicar la posición cuesta lineal.
- **Ignorar la localidad.** El recorrido de nodos dispersos puede ser mucho más lento que el de un arreglo, aun con igual cota.
- **Compartir referencias sin querer.** La multiplicación de listas anidadas repite el mismo objeto.

## Límites y cuándo no aplica

Las estructuras enlazadas pueden convenir cuando se conservan referencias a nodos, se insertan y borran con frecuencia en posiciones conocidas, o cuando se necesita estabilidad de referencias a los elementos (un nodo no se mueve al insertar otros). En lenguajes con arreglos contiguos y memoria jerárquica, suelen perder en la mayoría de cargas. La elección se decide midiendo con la carga real, no por la tabla de cotas.
