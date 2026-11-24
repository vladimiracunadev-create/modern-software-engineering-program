# Despliegue por etapas

## Definición

Un **despliegue por etapas** (*staged rollout*) es la publicación de una versión a fracciones crecientes de la flota con una regla para detenerla. `SE-271` (actualizaciones OTA y recuperación) lo enseña para flotas de dispositivos. La diferencia con un despliegue «de golpe» es doble: la exposición crece de a poco y cada paso tiene una condición explícita para avanzar o frenar.

## Por qué importa

Publicar a toda la flota a la vez expone a todos a un defecto. En dispositivos físicos recuperar uno es caro, y a veces imposible sin visita. `SE-271` lo resume: limitar la exposición de una versión nueva acota el daño si falla.

## Cómo funciona

Las etapas típicas son 1 %, 10 % y 100 %. Funcionan solo con dos condiciones:

1. **Cada etapa es lo bastante grande para ver el defecto.**
2. **El sistema recoge informes de fallo** y alguien (o una regla) los lee antes de avanzar.

`SE-271` da la cuenta: si un defecto afecta a una fracción *f* de los dispositivos, una etapa de *n* dispositivos espera *n·f* fallos. Si *n·f* es menor que el umbral de informes, el defecto no se ve y el despliegue avanza, justo lo que no debía. Una etapa de 100 dispositivos con un defecto que afecta al 1 % espera un fallo, que puede pasar inadvertido o ser atribuido al ruido.

## Ejemplo

Cálculo ilustrativo propio, con la fórmula de la clase: una flota de 10 000 dispositivos, etapa del 1 % (100 dispositivos), defecto con *f* = 2 %. Se esperan 2 fallos; si la regla de parada exige 5 informes, el despliegue pasa a 10 % y el defecto aparece con 20 fallos (1 000 × 2 %). La etapa inicial protegió poco, y el ajuste razonable es subir la primera etapa o bajar el umbral.

## Errores y confusiones comunes

- **Etapas demasiado pequeñas para detectar el defecto** (`n·f` bajo el umbral).
- **Avanzar por tiempo en vez de por señal:** el calendario no sustituye a los informes.
- **Un corte durante la actualización deja el dispositivo mudo,** problema de otra capa que la clase resuelve con dos ranuras y cambio de indicador al final; el despliegue por etapas no lo previene.
- **Confundirlo con la actualización diferencial,** que trata de los bytes enviados, no de a quién.

## Límites y cuándo no aplica

No detecta defectos que solo aparecen tras mucho tiempo o en un subconjunto no representado por la etapa (otro hardware, otra región). Requiere una forma de detener y de revertir. Las simulaciones de `SE-271` usaron fallos independientes y valores del autor, no una flota real.
