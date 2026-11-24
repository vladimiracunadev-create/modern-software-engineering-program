# Contextos

## Definición

En descubrimiento de producto, los **contextos** son el conjunto de condiciones físicas, sociales y técnicas en que ocurre un trabajo y que alteran su probabilidad de éxito (SE-122). No son los «contextos delimitados» del diseño dirigido por el dominio, que son otro concepto; aquí se trata de la situación en que una persona intenta hacer algo.

## Por qué importa

El mismo trabajo se cumple o fracasa según dispositivo, conexión, tiempo, ayuda disponible y consecuencias de equivocarse. Un producto que funciona en el contexto del equipo de desarrollo puede fallar en el de quien lo usa. Cambia cómo se evalúa una mejora: una afirmación de que algo mejoró debe decir para qué contextos.

## Cómo funciona

SE-122 ejemplifica el contexto como lo que **no está en la pantalla**: una conexión que se corta, un teléfono compartido, la ayuda de un familiar, una fecha límite que cae un domingo, un lector de pantalla. Dos personas con el mismo trabajo y contextos distintos pueden necesitar productos distintos. Por eso la descripción de un trabajo se acompaña de una lista corta de contextos que cambian el resultado.

La consecuencia metodológica es la **desagregación**. Si se decide con una métrica agregada, y las composiciones de contextos son distintas en cada opción, la opción «ganadora» puede empeorar la experiencia de un grupo específico. La corrección es desagregar por los contextos declarados y comparar con la misma mezcla (estandarizar) antes de decidir. SE-122 incluye un ejercicio con versión, comando y salida registrados, donde se añade un tercer contexto para comprobar si la inversión se mantiene: depende de cuántos intentos aporta cada plan a cada contexto, no solo de las tasas. Es el mismo mecanismo de la paradoja de Simpson.

Esto afecta también a las personas-ficha: una «persona» de producto no puede ser el promedio de nadie; debe ser un caso concreto con un contexto reconocible, construido a partir de observaciones, y declarada como ilustración, no como estadística. Su función es comunicar un contexto concreto, no representar estadísticamente.

## Ejemplo

Trabajo: «confirmar que mi entrega llegó». Contexto A: escritorio con buena conexión; contexto B: móvil con conexión inestable. Una mejora que acelera la confirmación un 20 % en promedio puede mejorar A un 30 % y empeorar B un 5 %. Con el agregado se declara éxito; desagregado por contexto, se ve el daño a B. (Cifras ilustrativas del razonamiento de SE-122.)

## Errores y confusiones comunes

- **La opción «ganadora» empeora a un grupo**: se decidió con la métrica agregada; corrección: desagregar y estandarizar la mezcla.
- **Describir el trabajo sin contextos.**
- **Persona-ficha como promedio.**
- **Confundir contexto con segmento**: el contexto describe la situación; el segmento, a un grupo de personas.

## Límites y cuándo no aplica

No se pueden enumerar todos los contextos posibles: se eligen los que cambian el resultado según evidencia. Con pocas observaciones, la lista de contextos es hipótesis. Y desagregar demasiado deja grupos tan pequeños que sus cifras no son fiables.
