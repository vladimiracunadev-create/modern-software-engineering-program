# NXDOMAIN

[↑ Glosario](../../README.md) · [← Número de prioridad de riesgo](./numero-de-prioridad-de-riesgo.md) · [Objetivo de nivel de servicio →](../o/objetivo-de-nivel-de-servicio.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Respuesta que afirma que el nombre consultado no existe.

Definición de trabajo de [SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md).

## Por qué importa

La clase donde se define, [SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md), existe con este propósito: la clase existe para seguir resolución DNS, delegación, caché y TTL para distinguir ausencia, demora y respuesta obsoleta.

## Cómo funciona

Según [SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md):

Una consulta contiene nombre, clase y tipo. A y AAAA asocian direcciones; CNAME redirige un nombre a otro; NS declara servidores de una zona; SOA contiene parámetros de autoridad. Pedir A y recibir solo AAAA no es lo mismo que NXDOMAIN.

Según [SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md):

Añade en un dominio de laboratorio un registro con destino incorrecto y TTL corto, o usa un nombre reservado. Registra respuesta positiva equivocada versus NXDOMAIN. Corrige y espera/explica la expiración sin afirmar que todos los caches ya cambiaron.

## Ejemplo

Ejemplo de [SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md) (sección «Ejemplo mínimo»):

Consulta A, AAAA y un nombre inexistente bajo un dominio que controles o de documentación. Registra código de respuesta, sección de respuesta, autoridad y TTL. Distingue `NOERROR` sin datos de `NXDOMAIN`.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **«DNS falla» ante cualquier error de red** — causa: no se distinguió NXDOMAIN de un resolvedor sin respuesta. Corrección: clasificar el código de error y probar con otro resolvedor. ([SE-041](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Pedir A y recibir solo AAAA no es lo mismo que NXDOMAIN. ([SE-041](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-040](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcance](../a/alcance.md), [Autoritativo](../a/autoritativo.md), [Diagnóstico](../d/diagnostico.md), [Garantía](../g/garantia.md), [Resolver](../r/resolver.md), [Vigencia de la caché](../v/vigencia-de-la-cache.md).
- **Se confunde con:** Pedir A y recibir solo AAAA no es lo mismo que NXDOMAIN.

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-037](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 1034 — Domain Names: Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 1035 — Domain Names: Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 8499 — DNS Terminology](https://www.rfc-editor.org/rfc/rfc8499) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 2308 — Negative Caching of DNS Queries](https://www.rfc-editor.org/rfc/rfc2308) — explica cómo se hacen cacheables las respuestas negativas y cómo expira esa evidencia.
- [RFC 4033 — DNS Security Introduction and Requirements](https://www.rfc-editor.org/rfc/rfc4033) — define objetivos, cadena de confianza y límites de DNSSEC.

---

[↑ Glosario](../../README.md) · [← Número de prioridad de riesgo](./numero-de-prioridad-de-riesgo.md) · [Objetivo de nivel de servicio →](../o/objetivo-de-nivel-de-servicio.md)
