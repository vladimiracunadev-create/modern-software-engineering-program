# SAN

[↑ Glosario](../../README.md) · [← SameSite](./samesite.md) · [Sandbox →](./sandbox.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Extensión que contiene identidades autorizadas.

Definición de trabajo de [SE-043 — TLS, certificados y confianza en tránsito](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md).

## Por qué importa

La clase donde se define, [SE-043 — TLS, certificados y confianza en tránsito](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md), existe con este propósito: la clase existe para explicar qué autentica y cifra TLS a partir de handshake, cadena y nombre del servicio.

## Cómo funciona

Según [SE-043 — TLS, certificados y confianza en tránsito](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md):

Conectar con `ssl` de Python a `example.com:443` y leer los datos de la sesión muestra qué se negoció y qué se verificó. Resultado observado en Linux: protocolo `TLSv1.3`, cifrado `TLS_AES_256_GCM_SHA384`, handshake de unos 145 ms (un viaje de ida y vuelta), un certificado con `commonName = example.com` y nombres alternativos (`subjectAltName`) `example.com` y `*.example.com`, emitido por «SSL Corporation», válido del 26 de septiembre al 25 de diciembre de 2026 (90 días). Con `openssl s_client` se vio la cadena presentada: la hoja, una CA intermedia («Cloudflare TLS Issuing ECC CA 3»), otra intermedia («SSL.com TLS Transit ECC CA R2») y la raíz «SSL.com TLS ECC Root CA 2022».

## Ejemplo

Ejemplo de [SE-043 — TLS, certificados y confianza en tránsito](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md) (sección «Ejemplo mínimo»):

Inspecciona un sitio público con herramientas del navegador o `openssl s_client` sin copiar identificadores personales. Registra SAN pertinente, emisor, vigencia, cadena y protocolo negociado. Explica cuál dato valida el nombre.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **`Hostname mismatch` con cadena válida** — causa: el nombre pedido no figura en la SAN. Corrección: usar el nombre correcto o emitir un certificado que lo incluya. ([SE-043](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-043 — TLS, certificados y confianza en tránsito](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md)) son: Estas definiciones son operativas: precisan el uso dentro de la petición observable de extremo a extremo y deben leerse junto a las fuentes. No convierten un término histórico o dependiente de implementación en una garantía universal. No enseña diseño criptográfico ni operación completa de una PKI. La revocación depende del ecosistema y la política. La clase siguiente ubica dónde terminan TLS y HTTP al introducir intermediarios.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-042](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Extensión](../e/extension.md), [Alcance](../a/alcance.md), [ALPN](../a/alpn.md), [Ancla de confianza](../a/ancla-de-confianza.md), [Certificado](../c/certificado.md), [Diagnóstico](../d/diagnostico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-043 — TLS, certificados y confianza en tránsito](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 8446 — TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 5280 — Internet X.509 PKI Certificate and CRL Profile](https://www.rfc-editor.org/rfc/rfc5280) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.

---

[↑ Glosario](../../README.md) · [← SameSite](./samesite.md) · [Sandbox →](./sandbox.md)
