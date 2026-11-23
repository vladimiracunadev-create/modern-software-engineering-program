# Criterio de aceptación

## Definición

Un **criterio de aceptación** es una condición concreta, con un resultado observable, que debe cumplirse para que una historia o un entregable se acepte. El sentido central es el de `SE-149` y `SE-188`: condiciones binarias (se cumplen o no) que, si se cumplen, hacen que la historia se considere completa para quien la pidió. Las demás clases lo reutilizan con el mismo núcleo: `SE-480` lo aplica a un release («afirmación sobre el canal con una prueba ejecutable y un resultado esperado»), `SE-554` a la salida de un modelo («condición verificable que la salida debe cumplir para aceptarse») y `SE-514` a un experimento de caos (el número de ensayos y la tolerancia de fallas, escritos antes de ejecutarlo).

## Por qué importa

Convierte la intención en condiciones que otra persona puede evaluar. Según `SE-149`, convierte «hecho» en una condición binaria; según `SE-188`, la intención en condiciones verificables que la usuaria o quien lleva el producto reconoce; según `SE-480`, «funciona» en pruebas con resultado. Sin ellos, la discusión sobre si algo está terminado ocurre al final, cuando es más cara.

## Cómo funciona

Según `SE-149`, un buen criterio es **binario**, **independiente de la implementación** y **comprobable por alguien que no escribió el código**. «La subida es rápida» no cumple; «un PDF de 10 MB se acepta y uno de 10,1 MB se rechaza con el mensaje que indica el límite» sí. `SE-188` pide escribirlos como ejemplos o escenarios en el lenguaje del dominio («cuando la entrega llega a las 24 horas exactas, entonces se cuenta un día de retraso»), con una condición y un resultado observable.

Dos distinciones evitan confusiones. El criterio **no es la prueba**: es la promesa a la que la prueba se refiere (`SE-149`). Y la aceptación **no es lo mismo que el terminado**: lo segundo es calidad técnica; lo primero, el reconocimiento de que resuelve el problema (`SE-188`).

## Ejemplo

En la plataforma de entregas de `SE-149`, el límite de subida se expresa con fronteras: un PDF de 10 MB se acepta y uno de 10,1 MB se rechaza con un mensaje que indica el límite. La clase añade además un registro de mutantes y una suite de pares para comprobar que los criterios detectan cambios, y propone cambiar una sola decisión (por ejemplo, el límite a 25 MB) y revisar qué escenarios deben reescribirse.

## Errores y confusiones comunes

- **Criterios vagos que se discuten al final.** «La pantalla debe ser intuitiva» invita a discutir; corrección (`SE-188`): reescribir como ejemplos con condición y resultado observable.
- **Confundir criterio con prueba.** El criterio es la promesa; la prueba la comprueba (`SE-149`).
- **Confundir aceptación con terminado.** Una historia puede estar técnicamente terminada y no ser aceptada, y viceversa (`SE-188`).

## Límites y cuándo no aplica

Un criterio escrito como ejemplo cubre los casos que se pensaron; `SE-149` usa suites de pares y mutantes porque los ejemplos pueden ser insuficientes. Los criterios deben revisarse cuando cambia la decisión que los motivó: `SE-149` propone justamente cambiar una decisión y comprobar qué escenarios deben reescribirse.
