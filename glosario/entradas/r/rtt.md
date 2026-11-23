# RTT

[↑ Glosario](../../README.md) · [← RTO (objetivo de tiempo de recuperación)](./rto-objetivo-de-tiempo-de-recuperacion.md) · [Rúbrica calibrada →](./rubrica-calibrada.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Tiempo de ida y vuelta observado.

Definición de trabajo de [SE-040 — TCP, UDP, QUIC y decisiones de transporte](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-046 — Captura, medición y diagnóstico de tráfico](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md): Tiempo aproximado de ida y vuelta.

## Por qué importa

La clase donde se define, [SE-040 — TCP, UDP, QUIC y decisiones de transporte](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md), existe con este propósito: la clase existe para seleccionar TCP, UDP o QUIC por fiabilidad, orden, latencia y control de congestión.

## Cómo funciona

Según [SE-040 — TCP, UDP, QUIC y decisiones de transporte](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md):

**Cómo leer la figura.** El primer panel contrasta el rechazo inmediato con el silencio: de cada destino salen el resultado de Linux y el de Windows, que se funden en una caja cuando coinciden. El segundo panel muestra el costo de dos escrituras pequeñas sobre una conexión reutilizada. **Dónde deja de valer:** los tiempos son de loopback; con un RTT real de decenas de milisegundos, la espera de 40 ms seguiría presente pero se sumaría a la latencia de red. La solución general es escribir mensajes completos de una sola vez y fijar `TCP_NODELAY` cuando se envían mensajes pequeños y la latencia importa.

Según [SE-046 — Captura, medición y diagnóstico de tráfico](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md):

«Lento» debe traducirse a una variable y una población: p95 del tiempo a primer byte para cierta operación, por ejemplo. Promedio oculta colas largas. Throughput no es ancho de banda teórico, y RTT no es tiempo completo de una transacción.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-040 — TCP, UDP, QUIC y decisiones de transporte](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md):

La petición observable de extremo a extremo usa HTTP sobre transporte confiable para informes y un canal de eventos donde las muestras antiguas pueden descartarse. La ficha de decisión compara orden, pérdida tolerable, movilidad, soporte de proxy, costo operativo y telemetría. QUIC se habilita solo si la ruta y la biblioteca lo soportan; existe fallback medido.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-040 — TCP, UDP, QUIC y decisiones de transporte](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md)) son:

- **Dos escrituras TCP llegan juntas y el receptor falla** — causa: se asumió que TCP conserva fronteras de mensaje. Corrección: definir framing con longitud o delimitador.
- **«El servidor ignoró mi mensaje UDP» sin evidencia** — causa: UDP no confirma entrega. Corrección: añadir confirmación y reintento a nivel de aplicación o usar otro transporte.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** los tiempos son de loopback; con un RTT real de decenas de milisegundos, la espera de 40 ms seguiría presente pero se sumaría a la latencia de red. ([SE-040](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md))
- Throughput no es ancho de banda teórico, y RTT no es tiempo completo de una transacción. ([SE-046](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-039](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcance](../a/alcance.md), [Correlación](../c/correlacion.md), [Datagrama](../d/datagrama.md), [Diagnóstico](../d/diagnostico.md), [Flujo](../f/flujo.md), [Garantía](../g/garantia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-040 — TCP, UDP, QUIC y decisiones de transporte](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.
- [SE-046 — Captura, medición y diagnóstico de tráfico](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 768 — User Datagram Protocol](https://www.rfc-editor.org/rfc/rfc768) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9000 — QUIC](https://www.rfc-editor.org/rfc/rfc9000) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 1122 — Requirements for Internet Hosts: Communication Layers](https://www.rfc-editor.org/rfc/rfc1122) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.

---

[↑ Glosario](../../README.md) · [← RTO (objetivo de tiempo de recuperación)](./rto-objetivo-de-tiempo-de-recuperacion.md) · [Rúbrica calibrada →](./rubrica-calibrada.md)
