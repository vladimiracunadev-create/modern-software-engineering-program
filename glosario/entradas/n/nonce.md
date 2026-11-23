# Nonce

[↑ Glosario](../../README.md) · [← Nombre accesible](./nombre-accesible.md) · [Normalización →](./normalizacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Valor que no debe repetirse con la misma clave; no es secreto.

Definición de trabajo de [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md).

## Por qué importa

En [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md), el tema «Cifrado autenticado y nonces» importa porque el nonce repetido destruye la confidencialidad sin que haya error visible.

## Cómo funciona

Según [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md):

Un cifrado de flujo (y los modos de contador, entre ellos GCM) produce una secuencia pseudoaleatoria a partir de la clave y un **nonce** (número usado una vez) y la combina por XOR con el mensaje. Si dos mensajes usan la misma clave y el mismo nonce, comparten la secuencia, y el XOR de los dos textos cifrados es el XOR de los dos textos en claro: quien conoce uno recupera el otro entero, y quien conoce una parte común (una plantilla, una cabecera, un formato) recupera esa parte del otro. No hay mensaje de error: todo funciona. El nonce debe ser **único por clave**, no secreto.

Según [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md):

Reproduce el fallo clásico de la clase: **un nonce repetido que no produce ningún error**. Reinicia el contador de nonces a cero, cifra dos comentarios y calcula el XOR de los textos cifrados.

## Ejemplo

Ejemplo de [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md) (sección «Ejemplo mínimo»):

Imprime `b'nota: 70/70 '`: el segundo mensaje, sin usar la clave. Registra versión de Python, comando y salida; después cambia el nonce de `m2` y comprueba que la salida deja de ser legible.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un mensaje se lee sin la clave** — causa: nonce repetido con la misma clave. Corrección: nonce aleatorio de 96 bits o contador persistente y una clave nueva antes del límite. ([SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Si dos mensajes usan la misma clave y el mismo nonce, comparten la secuencia, y el XOR de los dos textos cifrados es el XOR de los dos textos en claro: quien conoce uno recupera el otro entero, y quien conoce una parte común (una plantilla, una cabecera, un formato) recupera esa parte del otro. ([SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md))
- **un nonce repetido que no produce ningún error**. ([SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Secreto](../s/secreto.md), [Valor](../v/valor.md), [Cifrado autenticado](../c/cifrado-autenticado.md), [Cifrado de sobre](../c/cifrado-de-sobre.md), [Código de autenticación de mensaje](../c/codigo-de-autenticacion-de-mensaje.md), [Comparación de tiempo constante](../c/comparacion-de-tiempo-constante.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md), [SE-236](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) — GCM, IV y límite por clave; autoridad: NIST.
- [NIST SP 800-57 Parte 1 Rev. 5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final) — gestión del ciclo de vida de las claves; autoridad: NIST.
- [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) — almacenamiento criptográfico; autoridad: OWASP.
- [Crosby, Wallach y Riedi, 2009](https://doi.org/10.1145/1455526.1455530) — límites de los ataques de tiempo remotos; autoridad: ACM Transactions on Information and System Security.
- [Saltzer y Schroeder, 1975](https://doi.org/10.1109/PROC.1975.9939) — economía de mecanismo y diseño abierto; autoridad: Proceedings of the IEEE.

---

[↑ Glosario](../../README.md) · [← Nombre accesible](./nombre-accesible.md) · [Normalización →](./normalizacion.md)
