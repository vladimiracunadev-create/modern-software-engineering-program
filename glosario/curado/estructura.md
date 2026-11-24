# Estructura

## Definición

En el programa, **estructura** es lo que se conserva de un problema cuando se descartan los detalles que no importan: las relaciones entre sus partes. `SE-049` lo plantea como pregunta («¿qué relaciones se conservan?») dentro del pensamiento computacional, y `SE-051` la concreta en las **estructuras de datos**: la forma en que se organizan los elementos para responder bien a las consultas que importan. Una estructura se elige por las preguntas que debe contestar, no por familiaridad.

## Por qué importa

Elegir la estructura es declarar las consultas del problema (`SE-051`). Si hay que preguntar «¿esto ya fue visto?», la estructura correcta es un conjunto, no una lista; usar la equivocada convierte una consulta casi inmediata en un recorrido completo. Además, la estructura puede ser lo que garantiza que un algoritmo termine.

## Cómo funciona

`SE-051` da el criterio de elección: la estructura que **preserve la operación que importa**.

- ¿«ya fue visto»? → un conjunto.
- ¿asociar clave y valor? → un mapa.
- ¿las relaciones entre elementos son el dato? → un grafo.

Y muestra un segundo papel: en un recorrido de un grafo con ciclo, sin precauciones, el proceso no termina. En el grafo A→{B,C}, B→D, C→D, D→A, un recorrido en anchura con un conjunto de visitados produce A, B, C, D y se detiene: cada nodo entra una sola vez. Esa estructura es el invariante que garantiza la terminación, y se puede enunciar como una medida que decrece: la cantidad de nodos aún no visitados. La terminación se demuestra, no se espera.

## Ejemplo

Ilustración con la misma consulta en dos estructuras:

```python
vistos_lista = []            # "x in vistos_lista" recorre la lista: O(n)
vistos_conjunto = set()      # "x in vistos_conjunto" es de costo promedio constante
```

En el recorrido del grafo anterior, sin `vistos` el ciclo D→A reinicia el recorrido indefinidamente.

## Errores y confusiones comunes

- **Una lista donde se pregunta «¿ya está?».** Causa: estructura equivocada para la consulta; corrección: cambiar a conjunto o mapa y medir (`SE-051`).
- **Recorrer un grafo sin conjunto de visitados.** El ciclo impide la terminación.
- **Confundir estructura de datos con estructura del problema.** La primera es una elección de implementación; la segunda son las relaciones que el modelo preserva (`SE-049`).

## Límites y cuándo no aplica

No hay estructura óptima en abstracto: depende del conjunto de consultas y del tamaño. Para colecciones pequeñas la diferencia puede ser irrelevante y la claridad pesa más. Y la elección debe medirse (`SE-051` pide medir al cambiar), porque la constante oculta o la localidad de memoria pueden invertir la expectativa teórica.
