# Identificador de correlación

## Definición

Un **identificador de correlación** es un valor que enlaza una respuesta con su solicitud, o que acompaña a un flujo para unir los registros y tramos de componentes distintos. El programa lo define de formas cercanas: en `SE-319`, asocia respuesta y solicitud sin depender del orden; en `SE-244`, une la respuesta al cliente con el registro interno de la misma solicitud; en `SE-382`, `SE-494` y `SE-308`, se propaga entre servicios y se registra en cada evento que la solicitud toca.

## Por qué importa

Sin él, depurar un incidente distribuido es adivinar qué línea de qué servicio pertenece a qué petición. Con él, a partir de una queja de un cliente («esta petición falló») se recupera toda la historia en todos los componentes.

## Cómo funciona

`SE-382` lo explica con trazas. Una **traza** es el recorrido de una petición por varios componentes; cada paso es un **tramo** (*span*) con un padre. Para unir tramos de procesos distintos, cada uno debe recibir y reenviar un identificador o un contexto de traza. W3C Trace Context lo estandariza en un encabezado, `traceparent`, que lleva el identificador de la traza y del tramo padre.

Cómo se usa en la práctica:

1. **Generar** el identificador en el borde, si la petición no lo trae.
2. **Propagarlo** en cada llamada saliente (encabezado o metadato del mensaje).
3. **Registrarlo** en cada línea de log (`SE-494`, logs estructurados).
4. **Devolverlo** al cliente en la respuesta o en el error (`SE-244`), para que lo cite al reportar un problema.

La propiedad crítica: la cadena se rompe en el primer eslabón que no reenvía el contexto; un solo servicio que lo ignore hace que las trazas posteriores aparezcan como flujos independientes. Por eso la propagación se prueba, no se supone.

## Ejemplo

Ilustración propia: la persona recibe un error con `id: 7f3a…`; soporte busca ese valor en los registros del gateway, del servicio de entregas y de la cola, y reconstruye en un solo vistazo dónde se detuvo. En mensajería (`SE-319`), una respuesta lleva el identificador de la solicitud, y quien la recibe sabe a cuál pertenece aunque lleguen desordenadas.

## Errores y confusiones comunes

- **Un servicio que no propaga el contexto,** y la traza se corta.
- **Usar datos personales como identificador:** debe ser opaco.
- **Confundirlo con un identificador de idempotencia:** aquel agrupa los registros de un flujo; este evita repetir un efecto.
- **No devolverlo al cliente,** de modo que no puede citarlo.

## Límites y cuándo no aplica

Une lo que se registró, pero no registra lo que nadie registró. Una petición que se fragmenta en trabajo asíncrono exige decidir si hereda el identificador o crea uno nuevo enlazado. Generarlo y propagarlo consume algo de ancho de banda; con un solo servicio su valor es menor.
