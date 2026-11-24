# Hipótesis de estado estable

## Definición

La **hipótesis de estado estable** es una afirmación comprobable, con umbral, sobre el comportamiento normal del sistema, que un experimento de presión o de caos busca refutar. `SE-443` la define así: por ejemplo, «el p95 de latencia por ventana de diez segundos es menor de X y la tasa de errores menor de Y». Es el punto de partida de la ingeniería del caos: sin una definición de «normal» medible, no hay forma de saber si el fallo inyectado cambió algo.

## Por qué importa

Convierte un experimento en un resultado interpretable. Sin hipótesis, «tiramos un servidor y parecía funcionar» es una impresión. Con ella, el experimento se aprueba o se refuta con datos, y la decisión de qué hacer con el sistema (confiar, corregir, volver a probar) tiene base. Además la hipótesis fuerza a elegir qué señales importan al usuario, y no solo las que son fáciles de medir.

## Cómo funciona

La hipótesis se expresa con **señales observables** (latencia p95, tasa de errores, fracción de peticiones correctas) y **umbrales**. El experimento introduce un fallo y comprueba si la hipótesis se sostiene; si no, se encontró una debilidad.

El umbral importa más de lo que parece (`SE-443`):

- Uno tomado del **máximo de una sola ejecución base** falla solo con frecuencia: da falsas alarmas.
- Uno demasiado **holgado** no detecta fallos sutiles.

Por eso se mide el **ruido de base** con varias ejecuciones y se verifica con una **prueba A/A** (comparar el sistema contra sí mismo) que el umbral no se supera cuando no pasa nada. La causa es estadística: la métrica ya varía sin fallo, y el umbral debe separarse de esa variación natural.
## Ejemplo

`SE-443` trabaja con la API de entregas en tiempo virtual y semillas fijas. Se miden varias ejecuciones sin fallo para conocer el ruido del p95 por ventana de diez segundos. El umbral se fija con ese ruido, no con el máximo de una ejecución; se comprueba con A/A que no salta sin fallo; luego se inyecta el fallo y se comprueba si el p95 y la tasa de errores se mantienen dentro del umbral. Un resultado que supera el umbral refuta la hipótesis: hay un hallazgo. Uno que no lo supera solo confirma la hipótesis *para ese fallo y ese radio de impacto*.

## Errores y confusiones comunes

- **El experimento aborta sin fallo.** Umbral demasiado estrecho; fijarlo con varias ejecuciones base y una prueba A/A (`SE-443`).
- **No se ve un fallo sutil.** Umbral holgado o radio demasiado pequeño; calcular la detección y ajustar.
- **Hipótesis vagas** («el sistema sigue funcionando»). No se pueden refutar; deben incluir señal, umbral y ventana.
- **Confundirla con un SLO.** Un SLO es un compromiso de servicio; la hipótesis es una afirmación de prueba, aunque puede apoyarse en los mismos indicadores.

## Límites y cuándo no aplica

Los experimentos de `SE-443` son en tiempo virtual y con semillas fijas, no en producción; sus resultados ilustran el método. Una hipótesis confirmada no demuestra resiliencia general, solo ante la falla probada. Requiere buena observabilidad: si las señales no existen o no son fiables, no puede formularse. Y no aplica a sistemas cuyo comportamiento normal no es estable (cargas muy estacionales sin modelo de la variación), donde primero hay que caracterizar el ruido.
