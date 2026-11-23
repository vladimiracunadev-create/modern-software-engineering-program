# Cifrado autenticado

[↑ Glosario](../../README.md) · [← Cifra etiquetada](./cifra-etiquetada.md) · [Cifrado de sobre →](./cifrado-de-sobre.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Primitiva que entrega confidencialidad e integridad de un mensaje y de los datos asociados con una sola clave y un nonce único.

Definición de trabajo de [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md).

## Por qué importa

En [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md), el tema «Cifrado autenticado y nonces» importa porque el nonce repetido destruye la confidencialidad sin que haya error visible.

## Cómo funciona

Según [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md):

La **confidencialidad** impide leer; la **integridad** detecta modificaciones; la **autenticidad** vincula el mensaje con quien lo produjo. No son la misma cosa y cifrar no da las otras dos: un texto cifrado sin autenticación se puede alterar a ciegas y muchas veces el cambio se refleja en el texto en claro. Por eso se usa **cifrado autenticado con datos asociados** (AEAD), que entrega confidencialidad e integridad a la vez, y se rechazan los modos sin autenticación. Para firmar enlaces o tokens de recuperación se usa un **código de autenticación de mensaje** (MAC, por ejemplo HMAC) con una clave del servidor; para que un tercero verifique sin poder firmar hace falta una firma de clave pública.

Según [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md):

El equipo define tres usos y su primitiva: adjuntos en reposo con AEAD y clave de datos por archivo envuelta con una clave maestra del servicio de gestión de claves; enlaces de descarga firmados con HMAC-SHA256 con una clave propia de ese propósito, vencimiento incluido en la firma y verificación con `hmac.compare_digest`; tokens de recuperación de cuenta generados con `secrets`, guardados solo como hash y de un solo uso. Para los nonces usa nonces aleatorios de 96 bits y un contador de uso por clave de datos que fuerza una clave nueva antes de 2^32 usos. Cada objeto cifrado guarda el identificador de la clave, de modo que ante una filtración se sabe qué hay que recifrar.

## Ejemplo

Ejemplo de [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md) (sección «Ejemplo profesional»):

El equipo define tres usos y su primitiva: adjuntos en reposo con AEAD y clave de datos por archivo envuelta con una clave maestra del servicio de gestión de claves; enlaces de descarga firmados con HMAC-SHA256 con una clave propia de ese propósito, vencimiento incluido en la firma y verificación con `hmac.compare_digest`; tokens de recuperación de cuenta generados con `secrets`, guardados solo como hash y de un solo uso. Para los nonces usa nonces aleatorios de 96 bits y un contador de uso por clave de datos que fuerza una clave nueva antes de 2^32 usos.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un texto cifrado alterado se descifra** — causa: cifrado sin autenticación. Corrección: AEAD y rechazo ante fallo de la etiqueta. ([SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Por eso se usa **cifrado autenticado con datos asociados** (AEAD), que entrega confidencialidad e integridad a la vez, y se rechazan los modos sin autenticación. ([SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Nonce](../n/nonce.md), [Cifrado de sobre](./cifrado-de-sobre.md), [Código de autenticación de mensaje](./codigo-de-autenticacion-de-mensaje.md), [Comparación de tiempo constante](./comparacion-de-tiempo-constante.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «AEAD».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) — GCM, IV y límite por clave; autoridad: NIST.
- [NIST SP 800-57 Parte 1 Rev. 5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final) — gestión del ciclo de vida de las claves; autoridad: NIST.
- [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) — almacenamiento criptográfico; autoridad: OWASP.
- [Crosby, Wallach y Riedi, 2009](https://doi.org/10.1145/1455526.1455530) — límites de los ataques de tiempo remotos; autoridad: ACM Transactions on Information and System Security.
- [Saltzer y Schroeder, 1975](https://doi.org/10.1109/PROC.1975.9939) — economía de mecanismo y diseño abierto; autoridad: Proceedings of the IEEE.

---

[↑ Glosario](../../README.md) · [← Cifra etiquetada](./cifra-etiquetada.md) · [Cifrado de sobre →](./cifrado-de-sobre.md)
