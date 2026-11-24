# Muestreo

## Definición

En observabilidad, **muestreo** es conservar solo una parte de los registros o trazas para limitar el volumen (`SE-494`, `SE-496`).

## Por qué importa

Almacenar todo cuesta; muestrear mal borra justo lo que se necesitaba. La decisión es qué se conserva, y de ella depende que el incidente o el error raro dejen rastro.

## Cómo funciona

`SE-496` distingue dos momentos. En el **muestreo de cabeza**, se decide al comenzar la traza (barato, pero ciego al resultado). En el **muestreo de cola**, se decide al terminar, con conocimiento del estado y la duración, de modo que se pueden conservar todas las trazas con error o lentas. Para que el de cola decida bien, todos los tramos de una traza deben llegar al mismo recolector; se consigue enrutando por hash del identificador de traza. `SE-494` añade el criterio para registros: conservar por contenido (nivel, estado) en lugar de uniformemente.

## Ejemplo

Con muestreo uniforme del 1 %, un error que ocurre en 1 de cada 10 000 peticiones casi nunca queda registrado. Con una regla que conserva todo lo de estado de error y el 1 % del resto, el error siempre se ve.

## Errores y confusiones comunes

- **El error del cliente no tiene traza.** El muestreo de cabeza descartó la petición; usar de cola o reglas por estado y duración.
- **El muestreo de cola decide mal.** Los tramos llegan a recolectores distintos; enrutar por hash del identificador.
- **El muestreo borra el incidente.** Muestreo uniforme sobre eventos raros; conservar por contenido.

## Límites y cuándo no aplica

Las métricas agregadas conviene calcularlas antes de muestrear, o se sesgan. Muestrear reduce costo pero no sustituye a decidir qué señales importan.
