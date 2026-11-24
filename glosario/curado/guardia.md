# Guardia

## Definición

La **guardia** (*on-call*) es el turno en que una persona o grupo responde a las páginas de un servicio (`SE-499`).

## Por qué importa

La guardia es un sistema con una capacidad finita. Si se diseña sin calcularla, termina siendo siempre la misma persona, con sueño interrumpido y rotación de personal. La sostenibilidad de la guardia es una condición de la fiabilidad del servicio.

## Cómo funciona

Una persona en guardia una semana de cada *n* atiende todas las páginas de esa semana, y las nocturnas interrumpen el sueño. Con pocas personas, cada una pasa muchas semanas al año en guardia, y las ausencias (vacaciones, enfermedad, formación) concentran la carga en quienes quedan. `SE-499` cita el libro de SRE: no más del 25 % del tiempo de una persona debe ser de guardia, de lo que se deduce un mínimo de personas para una rotación continua con primaria y secundaria (ocho en un solo sitio), además de limitar las incidencias por turno. La medida concreta de sostenibilidad es el número de noches interrumpidas por persona y por periodo.

## Ejemplo

`SE-499` (caso hipotético): el equipo reescribe el runbook de `EntregasConsumoRapido`, lo guarda junto al código y añade un verificador de integración continua (campos, comandos con salida esperada, reversión de lo destructivo, fecha menor de 90 días y alerta existente en el catálogo). Cada trimestre una persona que no lo escribió lo ejecuta en pruebas con un despliegue defectuoso inyectado.

## Errores y confusiones comunes

**La guardia es siempre la misma persona.** Equipo pequeño o ausencias sin plan; calcular la carga y ampliar la rotación o reducir el alcance.

## Límites y cuándo no aplica

Las cifras (25 %, ocho personas) son de un modelo de operación grande; un equipo pequeño debe reducir el alcance del servicio que cubre o compartir la rotación, no copiar el número.
