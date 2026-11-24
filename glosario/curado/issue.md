# Issue

## Definición

En el programa, un **issue** es un problema que ya ocurrió y requiere acción, con responsable, fecha y criterio de cierre (SE-187). SE-198 usa el mismo término en el sentido de la plataforma de colaboración: un registro con identificador estable de un problema, una propuesta o una decisión pendiente. Los dos sentidos convergen en que el issue es un registro con dueño; esta entrada desarrolla ambos y marca la diferencia con el riesgo.

## Por qué importa

Distinguir un issue de un riesgo cambia cómo se gestiona. Un riesgo es algo que puede ocurrir y se gestiona con probabilidad y respuesta; un issue ya ocurrió y se gestiona con responsable, fecha y cierre. La confusión habitual es llamar «riesgo» a todo lo que preocupa y dejar los issues en una hoja sin dueño: nadie los cierra.

## Cómo funciona

SE-187 describe el issue como un problema presente (el entorno de pruebas se cayó, un contrato se rompió) que **no tiene probabilidad, solo impacto**. Necesita tres cosas: un responsable, una fecha y un criterio de cierre. La transición clave es la de **riesgo materializado → issue**: cuando un riesgo ocurre, pasa al registro de issues, y esa transición se anota, porque es la señal de que el disparador funcionó o de que no existía.

El ejemplo de SE-187 reorganiza una hoja de 23 filas en cuatro registros: riesgos (seis, con causa, efecto, probabilidad, impacto, disparador, respuesta y responsable), supuestos (cinco, con quién los afirma, evidencia y fecha de validación), issues (cuatro, con responsable y fecha) y decisiones (siete, con contexto y disparador). Cada tipo tiene su propio ciclo.

En la plataforma de colaboración (SE-198), el issue es la unidad de seguimiento y se enlaza con el código: una palabra clave en el mensaje de la integración (por ejemplo «closes #12») cierra el issue automáticamente. Dos fallos con causa conocida: el issue no se cierra al integrar porque la sintaxis no es la reconocida o falta la palabra por cada número (corrección: repetir la palabra clave para cada número y usar la forma documentada); y el issue se cierra sin que el defecto desaparezca porque no hay una prueba que falle antes y pase después (corrección: añadir la prueba de regresión como criterio de cierre).

## Ejemplo

El equipo de la plataforma registra: «Issue 3: el entorno de pruebas no responde desde el martes. Responsable: infraestructura. Fecha: jueves. Cierre: la suite completa corre en el entorno». Antes era un riesgo («el entorno podría caerse»); al ocurrir pasa a issue y se anota que el disparador funcionó o no existía. (Redacción ilustrativa.)

## Errores y confusiones comunes

- **Llamar riesgo a todo**: los problemas presentes quedan sin dueño.
- **Issues sin criterio de cierre**: se cierran por cansancio, no por verificación.
- **Cerrar sin prueba de regresión**: el defecto puede volver.
- **Confundir issue con tarea**: una tarea es trabajo planificado; un issue es un problema o decisión registrada.

## Límites y cuándo no aplica

En muchos equipos la plataforma llama «issue» a cualquier ítem (también ideas, preguntas, tareas); el sentido estricto de SE-187 conviene como disciplina de gestión pero no siempre coincide con el uso de la herramienta. Para trabajo de una sola persona y corta duración, un registro formal puede ser exceso.
