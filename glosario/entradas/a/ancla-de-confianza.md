# Ancla de confianza

[↑ Glosario](../../README.md) · [← Ancla](./ancla.md) · [Ancla del ciclo →](./ancla-del-ciclo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Certificado o clave aceptado localmente como inicio de validación.

Definición de trabajo de [SE-043 — TLS, certificados y confianza en tránsito](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md).

## Por qué importa

La clase donde se define, [SE-043 — TLS, certificados y confianza en tránsito](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md), existe con este propósito: la clase existe para explicar qué autentica y cifra TLS a partir de handshake, cadena y nombre del servicio.

## Cómo funciona

[SE-043 — TLS, certificados y confianza en tránsito](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Estas definiciones son operativas: precisan el uso dentro de la petición observable de extremo a extremo y deben leerse junto a las fuentes. No convierten un término histórico o dependiente de implementación en una garantía universal.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-043 — TLS, certificados y confianza en tránsito](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md):

La petición observable de extremo a extremo monitorea días hasta expiración y prueba la cadena desde un cliente limpio. La rotación instala certificado e intermedios antes del corte y conserva rollback. Ante un error, el informe distingue reloj incorrecto, nombre distinto, expiración, ancla ausente y cadena incompleta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-043 — TLS, certificados y confianza en tránsito](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md)) son:

- **`unable to get local issuer certificate`** — causa: el almacén del cliente no tiene la raíz o falta una intermedia. Corrección: comprobar el almacén de esa herramienta y la cadena que presenta el servidor.
- **`Hostname mismatch` con cadena válida** — causa: el nombre pedido no figura en la SAN. Corrección: usar el nombre correcto o emitir un certificado que lo incluya.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-043 — TLS, certificados y confianza en tránsito](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md)) son: Estas definiciones son operativas: precisan el uso dentro de la petición observable de extremo a extremo y deben leerse junto a las fuentes. No convierten un término histórico o dependiente de implementación en una garantía universal. No enseña diseño criptográfico ni operación completa de una PKI. La revocación depende del ecosistema y la política. La clase siguiente ubica dónde terminan TLS y HTTP al introducir intermediarios.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-042](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Certificado](../c/certificado.md), [Validación](../v/validacion.md), [Alcance](./alcance.md), [ALPN](./alpn.md), [Diagnóstico](../d/diagnostico.md), [Garantía](../g/garantia.md).
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

[↑ Glosario](../../README.md) · [← Ancla](./ancla.md) · [Ancla del ciclo →](./ancla-del-ciclo.md)
