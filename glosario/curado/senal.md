# Señal

## Definición

Una **señal** es cualquier dato que un sistema emite sobre su propio comportamiento. `SE-493` distingue cuatro clases: **registros** (un evento discreto con contexto), **métricas** (un número agregado en el tiempo), **trazas** (el recorrido de una petición por varios servicios, formado por tramos llamados *spans*) y **perfiles** (dónde gasta tiempo o memoria el código). La **telemetría** es el conjunto de lo que se recoge y se envía fuera del proceso.

## Por qué importa

Lo que no emite señal no se puede diagnosticar. Elegir qué señales emitir decide qué preguntas podrán responderse cuando algo falle: `SE-493` pone la vara en la capacidad de decir qué pregunta *no* se podría responder y qué señal habría que añadir, no en que el servicio tenga un panel.

## Cómo funciona

Cada clase responde a preguntas distintas. El registro dice qué pasó en una unidad de trabajo («entrega 123 aceptada en 83 ms»); la métrica dice cuánto y con qué tendencia («peticiones por segundo por endpoint»); la traza dice por dónde pasó una petición; el perfil, por qué el código gasta recursos. Un **evento ancho** es un registro estructurado con muchos campos (versión, cliente, curso, duración, identificador de traza) escrito una vez por unidad de trabajo, de modo que se puede agrupar por cualquier campo.

## Ejemplo

`SE-493`: la guardia despierta al equipo de la pasarela, pero el servicio degradado es el de almacenamiento. Hipótesis rivales: defecto en la pasarela, red degradada, o duración inclusiva. Se compara el p99 de cada servicio con su línea base; si el mayor aumento relativo está en almacenamiento y la pasarela solo suma una constante, la duración inclusiva explica la señal.

## Errores y confusiones comunes

- **Todos los paneles se ven mal a la vez.** Duración inclusiva: todos incluyen al servicio lento; comparar con la línea base de cada servicio o medir el tiempo propio.
- **El panel global está sano y un cliente protesta.** El promedio lo dominan los clientes grandes; agrupar por segmento.

## Límites y cuándo no aplica

Más señales no equivalen a más comprensión: cuestan almacenamiento y atención, y una señal sin pregunta asociada es ruido. Una señal es un síntoma, no la causa.
