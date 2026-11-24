# Perfil como hipótesis

## Definición

**Perfil como hipótesis** es la lectura que `SE-099` propone de los resultados de un *profiler* (perfilador): **el perfil señala dónde se observa el costo, no por qué**. Un perfilador de CPU, memoria, entrada y salida o red mide en qué funciones o líneas se gasta tiempo o recursos; esa información es una pista y no una explicación. La causa se formula como una **hipótesis**, se cambia una variable y se repite la medición con la salida correcta para confirmar o descartar.

## Por qué importa

El perfil produce una lista ordenada y convincente, y es tentador optimizar lo primero que aparece. Pero una función «caliente» puede serlo por razones ajenas a su código (se llama demasiadas veces desde otro lugar, espera una red lenta) o ser irrelevante para el objetivo del servicio. `SE-099` lo resume: **optimizar una función caliente irrelevante para el SLO es trabajo sin impacto**. La decisión que cambia es qué se hace tras ver el perfil: no se edita, se formula una causa y se prueba.

## Cómo funciona

El ciclo tiene cuatro pasos:

1. **Fijar el objetivo:** qué se quiere mejorar (latencia, memoria, rendimiento) y qué umbral importa (el SLO).
2. **Perfilar y formular la hipótesis:** «el tiempo se va en serializar, porque se serializa cada elemento por separado».
3. **Cambiar una variable** (agrupar la serialización) y **repetir la medición comprobando que la salida sigue siendo correcta**. Una versión más rápida que devuelve resultados erróneos no es una mejora.
4. **Confirmar con la medición sin perfilador:** el perfilador mismo altera el tiempo.

Por eso `SE-099` documenta dos trampas. Un perfil determinista (que registra cada llamada) puede **inflar** el costo de funciones muy llamadas y llevar a optimizar lo que no era el problema; se confirma con el tiempo total sin perfilador. Y activar el perfil de memoria durante la medición de tiempo distorsiona el resultado: en la clase, con `tracemalloc` activo la prueba fue 62 veces más lenta; se perfilan memoria y tiempo en ejecuciones separadas.

## Ejemplo

Se perfila un servicio que tarda más de lo permitido. El perfil muestra que 60 % del tiempo está en `serializar`. La hipótesis: se llama una vez por elemento. Se cambia una variable:

```python
# antes: for c in casos: salida.append(serializar(c))
# después:
salida = serializar_lote(casos)        # misma salida, una llamada
assert salida == [serializar(c) for c in casos]   # la salida sigue siendo correcta
```

Se mide de nuevo **sin perfilador** con la misma carga. Si el tiempo total baja de forma relevante respecto del SLO, la hipótesis se confirma; si no, se descarta y se pasa a la siguiente. El perfil nunca fue la conclusión: fue el punto de partida.

## Errores y confusiones comunes

- **Optimizar la primera función de la lista.** Puede ser inflada por el perfilador o irrelevante para el objetivo.
- **Medir con el perfilador activo.** Altera el tiempo.
- **Mezclar perfil de memoria y de tiempo.** Se distorsionan mutuamente.
- **Mejorar sin verificar la salida.** Se puede acelerar un resultado incorrecto.

## Límites y cuándo no aplica

Un perfil dinámico observa **las entradas ejecutadas** (`SE-099`): lo que no se ejercitó en la medición no aparece. No dice nada del comportamiento con otros datos ni de rutas raras. Perfilar tampoco reemplaza el diseño: si el problema es algorítmico (un `O(n²)` que solo duele con tamaños grandes), el perfil con datos pequeños no lo muestra. La clase siguiente complementa con análisis estático, que detecta clases distintas de defectos.
