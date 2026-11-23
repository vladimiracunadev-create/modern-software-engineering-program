# Calidad de servicio

[↑ Glosario](../../README.md) · [← Calibración](./calibracion.md) · [Calidad del producto →](./calidad-del-producto.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Garantía de entrega de un mensaje: a lo sumo una vez, al menos una vez o exactamente una vez.

Definición de trabajo de [SE-270 — Protocolos IoT y conectividad intermitente](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md).

## Por qué importa

La clase donde se define, [SE-270 — Protocolos IoT y conectividad intermitente](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md), existe con este propósito: la clase existe para que elijas la garantía de entrega de un mensaje por lo que cuesta en paquetes y por lo que deja sin resolver, dimensiones una cola de almacenar y reenviar por la desconexión más larga que quieres cubrir y evites que miles de dispositivos tumben un servidor al reconectarse a la vez.

## Cómo funciona

[SE-270 — Protocolos IoT y conectividad intermitente](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-270 — Protocolos IoT y conectividad intermitente](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md):

El equipo de la plataforma define una política por tipo de mensaje. Las lecturas por minuto usan nivel 1 con identificador y marca de tiempo (el servidor descarta duplicados), una cola de 120 muestras que descarta lo más viejo y se vacía a 10 por minuto al reconectar. La alarma de CO₂ usa nivel 1 con un envío inmediato y un resumen en el siguiente, y se marca «reenviada» si se retrasa más de cinco minutos. Los comandos hacia el nodo usan nivel 2 o son idempotentes.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-270 — Protocolos IoT y conectividad intermitente](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md)) son:

- **Faltan lecturas tras un corte** — causa: sin cola local o cola pequeña. Corrección: dimensionar la cola por la desconexión más larga y avisar de pérdidas.
- **Alarmas duplicadas** — causa: nivel 1 con consumidor no idempotente. Corrección: identificador de mensaje y descarte de duplicados.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-270 — Protocolos IoT y conectividad intermitente](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md)) son: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún agente MQTT, ningún servidor ni una red real: la pérdida independiente, las desconexiones geométricas y el colapso del servidor por encima de 1,5 veces su capacidad son construcciones del autor. La siguiente clase usa este canal para actualizar el firmware sin dejar el dispositivo inservible.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [A lo sumo una vez](../a/a-lo-sumo-una-vez.md), [Al menos una vez](../a/al-menos-una-vez.md), [Garantías de entrega](../g/garantias-de-entrega.md), [Garantía](../g/garantia.md), [Almacenar y reenviar](../a/almacenar-y-reenviar.md), [Dispersión](../d/dispersion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-270 — Protocolos IoT y conectividad intermitente](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «QoS».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OASIS, MQTT versión 3.1.1](https://docs.oasis-open.org/mqtt/mqtt/v3.1.1/mqtt-v3.1.1.html) — niveles de calidad de servicio; autoridad: OASIS.
- [OASIS, MQTT versión 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html) — expiración de mensajes y sesiones; autoridad: OASIS.
- [Shelby, Hartke y Bormann, RFC 7252: The Constrained Application Protocol (CoAP)](https://www.rfc-editor.org/rfc/rfc7252) — protocolo para nodos limitados con mensajes confirmables; autoridad: IETF.
- [Bormann, Ersue y Keränen, RFC 7228: Terminology for Constrained-Node Networks](https://www.rfc-editor.org/rfc/rfc7228) — características de las redes de nodos limitados; autoridad: IETF.
- [AWS Architecture Blog, «Exponential backoff and jitter»](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/) — comparación de estrategias de reintento; autoridad: Amazon Web Services.

---

[↑ Glosario](../../README.md) · [← Calibración](./calibracion.md) · [Calidad del producto →](./calidad-del-producto.md)
