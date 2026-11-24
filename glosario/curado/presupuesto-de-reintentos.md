# Presupuesto de reintentos

## Definición

Un **presupuesto de reintentos** es un límite global a la fracción de peticiones que pueden ser reintentos (`SE-320`, `SE-373`, `SE-389`, `SE-438`). En lugar de limitar cuántas veces reintenta cada llamada, limita cuánto del tráfico total puede ser reintento, para que insistir no empeore el fallo.

## Por qué importa

Reintentar parece inocuo: si algo falla, se vuelve a intentar. Pero cuando el servicio está en dificultades, cada reintento añade carga justo donde ya sobra, y puede convertir un fallo breve en una caída prolongada. La decisión que cambia es dónde se pone el límite: no solo por llamada, sino sobre el total, de modo que la insistencia sea acotada pase lo que pase.

## Cómo funciona

`SE-320` muestra la amenaza con aritmética. Si el cliente web reintenta 3 veces, el servicio de aplicación que lo atiende reintenta 3 veces y el cliente del proveedor reintenta 3 veces, una sola petición del usuario puede producir 3 × 3 × 3 = **27** intentos sobre el proveedor cuando este falla. El efecto es **multiplicativo** porque cada capa reintenta sin saber que las demás también lo hacen.

El presupuesto acota el total: cada capa puede reintentar como máximo una fracción de sus peticiones. En el ejemplo de la clase, el 10 %, de modo que el factor de amplificación de las tres capas es 1,1³ ≈ **1,33**. El valor del presupuesto es una decisión; lo que el cálculo muestra es la forma de la amenaza (multiplicativa) y de su solución: acotar globalmente, no por llamada.

La clase lo combina con otras defensas: **jitter completo** (aleatorizar la espera para que los clientes no reintenten sincronizados), el interruptor (circuit breaker) y una simulación que reproduce la caída y comprueba el pico. `SE-389` simula un presupuesto del 10 % por capa con distintas tasas de fallo, para 1 000 clientes que fallaron a la vez, comparando retroceso con y sin jitter. `SE-373` y `SE-438` aplican la misma idea a integración y a calidad: la regla de reintentar en una sola capa, con retroceso, aleatoriedad y presupuesto.

## Ejemplo

Un proveedor falla durante 30 segundos. Sin presupuesto, cada una de las tres capas reintenta tres veces y el proveedor recibe hasta 27 veces el tráfico habitual, lo que impide su recuperación. Con un presupuesto del 10 % por capa, el exceso nunca pasa de un 33 % y el proveedor puede recuperarse. Cálculo de `SE-320`.

## Errores y confusiones comunes

- **La carga se triplica tras un fallo breve**: reintento inmediato sin límite; se corrige con presupuesto y espera con jitter (`SE-438`).
- **Reintentar en todas las capas**: la amplificación se multiplica.
- **Confundirlo con un número máximo de intentos por llamada**: es un límite sobre la fracción global.
- **Reintentar operaciones no idempotentes** sin protección.

## Límites y cuándo no aplica

El valor del 10 % es un ejemplo, no una recomendación general: se decide según el servicio y su tolerancia. El presupuesto limita la amplificación pero no arregla el fallo: sin un interruptor que deje de llamar y sin degradación, las peticiones simplemente fallan. Y los experimentos de las clases son simulaciones con parámetros del autor, no mediciones de sistemas reales.
