# Receptor idempotente

## Definición

Un **receptor idempotente** es un receptor para el que procesar un mensaje repetido no cambia el resultado: ante un duplicado, no repite el efecto. Es el sentido de `SE-319` (Enterprise Integration Patterns como lenguaje común) y de `SE-298` (low-code y automatización visual). Es el patrón que acompaña a un canal de entrega al menos una vez.

## Por qué importa

Convierte «al menos una vez» en efecto único. Un canal que puede duplicar mensajes no es defectuoso: cumple lo que promete. La responsabilidad de que un duplicado no cobre dos veces es del receptor.

## Cómo funciona

`SE-319` lo muestra con un experimento: 1000 mensajes (60 % pagos, 20 % avisos, 20 % bajas) por un canal al menos una vez que duplica un 20 % y reordena en ventanas de 6. Se entregan 1208 mensajes (208 duplicados).

- La suma real de pagos es **15 682**.
- Sin receptor idempotente, el consumidor suma **18 759**, un error de **+3 077**.
- Con un receptor que guarda los identificadores vistos y descarta los repetidos, suma **15 682**.

Dos decisiones de diseño:

1. **El identificador del mensaje debe ser estable:** el mismo en cada reenvío. Un identificador generado en el receptor no sirve, porque cada llegada parecería un mensaje nuevo.
2. **Cuánto conservar los identificadores.** Una ventana finita (por ejemplo, 7 días) acota la memoria, pero exige que el canal no reenvíe más tarde que esa ventana.

El diagnóstico de la clase es ordenado: contar cuántos identificadores aparecen más de una vez (208 de 1208), comprobar la garantía del proveedor (al menos una vez), y concluir que la causa no es el código de suma sino la ausencia de receptor idempotente.

## Ejemplo

Ilustración propia: la tabla `procesados(mensaje_id primary key)`. El receptor inserta el identificador en la misma transacción que aplica el efecto; si el `INSERT` choca con la clave, el mensaje ya se procesó y se descarta. Es la *inbox* de `SE-377`.

## Errores y confusiones comunes

- **Generar el identificador en el receptor** o derivarlo de datos que cambian en cada reenvío.
- **Comprobar el identificador y aplicar el efecto en transacciones separadas:** una caída entre ambos rompe la garantía.
- **Olvidar la caducidad de los identificadores** y quedarse sin memoria.
- **Confundirlo con la idempotencia de la operación:** puede lograrse de dos modos (la operación es naturalmente idempotente, o el receptor deduplica).

## Límites y cuándo no aplica

La ventana de retención limita la protección. Si el efecto es sobre un sistema externo sin clave de idempotencia, la deduplicación local no basta. El experimento de `SE-319` es una simulación con duplicados y reordenamientos construidos por el autor.
