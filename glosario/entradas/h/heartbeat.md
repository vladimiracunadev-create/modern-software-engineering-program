# Heartbeat

[↑ Glosario](../../README.md) · [← Heap y prioridad parcial](./heap-y-prioridad-parcial.md) · [Hecho →](./hecho.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Mensaje periódico para comprobar continuidad.

Definición de trabajo de [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md).

## Por qué importa

La clase donde se define, [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md), existe con este propósito: la clase existe para modelar conexiones persistentes y tiempo real por estados, framing, heartbeat y backpressure.

## Cómo funciona

Según [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md):

Un socket pasa por crear, conectar o escuchar, intercambiar con *framing*, esperar y cerrar. Cada fase necesita su plazo: una lectura con timeout de 0,1 s contra un servidor lento lanzó `TimeoutError` a los 0,1 s, de modo que la aplicación recupera el control. Cerrar correctamente importa: si un extremo cierra y el otro no, el segundo queda en `CLOSE-WAIT`. Y una conexión inactiva *no detecta* que el otro extremo desapareció sin enviar FIN ni RST (un corte de energía, un cable desconectado): hacen falta *heartbeats* a nivel de aplicación o *keepalives* de TCP con un plazo y una política de reconexión. Los canales de larga vida (SSE, WebSocket) añaden además la necesidad de reanudar desde el último evento recibido.

Según [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md):

Una conexión que un extremo considera viva y el otro ya no, porque no hubo FIN ni RST. Se detecta con *heartbeats* y plazos. Sin ellos, la aplicación espera indefinidamente a un interlocutor desaparecido.

## Ejemplo

Ejemplo de [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md) (sección «Preguntas frecuentes»):

Una conexión que un extremo considera viva y el otro ya no, porque no hubo FIN ni RST. Se detecta con *heartbeats* y plazos. Sin ellos, la aplicación espera indefinidamente a un interlocutor desaparecido.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Esperas infinitas por un interlocutor caído** — causa: no hay heartbeat ni plazo. Corrección: añadir heartbeats, keepalives y un timeout por fase. ([SE-045](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Y una conexión inactiva *no detecta* que el otro extremo desapareció sin enviar FIN ni RST (un corte de energía, un cable desconectado): hacen falta *heartbeats* a nivel de aplicación o *keepalives* de TCP con un plazo y una política de reconexión. ([SE-045](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-044](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcance](../a/alcance.md), [Backpressure](../b/backpressure.md), [Cursor](../c/cursor.md), [Diagnóstico](../d/diagnostico.md), [Framing](../f/framing.md), [Garantía](../g/garantia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-040](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 6455 — The WebSocket Protocol](https://www.rfc-editor.org/rfc/rfc6455) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.

---

[↑ Glosario](../../README.md) · [← Heap y prioridad parcial](./heap-y-prioridad-parcial.md) · [Hecho →](./hecho.md)
