# Doble de prueba

## Definición

Un **doble de prueba** es un sustituto de un componente real que se usa durante una prueba para hacerla más rápida, aislada o determinista. Es la definición de `SE-166`, `SE-328` y `SE-427`; `SE-263` añade la condición que lo hace legítimo: un adaptador sustituto debe cumplir el mismo contrato que el real. `SE-166` nombra tres variantes habituales: *stub*, *mock* y *fake*.

## Por qué importa

Probar contra un proveedor real puede ser lento, caro o imposible de controlar (una red, un reloj, un cobro). El doble quita esa dependencia y permite repetir la misma condición cuantas veces haga falta. Pero `SE-166` señala el costo oculto: **el doble encarna la creencia del consumidor sobre el proveedor**, y cuando el proveedor cambia, el doble sigue diciendo lo mismo, de modo que las pruebas pasan sobre una realidad que ya no existe.

## Cómo funciona

El doble ocupa el lugar de una dependencia detrás de una interfaz y responde según lo que quien escribe la prueba decidió. `SE-166` nombra tres variantes habituales (*stub*, *mock* y *fake*) y `SE-427` amplía el abanico a bases en memoria, contenedores y máquinas virtuales: lo que se reemplaza en una prueba es una decisión que se paga en **fidelidad**, en **acoplamiento a la implementación** y en **diferencias de entorno** que cambian el resultado. La frase de `SE-427` lo resume: todo doble es una apuesta, porque ahorra tiempo y aislamiento a cambio de dejar de comprobar algo.

La defensa contra la deriva es **verificar el doble contra el proveedor real**, de modo que cada afirmación del doble sea una afirmación comprobada; esa es la idea de fondo de las pruebas de contrato (`SE-166`). `SE-263` lo aplica a un producto con dos plataformas: un contrato de adaptadores impide que los dobles de prueba prometan lo que la plataforma real no cumple.

## Ejemplo

`SE-166` presenta el riesgo desde el consumidor: el doble dice lo que el consumidor cree, y si el proveedor cambia, las pruebas del consumidor siguen pasando sobre una realidad que ya no existe. La corrección que propone la clase es comprobar el doble contra el proveedor real. `SE-263` la aplica con un contrato de adaptadores que obliga al adaptador sustituto y al real a cumplir lo mismo.

## Errores y confusiones comunes

- **Confiar en el doble sin verificarlo.** Cuando el proveedor cambia, el doble sigue diciendo lo mismo (`SE-166`).
- **Ignorar el costo de fidelidad y de acoplamiento.** Cada doble deja de comprobar algo y puede atar la prueba a la implementación (`SE-427`).
- **Tomar un doble por un contrato.** Un doble describe lo que el consumidor espera; el contrato se verifica contra el proveedor (`SE-423`).

## Límites y cuándo no aplica

Un doble no prueba el sistema real: prueba el consumidor frente a una creencia. `SE-166` lo trata como herramienta legítima con un riesgo concreto, y la mitigación (verificarlo contra el proveedor) tiene un costo de mantenimiento. No sustituye a las pruebas de integración con el proveedor real en el nivel donde se necesite comprobar el comportamiento de verdad, ni a la observación en producción.
