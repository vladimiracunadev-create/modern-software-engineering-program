# Mantenimiento

## Definición

El **mantenimiento** es la corrección, adaptación o mejora posterior a la puesta en operación (`SE-003`). No es la fase final de un proceso en cascada: `SE-003` insiste en que el mantenimiento reabre decisiones de diseño y pruebas, y que lo que se aprende al operar corrige requisitos. La palabra se aplica también a artefactos que envejecen, como los runbooks (`SE-499`).

## Por qué importa

Gran parte de la vida y del costo de un sistema ocurre después del primer despliegue. Tratarlo como un apéndice lleva a diseños difíciles de cambiar y a documentación que miente. `SE-003` presenta el ciclo de vida con bucles que impiden leerlo como cascada: operar enseña, el mantenimiento reabre diseño y pruebas, y el retiro devuelve a la concepción el criterio de no construir y la exportabilidad.

## Cómo funciona

La causa de la necesidad de mantenimiento es que el entorno y los requisitos cambian aunque el código no. Se distinguen tres tipos en la definición del programa: **corrección** (arreglar defectos), **adaptación** (seguir siendo válido ante cambios del entorno) y **mejora** (nueva capacidad o calidad).

`SE-499` aplica la idea a los runbooks: envejecen cuando cambia el sistema (se renombra un servicio, cambia el comando de despliegue, se mueve la consola). Tres hábitos los mantienen:

- **dueño:** cada runbook tiene un equipo responsable;
- **fecha de verificación:** la última vez que alguien lo *ejecutó*, no la última vez que se editó;
- **ejercicio:** una prueba programada en un entorno seguro, en la que alguien ajeno al autor sigue el runbook.

Cada incidente real se convierte en una revisión: si el runbook faltó, se corrige. Automatizar pasos seguros (comprobar el estado, recopilar datos) reduce errores humanos; automatizar pasos destructivos exige más cuidado porque amplifica un error de significado.

## Ejemplo

Un runbook dice «reinicia el servicio `entregas-api`»; seis meses después el servicio se renombró. La verificación periódica por alguien ajeno al autor detecta que el comando ya no existe antes de que haga falta en un incidente.

## Errores y confusiones comunes

- **Runbook con «revisa los servicios».** Causa: pasos sin comando ni salida esperada; corrección: un paso por acción, con comando y resultado esperado (`SE-499`).
- **La guardia es siempre la misma persona.** Causa: equipo pequeño o ausencias sin plan; corrección: calcular la carga y ampliar la rotación o reducir el alcance (`SE-499`).
- **Dar por terminado el proyecto al entregar.** Ignora los bucles del ciclo de vida (`SE-003`).

## Límites y cuándo no aplica

No todo cambio es mantenimiento: construir una capacidad nueva de gran tamaño es desarrollo. Un sistema sin dueño no puede mantenerse; `SE-003` lo vincula a decidir también el retiro. Y los hábitos de `SE-499` son prácticas del curso para runbooks, no una norma sobre cualquier artefacto.
