# Cursor

[↑ Glosario](../../README.md) · [← Cuota](./cuota.md) · [Custodia →](./custodia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Posición reanudable dentro de una secuencia de eventos.

Definición de trabajo de [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md).

## Por qué importa

La clase donde se define, [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md), existe con este propósito: la clase existe para modelar conexiones persistentes y tiempo real por estados, framing, heartbeat y backpressure.

## Cómo funciona

Según [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md):

Si el productor supera al consumidor, una cola infinita solo aplaza el fallo. Se puede bloquear, muestrear, descartar con política o desconectar con cursor. Un ID monotónico o token de reanudación permite solicitar eventos posteriores, pero necesita retención y semántica de duplicados.

Según [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md):

La petición observable de extremo a extremo usa SSE para estados unidireccionales y entrega `id` por evento. El cliente reanuda con el último ID; el servidor conserva una ventana finita y responde explícitamente cuando el cursor expiró. Métricas separan conexiones abiertas, clientes lentos, bytes pendientes y reconexiones.

## Ejemplo

Ejemplo de [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md) (sección «Ejemplo profesional»):

La petición observable de extremo a extremo usa SSE para estados unidireccionales y entrega `id` por evento. El cliente reanuda con el último ID; el servidor conserva una ventana finita y responde explícitamente cuando el cursor expiró. Métricas separan conexiones abiertas, clientes lentos, bytes pendientes y reconexiones.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md)) son:

- **Latencia de ≈40 ms con conexión reutilizada** — causa: dos escrituras pequeñas con Nagle y ACK retrasado. Corrección: escribir el mensaje completo o fijar `TCP_NODELAY`.
- **Memoria creciente en el emisor** — causa: ignora la contrapresión y acumula una cola sin límite. Corrección: limitar la cola y definir política al llenarse.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md)) son: Estas definiciones son operativas: precisan el uso dentro de la petición observable de extremo a extremo y deben leerse junto a las fuentes. No convierten un término histórico o dependiente de implementación en una garantía universal. Tiempo real aquí significa baja latencia percibida, no garantía hard real-time. Proxies pueden imponer timeouts. La siguiente clase enseña a capturar y medir sin violar privacidad.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-044](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento](../e/evento.md), [Secuencia](../s/secuencia.md), [Alcance](../a/alcance.md), [Backpressure](../b/backpressure.md), [Diagnóstico](../d/diagnostico.md), [Framing](../f/framing.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-221](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md), [SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md), [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md), [SE-063](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md).

**Aparece en los casos de estudio:** [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 6455 — The WebSocket Protocol](https://www.rfc-editor.org/rfc/rfc6455) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.

---

[↑ Glosario](../../README.md) · [← Cuota](./cuota.md) · [Custodia →](./custodia.md)
