# Regla de decisión

## Definición

Una **regla de decisión** es el procedimiento por el cual un proyecto acepta o rechaza una propuesta (SE-200). SE-287 usa el término en un sentido emparentado: un criterio escrito que asigna un candidato a una carga (qué elementos van a qué lugar), que hace la elección revisable. En ambos, lo esencial es que la regla esté escrita antes de decidir.

## Por qué importa

Cada regla tolera un tipo de error distinto, y la disponibilidad de las personas decide cuál es adecuada. Si no hay regla, las decisiones dependen de quién tiene más peso o de quién insiste más. Con una regla escrita, quien contribuye sabe qué esperar y la decisión puede revisarse. Cambia cómo se gobierna un proyecto: no solo qué se decide, sino cómo.

## Cómo funciona

SE-200 enumera cuatro familias de reglas: un **líder con la última palabra**, **votación por mayoría**, **consenso con veto** y **consenso por falta de objeción en un plazo** (consenso perezoso). Cada una paga con un error diferente. La que acepta por silencio es rápida y deja pasar lo que nadie leyó (acepta propuestas dañinas). La que exige votos mínimos se bloquea si faltan votantes (rechaza propuestas buenas por falta de quórum). El líder único decide rápido y concentra el riesgo en una persona.

La clase representa esto en una figura: cada grupo es una regla de decisión y sus barras muestran el porcentaje de propuestas dañinas aceptadas, de buenas rechazadas y el tiempo de decisión, en una simulación. Lo que enseña es el compromiso entre velocidad y protección, no una regla óptima.

En la plataforma de entregas, la regla escrita en `CONTRIBUTING.md` es graduada: los cambios pequeños los aprueba una mantenedora; los que modifican una regla de negocio exigen dos aprobaciones y un plazo de 72 horas; los cambios de gobierno exigen consenso. La graduación asigna más exigencia donde el error cuesta más. Se acompaña con un indicador mensual de cuántas personas cubren la mitad de los commits, para planificar relevos (factor de camión), y con un tiempo objetivo de primera respuesta a contribuciones externas.

En SE-287, la misma idea se aplica a asignar un candidato a una carga: un criterio escrito (por ejemplo, un umbral o un orden de preferencia) que otra persona puede reaplicar y discutir.

## Ejemplo

Un cambio de texto en la documentación se aprueba con una sola revisora; una modificación de la fórmula de penalización necesita dos aprobaciones y esperar 72 horas, para que quien esté de vacaciones tenga ocasión de objetar. Si nadie objeta en el plazo, procede (consenso perezoso, solo en cambios de bajo riesgo). (Estructura tomada de SE-200.)

## Errores y confusiones comunes

- **Contribuciones externas sin respuesta**: no hay tiempo objetivo ni responsable; corrección: fijar un tiempo de primera respuesta y rotar quien lo cumple.
- **Una sola regla para todo**: la misma exigencia para un cambio de texto y para el gobierno.
- **No escribirla**: se improvisa y se percibe arbitraria.
- **Confundir regla de decisión con regla de negocio**: la primera gobierna el proyecto; la segunda, el producto.

## Límites y cuándo no aplica

Una regla escrita no sustituye la confianza ni el liderazgo. En proyectos muy pequeños, con una o dos personas, el formalismo sobra. Las cifras de la simulación son ilustrativas de un modelo, no mediciones de proyectos reales.
