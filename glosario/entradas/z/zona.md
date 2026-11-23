# Zona

[↑ Glosario](../../README.md) · [← Workspace, mounts y permisos](../w/workspace-mounts-y-permisos.md) · [Zona cruda →](./zona-cruda.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Porción administrada del espacio DNS.

Definición de trabajo de [SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md).

## Por qué importa

La clase donde se define, [SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md), existe con este propósito: la clase existe para seguir resolución DNS, delegación, caché y TTL para distinguir ausencia, demora y respuesta obsoleta.

## Cómo funciona

Según [SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md):

DNS es una base distribuida y jerárquica. La raíz delega zonas; una zona no equivale necesariamente a un dominio visual. Los servidores autoritativos responden por datos de una zona, mientras un resolver recursivo persigue delegaciones y conserva resultados.

Según [SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md):

Significa que el resolvedor consultado afirma que no existe. Puede deberse a un error de escritura, a una zona incompleta o a un resolvedor que filtra nombres. Se contrasta preguntando a otro resolvedor y al servidor autoritativo.

## Ejemplo

Ejemplo de [SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md) (sección «Preguntas frecuentes»):

Significa que el resolvedor consultado afirma que no existe. Puede deberse a un error de escritura, a una zona incompleta o a un resolvedor que filtra nombres. Se contrasta preguntando a otro resolvedor y al servidor autoritativo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md)) son:

- **«DNS falla» ante cualquier error de red** — causa: no se distinguió NXDOMAIN de un resolvedor sin respuesta. Corrección: clasificar el código de error y probar con otro resolvedor.
- **Comparar resultados de dos entornos sin declararlos** — causa: la resolución depende de caché, familia y resolvedor. Corrección: registrar dónde y con qué herramienta se resolvió.

Según [SE-041](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md): La raíz delega zonas; una zona no equivale necesariamente a un dominio visual.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La raíz delega zonas; una zona no equivale necesariamente a un dominio visual. ([SE-041](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-040](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcance](../a/alcance.md), [Autoritativo](../a/autoritativo.md), [Diagnóstico](../d/diagnostico.md), [Garantía](../g/garantia.md), [NXDOMAIN](../n/nxdomain.md), [Resolver](../r/resolver.md).
- **Se confunde con:** La raíz delega zonas; una zona no equivale necesariamente a un dominio visual.

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-041 — DNS, nombres, resolución y fallos](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.

**También se usa en** (87 clases más lo mencionan; las que más):

[SE-297](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md), [SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md), [SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md), [SE-231](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md), [SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md), [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-572](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md), [SE-309](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Slack](../../../casos/exito/slack.md).

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

[↑ Glosario](../../README.md) · [← Workspace, mounts y permisos](../w/workspace-mounts-y-permisos.md) · [Zona cruda →](./zona-cruda.md)
