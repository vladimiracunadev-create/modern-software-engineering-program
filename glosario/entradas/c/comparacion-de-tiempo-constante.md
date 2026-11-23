# Comparación de tiempo constante

[↑ Glosario](../../README.md) · [← Comparabilidad y reporte](./comparabilidad-y-reporte.md) · [Comparación diferencial →](./comparacion-diferencial.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md)

## Definición

Comparación cuyo tiempo no depende de en qué posición difieren los valores comparados.

Definición de trabajo de [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md).

## Por qué importa

La clase donde se define, [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md), existe con este propósito: la clase existe para que uses la criptografía como un contrato con condiciones de uso y no como un adjetivo («está cifrado»).

## Cómo funciona

Según [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md):

Verificar una etiqueta es comparar la calculada con la recibida. Una comparación que se detiene en el primer byte distinto tarda más cuanto más largo es el prefijo correcto, y esa diferencia de tiempo es una señal: el atacante prueba 256 valores para el primer byte, se queda con el más lento, repite con el segundo, y reconstruye la etiqueta en una cantidad lineal de consultas en vez de exponencial. En una red real el ruido oculta una parte de la señal, y Crosby y sus colegas midieron qué diferencias son distinguibles; con muchas repeticiones se promedian.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md):

El equipo define tres usos y su primitiva: adjuntos en reposo con AEAD y clave de datos por archivo envuelta con una clave maestra del servicio de gestión de claves; enlaces de descarga firmados con HMAC-SHA256 con una clave propia de ese propósito, vencimiento incluido en la firma y verificación con `hmac.compare_digest`; tokens de recuperación de cuenta generados con `secrets`, guardados solo como hash y de un solo uso.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md)) son:

- **Un mensaje se lee sin la clave** — causa: nonce repetido con la misma clave. Corrección: nonce aleatorio de 96 bits o contador persistente y una clave nueva antes del límite.
- **Se puede falsificar una firma por red** — causa: comparación con `==`. Corrección: `hmac.compare_digest` y respuesta uniforme.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Por eso se usa una **comparación de tiempo constante** (`hmac.compare_digest`) que examina todos los bytes sin importar dónde está la primera diferencia, y se evita que otra parte del código (un registro, una rama temprana) reintroduzca la señal. ([SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Valor](../v/valor.md), [Cifrado autenticado](./cifrado-autenticado.md), [Cifrado de sobre](./cifrado-de-sobre.md), [Código de autenticación de mensaje](./codigo-de-autenticacion-de-mensaje.md), [Nonce](../n/nonce.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-461 — Criptografía aplicada y gestión de claves](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md).

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

[↑ Glosario](../../README.md) · [← Comparabilidad y reporte](./comparabilidad-y-reporte.md) · [Comparación diferencial →](./comparacion-diferencial.md)
