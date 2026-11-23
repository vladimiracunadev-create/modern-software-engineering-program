# Modelo de fallos

[↑ Glosario](../../README.md) · [← Modelo de estados](./modelo-de-estados.md) · [Modelo de información →](./modelo-de-informacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Declaración de qué tipos de falla pueden tener los nodos (parada, omisión, bizantino).

Definición de trabajo de [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md).

## Por qué importa

En [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md), el tema «Modelos de fallo y de sistema» importa porque decide qué garantías se pueden prometer.

## Cómo funciona

Según [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md):

Un **modelo de fallos** declara qué pueden hacer mal los nodos: *parada* (dejan de funcionar y no vuelven), *parada y recuperación* (vuelven con o sin memoria de lo ocurrido), *omisión* (pierden mensajes), *bizantino* (actúan de forma arbitraria o maliciosa). Un **modelo de sistema** declara el comportamiento del tiempo: *síncrono* (hay cotas conocidas de retardo y de velocidad), *asíncrono* (no hay cotas) o *parcialmente síncrono* (hay cotas, pero no se conocen o solo valen tras un tiempo). Las garantías que se pueden ofrecer dependen del modelo: en el asíncrono, un nodo muy lento no se distingue de uno caído; en el síncrono sí, a cambio de suponer cotas que una red real no garantiza. Los servicios reales operan en el parcialmente síncrono y por eso necesitan tiempos límite.

Según [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md):

El equipo de entregas escribe su modelo de fallos en media página: los servicios pueden pararse y recuperarse, los mensajes pueden perderse o retrasarse, no hay nodos bizantinos y el sistema es parcialmente síncrono con una cota de red razonable pero no garantizada. De ahí salen tres decisiones. El registro de una entrega lleva una clave de idempotencia generada por el cliente (`SE-392`), de modo que reintentar es seguro. Solo reintenta la capa más cercana al usuario, con un máximo de dos reintentos, retroceso exponencial con jitter completo y un presupuesto del 10 % por servicio.

## Ejemplo

Ejemplo de [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md) (sección «Ejemplo profesional»):

El equipo de entregas escribe su modelo de fallos en media página: los servicios pueden pararse y recuperarse, los mensajes pueden perderse o retrasarse, no hay nodos bizantinos y el sistema es parcialmente síncrono con una cota de red razonable pero no garantizada. De ahí salen tres decisiones. El registro de una entrega lleva una clave de idempotencia generada por el cliente (`SE-392`), de modo que reintentar es seguro. Solo reintenta la capa más cercana al usuario, con un máximo de dos reintentos, retroceso exponencial con jitter completo y un presupuesto del 10 % por servicio.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md)) son:

- **Registros duplicados tras una lentitud** — causa: reintento de una operación ya ejecutada. Corrección: clave de idempotencia o consulta del estado.
- **El servicio de abajo cae cuando el de arriba se recupera** — causa: reintentos multiplicados por varias capas. Corrección: reintentar en una sola capa con presupuesto.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Traslada el análisis a otro dominio (por ejemplo, un servicio de pagos de una tienda): cambia las operaciones y conserva el procedimiento de declarar el modelo de fallos, repartir la incertidumbre del tiempo agotado, limitar la amplificación y elegir el límite de un detector con la cola del retardo. ([SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-388](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Omisión](../o/omision.md), [Tipo](../t/tipo.md), [Detector de fallos](../d/detector-de-fallos.md), [Fallo parcial](../f/fallo-parcial.md), [Presupuesto de reintentos](../p/presupuesto-de-reintentos.md), [Tiempo agotado ambiguo](../t/tiempo-agotado-ambiguo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), [SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md), [SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md), [SE-454](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-454-verificacion-y-cobertura-mc-dc-hil-y-sil/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Kleppmann, «Designing Data-Intensive Applications»](https://dataintensive.net/) — modelos de fallo y de sistema; autoridad: autor del libro.
- [Fischer, Lynch y Paterson, «Impossibility of distributed consensus with one faulty process»](https://doi.org/10.1145/3149.214121) — indistinguibilidad de un nodo lento y uno caído; autoridad: artículo original (1985).
- [Chandra y Toueg, «Unreliable failure detectors…»](https://doi.org/10.1145/226643.226647) — detectores de fallos no fiables; autoridad: artículo original (1996).
- [AWS Builders' Library: timeouts, reintentos y retroceso con jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — amplificación y jitter; autoridad: Amazon Web Services.
- [Google SRE: fallos en cascada](https://sre.google/sre-book/addressing-cascading-failures/) — propagación de la sobrecarga; autoridad: Google.

---

[↑ Glosario](../../README.md) · [← Modelo de estados](./modelo-de-estados.md) · [Modelo de información →](./modelo-de-informacion.md)
