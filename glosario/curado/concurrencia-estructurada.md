# Concurrencia estructurada

## Definición

La **concurrencia estructurada** es la disciplina por la que toda tarea hija vive dentro de un bloque que la espera, propaga sus errores y la cancela al salir (`SE-387`). La vida de las tareas queda anidada en la estructura del código, igual que las variables locales quedan anidadas en las funciones.

## Por qué importa

Lanzar tareas «sueltas» deja trabajo huérfano: tareas que siguen escribiendo, con sus efectos, sin un dueño que las vea o las espere. Eso produce errores que aparecen después y lejos de su causa. La decisión que cambia es cómo se lanzan las tareas concurrentes: dentro de un bloque con dueño, no como disparos al aire. Lo que se gana es una propiedad de razonamiento: cuando el bloque termina, no queda nada en vuelo que haya nacido dentro de él.

## Cómo funciona

`SE-387` fija tres reglas del bloque:

1. **No termina hasta que todas las hijas terminan**: el bloque espera.
2. **Un error de una hija cancela a las hermanas**: no quedan tareas corriendo sobre un resultado que ya es inválido.
3. **El error se propaga al padre**: no se pierde en silencio.

En Python, `asyncio.TaskGroup` (Python 3.11) ofrece esta estructura. Frente a ello, `create_task` sin esperar la tarea, o `gather` que propaga el primer error sin cancelar al resto, dejan tareas huérfanas: siguen vivas tras el error, a veces escribiendo en un recurso que el padre ya considera cerrado. La causa es que el ciclo de vida de la tarea no está ligado a ningún alcance del código; nadie es responsable de ella.

La cancelación en estos modelos es cooperativa: la tarea hija debe ceder en puntos de espera para que pueda cancelarse.

## Ejemplo

Un servicio consulta tres fuentes en paralelo para armar una respuesta. Con un `TaskGroup`, si una consulta falla las otras dos se cancelan y el error sube al llamador; al salir del bloque no queda ninguna consulta en vuelo. Con tareas sueltas, las otras dos siguen ejecutándose y pueden escribir en una caché después de que el llamador devolvió un error. Es el contraste que describe `SE-387`.

## Errores y confusiones comunes

- **Tareas que escriben después de un error**: tareas sueltas sin dueño; se corrige con `TaskGroup` o un bloque que las espere.
- **La memoria crece durante una ráfaga y el proceso muere**: buzón sin límite; se corrige con cola acotada con rechazo o espera.
- **Creer que `gather` equivale a la estructura**: propaga el primer error pero no cancela al resto.
- **Olvidar la cancelación cooperativa**: una hija que nunca cede no se puede cancelar.

## Límites y cuándo no aplica

Encaja cuando las tareas tienen un ciclo de vida acotado por una operación. Para trabajo que debe sobrevivir a la petición que lo originó (un proceso en segundo plano de larga vida), un bloque que lo espere no es la forma correcta: se necesita un supervisor o una cola. La disciplina es de ciertos lenguajes y bibliotecas: depende de que el entorno ofrezca el bloque, y en otros hay que construirla a mano.
