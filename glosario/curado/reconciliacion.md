# Reconciliación

## Definición

La **reconciliación** es la comparación periódica de dos registros independientes del mismo hecho, para detectar y reparar sus diferencias (`SE-596`). El programa la usa con matices:

- En `SE-378` y `SE-352` (datos): comparación periódica entre dos fuentes para detectar y reparar diferencias que ninguna restricción impide.
- En `SE-379` (integración): comparación periódica entre lo recibido y el listado del proveedor para procesar lo que faltó.
- En `SE-487` (CI/CD): comparación periódica del estado real con el deseado y aplicación de la diferencia.
- En `SE-524` (modernización): comparación de dos copias para encontrar y reparar diferencias.

No debe confundirse con la conciliación contable de `SE-417` (otra entrada), aunque comparten la idea de contrastar fuentes.

## Por qué importa

Ningún mecanismo de sincronización es infalible: un evento perdido, un conector parado dos días o un esquema que cambió sin aviso dejan divergencias silenciosas. La decisión que cambia es no confiar solo en el flujo en tiempo real: se añade una verificación periódica que encuentre lo que falló antes que un usuario.

## Cómo funciona

`SE-378` explica el mecanismo: una lápida olvidada, un conector parado o un cambio de esquema dejan divergencias. La reconciliación **compara periódicamente origen y destino** con conteos, sumas de control por rangos o muestras, y reporta las diferencias. Es también la herramienta de arranque y reparación: al detectar una divergencia, se vuelve a tomar una instantánea del rango afectado.

Su costo se acota comparando **agregados por rango** y descendiendo solo donde difieren (`SE-524`): si la suma del rango coincide, no hace falta mirar sus filas; si difiere, se parte el rango y se repite. Así la reconciliación que tardaba horas porque comparaba todo siempre pasa a comparar solo lo distinto.

En integración (`SE-379`), recibir webhooks no basta: pueden perderse. Se compara periódicamente lo recibido con el listado del proveedor, desde un punto de control, y se alerta si el avance se detiene. En despliegue (`SE-487`), la reconciliación continua del estado real contra el deseado es el principio de los controladores declarativos.

## Ejemplo

Un servicio recibe eventos de pago por webhook. Tras un mantenimiento, el endpoint estuvo caído y se perdieron algunos. Cada hora, un trabajo lista los pagos del proveedor desde el último punto de control, compara con lo recibido y procesa lo que faltó. Si el punto de control no avanza, genera una alerta. Mecanismo de `SE-379`.

## Errores y confusiones comunes

- **Se pierden avisos tras un mantenimiento**: no hay reconciliación periódica; se corrige con listado desde un punto de control y alerta si no avanza.
- **La reconciliación tarda horas**: compara todo siempre; se corrige con sumas por rangos y descendiendo solo a los distintos.
- **Confundirla con reintentar**: reintentar repara fallos conocidos; reconciliar encuentra los desconocidos.
- **Reconciliar sin decidir cuál fuente manda**.

## Límites y cuándo no aplica

Detecta divergencias con un retraso igual a su periodo: no sustituye la consistencia en tiempo real. Requiere dos fuentes realmente independientes y una clave común para compararlas; si ambas comparten el error, no lo ve. Y la reparación automática exige criterio claro sobre qué fuente es la verdad.
