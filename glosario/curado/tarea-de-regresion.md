# Tarea de regresión

## Definición

Una **tarea de regresión** es una tarea de evaluación derivada de un fallo ya diagnosticado, que protege contra su reaparición. `SE-585` la define como tarea derivada de un fallo diagnosticado; `SE-587` y `SE-588` la precisan como la tarea que protege contra la reaparición de un fallo. Es la versión, para el arnés de un agente, de lo que en el software clásico es una prueba de regresión.

## Por qué importa

Decide si el arnés mejora o solo cambia. Si cada fallo diagnosticado se arregla y se olvida, el mismo fallo reaparece al cambiar el archivo de instrucciones, los permisos o la parada. Con tareas de regresión, la evaluación del arnés **crece con sus propios fallos** (`SE-587`) y cada corrección deja un detector permanente.

## Cómo funciona

Cada fallo diagnosticado produce una tarea con tres elementos (`SE-587`):

1. la **tarea que lo reveló**;
2. la **configuración que lo inyecta**;
3. el **criterio** que debe cumplirse tras el arreglo.

El conjunto se ejecuta en la **integración continua** del arnés y detecta cuándo un cambio reintroduce algún fallo. La causa de su valor es que los fallos de un agente dependen de configuración (herramientas ofrecidas, permisos, reglas de parada, instrucciones), y esa configuración cambia con las versiones del producto; una tarea de regresión comprueba la pieza que depende de ella.

## Ejemplo

`SE-587`: la persona de guardia recibe quince tareas fallidas de la noche. Agrupa las trazas por patrón: tres grupos. Nueve repiten lecturas, cuatro piden el cierre dos veces, dos tienen una escritura denegada. Para el primer grupo comprueba el campo de herramientas ofrecidas: la escritura no figura, porque una actualización del producto había renombrado la herramienta y el arnés no la reconocía. Arregla esa pieza, repite las nueve tareas y se resuelven. Luego añade al conjunto de regresión la prueba de que la herramienta de escritura está ofrecida. El segundo grupo era una parada ignorada tras un cambio de versión del arnés; el tercero, un permiso demasiado estricto.

En `SE-588` se corrige un patrón para limitarlo a los archivos de prueba, se repiten las seis tareas y se añade una tarea de regresión: «un agente puede escribir el código y no las pruebas».

## Errores y confusiones comunes

- **Arreglar sin dejar tarea.** El fallo reaparece tras el siguiente cambio de configuración.
- **Una tarea que no reproduce el fallo.** Debe fallar *antes* del arreglo; si pasa en ambos casos, no protege nada.
- **Confundirla con una prueba unitaria.** Evalúa el comportamiento del arnés completo (agente, herramientas, permisos), no una función.
- **Un conjunto que solo crece.** Conviene revisar tareas obsoletas, pero retirar solo con criterio.

## Límites y cuándo no aplica

Solo protege fallos *ya diagnosticados*: no detecta clases nuevas. Con componentes no deterministas, una tarea puede pasar o fallar por azar; hay que repetir y decidir con un criterio estadístico. En `SE-587` el conjunto es de seis fallos de un caso de estudio, no una muestra representativa de agentes reales. Y una tarea de regresión demasiado atada al texto exacto de una traza se rompe por cambios inocuos; el criterio debe estar en el resultado, no en la redacción.
