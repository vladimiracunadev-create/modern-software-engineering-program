# Aprobación humana

## Definición

La **aprobación humana** es la confirmación explícita de una persona antes de una acción (`SE-586`). En el desarrollo con agentes es uno de los controles que se aplican de forma proporcional al riesgo.

## Por qué importa

Gobernar el desarrollo con agentes es decidir cuánto control reciben distintos cambios. `SE-586` apoya esa decisión en dos referencias: NIST organiza la gestión del riesgo de IA en funciones (gobernar, mapear, medir y gestionar), y su valor para la clase es la secuencia (quién decide, qué puede salir mal, medir, actuar); OWASP recomienda limitar la autonomía de un agente y exigir aprobación humana para acciones de alto impacto.

## Cómo funciona

La **proporcionalidad** es la idea central: no todo cambio exige la misma aprobación. Acciones reversibles y de bajo impacto avanzan sin interrupción; las de alto impacto (borrados, despliegues, gastos, envíos externos) se detienen hasta que una persona confirma. La aprobación solo sirve si la persona recibe la información necesaria para decidir.

## Ejemplo

Un agente puede leer archivos y proponer cambios sin aprobación; antes de ejecutar una migración que altera datos, detiene la ejecución y presenta qué hará y qué se perdería si se equivoca.

## Errores y confusiones comunes

Pedir aprobación para todo (se aprende a pulsar «sí» sin leer); pedirla sin mostrar el efecto de la acción.

## Límites y cuándo no aplica

No sustituye a los controles técnicos (confinamiento, permisos mínimos): una persona cansada o sin contexto aprueba lo que no debería. Es un control más, no el único.
