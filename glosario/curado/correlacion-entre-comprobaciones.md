# Correlación entre comprobaciones

## Definición

La **correlación entre comprobaciones** es el grado en que dos comprobaciones fallan o aciertan sobre los mismos defectos (SE-188). Si dos comprobaciones detectan los mismos defectos, están muy correlacionadas; si detectan defectos distintos, poco. Es la razón por la que añadir comprobaciones reduce menos escapes de lo que se espera.

## Por qué importa

Cambia cómo se diseña una definición de terminado: la pregunta pasa de «¿cuántas comprobaciones hay?» a «¿qué ve cada una que las demás no ven?». Añadir una comprobación que ve lo mismo que otra casi no reduce los escapes, aunque cueste tiempo en cada cambio. Es la causa de los equipos con muchas casillas y escapes constantes.

## Cómo funciona

SE-188 parte de un modelo simple. Si cada comprobación detectara defectos al azar, con su propia probabilidad, añadir otra siempre reduciría los escapes de forma **multiplicativa**: dos comprobaciones que detectan el 60 % dejarían pasar 0,4 × 0,4 = 16 %. Pero las comprobaciones miran cosas parecidas: los defectos «fáciles» los ve cualquiera, y los «difíciles» se escapan a todas. Esa **correlación** hace que la segunda y la tercera comprobación aporten mucho menos de lo esperado y que, a partir de cierto punto, no aporten nada. En el caso extremo de correlación total, dos comprobaciones iguales dejan pasar tanto como una (40 %).

La clase cita la observación de Jones: ninguna técnica los elimina todos, y las combinaciones de técnicas **distintas** rinden más que repetir la misma. La consecuencia de diseño es elegir comprobaciones que vean defectos distintos (una revisión humana, una prueba automática, un análisis estático y una prueba de aceptación miran cosas diferentes), no acumular más de la misma.

El procedimiento práctico: **medir qué ve cada comprobación** con los escapes reales o con inyección de defectos, y retirar las que ven lo mismo. El equipo de la plataforma de entregas redujo su definición de terminado de catorce casillas a tres niveles según el tipo de cambio, con una razón registrada por casilla (qué escape evitó la última vez). Un fragmento de SE-188 calcula los escapes esperados de dos comprobaciones independientes y de dos que ven lo mismo, y pide predecir cuál deja pasar menos.

## Ejemplo

Dos comprobaciones detectan cada una el 60 % de los defectos. Si son independientes, escapa el 16 %. Si son idénticas, escapa el 40 %. Si se solapan en la mitad de lo que ven, el escape queda entre ambos valores. En un equipo real, añadir una tercera revisión de estilo a una de estilo y formato no baja los escapes del trimestre, mientras que añadir una prueba de aceptación con ejemplos de frontera sí. (Aritmética ilustrativa del argumento de SE-188.)

## Errores y confusiones comunes

- **Catorce casillas y escapes que no bajan**: comprobaciones correlacionadas; corrección: medir qué ve cada una y retirar las que ven lo mismo.
- **Pensar que la probabilidad de detección se multiplica siempre.**
- **Historias que esperan dos semanas para estar «listas»**: una definición de listo demasiado exigente; reducirla a las preguntas que evitan el rehacer.
- **Medir las comprobaciones solo por su tasa individual.**

## Límites y cuándo no aplica

Medir la correlación exige datos de escapes o una inyección controlada; con pocos defectos, la estimación es ruidosa. Para trabajo de muy bajo riesgo, una sola comprobación basta. La correlación no dice cuál comprobación es mejor, solo cuánto se solapan.
