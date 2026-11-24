# Lote

## Definición

Un **lote** (*batch*) es un grupo de elementos que se mueven juntos por una etapa de un flujo (`SE-184`). En inferencia de modelos, `SE-606` lo precisa como el conjunto de peticiones procesadas en una sola ejecución del modelo. La idea común es agrupar para repartir un costo fijo entre varios elementos, a cambio de esperar.

## Por qué importa

Es una de las palancas principales de rendimiento, y una de las más malinterpretadas. Agrupar sube el *throughput* (peticiones por segundo) pero aumenta la latencia de cada petición, que debe esperar a que el lote se llene y termine. En procesos (`SE-184`), el trabajo por lotes también explica esperas: más personas no aceleran lo que espera a que se complete un lote.

## Cómo funciona

`SE-281` descompone el costo de una llamada a un cálculo: un costo fijo (lanzar, sincronizar, mover datos) y uno variable por elemento. Agrupar reparte el costo fijo. En la CPU del laboratorio, una capa densa de 1024×1024 en 32 bits dio, por lote: lote 1, 0,27 ms y unas 3 700 peticiones por segundo; lote 16, 4,8 ms y 3 300 (sin ganancia aún); lote 64, 7,9 ms y 8 100; lote 256, 14,3 ms y 17 900. El throughput sube con el tamaño del lote, pero la latencia por lote sube también, y la espera por llenar el lote se suma.

El tamaño óptimo, por tanto, no es el que maximiza throughput sino el que cabe en el tiempo que el objetivo de latencia permite esperar. En la práctica se agrupa con un **tiempo máximo de espera**: se cierra el lote cuando se llena o vence el plazo, lo que ocurra antes.

## Ejemplo

`SE-281`, diagnóstico paso a paso: la utilización de la unidad promedia 8 %; el tamaño de lote en producción es 1 porque la política de agrupar no se configuró; la corrección agrupa peticiones con una espera máxima de 5 ms, comparte la unidad con la carga nocturna y mantiene una unidad mínima caliente. Ilustración:

```python
def cerrar_lote(cola, max_n=64, max_espera_ms=5):
    return len(cola) >= max_n or cola.edad_ms() >= max_espera_ms
```

## Errores y confusiones comunes

- **Contratar personas y el plazo no mejora.** Causa: la espera venía de lotes y variabilidad; corrección: medir tamaños y lotes antes de añadir capacidad (`SE-184`).
- **Maximizar throughput ignorando la latencia.** El lote de 256 es el más eficiente y también el más lento por petición.
- **Confundir lote con paralelismo.** Es agrupar trabajo, no ejecutar a la vez en varios núcleos.

## Límites y cuándo no aplica

Con una demanda de 200 peticiones por segundo, llenar un lote de 256 tardaría más de un segundo: allí el lote grande no es viable si el objetivo de latencia es menor (`SE-281`). Las cifras de la clase corresponden a una CPU y una capa concretas y no se trasladan a otro hardware sin medir. Y en flujos, un paso que retiene todo el lote rompe la memoria acotada (`SE-339`).
