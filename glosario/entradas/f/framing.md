# Framing

[↑ Glosario](../../README.md) · [← Framework e inversión de control](./framework-e-inversion-de-control.md) · [Frecuencia de despliegue →](./frecuencia-de-despliegue.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Regla para delimitar mensajes sobre un transporte.

Definición de trabajo de [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md).

## Por qué importa

La clase donde se define, [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md), existe con este propósito: la clase existe para modelar conexiones persistentes y tiempo real por estados, framing, heartbeat y backpressure.

## Cómo funciona

Según [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md):

Un socket pasa por crear, conectar o escuchar, intercambiar con *framing*, esperar y cerrar. Cada fase necesita su plazo: una lectura con timeout de 0,1 s contra un servidor lento lanzó `TimeoutError` a los 0,1 s, de modo que la aplicación recupera el control. Cerrar correctamente importa: si un extremo cierra y el otro no, el segundo queda en `CLOSE-WAIT`. Y una conexión inactiva *no detecta* que el otro extremo desapareció sin enviar FIN ni RST (un corte de energía, un cable desconectado): hacen falta *heartbeats* a nivel de aplicación o *keepalives* de TCP con un plazo y una política de reconexión. Los canales de larga vida (SSE, WebSocket) añaden además la necesidad de reanudar desde el último evento recibido.

Según [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md):

Sondeo es simple y escala mal en latencia y carga; SSE es unidireccional del servidor al cliente, sobre HTTP, con reanudación; WebSocket es bidireccional y exige gestionar su propio ciclo de vida y framing. La elección depende de la dirección del flujo, la frecuencia y los intermediarios (algunos proxies cortan conexiones inactivas).

## Ejemplo

Ejemplo de [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md) (sección «Preguntas frecuentes»):

Sondeo es simple y escala mal en latencia y carga; SSE es unidireccional del servidor al cliente, sobre HTTP, con reanudación; WebSocket es bidireccional y exige gestionar su propio ciclo de vida y framing. La elección depende de la dirección del flujo, la frecuencia y los intermediarios (algunos proxies cortan conexiones inactivas).

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Mensajes truncados o pegados** — causa: se asumió que TCP conserva fronteras. Corrección: definir framing con longitud o delimitador. ([SE-045](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md)) son: Estas definiciones son operativas: precisan el uso dentro de la petición observable de extremo a extremo y deben leerse junto a las fuentes. No convierten un término histórico o dependiente de implementación en una garantía universal. Tiempo real aquí significa baja latencia percibida, no garantía hard real-time. Proxies pueden imponer timeouts. La siguiente clase enseña a capturar y medir sin violar privacidad.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-044](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Regla](../r/regla.md), [Sobre](../s/sobre.md), [Alcance](../a/alcance.md), [Backpressure](../b/backpressure.md), [Cursor](../c/cursor.md), [Diagnóstico](../d/diagnostico.md).
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

[↑ Glosario](../../README.md) · [← Framework e inversión de control](./framework-e-inversion-de-control.md) · [Frecuencia de despliegue →](./frecuencia-de-despliegue.md)
