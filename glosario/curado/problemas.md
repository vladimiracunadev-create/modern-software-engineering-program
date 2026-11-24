# Problemas

## Definición

En descubrimiento de producto, un **problema** es una brecha entre lo que una persona intenta lograr y lo que logra, con una consecuencia observable y una causa que puede investigarse (SE-121). Sin esos tres elementos, dice la clase, es una opinión. No es lo mismo que una solución deseada ni que un estado de ánimo.

## Por qué importa

Cambia el punto de partida de todo el trabajo posterior. Si el equipo parte de una solución («agregar un botón»), solo discute soluciones; si parte de un problema bien enunciado, puede comparar soluciones y comprobar si alguna sirvió. Un enunciado de problema que otras personas pueden confirmar o refutar permite acordar antes de construir.

## Cómo funciona

SE-121 propone una estructura de enunciado: **actor** + **lo que intenta lograr** + **lo que se lo impide** + **consecuencia**. Ejemplo de la clase: «los estudiantes pierden su avance cuando la sesión expira y no pueden recuperarlo». Es **investigable** cuando existe una observación que lo confirmaría o lo refutaría (por ejemplo, registros de sesiones expiradas con borrador sin guardar). Esa observación es lo que distingue un problema de una impresión.

En contraste, «los usuarios están insatisfechos» no es un problema sino un estado de ánimo, sin actor concreto ni observable. La diferencia importa porque solo un enunciado investigable permite que otra persona llegue a la misma conclusión desde los mismos datos.

Dos fallos que la clase prevé. Primero, la reunión que discute «la solución» una hora sin acordar el problema: se aceptó la petición original como requisito; la corrección es reformular la petición como necesidad («necesito… para…») antes de proponer opciones. Segundo, el enunciado que pasa el linter pero nadie reconoce como real: la regla comprueba forma, no existencia; la corrección es pedir a una segunda persona que cite un registro o una observación que lo confirme.

## Ejemplo

En la plataforma de entregas (SE-121), el análisis de tickets sintéticos muestra que la causa más frecuente es la expiración de sesión. El problema enunciado: «estudiantes que escriben una entrega larga pierden el texto al expirar la sesión y no pueden recuperarlo». La observación que lo confirmaría: registros de sesiones expiradas con borrador no guardado. Las clases siguientes preguntan quiénes son las personas afectadas (SE-122), qué se sabe de ellas por entrevistas (SE-123) y qué hipótesis contrastar (SE-124).

## Errores y confusiones comunes

- **Discutir la solución sin acordar el problema.**
- **Enunciado sin actor ni observable**: «es confuso» no sirve.
- **Enunciado que oculta una solución**: «falta un botón de guardar» ya es una solución.
- **Confundir problema con oportunidad**: el problema es la brecha; la oportunidad añade tamaño, frecuencia y ventana.

## Límites y cuándo no aplica

Un buen enunciado no prueba que el problema merezca resolverse: eso lo decide su tamaño y la prioridad. Algunos problemas se descubren al construir y no admiten enunciado previo; entonces el prototipo hace de investigación. Los tickets de SE-121 son sintéticos: ilustran el método, no la frecuencia real de ninguna causa.
