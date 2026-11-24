# Punto de sensibilidad

## Definición

Un **punto de sensibilidad** es un parámetro cuyo cambio pequeño invierte la decisión o cambia mucho una medida (`SE-347`, `SE-337`). En la evaluación de arquitecturas con métodos como ATAM, `SE-335` lo define como un parámetro del que depende de forma notable un atributo de calidad.

## Por qué importa

Una recomendación de arquitectura sale de un modelo con supuestos. Saber **cuáles** de esos supuestos deciden el resultado permite saber dónde conviene invertir en medir y dónde da igual. La decisión que cambia es dónde se pone la atención: en los pocos parámetros que mueven la decisión, no en los muchos que no.

## Cómo funciona

`SE-347` calcula la utilidad de varios candidatos (monolito modular, microservicios, celdas) variando el tamaño de la organización de 2 a 30 equipos. Resultado del modelo de la clase: con cliente dominante, la celda gana en todos los tamaños (su utilidad baja de 0,813 con 2 equipos a 0,696 con 30 y sigue por encima del monolito y de los microservicios). Sin cliente dominante, el monolito modular gana hasta 25 equipos y los microservicios desde 26: la utilidad del monolito cae con la coordinación (0,807 con 2 equipos, 0,668 con 30), mientras la de los microservicios se mantiene en 0,670 porque su coordinación es cero.

El punto de sensibilidad respecto de los equipos es **26**: ahí se invierte la decisión. En `SE-335`, ATAM concluye con tres clases de hallazgo: **riesgos** (decisiones que pueden causar problemas), **puntos de sensibilidad** (parámetros de los que depende mucho un atributo) y **compromisos** (decisiones que mejoran un atributo a costa de otro). Cada hallazgo se apoya en un escenario concreto, lo que lo hace discutible y repetible.

Su utilidad práctica: indica qué dato vale la pena medir con precisión. Si la decisión cambia con 26 equipos, importa saber si la organización está cerca de ese valor.

## Ejemplo

Con el modelo de `SE-347`, una organización con 24 equipos sin cliente dominante elegiría el monolito modular, pero está a dos equipos del punto de inversión. Saber que el punto es 26 le dice que debe vigilar el crecimiento y preparar las fronteras para una separación posterior, no que deba migrar hoy.

## Errores y confusiones comunes

- **Tomar el valor como regla general**: `SE-347` advierte que «separa cuando hay más de unos 25 equipos» sale de ese modelo y no de un estudio.
- **Confundirlo con un riesgo**: el punto de sensibilidad es un parámetro; el riesgo, una decisión que puede causar problemas.
- **Ignorar que cambia al cambiar los supuestos**: es una propiedad del modelo.
- **Buscarlo sin escenarios**: sin un atributo de calidad concreto no hay sensibilidad que medir.

## Límites y cuándo no aplica

La cifra de 26 depende de todos los supuestos del modelo de la clase (pesos, coordinación, utilidades), que son del autor. Cambiar un peso mueve el punto. El análisis de sensibilidad solo cubre los parámetros que el modelo incluye; un factor omitido no aparece. Sirve para decidir dónde mirar, no para sustituir la medición de la organización real.
