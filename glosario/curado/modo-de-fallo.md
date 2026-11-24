# Modo de fallo

## Definición

En el diseño de controles de agentes, el **modo de fallo** es el comportamiento de un control cuando no puede decidir: **abrirse** (dejar pasar) o **cerrarse** (bloquear). Es la definición de `SE-570`. (En análisis de peligros, «modo de fallo» también designa la forma en que falla un componente, como en el FMEA que menciona `SE-445`.)

## Por qué importa

Todo control tiene dos modos de fallo y ninguno es correcto en general. Un control que protege un recurso irrecuperable debe fallar cerrado, y aceptar la molestia de bloquear cuando se rompe; uno de conveniencia (un formateador, un aviso) puede fallar abierto.

## Cómo funciona

La decisión se toma para cada gancho, se escribe y se prueba, incluidos los casos de caída, de excepción y de tiempo agotado, porque son los que ejercitan el modo de fallo. Una forma sencilla (`SE-570`): el gancho termina con éxito solo cuando completó la comprobación y decidió permitir; con otro código bloquea; y cualquier otro resultado se interpreta en la capa que lo invoca como bloqueo.

## Ejemplo

`SE-570` (escenario hipotético): el equipo de *Avisos* escribe un gancho que termina con 0 solo si comprobó y permite y con 2 cuando bloquea; lo prueba como proceso con cuatro eventos de simulación (caída, tiempo agotado, entrada vacía, JSON inválido) y comprueba que ninguna acción peligrosa llega a ejecutarse.

## Errores y confusiones comunes

**El control «no hace nada» y no hay error.** Falla abierto: el error del gancho no bloquea; usar el código de bloqueo para la política y probar la caída.

## Límites y cuándo no aplica

Fallar cerrado tiene costo de disponibilidad: si el control se cae con frecuencia, bloquea trabajo legítimo. Se decide por el daño del peor caso en cada control.
