# Patrones de reparación

## Definición

Los **patrones de reparación** son movimientos repetibles para volver verificable una frase de un requisito: cuantificar, acotar, condicionar y separar (SE-155). Se aplican a requisitos con defectos de ambigüedad, vaguedad o compromiso múltiple.

## Por qué importa

Ofrecen movimientos repetibles para convertir adjetivos en criterios. «Rápido», «fácil» o «seguro» no se pueden probar; reparar la frase con uno o más movimientos la vuelve medible. Cambia la forma de revisar una especificación: no solo se señala el defecto, se propone un procedimiento para repararlo.

## Cómo funciona

SE-155 describe **cuatro movimientos recurrentes**:

- **Cuantificar**: sustituir un adjetivo por un número con unidad («rápido» por «p95 ≤ 1.500 ms»).
- **Acotar**: decir bajo qué carga o entorno («con 200 usuarios concurrentes»).
- **Condicionar**: separar el estímulo de la respuesta («cuando la sesión expira…»).
- **Separar**: dividir una frase con varios compromisos en requisitos singulares («guardará y cifrará y avisará» son tres).

Aplicados juntos, «el sistema responderá rápido» pasa a «con 200 usuarios concurrentes, el 95 % de las peticiones de listado responde en 1.500 ms o menos». Los movimientos **no inventan el valor**: lo toman de una necesidad o una medición. Por eso, un número sin origen es un defecto nuevo. La corrección es registrar la necesidad o la medición de la que proviene y, si falta, marcarlo como **hipótesis**.

La reparación se acompaña de un **procedimiento de verificación** que dice cómo se comprobará, y de la decisión sobre lo que **no** se repara (qué se deja deliberadamente informal y por qué). Otro riesgo que la clase señala: la prueba pasa y las personas siguen quejándose porque la reparación mide un proxy de lo que importa; se valida con personas el umbral y se revisa si el proxy refleja la necesidad.

## Ejemplo

Requisito original: «La subida de archivos debe ser rápida y segura». Separar: dos requisitos. Cuantificar y acotar el primero: «con conexión de 10 Mbit/s, un PDF de 10 MB se sube en menos de 12 s en el 95 % de los intentos». Condicionar el segundo: «cuando el archivo tiene una extensión no permitida, el sistema lo rechaza con un mensaje que indica las extensiones aceptadas». Cada uno se puede probar. (Reparación ilustrativa con los movimientos de SE-155.)

## Errores y confusiones comunes

- **Cifra sin origen**: nadie sabe de dónde salió; corrección: registrar la necesidad o la medición, o marcarla como hipótesis.
- **La prueba pasa y la gente se queja**: el proxy no refleja la necesidad.
- **Reparar solo la forma**: añadir un número arbitrario para parecer preciso.
- **Aplicar un solo movimiento** donde hacen falta varios.

## Límites y cuándo no aplica

No todo requisito debe cuantificarse: algunos se verifican con inspección o con una prueba con personas y un umbral. Un número impuesto sin respaldo da una falsa precisión. La reparación depende de saber qué importa; si no se conoce la necesidad, primero se investiga.
