# Prueba de caracterización

## Definición

Una **prueba de caracterización** es una prueba que fija el comportamiento actual de un código, sea o no el correcto, para detectar cambios no deseados (`SE-519`). `SE-311`, `SE-323` y `SE-558` la usan en el mismo sentido: fija lo que el código hace hoy, sin afirmar que sea lo correcto. Es el fundamento del maestro dorado.

## Por qué importa

En un sistema heredado muchas veces no hay especificación fiable: la especificación es el propio sistema. Escribir antes «lo correcto» puede ser imposible o carísimo. La decisión que cambia es el orden del trabajo: primero se observa y se registra lo que el código hace, y con esa red de seguridad se refactoriza o se moderniza.

## Cómo funciona

Una prueba normal expresa lo que el código **debería** hacer según una especificación. Una prueba de caracterización expresa lo que **hace hoy**: se ejecuta el código con una entrada, se observa la salida y se escribe como expectativa. Su valor es que sirve de red de seguridad: si después de un cambio la salida difiere, el cambio alteró un comportamiento, y entonces alguien decide si fue deseado (`SE-519`).

La técnica invierte el orden habitual (primero se observa, luego se afirma). El resultado puede incluir comportamientos que hoy parecen errores; se registran igual, porque otros sistemas pueden depender de ellos, y se marcan para decidir aparte.

`SE-323` la presenta como maestro dorado (también llamado prueba de aprobación): en el experimento se generan 5 000 entradas con semilla fija (canal, urgencia, horas, adjuntos y tamaño del grupo) y se guarda la salida de la función antigua; el refactor produce la misma salida en las 5 000 (0 diferencias). La semilla es parte de la evidencia: sin ella, otra persona no puede repetir la comprobación. La calidad depende de que las entradas cubran los bordes de decisión, y de medir mutantes para saber si las pruebas detectarían un cambio real.

## Ejemplo

Una función heredada de cálculo de plazos no tiene pruebas. Se generan entradas representativas y de borde, se ejecuta la función y se guardan las salidas como expectativas. Se refactoriza por pasos y se ejecutan las pruebas tras cada paso. Una diferencia en un caso concreto revela un cambio de comportamiento antes de llegar a producción. Procedimiento de `SE-519`.

## Errores y confusiones comunes

- **La prueba pasa y producción cambia**: los ejemplos no cubren los bordes de decisión; se corrige añadiendo casos de borde y midiendo mutantes.
- **La prueba falla de forma intermitente**: orden de un conjunto, reloj o azar; se corrige repitiendo con condiciones distintas y normalizando la fuente.
- **Actualizarla sin pensar cuando falla**: deja de proteger.
- **Tratarla como especificación**: registra defectos junto con virtudes.

## Límites y cuándo no aplica

Es útil cuando no hay pruebas finas y se quiere cambiar sin definir primero lo correcto; donde existen pruebas que documentan la intención, esas son preferibles. No dice que el comportamiento sea bueno, solo que no cambió. Y protege únicamente los comportamientos que las entradas ejercitan: sin buena cobertura y medición de mutantes, da una confianza que el código no tiene.
