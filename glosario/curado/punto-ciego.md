# Punto ciego

## Definición

Un **punto ciego** es una familia de cambios que ninguna regla detecta (`SE-372`). `SE-541` la precisa para pruebas: una clase de defecto que un oráculo no puede ver. Dos mecanismos de comprobación que miran lo mismo desde el mismo ángulo comparten el punto ciego.

## Por qué importa

Un conjunto de comprobaciones verde no dice que todo esté bien, sino que lo que miran está bien. La decisión que cambia es cómo se combinan las defensas: no se acumulan comprobaciones del mismo tipo, sino de ángulos distintos, con puntos ciegos distintos y un costo proporcional al riesgo.

## Cómo funciona

`SE-541` observa que cada oráculo mira una parte del comportamiento:

- Las **pruebas de ejemplo** miran los casos que alguien imaginó.
- El **contrato** mira propiedades generales, no valores concretos.
- Los **escenarios con reloj** miran secuencias en el tiempo, pero eligen horas concretas.
- El **modelo de referencia** compara contra una segunda escritura de la regla y comparte con la primera cualquier malentendido de la especificación.

El punto ciego aparece donde ninguno mira. En el laboratorio de la clase, las ocho pruebas y los escenarios dejan vivo el mismo mutante, uno que avisa en el instante exacto del vencimiento, porque ninguno prueba esa hora exacta. Ese cambio no lo ve ningún oráculo, aunque cada uno sea razonable por separado.

La consecuencia, según la clase, es que la pregunta «¿cuál oráculo basta?» no tiene respuesta única, porque mezcla preguntas distintas. Ninguna técnica mata todos los mutantes por sí sola, salvo el modelo de referencia, que comparte los malentendidos de la especificación. Lo defendible es una combinación con puntos ciegos distintos. `SE-372` lo aplica a datos: familias de cambios que ninguna regla de calidad detecta.

## Ejemplo

Un recordatorio debe avisar antes del vencimiento. Un mutante cambia la comparación para avisar también en el instante exacto. Las pruebas de ejemplo no usan esa hora; el contrato no la fija; los escenarios eligen horas distintas. Solo un caso de borde en el instante exacto lo detectaría. Esa hora es el punto ciego de todo el conjunto. Es el caso del laboratorio de `SE-541`.

## Errores y confusiones comunes

- **Suponer que más pruebas del mismo tipo cierran el punto ciego**: lo comparten.
- **Confiar en un modelo de referencia** sin ver que hereda los malentendidos de la especificación.
- **Confundirlo con baja cobertura**: puede haber cobertura de líneas y aun así un punto ciego de sentido.
- **No medir con mutantes**: es la forma de hacerlo visible.

## Límites y cuándo no aplica

El punto ciego se conoce solo cuando se encuentra: no existe un método para listar todos los de un conjunto. La medición con mutantes revela los que los mutantes cubren, no los demás. Y no todos los puntos ciegos merecen cerrarse: el costo de ver una clase de defecto debe ser proporcional al riesgo.
