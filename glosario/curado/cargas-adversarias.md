# Cargas adversarias

## Definición

Las **cargas adversarias** son entradas elegidas, no al azar sino a propósito, para provocar el **peor caso** de una estructura o un algoritmo. `SE-095` da cuatro familias: entradas **ordenadas** (que degeneran un árbol de búsqueda sin balance), **hashes conflictivos** (que concentran claves en pocos cubos de una tabla), **prioridades iguales** (que ponen a prueba el desempate de una cola) y **grafos cíclicos** (que rompen recorridos que suponen árboles). «Adversaria» no implica atacante: basta con que la entrada sea desfavorable.

## Por qué importa

Las cotas habituales (`O(log n)`, `O(1)` esperado) describen casos típicos; el peor caso puede ser órdenes de magnitud peor. Una medición con datos aleatorios y cómodos produce una mediana excelente que no dice nada de lo que pasa cuando llega la entrada difícil. La decisión que cambia es cuándo mirar el peor caso: `SE-095` lo vincula con **seguridad y disponibilidad**, porque un servicio con una mediana buena puede caerse con unas pocas entradas bien elegidas. No toda entrada adversaria es probable, pero si el costo de que ocurra es alto, hay que acotar su impacto.

## Cómo funciona

Cada carga ataca una suposición de la estructura:

- **Entrada ordenada → árbol de búsqueda sin balance.** Cada clave nueva es mayor que las anteriores y se cuelga siempre del mismo lado; la altura pasa de `log n` a `n` (`SE-088` mide 4 000 claves ordenadas con altura 4 000 contra 30 con orden barajado).
- **Hashes conflictivos → tabla hash.** Si muchas claves caen en el mismo cubo, la búsqueda recorre una lista larga y el `O(1)` esperado se vuelve `O(n)`. Si un atacante puede elegir las claves y conoce la función hash, puede provocarlo a propósito.
- **Prioridades iguales → cola de prioridad.** Sin regla de desempate, el orden de salida entre iguales queda sin definir; el resultado no es reproducible.
- **Grafos cíclicos → recorridos.** Un recorrido que asume jerarquía entra en bucle si no marca nodos visitados.

La lección común es que la garantía depende de una condición sobre los datos; la carga adversaria viola esa condición a propósito, y medirla muestra cuánto cuesta violarla.

## Ejemplo

En el taller de `SE-095`, la biblioteca de estructuras y algoritmos se prueba con un perfil de operaciones y tamaños declarado antes de medir, y se añade un conjunto de cargas adversarias a cada candidato. Para una estructura que usa claves de texto, una carga puede ser un lote de claves construido para colisionar. Ilustración (la forma exacta depende de la implementación):

```python
datos_ordenados = list(range(n))            # peor caso de un BST sin balance
datos_barajados = random.sample(datos_ordenados, n)
t_orden = medir(lambda: insertar_todo(arbol, datos_ordenados))
t_azar  = medir(lambda: insertar_todo(arbol, datos_barajados))
```

Si `t_orden / t_azar` crece con `n`, la estructura no está equilibrada y su cota depende de la entrada. Es una prueba barata que cambia la recomendación: o se equilibra, o se baraja, o se elige otra estructura.

## Errores y confusiones comunes

- **Medir solo con datos aleatorios.** Oculta el peor caso real de datos que llegan ordenados con frecuencia (identificadores crecientes, marcas de tiempo).
- **Tomar el peor caso como el caso típico.** Una carga adversaria acota el riesgo; no describe el uso normal.
- **Ignorar la exposición.** Una tabla hash alimentada con claves controladas por usuarios externos exige considerar colisiones deliberadas.
- **Recomendar sin declarar carga ni tamaño.** La recomendación no convence a otro equipo si no dice con qué datos se probó.

## Límites y cuándo no aplica

El taller cubre cargas sintéticas y una plataforma (`SE-095`): una carga adversaria inventada no demuestra qué entradas llegarán en producción. Para código interno con datos controlados y de tamaño pequeño, probar peores casos extremos puede ser exceso. Y no sustituye medir con tráfico real ni las defensas en capas (límites de tamaño, tiempos máximos, aleatorización de hashes) cuando el riesgo es de disponibilidad.
