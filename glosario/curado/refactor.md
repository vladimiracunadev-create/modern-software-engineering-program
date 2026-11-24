# Refactor

## Definición

Un **refactor** es un cambio de estructura que conserva el comportamiento, hecho con todas las pruebas en verde (`SE-542`).

## Por qué importa

La definición contiene su propia señal de alarma: si una prueba falla, el cambio no era un refactor. Esa regla distingue mejorar el diseño de cambiar el comportamiento por accidente, y separa los dos tipos de trabajo en commits y revisiones distintos.

## Cómo funciona

En el ciclo de TDD, el refactor es el tercer paso (rojo, verde, refactor): ocurre solo con las pruebas en verde y se detiene si alguna falla. Es el momento del diseño: nombres, eliminación de duplicación, una función extraída. Las pruebas **protegen** el refactor, pero no lo **guían**: el diseño que sale depende de quien refactoriza.

## Ejemplo

Extraer el cálculo del promedio a una función con nombre propio, renombrar variables y quitar un bloque duplicado, ejecutando la suite después de cada paso pequeño; si un paso la rompe, se revierte.

## Errores y confusiones comunes

Mezclar refactor con cambios de comportamiento en un mismo cambio; refactorizar sin pruebas que fijen el comportamiento; creer que TDD garantiza buen diseño.

## Límites y cuándo no aplica

`SE-542` señala que la afirmación de que TDD «produce mejor diseño» es donde los profesionales discrepan, y que la clase no mide ese efecto. Sin pruebas de caracterización, en código heredado, el refactor se hace después de fijar el comportamiento actual.
