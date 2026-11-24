# Condición de aborto

## Definición

Una **condición de aborto** es una regla evaluada de forma automática durante un experimento que, si se cumple, lo detiene y revierte la falla (`SE-506`). `SE-394` la usa en el sentido de umbral de una métrica que detiene el experimento. Es el freno de seguridad de la ingeniería del caos.

## Por qué importa

Un experimento de falla inyectada puede salirse de lo previsto: el servicio puede degradarse más de lo esperado o la falla puede alcanzar a otro servicio. Sin freno automático, el daño depende de que una persona mire a tiempo. La decisión que cambia es que el experimento solo se autoriza cuando se sabe, antes de empezar, en qué punto se detiene solo.

## Cómo funciona

`SE-506` cita dos implementaciones reales. AWS FIS usa **condiciones de parada**: alarmas de CloudWatch construidas a partir del estado estable que detienen el experimento si el servicio alcanza un estado inaceptable; un experimento detenido no se puede reanudar. ChAP incorpora un interruptor propio que lo termina automáticamente si se supera un presupuesto de error predefinido.

La clase da tres rasgos que separan una condición útil de una decorativa. El primero: se evalúa sobre el **grupo experimental** y no sobre el tráfico global, porque un grupo del 1 % no mueve el global. Los otros los muestra una simulación: el experimento planeado inyecta 20 % de errores, pero a los 60 s la falla empeora a 100 %. Se comparan cuatro políticas (sin aborto; abortar si el global falla más de 1 % en 10 s; abortar si el grupo experimental falla más de 50 % en 10 s; abortar al acumular 300 peticiones dañadas) y se mide el daño en peticiones. Sin aborto, el daño crece de 104 a 11 444 peticiones del radio menor al mayor; con 2 % del tráfico, los abortos por umbral se disparan a los 65 s y limitan el daño a 34.

## Ejemplo

Un experimento inyecta latencia en el 1 % del tráfico. Su condición de aborto es una alarma sobre la tasa de errores del grupo experimental; si supera el 50 % durante 10 segundos, el experimento se detiene y la falla se revierte. Si la falla empeora por compartir un recurso con otro servicio, el freno actúa en segundos en lugar de esperar a una persona.

## Errores y confusiones comunes

- **El experimento «terminó» sin conclusión**: falta el estado estable o la condición de aborto; se definen antes y se registra el resultado (`SE-394`).
- **Medir sobre el tráfico global**: un grupo pequeño no mueve el global y la condición nunca dispara.
- **Condición inalcanzable**: un umbral que nunca se cumple es decorativo; un linter de forma, como el de `SE-394`, lo comprueba.
- **Confiar solo en el aborto**: no sustituye acotar el alcance.

## Límites y cuándo no aplica

La condición reduce el daño pero no lo elimina: entre la causa y la detección hay una ventana, y el daño acumulado en esa ventana ya ocurrió. `SE-394` permite experimentos en producción solo con alcance acotado, hipótesis medible, condición de aborto y ensayo previo en entornos de prueba. Las cifras de la simulación son del escenario construido en la clase; el valor del umbral y de la ventana depende de cada servicio.
