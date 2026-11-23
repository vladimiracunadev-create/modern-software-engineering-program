# Código de autenticación de mensaje

[↑ Glosario](../../README.md) · [← Codificación y acuerdo](./codificacion-y-acuerdo.md) · [Código de conducta →](./codigo-de-conducta.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Etiqueta calculada con una clave secreta que permite verificar la integridad y el origen de un mensaje.

Definición de trabajo de [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-038 — Ethernet, Wi-Fi, direccionamiento y redes locales](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md): Dirección utilizada en un dominio de enlace.

## Por qué importa

La clase donde se define, [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md), existe con este propósito: la clase existe para que uses la criptografía como un contrato con condiciones de uso y no como un adjetivo («está cifrado»).

## Cómo funciona

Según [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md):

La **confidencialidad** impide leer; la **integridad** detecta modificaciones; la **autenticidad** vincula el mensaje con quien lo produjo. No son la misma cosa y cifrar no da las otras dos: un texto cifrado sin autenticación se puede alterar a ciegas y muchas veces el cambio se refleja en el texto en claro. Por eso se usa **cifrado autenticado con datos asociados** (AEAD), que entrega confidencialidad e integridad a la vez, y se rechazan los modos sin autenticación. Para firmar enlaces o tokens de recuperación se usa un **código de autenticación de mensaje** (MAC, por ejemplo HMAC) con una clave del servidor; para que un tercero verifique sin poder firmar hace falta una firma de clave pública.

Según [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md):

HMAC es un MAC; el problema es la clave. La clave de un MAC debe ser aleatoria y secreta, no una contraseña. Si la clave se deriva de una contraseña, se pasa antes por una función de derivación con costo.

## Ejemplo

Ejemplo de [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md) (sección «Preguntas frecuentes»):

HMAC es un MAC; el problema es la clave. La clave de un MAC debe ser aleatoria y secreta, no una contraseña. Si la clave se deriva de una contraseña, se pasa antes por una función de derivación con costo.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md)) son:

- **Un mensaje se lee sin la clave** — causa: nonce repetido con la misma clave. Corrección: nonce aleatorio de 96 bits o contador persistente y una clave nueva antes del límite.
- **Se puede falsificar una firma por red** — causa: comparación con `==`. Corrección: `hmac.compare_digest` y respuesta uniforme.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Para firmar enlaces o tokens de recuperación se usa un **código de autenticación de mensaje** (MAC, por ejemplo HMAC) con una clave del servidor; para que un tercero verifique sin poder firmar hace falta una firma de clave pública. ([SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md))
- La dirección MAC identifica una interfaz en ese alcance, no una identidad global de la persona ni una ruta por Internet. ([SE-038](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-037](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dominio](../d/dominio.md), [Enlace](../e/enlace.md), [Etiqueta](../e/etiqueta.md), [Origen](../o/origen.md), [Alcance](../a/alcance.md), [ARP](../a/arp.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-038 — Ethernet, Wi-Fi, direccionamiento y redes locales](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.
- [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md), [SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md), [SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «MAC».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) — GCM, IV y límite por clave; autoridad: NIST.
- [NIST SP 800-57 Parte 1 Rev. 5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final) — gestión del ciclo de vida de las claves; autoridad: NIST.
- [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) — almacenamiento criptográfico; autoridad: OWASP.
- [Crosby, Wallach y Riedi, 2009](https://doi.org/10.1145/1455526.1455530) — límites de los ataques de tiempo remotos; autoridad: ACM Transactions on Information and System Security.
- [Saltzer y Schroeder, 1975](https://doi.org/10.1109/PROC.1975.9939) — economía de mecanismo y diseño abierto; autoridad: Proceedings of the IEEE.

---

[↑ Glosario](../../README.md) · [← Codificación y acuerdo](./codificacion-y-acuerdo.md) · [Código de conducta →](./codigo-de-conducta.md)
