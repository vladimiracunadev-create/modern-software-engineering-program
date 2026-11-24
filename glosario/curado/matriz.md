# Matriz

## Definición

En integración continua, una **matriz** genera un job por cada combinación de valores de varios factores, como sistema operativo, versión del lenguaje y base de datos (`SE-482`).

## Por qué importa

El número de combinaciones es el producto de los niveles: tres sistemas, cuatro versiones y tres bases dan 36 jobs. Cada factor adicional multiplica el costo. La pregunta correcta no es «¿qué combinaciones existen?» sino «¿qué defectos esperamos y de cuántos factores dependen?».

## Cómo funciona

`SE-482` apoya la decisión en evidencia empírica del NIST: la mayoría de los defectos de configuración dependen de pocos factores a la vez, por lo que la **cobertura de parejas** (cada par de valores aparece al menos una vez) reduce muchísimo el número de jobs sin perder casi detección. Se combinan exclusiones con motivo.

## Ejemplo

El equipo de la API de entregas declara su compatibilidad y reemplaza la matriz completa por una de cobertura de parejas, calculando antes el camino crítico de la canalización.

## Errores y confusiones comunes

**La matriz triplica el costo cada trimestre.** Se añaden factores sin retirar ninguno; cobertura de parejas y exclusiones con motivo.

## Límites y cuándo no aplica

En el experimento, los defectos son un nivel por factor elegido al azar, algo mucho más regular que los reales; una interacción que depende de una combinación inusual (una versión con una base en un sistema concretos) la ve solo la matriz completa.
