# Benchmark

## Definición

Un **benchmark** es una medición repetible del tiempo o del consumo de un fragmento de código, con una entrada y un protocolo declarados (`SE-437`). `SE-022` lo presenta como un experimento comparativo bajo protocolo y `SE-055` como la medición controlada de una implementación. La palabra no designa «un número»: designa el número junto con la descripción que lo hace interpretable.

## Por qué importa

Las decisiones de rendimiento (elegir una estructura de datos, aceptar o rechazar una optimización, fijar un timeout) se apoyan en cifras. Si la cifra mide otra cosa, la decisión es errónea y además parece fundada. `SE-437` toma los tiempos medidos para decidir timeouts y reintentos, así que un benchmark defectuoso se propaga a esas decisiones.

## Cómo funciona

Un benchmark puede medir lo que no se quería (`SE-437`). Las causas típicas:

- **Caché o resultado constante:** si la función usa `functools.lru_cache` y se llama con el mismo argumento, se mide una búsqueda en un diccionario y no el trabajo.
- **Entrada demasiado pequeña:** domina el costo fijo de la llamada.
- **Entrada demasiado regular:** el procesador predice los saltos y la caché la favorece más que a datos reales.
- **Estado global modificado:** la segunda ejecución ya no parte del mismo estado.

La regla es describir qué entrada, qué estado inicial y qué se descarta. `SE-022` añade que hay que distinguir qué se mide: latencia (cuánto tarda una unidad), *throughput* (cuántas se completan por tiempo) y utilización (cuánto ocupa un recurso); mejorar una puede empeorar otra. La carga incluye tamaño, distribución, concurrencia, estado y criterio de corrección. `SE-437` propone una prueba A/A (comparar una versión consigo misma) para ver cuánta falsa diferencia produce el protocolo.

## Ejemplo

En el caso conductor de `SE-437` (ordenación de entregas de la API), el artefacto es un protocolo de benchmark con su prueba A/A; al cambiar el número de repeticiones, cambia la tasa de falsas diferencias. Ilustración mínima de un defecto:

```python
@lru_cache
def f(x): return sorted(range(x))
timeit.timeit(lambda: f(10_000), number=1000)   # mide el diccionario
```

## Errores y confusiones comunes

- **Un tiempo imposible.** Causa: caché o resultado constante medido en lugar del trabajo; corrección: variar la entrada y reiniciar la caché (`SE-437`).
- **Comparar versiones que dan resultados distintos.** No es un benchmark (`SE-022`): primero hay que verificar la corrección.
- **Confundirlo con un perfil.** El perfil dice dónde se gasta el tiempo; el benchmark compara cuánto.

## Límites y cuándo no aplica

Un benchmark vale para la entrada, el entorno y el protocolo declarados; no se extrapola sin más a producción. Un número sin descripción de entrada, estado inicial y descartes no tiene significado (`SE-437`). Y medir bien no decide por sí solo: el costo de una optimización en complejidad también cuenta.
