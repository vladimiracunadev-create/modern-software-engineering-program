# Tarea

## Definición

**Tarea** es una palabra con varios sentidos en el programa. El principal (SE-205, documentación) es una acción con verbo y resultado observable que una audiencia quiere completar usando la documentación. SE-169 (usabilidad) la define como el objetivo de una persona con un resultado observable, independiente de la pantalla que se use. SE-230 (concurrencia) la usa para la unidad de trabajo que el bucle de eventos toma de una cola y ejecuta hasta vaciar la pila. SE-566 (desarrollo asistido por IA) la usa para una unidad de trabajo ordenada, con dependencias, archivos afectados y, si procede, marca de ejecución en paralelo. Esta entrada desarrolla sobre todo el sentido de personas (SE-205, SE-169) y señala los técnicos.

## Por qué importa

Una tarea es la unidad por la que la gente busca, aunque no la formule como título. Si una página no responde a un verbo, no se encuentra; si una interfaz se diseña por pantallas y no por tareas, se pierde el objetivo de la persona. Cambia cómo se organiza la documentación y cómo se evalúa la usabilidad: por tareas completadas, no por páginas escritas.

## Cómo funciona

Una tarea tiene **un verbo y un resultado observable**: «cambiar el plazo de una tarea y avisar a la clase». Se reconoce la página que responde a una tarea porque **termina cuando el resultado existe**; una página que describe «el módulo de calendario» no termina nunca. Las tareas además delimitan lo que no hay que escribir: si ninguna audiencia necesita saber cómo se implementa el redondeo para hacer su tarea, esa explicación pertenece a otra página.

En usabilidad (SE-169), la tarea es independiente de la pantalla: «entregar el trabajo» puede hacerse desde el móvil o la web, y evaluar por tarea permite comparar diseños distintos con el mismo criterio de éxito.

En los sentidos técnicos, la lógica es parecida: una tarea del bucle de eventos (SE-230) es una unidad que se ejecuta hasta vaciar la pila; una tarea de un plan de IA (SE-566) es una unidad ordenada con dependencias y archivos afectados, de modo que las independientes pueden ejecutarse en paralelo y las dependientes, en orden.

## Ejemplo

El portal documental de la plataforma de entregas (SE-205) tiene un inventario de tareas por audiencia: estudiante (entender el descuento, pedir prórroga), docente (cambiar plazo, conceder prórroga, corregir una nota), secretaría (exportar el acta con la nota final) y mantenimiento (depurar el cálculo, cambiar el tope). «Conceder prórroga» es una tarea con verbo y resultado: tras la guía, la prórroga existe y la estudiante ve el nuevo plazo.

## Errores y confusiones comunes

- **Páginas por módulo, no por tarea**: nadie encuentra lo que busca.
- **Confundir tarea con función del producto**: la función es del producto; la tarea, de la persona.
- **Definir la tarea por la pantalla**: se pierde el objetivo.
- **Mezclar los sentidos**: tarea de documentación, de usabilidad, del bucle de eventos y de un plan de IA son conceptos distintos.

## Límites y cuándo no aplica

Para documentación de referencia (parámetros, firmas), la tarea no es el eje: se organiza como el producto. Una tarea mal acotada (demasiado grande) no «termina» y no se puede comprobar. En el sentido técnico de concurrencia, no hay relación con las tareas de los equipos ni de los tableros.
