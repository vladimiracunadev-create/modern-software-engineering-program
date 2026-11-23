# Cifrado de sobre

[↑ Glosario](../../README.md) · [← Cifrado autenticado](./cifrado-autenticado.md) · [Circuit breaker →](./circuit-breaker.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Estructura en la que cada dato se cifra con una clave propia y esa clave se cifra con otra superior, de modo que rotar la superior no obliga a recifrar los datos.

Definición de trabajo de [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md).

## Por qué importa

La clase donde se define, [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md), existe con este propósito: la clase existe para que uses la criptografía como un contrato con condiciones de uso y no como un adjetivo («está cifrado»).

## Cómo funciona

Según [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md):

Las claves tienen un ciclo de vida: generación, activación, uso, rotación, retiro y destrucción (NIST SP 800-57). Dos estructuras reducen el costo de rotar. La **jerarquía de claves** (cifrado de sobre) cifra cada objeto con una clave de datos propia y envuelve las claves de datos con una clave maestra: rotar la maestra obliga a reenvolver las claves de datos (pequeñas), no a recifrar los datos (grandes). La **separación por propósito** usa una clave por función (cifrar adjuntos, firmar enlaces, tokens de recuperación) para que la filtración de una no comprometa las demás. Tras una filtración hay que saber qué datos cifró la clave, de modo que cada objeto cifrado registra el identificador de la clave que lo protegió.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md):

El equipo define tres usos y su primitiva: adjuntos en reposo con AEAD y clave de datos por archivo envuelta con una clave maestra del servicio de gestión de claves; enlaces de descarga firmados con HMAC-SHA256 con una clave propia de ese propósito, vencimiento incluido en la firma y verificación con `hmac.compare_digest`; tokens de recuperación de cuenta generados con `secrets`, guardados solo como hash y de un solo uso.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una clave filtrada obliga a recifrarlo todo** — causa: una sola clave para todo. Corrección: cifrado de sobre y claves por propósito con identificador de clave en cada objeto. ([SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **jerarquía de claves** (cifrado de sobre) cifra cada objeto con una clave de datos propia y envuelve las claves de datos con una clave maestra: rotar la maestra obliga a reenvolver las claves de datos (pequeñas), no a recifrar los datos (grandes). ([SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estructura](../e/estructura.md), [Cifrado autenticado](./cifrado-autenticado.md), [Código de autenticación de mensaje](./codigo-de-autenticacion-de-mensaje.md), [Comparación de tiempo constante](./comparacion-de-tiempo-constante.md), [Nonce](../n/nonce.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

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

[↑ Glosario](../../README.md) · [← Cifrado autenticado](./cifrado-autenticado.md) · [Circuit breaker →](./circuit-breaker.md)
