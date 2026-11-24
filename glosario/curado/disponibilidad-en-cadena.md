# Disponibilidad en cadena

## Definición

La **disponibilidad en cadena** es la probabilidad de que una operación termine bien cuando necesita que varias dependencias respondan; con fallos independientes, es el producto de las de cada una (`SE-373`). Es el modelo más simple de por qué una cadena de eslabones muy fiables es menos fiable que cada eslabón.

## Por qué importa

Cada dependencia síncrona que se añade a la ruta crítica de una petición tiene un precio de disponibilidad, aunque el código sea correcto. La decisión que cambia es qué dependencias se permiten en el camino síncrono: la pregunta útil es cuáles son necesarias para responder **ahora**, y cuáles pueden salir de la ruta o degradarse.

## Cómo funciona

Si una petición necesita que *k* dependencias respondan y cada una falla con probabilidad *p* de forma independiente, la probabilidad de éxito es (1 − p)^k. Con *p* = 1 % y cinco dependencias, el éxito baja a 95,1 %. La causa es que la petición solo tiene éxito si **todas** las dependencias acompañan a la vez; los fallos de distintas dependencias se acumulan en vez de promediarse.

`SE-373` marca dos matices. Primero, la independencia es una hipótesis optimista: fallos correlacionados (un mismo despliegue, una misma red) empeoran el resultado. Segundo, lo útil del modelo es la dirección, no el número exacto: más eslabones síncronos, menos disponibilidad.

La clase lo conecta con las medidas de arquitectura: sacar una dependencia de la ruta crítica (por ejemplo, por mensajería asíncrona) o degradar su respuesta elimina un eslabón de la cadena. Y con una advertencia sobre los reintentos: reintentar en varias capas multiplica la carga sobre el servicio enfermo e impide su recuperación; se corrige reintentando en una capa, con retroceso, aleatoriedad y presupuesto.

## Ejemplo

La entrega de un trabajo depende, en la ruta síncrona, de cinco servicios, cada uno con 99 % de éxito: 0,99⁵ ≈ 95,1 %. Los estudiantes ven errores aunque el calificador funciona, porque la entrega depende además de un servicio secundario en la misma ruta. Sacar ese servicio de la ruta crítica o degradar su respuesta devuelve la disponibilidad a la del resto. Escenario y cifra de `SE-373`.

## Errores y confusiones comunes

- **Los estudiantes ven errores aunque el calificador funciona**: la entrega depende de un servicio secundario en la ruta síncrona; se corrige sacando la dependencia o degradando su respuesta.
- **El servicio enfermo no se recupera**: reintentos en varias capas multiplican la carga.
- **Promediar en lugar de multiplicar**: la disponibilidad de la cadena no es la media de los eslabones.
- **Asumir independencia sin comprobarla**.

## Límites y cuándo no aplica

`SE-373` indica que sus experimentos usan datos sintéticos, sin red, servidor, corredor de mensajes ni medición de latencia: las tasas de fallo, la llegada constante, la caída de 600 s y el presupuesto de reintentos son construcciones del autor, y los resultados no se extrapolan a otros sistemas. El modelo no aplica a dependencias opcionales o en paralelo (ahí corresponde la disponibilidad compuesta con redundancia), ni a operaciones cuyo éxito parcial es aceptable.
