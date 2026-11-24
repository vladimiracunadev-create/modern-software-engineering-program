# Historias de usuario

## Definición

Una **historia de usuario** es una unidad de valor pequeña, negociable y comprobable, expresada como tarjeta, conversación y confirmación (SE-148). La tarjeta es la frase corta «como… quiero… para…»; la conversación es el diálogo que provoca; la confirmación son los criterios que la cierran.

## Por qué importa

Divide el valor en incrementos que se pueden negociar, estimar y probar. Cambia cómo se planifica: en lugar de especificar todo por adelantado, se trabaja con piezas pequeñas cuyo detalle se acuerda cuando toca construirlas. Lo importante, dice SE-148, no es la plantilla de la tarjeta sino la conversación que provoca.

## Cómo funciona

El criterio de calidad más extendido es INVEST: independiente, negociable, valiosa, estimable, pequeña, comprobable. SE-148 lo usa para decidir si algo es una historia. Una que no cumple «valiosa» (por ejemplo, «crear la tabla de borradores») es una tarea técnica: no tiene valor visible para quien la pidió. Una que no cumple «pequeña» es un épico que todavía no se cortó.

La causa de que funcione es que la tarjeta es deliberadamente incompleta: obliga a conversar, y esa conversación hace aparecer lo que un documento exhaustivo escondería. Se cierra con la confirmación: los criterios de aceptación, preferiblemente como ejemplos (SE-149). Y se corta en vertical (corte vertical), de modo que cada historia atraviese las capas y pueda mostrarse.

SE-148 distingue historias de otras formas de contar un requisito: casos de uso (con actor, escenario principal y extensiones) y job stories (centradas en la situación y la motivación, no en el rol). Las job stories son útiles cuando el rol no explica el comportamiento o cuando el mismo actor está en situaciones muy distintas; para un sistema con roles bien separados y permisos distintos, la historia de usuario sigue siendo clara. La decisión es de claridad, no de moda.

## Ejemplo

En la plataforma de entregas: «Como estudiante, quiero subir mi entrega en PDF, para que quede registrada antes del plazo». La conversación aclara el tamaño máximo y qué ocurre tras el plazo; la confirmación se escribe como ejemplos: un PDF de 10 MB se acepta y uno de 10,1 MB se rechaza con un mensaje que indica el límite. (La historia es una ilustración; el límite viene de SE-149.)

## Errores y confusiones comunes

- **Todas las historias empiezan con «Como usuario»**: no se definió el catálogo de actores; corrección: crear el catálogo con objetivo y contacto y exigir que cada historia nombre uno.
- **El caso de uso solo describe el camino feliz**: las extensiones se consideraron detalles.
- **Historias como tareas técnicas** sin valor visible.
- **Tomar la tarjeta por la especificación**: la tarjeta recuerda una conversación; no la reemplaza.

## Límites y cuándo no aplica

Las historias son poco adecuadas para requisitos transversales (rendimiento, seguridad) que no encajan en un incremento de usuario; esos se expresan como escenarios de calidad. Cuando hay obligaciones legales o contratos que exigen especificación detallada y trazable, las historias solas no bastan. SE-148 declara que no se midió ningún equipo ni se comparó la comprensión de las personas con cada forma de relato.
