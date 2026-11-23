# Autoritativo

[↑ Glosario](../../README.md) · [← Autoridad formal](./autoridad-formal.md) · [Autorización →](./autorizacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Servidor que publica datos de una zona.

Definición de trabajo de [SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md).

## Por qué importa

La clase donde se define, [SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md), existe con este propósito: la clase existe para seguir resolución DNS, delegación, caché y TTL para distinguir ausencia, demora y respuesta obsoleta.

## Cómo funciona

Según [SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md):

DNS es una base distribuida y jerárquica. La raíz delega zonas; una zona no equivale necesariamente a un dominio visual. Los servidores autoritativos responden por datos de una zona, mientras un resolver recursivo persigue delegaciones y conserva resultados.

Según [SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md):

Durante la migración de la petición observable de extremo a extremo, el equipo reduce TTL con antelación, verifica ambos autoritativos y consulta desde resolvers independientes. Conserva tiempo, servidor consultado y respuesta. Un override local se usa solo para aislar DNS; no se publica como solución definitiva.

## Ejemplo

Ejemplo de [SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md) (sección «Ejemplo profesional»):

Durante la migración de la petición observable de extremo a extremo, el equipo reduce TTL con antelación, verifica ambos autoritativos y consulta desde resolvers independientes. Conserva tiempo, servidor consultado y respuesta. Un override local se usa solo para aislar DNS; no se publica como solución definitiva.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md)) son:

- **«DNS falla» ante cualquier error de red** — causa: no se distinguió NXDOMAIN de un resolvedor sin respuesta. Corrección: clasificar el código de error y probar con otro resolvedor.
- **Comparar resultados de dos entornos sin declararlos** — causa: la resolución depende de caché, familia y resolvedor. Corrección: registrar dónde y con qué herramienta se resolvió.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md)) son: Estas definiciones son operativas: precisan el uso dentro de la petición observable de extremo a extremo y deben leerse junto a las fuentes. No convierten un término histórico o dependiente de implementación en una garantía universal. No cubre operación completa de DNSSEC ni registradores. Las herramientas pueden omitir el camino usado por una aplicación. La siguiente clase interpreta la petición HTTP una vez resuelto y conectado el origen.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-040](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Zona](../z/zona.md), [Alcance](./alcance.md), [Diagnóstico](../d/diagnostico.md), [Garantía](../g/garantia.md), [NXDOMAIN](../n/nxdomain.md), [Resolver](../r/resolver.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md).

**Aparece en los casos de estudio:** [Caída global de Meta](../../../casos/fallo/meta-2021.md).

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

[↑ Glosario](../../README.md) · [← Autoridad formal](./autoridad-formal.md) · [Autorización →](./autorizacion.md)
