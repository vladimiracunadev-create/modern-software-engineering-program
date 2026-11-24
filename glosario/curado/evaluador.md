# Evaluador

## Definición

Un **evaluador** es el componente que juzga un resultado y devuelve las fallas concretas (`SE-591`). En el patrón generador-evaluador, un generador produce, el evaluador revisa y devuelve *qué falló*, y el generador corrige.

## Por qué importa

Convierte una puerta de «pasa o no pasa» en un bucle de mejora. Pero un evaluador es una fuente de verdad solo en la medida de su acierto: un resultado general de la clase.

## Cómo funciona

Funciona cuando hay un criterio de evaluación claro y la iteración mejora el resultado. En el experimento de `SE-591`, el aviso tiene cuatro restricciones comprobables y el generador sintético corrige cada falla señalada con probabilidad 0,80 y estropea con 0,03 lo que estaba bien; sin revisión pasan el 35,5 %. El diagnóstico de la clase muestra qué ocurre con un evaluador malo: un modelo juez acepta «URGENTE» si la fecha es correcta y ordena cambios en lo que estaba bien, y el generador oscila (las vueltas por aviso suben de 1,6 a 3,4). El verificador programático detecta el tono en el 100 % de los casos.

## Ejemplo

Para criterios comprobables por código (formato, tono, fecha) conviene un verificador programático; el modelo juez se reserva para lo que el código no decide.

## Errores y confusiones comunes

Usar un juez sin medir su acierto; permitir que el evaluador ordene cambios sobre lo que estaba bien.

## Límites y cuándo no aplica

Sin criterio claro, la iteración no converge. El número de vueltas necesita una condición de parada.
