# Almacenar y reenviar

[↑ Glosario](../../README.md) · [← Almacenamiento temporal](./almacenamiento-temporal.md) · [ALPN →](./alpn.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Política por la que un dispositivo guarda datos localmente mientras no hay red y los envía al reconectar.

Definición de trabajo de [SE-270 — Protocolos IoT y conectividad intermitente](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md).

## Por qué importa

En [SE-270 — Protocolos IoT y conectividad intermitente](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md), el tema «Almacenar y reenviar» importa porque la capacidad de la cola decide cuántos datos se pierden y cuánto tardan.

## Cómo funciona

Según [SE-270 — Protocolos IoT y conectividad intermitente](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md), en la sección «Almacenar y reenviar»:

Mientras no hay red, el dispositivo guarda los datos en una cola local de capacidad fija; al reconectar, los envía a una velocidad limitada. La capacidad se elige por la desconexión más larga que se quiere cubrir (con una muestra por minuto, 60 muestras cubren una hora). Más capacidad pierde menos datos y los entrega más viejos. La política al llenarse (descartar lo más viejo, lo más nuevo o promediar) se decide por el valor de un dato antiguo: para una alarma de CO₂ un dato de hace una hora vale poco; para un historial de consumo vale lo mismo que uno reciente.

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
- **Ver también:** [Dispositivo](../d/dispositivo.md), [Guarda](../g/guarda.md), [Calidad de servicio](../c/calidad-de-servicio.md), [Dispersión](../d/dispersion.md), [Idempotencia](../i/idempotencia.md), [Retroceso exponencial](../r/retroceso-exponencial.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-270 — Protocolos IoT y conectividad intermitente](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md).

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

[↑ Glosario](../../README.md) · [← Almacenamiento temporal](./almacenamiento-temporal.md) · [ALPN →](./alpn.md)
