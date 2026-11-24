# Subtipado conductual

## Definición

El **subtipado conductual** es la relación por la cual una subclase puede sustituir a su base sin romper a los clientes: acepta al menos lo mismo y garantiza al menos lo mismo (SE-159). Es la formalización de Liskov y Wing del principio de sustitución. Se llama conductual porque se refiere al comportamiento prometido, no a la forma de las firmas.

## Por qué importa

La herencia sintáctica no basta. Una subclase puede compilar, heredar todos los métodos y aun así romper llamadas válidas de los clientes de la base. El subtipado conductual da el criterio para decidir si un cambio de contrato es seguro, y por eso también sirve para versionar servicios: es el mismo principio que la compatibilidad hacia atrás.

## Cómo funciona

SE-159 enuncia tres condiciones:

- **Precondición igual o más débil**: la subclase acepta al menos lo mismo que la base.
- **Postcondición igual o más fuerte**: garantiza al menos lo mismo.
- **Invariante preservado**: no rompe lo que la clase base mantiene siempre cierto.

La razón es la perspectiva del cliente. Quien escribió código contra la base confía en dos cosas: que lo que le pasa se acepta (si cumple la precondición) y que lo que recibe cumple la postcondición. Una subclase que **exige más** (precondición más fuerte) rechaza llamadas que el cliente tenía derecho a hacer; una que **promete menos** (postcondición más débil) entrega algo con lo que el cliente no contaba.

La clase da el contraejemplo: una subclase `CalificacionEstricta` que exige `1 ≤ horas ≤ 48` donde la base acepta `0 ≤ horas ≤ 72`. Compila, hereda y rompe llamadas válidas (con 0 horas o con 60). El criterio vale también para versionar servicios: una nueva versión es sustituible por la anterior si acepta más (o igual) y garantiza más (o igual).

Sobre el invariante, SE-159 señala un fallo frecuente: el invariante falla lejos de donde se corrompió el estado porque se comprobó al final o cada muchas operaciones; la corrección es comprobarlo en la frontera de cada operación pública, al menos en pruebas.

## Ejemplo

Base: `calificar(horas)` acepta `0 ≤ horas ≤ 72` y garantiza que la nota queda en `[0, 100]`. Subclase correcta: acepta `0 ≤ horas ≤ 96` (más débil) y garantiza nota en `[0, 100]` con además un mensaje (más fuerte). Subclase incorrecta: acepta `1 ≤ horas ≤ 48` (más fuerte) y puede devolver nota `None` en un caso (postcondición más débil). El código de un cliente que llama con 0 horas fallará con la segunda. (Ejemplo derivado del de SE-159.)

## Errores y confusiones comunes

- **Una subclase rompe a los clientes pese a compilar**: reforzó una precondición o debilitó una postcondición.
- **Creer que si el compilador lo acepta es sustituible.**
- **Invariantes comprobados tarde.**
- **Confundir subtipado con herencia de implementación**: se puede heredar código sin ser subtipo.

## Límites y cuándo no aplica

Solo es verificable si los contratos están escritos; con contratos implícitos, el criterio es una guía de revisión. No resuelve el acoplamiento por herencia ni sustituye otras razones para preferir composición. Para propiedades no funcionales (rendimiento, tiempo) la sustituibilidad también puede romperse sin violar pre y postcondiciones formales.
