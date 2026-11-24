# Selección parcial

## Definición

La **selección parcial** es obtener solo una parte del orden de una colección sin ordenarla toda: los *k* mayores (*top-k*), el elemento que ocuparía la posición *k* (la mediana, por ejemplo) o los primeros resultados. En `SE-090` se presentan dos técnicas: un **montículo (*heap*) de tamaño *k*** y **quickselect**. La idea común es que para responder «¿cuáles son los 10 mejores de un millón?» no hace falta ordenar el millón.

## Por qué importa

Ordenar *n* elementos cuesta `O(n log n)`. Si solo se necesitan unos pocos, ese trabajo es en gran parte inútil. La decisión que cambia es qué se calcula: el resultado que se necesita y no más. Con *k* pequeño frente a *n*, la selección parcial es sensiblemente más barata en tiempo y, con el montículo, en memoria. Además, permite procesar datos que llegan como flujo sin guardarlos todos.

## Cómo funciona

Hay dos mecanismos con compromisos distintos:

- **Montículo de tamaño *k*:** se mantiene un montículo mínimo con los *k* mejores vistos hasta el momento. Para cada elemento nuevo, si es mejor que el menor del montículo, lo reemplaza. Cada operación cuesta `O(log k)`, y el total es `O(n log k)`. Usa **espacio acotado** (*k* elementos) y funciona con datos **en flujo**, sin conocer *n* de antemano. En Python, `heapq.nlargest` lo implementa.
- **Quickselect:** igual que el *quicksort*, elige un pivote y reparte, pero **solo continúa en el lado que contiene la posición buscada**. El costo esperado es **lineal** `O(n)` con pivotes adecuados, aunque el peor caso es `O(n²)` si los pivotes son malos (pivote aleatorio lo evita en la práctica). Modifica o necesita copia de los datos y no encaja con flujos.

La elección depende, como indica `SE-090`, de **si llegan datos en flujo, si *k* cambia y si se necesita la salida ordenada**. El montículo da los *k* mejores pero no ordenados entre sí sin un paso final; quickselect da la partición, no el orden.

## Ejemplo

Obtener los 5 casos más urgentes de una lista grande:

```python
import heapq

# O(n log k), memoria O(k); no ordena todo
top5 = heapq.nsmallest(5, casos, key=lambda c: c["prioridad"])

# lo equivalente, pero ordenando todo: O(n log n)
top5_lento = sorted(casos, key=lambda c: c["prioridad"])[:5]
```

Con *n* grande y *k* = 5, la primera forma hace mucho menos trabajo. Si los casos llegan por un flujo (no se pueden guardar todos), el montículo es la única de las dos opciones viable. Para la mediana de datos en memoria, quickselect (o `statistics.median`, que ordena) son alternativas con costos distintos. Esta nota coincide con los defectos que la clase asocia al ordenamiento: pivote fijo en un *quicksort* ingenuo es lento con datos casi ordenados, y `NaN` o un comparador no transitivo dejan un resultado «ordenado» que no lo está; la selección parcial hereda ambos riesgos.

## Errores y confusiones comunes

- **Ordenar todo para quedarse con unos pocos.** Trabajo desperdiciado.
- **Suponer que el resultado del montículo está ordenado.** Hay que ordenarlo al final si se necesita.
- **Usar quickselect con un pivote fijo.** Degrada con entradas ordenadas.
- **Ignorar el contrato de comparación.** Con `NaN`, el resultado es incorrecto.

## Límites y cuándo no aplica

Elegir *top-k* no resuelve decisiones secuenciales con subproblemas o restricciones (`SE-090`): seleccionar los mejores uno a uno no equivale a elegir el mejor conjunto cuando los elementos interactúan; ahí entran las estrategias voraces y la programación dinámica. Si *k* es comparable a *n*, ordenar todo es igual de bueno y más simple. Y para colecciones pequeñas la diferencia es irrelevante.
