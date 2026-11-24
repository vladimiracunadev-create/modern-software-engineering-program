# Agente

## Definición

Un **agente** es un sistema donde el modelo decide el siguiente paso y el uso de herramientas en cada vuelta. `SE-589` lo define con una pregunta operativa: ¿qué componente elige la próxima acción? Si la elige el código (un `if`, una tabla de rutas, una secuencia fija en la que el modelo rellena huecos), es un *workflow*; si la elige el modelo a partir de lo que ha visto hasta ese momento, es un agente.

## Por qué importa

De esa frase salen todas las consecuencias de diseño. El workflow es predecible y barato porque su grafo de ejecución existe antes de la entrada; el agente es flexible porque su grafo se construye sobre la marcha, y por eso mismo no se puede revisar de antemano, solo acotar. Elegir entre uno y otro decide cuánto control, costo y capacidad de prueba se tiene.

## Cómo funciona

El agente repite un ciclo: observa el estado, el modelo elige una acción (normalmente una herramienta), el arnés la ejecuta y el resultado vuelve al contexto. Termina por convergencia o por una condición de parada. Como el camino no está fijado, se controla desde fuera: herramientas disponibles, permisos, presupuesto de pasos y salida obligatoria. Un `while` donde el código decide la condición con reglas es un workflow; uno donde la decide el modelo es un agente (`SE-589`).

## Ejemplo

`SE-589`: la coordinación de un programa con 40 cursos decide el asistente de *Avisos*. Clasifica dos semanas de solicitudes reales en consultas de política, cambios de configuración e investigaciones. Para las dos primeras escribe workflows con un solo paso de modelo y una prueba por camino. Para las investigaciones diseña un agente con tres herramientas de solo lectura, un presupuesto de ocho pasos y una salida obligatoria: un informe con las evidencias que citó, o escalada a una persona. Lo que no se clasifica con confianza va a la persona.

## Errores y confusiones comunes

Llamar «agente» a cualquier uso de un modelo: si el código fija la secuencia, es un workflow. Dar a un agente más autonomía de la que su verificación permite.

## Límites y cuándo no aplica

Donde el camino es conocido de antemano, un workflow es más barato, predecible y fácil de probar; el agente solo se justifica cuando la tarea exige decidir el camino sobre la marcha. Las cifras del caso (40 cursos, ocho pasos) son del ejemplo de la clase, no de una medición.
