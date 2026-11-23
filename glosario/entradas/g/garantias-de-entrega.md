# Garantías de entrega

[↑ Glosario](../../README.md) · [← Garantía](./garantia.md) · [Gate →](./gate.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

MQTT define tres niveles. En el nivel 0 el emisor envía una vez y no espera confirmación: lo que se pierde, se pierde. En el nivel 1 el emisor reenvía hasta recibir confirmación: el mensaje llega al menos una vez, y puede llegar varias si se pierde la confirmación. En el nivel 2 un intercambio de cuatro paquetes con identificador evita que el receptor entregue dos veces: exactamente una vez, a costa de más paquetes y de estado en ambos lados.

Explicación de la sección «Garantías de entrega» de [SE-270 — Protocolos IoT y conectividad intermitente](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md).

## Por qué importa

En [SE-270 — Protocolos IoT y conectividad intermitente](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md), el tema «Garantías de entrega» importa porque cada nivel compra una garantía con paquetes y deja un caso residual.

En [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md), el tema «Garantías de entrega» importa porque elegir una garantía es elegir qué patrón se escribe

## Cómo funciona

Según [SE-270 — Protocolos IoT y conectividad intermitente](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md), en la sección «Garantías de entrega»:

MQTT define tres niveles. En el nivel 0 el emisor envía una vez y no espera confirmación: lo que se pierde, se pierde. En el nivel 1 el emisor reenvía hasta recibir confirmación: el mensaje llega al menos una vez, y puede llegar varias si se pierde la confirmación. En el nivel 2 un intercambio de cuatro paquetes con identificador evita que el receptor entregue dos veces: exactamente una vez, a costa de más paquetes y de estado en ambos lados. Ninguno elimina todos los casos: tras agotar los reintentos, el emisor puede no saber si el mensaje llegó.

## Ejemplo

Caso medido en la sección «Garantías de entrega» de [SE-270 — Protocolos IoT y conectividad intermitente](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md):

MQTT define tres niveles. En el nivel 0 el emisor envía una vez y no espera confirmación: lo que se pierde, se pierde. En el nivel 1 el emisor reenvía hasta recibir confirmación: el mensaje llega al menos una vez, y puede llegar varias si se pierde la confirmación. En el nivel 2 un intercambio de cuatro paquetes con identificador evita que el receptor entregue dos veces: exactamente una vez, a costa de más paquetes y de estado en ambos lados. Ninguno elimina todos los casos: tras agotar los reintentos, el emisor puede no saber si el mensaje llegó.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-270 — Protocolos IoT y conectividad intermitente](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md)) son:

- **Faltan lecturas tras un corte** — causa: sin cola local o cola pequeña. Corrección: dimensionar la cola por la desconexión más larga y avisar de pérdidas.
- **Alarmas duplicadas** — causa: nivel 1 con consumidor no idempotente. Corrección: identificador de mensaje y descarte de duplicados.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La garantía de entrega no sustituye al diseño del consumidor: lo complementa. ([SE-270](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Almacenar y reenviar](../a/almacenar-y-reenviar.md), [Calidad de servicio](../c/calidad-de-servicio.md), [Cola de cartas muertas](../c/cola-de-cartas-muertas.md), [Dispersión](../d/dispersion.md), [Entrega al menos una vez](../e/entrega-al-menos-una-vez.md), [Idempotencia](../i/idempotencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-270 — Protocolos IoT y conectividad intermitente](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.
- [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md), [SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md), [SE-318](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md), [SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OASIS, MQTT versión 3.1.1](https://docs.oasis-open.org/mqtt/mqtt/v3.1.1/mqtt-v3.1.1.html) — niveles de calidad de servicio; autoridad: OASIS.
- [OASIS, MQTT versión 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html) — expiración de mensajes y sesiones; autoridad: OASIS.
- [Shelby, Hartke y Bormann, RFC 7252: The Constrained Application Protocol (CoAP)](https://www.rfc-editor.org/rfc/rfc7252) — protocolo para nodos limitados con mensajes confirmables; autoridad: IETF.
- [Bormann, Ersue y Keränen, RFC 7228: Terminology for Constrained-Node Networks](https://www.rfc-editor.org/rfc/rfc7228) — características de las redes de nodos limitados; autoridad: IETF.
- [AWS Architecture Blog, «Exponential backoff and jitter»](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/) — comparación de estrategias de reintento; autoridad: Amazon Web Services.

---

[↑ Glosario](../../README.md) · [← Garantía](./garantia.md) · [Gate →](./gate.md)
