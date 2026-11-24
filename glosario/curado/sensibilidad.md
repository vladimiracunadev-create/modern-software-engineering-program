# Sensibilidad

## Definición

La **sensibilidad** es el cambio del resultado de un modelo al variar un supuesto mientras los demás se mantienen fijos (SE-191, SE-124, SE-281). SE-421 la formula como cuánto cambia un resultado cuando cambian los supuestos que lo producen. En ML y estadística, «sensibilidad» también designa la tasa de verdaderos positivos (otra entrada del glosario); este texto trata el análisis de sensibilidad de modelos y decisiones.

## Por qué importa

Ordena los supuestos por cuánto duele que fallen. Un modelo de plazo, de viabilidad o de decisión descansa en supuestos inciertos; no todos importan igual. La sensibilidad indica cuáles merecen atención, vigilancia o una primera prueba, y cuáles se pueden dejar. SE-255 añade un criterio de robustez: una decisión que cambia con una unidad en una puntuación no es robusta.

## Cómo funciona

El método de **una variable cada vez** (SE-191): se varía un supuesto dentro de un rango razonable, manteniendo los demás, y se compara el cambio del resultado (por ejemplo, el plazo). Se repite para cada supuesto y se ordenan por «oscilación». SE-191 precisa que el resultado **no dice cuál es más probable que falle, sino cuál duele más si falla**. Se vigilan primero los supuestos de **alta sensibilidad y baja credibilidad**: los que mueven mucho y de los que menos se sabe. La vigilancia se concreta en señales con umbral (por ejemplo, «si el rendimiento de las últimas cuatro semanas baja de cierto valor, se revisa el plan»).

En un embudo multiplicativo (SE-124), el resultado es el producto de las tasas de cada paso; se varía cada tasa entre su mínimo y su máximo con las demás en su valor central, y la oscilación indica cuánto cambia el resultado final. El hallazgo habitual es que el supuesto que más mueve el resultado **no es el que el equipo mide por costumbre** (alcance, visitas) sino uno de comportamiento (interés, activación), que solo se aprende con prototipos y conversaciones.

Para decisiones con criterios ponderados (SE-255), la sensibilidad se estudia sorteando pesos y contando con qué frecuencia gana cada opción: si la ganadora cambia con pequeños movimientos de pesos, la decisión no es robusta.

## Ejemplo

Un embudo con cuatro pasos: alcance 50 %–70 %, interés 5 %–15 %, activación 30 %–60 %, pago 10 %–20 %. Con las demás tasas en el centro, el interés mueve el resultado final por un factor de 3 (de 5 % a 15 %); el alcance, por 1,4. El supuesto a probar primero es el interés, no el alcance. (Rangos ilustrativos en la línea de SE-124.)

## Errores y confusiones comunes

- **Medir lo cómodo y no lo sensible.**
- **Variar todos los supuestos a la vez** y no saber cuál mueve el resultado.
- **Confundir sensibilidad con probabilidad de fallo.**
- **Ignorar la interacción entre supuestos**: con una variable cada vez no se ve.

## Límites y cuándo no aplica

El análisis de una variable cada vez no capta interacciones; para eso existe la sensibilidad global (otra entrada). Depende de los rangos elegidos: rangos arbitrarios dan oscilaciones arbitrarias. Con un modelo mal especificado, la sensibilidad se calcula sobre algo que no refleja la realidad.
