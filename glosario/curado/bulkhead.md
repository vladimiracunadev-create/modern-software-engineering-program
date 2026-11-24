# Bulkhead

## Definición

Un **bulkhead** (mamparo) reparte un recurso finito (hilos, conexiones, memoria) en compartimentos, uno por dependencia o por clase de solicitud, para que el fallo o la lentitud de un uso no consuma el recurso de los demás (`SE-439`). `SE-321` lo presenta como aislamiento de recursos por dependencia para contener una falla. El nombre viene de los compartimentos estancos de un barco.

## Por qué importa

Una dependencia lenta es más peligrosa que una caída: no devuelve error rápido, retiene los hilos. La decisión que cambia es cómo se dimensionan los recursos compartidos: en lugar de un único pool para todo, se decide cuánto del recurso puede perder cada dependencia sin arrastrar a las demás. El mamparo no arregla la dependencia lenta; la **confina**.

## Cómo funciona

El mecanismo, según `SE-439`, es aritmético. Si todas las llamadas comparten un pool de 20 trabajadores y una dependencia pasa de 50 ms a un segundo, sus llamadas ocupan los trabajadores unas veinte veces más tiempo; a la tasa de llegada de ese tráfico, el pool entero termina atendiendo solo a la dependencia lenta y las demás llamadas esperan en cola. Con pools separados, la dependencia lenta agota **su** compartimento; las otras siguen con el suyo. Las llamadas a la lenta fallan o esperan, pero el resto del servicio sigue sirviendo.

`SE-321` lo verifica con una simulación: dos dependencias, A sana (40 peticiones por segundo, unos 50 ms) y B que se degrada a 3 s durante 20 s de una ventana de 40 s. Con un grupo compartido de 10 hilos, solo el 30,6 % de las peticiones de A terminan dentro de 0,5 s, aunque A estaba sana; con grupos separados, A queda protegida. Los números son de esa simulación, no una regla general.

## Ejemplo

Un servicio de entregas llama a un sistema de calificaciones (crítico) y a uno de estadísticas (secundario). Con un solo pool, que las estadísticas se pongan lentas deja sin hilos a las calificaciones. Con mamparos por criticidad, las estadísticas tienen, por ejemplo, un pool pequeño; cuando se agota, esa función se degrada y las calificaciones siguen. El tamaño de cada compartimento es una decisión de diseño, no un valor universal.

## Errores y confusiones comunes

- **Una dependencia secundaria tumba la función principal**: es el error de `SE-439`, causado por un pool compartido; se corrige con mamparos por dependencia o por criticidad.
- **Creer que el mamparo cura la lentitud**: solo limita el daño.
- **Confundirlo con el circuit breaker**: el mamparo limita cuánto recurso puede consumir una dependencia; el circuit breaker decide cuándo dejar de llamarla. Se combinan.
- **Compartimentos demasiado pequeños**: una dependencia sana puede quedarse sin capacidad en un pico normal.

## Límites y cuándo no aplica

Repartir un recurso finito lo hace menos eficiente en conjunto: capacidad ociosa en un compartimento no la puede usar otro. Con una sola dependencia, o con recursos holgados respecto al tráfico, no aporta. Y solo protege los recursos que se dividen: si todos los compartimentos comparten, por ejemplo, la misma base de datos, esa base sigue siendo un punto común.
