# Rechazo implícito

## Definición

El **rechazo implícito** (*implicit rejection*) consiste en devolver un secreto distinto, en lugar de un error, ante un texto cifrado inválido. Es el sentido de `SE-285` (criptografía poscuántica y migración), donde se presenta como propiedad de ML-KEM. No es «rechazar sin avisar» en sentido general: es una decisión de diseño criptográfico para que el fallo no sea observable.

## Por qué importa

Evita señales por errores de descifrado. Y cambia cómo se integra la biblioteca: el código no puede apoyarse en «si falla, lo sabré».

## Cómo funciona

`SE-285`: en ML-KEM, descapsular un texto cifrado alterado no devuelve un error: devuelve otro secreto aparentemente válido. En el laboratorio, un bit cambiado en el primer byte del texto cifrado produjo un secreto distinto del original sin ninguna excepción.

La razón es de seguridad: si el descifrado fallara con un error observable, un atacante podría usar esos fallos como **oráculo** para aprender información sobre la clave privada. El rechazo implícito vuelve inobservable la diferencia entre un texto válido y uno inválido.

La consecuencia para el software: la detección no ocurre en la llamada. Ocurre más adelante, cuando los dos extremos derivan claves distintas y la autenticación del canal falla. Por eso `SE-285` recomienda usar siempre los protocolos que autentican el canal y no inventar los propios.

## Ejemplo

Con los datos del laboratorio de `SE-285`: se cifra, se cambia un bit del texto cifrado y se descapsula. La llamada no lanza excepción y devuelve un secreto de la misma longitud que el original. Quien compare ambos ve que son distintos; quien no compare, nunca se entera, hasta que el mensaje cifrado con esa clave no se descifra o la autenticación falla.

## Errores y confusiones comunes

- **Esperar una excepción** ante un texto cifrado manipulado.
- **Capturar un «fallo de descifrado» para reportar errores detallados:** justamente lo que el diseño evita.
- **Implementar comprobaciones propias** que reintroducen una señal observable.
- **Confundirlo con una vulnerabilidad:** es la defensa, no el defecto.

## Límites y cuándo no aplica

Protege contra una clase de ataques de oráculo sobre el descifrado, no contra manipulaciones que el protocolo no autentica. Depende de que la implementación respete la propiedad (sin diferencias de tiempo observables). Los resultados de la clase son de un laboratorio local, no de una prueba de seguridad de una biblioteca real.
