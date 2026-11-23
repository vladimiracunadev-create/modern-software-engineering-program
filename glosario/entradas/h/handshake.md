# Handshake

[↑ Glosario](../../README.md) · [← Handoff](./handoff.md) · [Happy path →](./happy-path.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Negociación inicial de parámetros, identidad y claves.

Definición de trabajo de [SE-043 — TLS, certificados y confianza en tránsito](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md).

## Por qué importa

La clase donde se define, [SE-043 — TLS, certificados y confianza en tránsito](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md), existe con este propósito: la clase existe para explicar qué autentica y cifra TLS a partir de handshake, cadena y nombre del servicio.

## Cómo funciona

Según [SE-043 — TLS, certificados y confianza en tránsito](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md):

TLS negocia parámetros, autentica al servidor mediante su certificado y deriva claves efímeras para proteger registros posteriores. La clave privada no viaja. Un handshake exitoso acredita control de una identidad según la política del cliente; no demuestra que la aplicación sea segura o honesta.

Según [SE-043 — TLS, certificados y confianza en tránsito](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md):

*Server Name Indication* es una extensión del handshake en la que el cliente declara el nombre que busca, para que un mismo IP sirva varios certificados. Si el nombre no es uno que el servidor atiende, puede cerrar el handshake con una alerta, como ocurrió en la prueba.

## Ejemplo

Ejemplo de [SE-043 — TLS, certificados y confianza en tránsito](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md) (sección «Preguntas frecuentes»):

*Server Name Indication* es una extensión del handshake en la que el cliente declara el nombre que busca, para que un mismo IP sirva varios certificados. Si el nombre no es uno que el servidor atiende, puede cerrar el handshake con una alerta, como ocurrió en la prueba.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-043 — TLS, certificados y confianza en tránsito](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md)) son:

- **`unable to get local issuer certificate`** — causa: el almacén del cliente no tiene la raíz o falta una intermedia. Corrección: comprobar el almacén de esa herramienta y la cadena que presenta el servidor.
- **`Hostname mismatch` con cadena válida** — causa: el nombre pedido no figura en la SAN. Corrección: usar el nombre correcto o emitir un certificado que lo incluya.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un handshake exitoso acredita control de una identidad según la política del cliente; no demuestra que la aplicación sea segura o honesta. ([SE-043](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-042](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Parámetro](../p/parametro.md), [Alcance](../a/alcance.md), [ALPN](../a/alpn.md), [Ancla de confianza](../a/ancla-de-confianza.md), [Certificado](../c/certificado.md), [Diagnóstico](../d/diagnostico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-043 — TLS, certificados y confianza en tránsito](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.

**También se usa en** (10 clases más lo mencionan; las que más):

[SE-045](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md), [SE-049](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md), [SE-037](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md), [SE-040](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md), [SE-038](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md), [SE-046](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md), [SE-060](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-060-proyecto-especificacion-y-solucion-contrastable/README.md), [SE-069](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 8446 — TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 5280 — Internet X.509 PKI Certificate and CRL Profile](https://www.rfc-editor.org/rfc/rfc5280) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.

---

[↑ Glosario](../../README.md) · [← Handoff](./handoff.md) · [Happy path →](./happy-path.md)
