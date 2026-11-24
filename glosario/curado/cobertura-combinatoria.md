# Cobertura combinatoria

## Definición

La **cobertura combinatoria** (de fuerza *t*) es la propiedad de un conjunto de casos de prueba por la cual cada combinación de *t* valores de factores distintos aparece al menos una vez. Es el sentido de `SE-149`. Con *t* = 2 se habla de cobertura de pares: no se prueban todas las combinaciones de todos los factores, sino todas las de cada par.

## Por qué importa

Cambia cuántas pruebas se escriben cuando intervienen muchos factores (rol, navegador, idioma, conexión, tipo de archivo, tamaño). Según `SE-149`, el producto completo crece de forma multiplicativa y se vuelve impracticable; una suite de pares lo reduce a un orden de magnitud manejable sin renunciar a las interacciones más probables.

## Cómo funciona

Con *t* = 2, el número de casos necesario crece aproximadamente como el producto de los dos dominios más grandes, no de todos. Así, seis factores con varios valores cada uno pasan de miles de combinaciones a algunas decenas. Se construye con un algoritmo de generación; en `SE-149` la suite de pares se obtuvo con un algoritmo voraz propio, que en cada paso elige el caso que cubre más pares aún no cubiertos.

El fundamento empírico es que la evidencia recopilada por NIST sugiere que la mayoría de las fallas dependen de pocos factores. La clase subraya la salvedad: «la mayoría» no es «todas». Una falla que exige tres valores simultáneos puede escapar de una suite de pares, y entonces se sube a *t* = 3 con un costo mayor.

## Ejemplo

En la plataforma de entregas de `SE-149`, el criterio de aceptación de la subida de archivos depende del rol, el tipo de archivo, el tamaño y la conexión. Probar el producto completo no es práctico; una suite de pares garantiza que cada pareja (por ejemplo, «docente» con «archivo grande») se ejerce al menos una vez. La clase la contrasta con un registro de mutantes y fallas sembradas para ver cuáles detecta, y se declara que esos mutantes y notas son supuestos del autor.

## Errores y confusiones comunes

- **Creer que pares detectan todo.** Una falla de tres factores puede escapar.
- **Confundir cobertura combinatoria con cobertura de código.** Una mide combinaciones de entradas; la otra, líneas o ramas ejecutadas.
- **Elegir mal los valores.** Sin fronteras ni clases no válidas, la suite cubre pares de valores felices.
- **Pruebas que pasan y el cliente rechaza la entrega.** El criterio solo cubría ejemplos felices; corrección de `SE-149`: añadir fronteras y clases no válidas.

## Límites y cuándo no aplica

No ayuda con factores que no son discretos o independientes (restricciones entre valores deben declararse, o se generan casos imposibles). Con pocos factores, probar el producto completo es más simple. Y los resultados de `SE-149` vienen de datos sintéticos y de un sistema de juguete: no demuestran eficacia en un sistema real. La técnica reduce número de casos; no dice si cada caso tiene un buen oráculo.
