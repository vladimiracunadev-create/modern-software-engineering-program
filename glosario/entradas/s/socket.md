# Socket

[↑ Glosario](../../README.md) · [← Sociotécnico](./sociotecnico.md) · [Software Architect →](./software-architect.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Endpoint de comunicación administrado por el sistema operativo.

Definición de trabajo de [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md).

## Por qué importa

La clase donde se define, [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md), existe con este propósito: la clase existe para modelar conexiones persistentes y tiempo real por estados, framing, heartbeat y backpressure.

## Cómo funciona

Según [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md):

Un socket es una abstracción del sistema operativo asociada a un endpoint. En TCP, escuchar, aceptar, leer, escribir y cerrar cambian estados y consumen descriptores, buffers y memoria. Que el cliente desaparezca no siempre se detecta hasta leer, escribir o vencer un temporizador.

Según [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md):

Una práctica provoca contrapresión de forma segura. Levanta un receptor local que acepte la conexión y *no lea*, y un emisor no bloqueante que envíe bloques de 64 KiB hasta recibir `BlockingIOError`; registra cuántos bytes aceptó el sistema. **Síntoma:** el envío se detiene sin error de red. **Hipótesis:** el receptor es lento o está colgado. **Prueba:** leer del receptor y comprobar que el emisor puede continuar. **Corrección de diseño:** el emisor define un límite de cola, un plazo y una política (descartar muestras antiguas o rechazar), y el receptor consume con un límite de tiempo. Limita el tamaño total enviado para no presionar el equipo, y cierra todos los sockets al terminar.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md):

La petición observable de extremo a extremo usa SSE para estados unidireccionales y entrega `id` por evento. El cliente reanuda con el último ID; el servidor conserva una ventana finita y responde explícitamente cuando el cursor expiró. Métricas separan conexiones abiertas, clientes lentos, bytes pendientes y reconexiones.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Sockets en `CLOSE-WAIT` acumulados** — causa: la aplicación no cierra su lado tras el FIN. Corrección: cerrar en todas las rutas (con administradores de contexto). ([SE-045](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En una prueba, un emisor envió datos a un receptor que *no leía*: pudo escribir 327 680 bytes (320 KiB) en Windows y 2 621 440 bytes (2,5 MiB) en Linux antes de que el envío se bloqueara (con el socket en modo no bloqueante, `send` lanzó `BlockingIOError`). ([SE-045](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-044](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Sistema operativo](./sistema-operativo.md), [Alcance](../a/alcance.md), [Backpressure](../b/backpressure.md), [Cursor](../c/cursor.md), [Diagnóstico](../d/diagnostico.md), [Framing](../f/framing.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-045 — Sockets, conexiones persistentes y tiempo real](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.

**También se usa en** (21 clases más lo mencionan; las que más):

[SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md), [SE-040](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md), [SE-046](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md), [SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md), [SE-279](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md), [SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md), [SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md), [SE-044](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 6455 — The WebSocket Protocol](https://www.rfc-editor.org/rfc/rfc6455) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.

---

[↑ Glosario](../../README.md) · [← Sociotécnico](./sociotecnico.md) · [Software Architect →](./software-architect.md)
