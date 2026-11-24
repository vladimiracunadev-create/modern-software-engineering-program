# Rechazo implícito

[↑ Glosario](../../README.md) · [← Receptor idempotente](./receptor-idempotente.md) · [Recomendación condicionada →](./recomendacion-condicionada.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

El **rechazo implícito** (*implicit rejection*) consiste en devolver un secreto distinto, en lugar de un error, ante un texto cifrado inválido. Es el sentido de [SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md) (criptografía poscuántica y migración), donde se presenta como propiedad de ML-KEM. No es «rechazar sin avisar» en sentido general: es una decisión de diseño criptográfico para que el fallo no sea observable.

## Por qué importa

Evita señales por errores de descifrado. Y cambia cómo se integra la biblioteca: el código no puede apoyarse en «si falla, lo sabré».

## Cómo funciona

[SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md): en ML-KEM, descapsular un texto cifrado alterado no devuelve un error: devuelve otro secreto aparentemente válido. En el laboratorio, un bit cambiado en el primer byte del texto cifrado produjo un secreto distinto del original sin ninguna excepción.

La razón es de seguridad: si el descifrado fallara con un error observable, un atacante podría usar esos fallos como **oráculo** para aprender información sobre la clave privada. El rechazo implícito vuelve inobservable la diferencia entre un texto válido y uno inválido.

La consecuencia para el software: la detección no ocurre en la llamada. Ocurre más adelante, cuando los dos extremos derivan claves distintas y la autenticación del canal falla. Por eso [SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md) recomienda usar siempre los protocolos que autentican el canal y no inventar los propios.

## Ejemplo

Con los datos del laboratorio de [SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md): se cifra, se cambia un bit del texto cifrado y se descapsula. La llamada no lanza excepción y devuelve un secreto de la misma longitud que el original. Quien compare ambos ve que son distintos; quien no compare, nunca se entera, hasta que el mensaje cifrado con esa clave no se descifra o la autenticación falla.

## Errores y confusiones comunes

- **Esperar una excepción** ante un texto cifrado manipulado.
- **Capturar un «fallo de descifrado» para reportar errores detallados:** justamente lo que el diseño evita.
- **Implementar comprobaciones propias** que reintroducen una señal observable.
- **Confundirlo con una vulnerabilidad:** es la defensa, no el defecto.

## Límites y cuándo no aplica

Protege contra una clase de ataques de oráculo sobre el descifrado, no contra manipulaciones que el protocolo no autentica. Depende de que la implementación respete la propiedad (sin diferencias de tiempo observables). Los resultados de la clase son de un laboratorio local, no de una prueba de seguridad de una biblioteca real.

## Relación con otros conceptos

- **Prerrequisito:** [Secreto](../s/secreto.md).
- **Ver también:** [Agilidad criptográfica](../a/agilidad-criptografica.md), [Criptografía poscuántica](../c/criptografia-poscuantica.md), [Desigualdad de Mosca](../d/desigualdad-de-mosca.md), [Híbrido](../h/hibrido.md), [ML-DSA](../m/ml-dsa.md), [ML-KEM](../m/ml-kem.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-285 — Criptografía poscuántica y migración](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Receptor idempotente](./receptor-idempotente.md) · [Recomendación condicionada →](./recomendacion-condicionada.md)
