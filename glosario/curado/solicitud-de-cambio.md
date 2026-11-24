# Solicitud de cambio

## Definición

Una **solicitud de cambio** es la propuesta registrada de modificar la línea base, con motivo, alcance y decisión (SE-153). Convierte una modificación en un objeto con autor, motivo y alcance.

## Por qué importa

Evita cambios silenciosos, obliga a nombrar el motivo y deja un historial que explica por qué el sistema es como es. Sin solicitudes, la línea base se edita sin que nadie lo sepa, y la pregunta «¿esto está dentro de lo acordado?» deja de tener respuesta. Cambia cómo se gestiona la especificación: los cambios pasan por un registro, no por conversaciones sueltas.

## Cómo funciona

SE-153 enumera el contenido: **qué cambia**, **quién lo pide**, **por qué**, **qué elementos alcanza** y **qué decisión se tomó**. El **alcance** se obtiene con el análisis de alcance: recorriendo las dependencias desde el elemento modificado para listar los requisitos, criterios, pruebas y documentos afectados. La decisión (aceptar, rechazar, aplazar) tiene un responsable y una fecha.

Registrarla sirve a tres cosas, dice la clase: **evita cambios silenciosos**, **obliga a nombrar el motivo** y **deja un historial**. Un cambio urgente puede saltarse la espera, pero **no el registro**: se registra después, lo antes posible. Esto conserva el principio sin convertirlo en burocracia que paralice.

La solicitud opera sobre una línea base con identidad estable (etiqueta y hash normalizado). Al aprobarse, se crea una nueva línea base con su propia identidad. Una prueba de regresión puede verificar el hash normalizado de la línea base y fallar si cambia sin una solicitud registrada, de modo que el proceso se hace cumplir. Dos síntomas que previene: nadie sabe cuál era la versión acordada (no hay línea base identificada) y un cambio «pequeño» rompe media especificación (no se calculó el alcance).

SE-153 muestra una solicitud de cambio con su análisis y su decisión sobre la línea base 1: propone un cambio, lista lo que alcanza, y registra la decisión.

## Ejemplo

SC-014. Qué cambia: el tope de penalización pasa del 50 % al 30 %. Quién: coordinación académica. Por qué: reclamos por descuentos excesivos. Alcance: regla BR-07, requisito REQ-12, pruebas de frontera TST-31 a TST-34, texto de política publicado. Decisión: aceptada el 4 de marzo, responsable: producto. Resultado: línea base 2. (Solicitud ilustrativa en el formato de SE-153.)

## Errores y confusiones comunes

- **Nadie sabe cuál era la versión acordada**: no hay línea base identificada.
- **Un cambio «pequeño» rompe media especificación**: no se calculó el alcance.
- **Registrar solo los cambios grandes.**
- **Saltarse el registro por urgencia.**

## Límites y cuándo no aplica

En un proyecto exploratorio con requisitos que cambian a diario, una solicitud formal por cada cambio frena el aprendizaje; se usa una línea base ligera por iteración. El registro no garantiza que el cambio sea bueno, solo que sea visible y atribuible.
