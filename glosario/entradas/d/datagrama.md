# Datagrama

[↑ Glosario](../../README.md) · [← Database Reliability Engineer](./database-reliability-engineer.md) · [Dato personal →](./dato-personal.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Mensaje independiente transportado como unidad.

Definición de trabajo de [SE-040 — TCP, UDP, QUIC y decisiones de transporte](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md).

## Por qué importa

La clase donde se define, [SE-040 — TCP, UDP, QUIC y decisiones de transporte](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md), existe con este propósito: la clase existe para seleccionar TCP, UDP o QUIC por fiabilidad, orden, latencia y control de congestión.

## Cómo funciona

Según [SE-040 — TCP, UDP, QUIC y decisiones de transporte](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md):

UDP preserva fronteras de datagrama y aporta comprobación mínima, pero no promete entrega, orden, unicidad ni control de congestión para la aplicación. Esa falta de garantías puede ser adecuada cuando importa la actualidad y perder una muestra es mejor que acumular retraso.

## Ejemplo

Ejemplo de [SE-040 — TCP, UDP, QUIC y decisiones de transporte](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md) (sección «Ejemplo mínimo»):

Envía dos mensajes por un socket TCP local y demuestra que el receptor necesita longitud o delimitador. Repite conceptualmente con UDP y explica qué cambia si el segundo datagrama se pierde.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-040 — TCP, UDP, QUIC y decisiones de transporte](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md)) son:

- **Dos escrituras TCP llegan juntas y el receptor falla** — causa: se asumió que TCP conserva fronteras de mensaje. Corrección: definir framing con longitud o delimitador.
- **«El servidor ignoró mi mensaje UDP» sin evidencia** — causa: UDP no confirma entrega. Corrección: añadir confirmación y reintento a nivel de aplicación o usar otro transporte.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- UDP preserva fronteras de datagrama y aporta comprobación mínima, pero no promete entrega, orden, unicidad ni control de congestión para la aplicación. ([SE-040](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-039](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcance](../a/alcance.md), [Diagnóstico](./diagnostico.md), [Flujo](../f/flujo.md), [Garantía](../g/garantia.md), [Idempotencia](../i/idempotencia.md), [RTT](../r/rtt.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-040 — TCP, UDP, QUIC y decisiones de transporte](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-037](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 768 — User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9000 — QUIC](https://www.rfc-editor.org/rfc/rfc9000) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.

---

[↑ Glosario](../../README.md) · [← Database Reliability Engineer](./database-reliability-engineer.md) · [Dato personal →](./dato-personal.md)
