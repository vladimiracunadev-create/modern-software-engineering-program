# Tiempo agotado ambiguo

[↑ Glosario](../../README.md) · [← Throughput](./throughput.md) · [Tiempo de ciclo o plazo →](./tiempo-de-ciclo-o-plazo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Ausencia de respuesta que no permite saber si la operación se ejecutó.

Definición de trabajo de [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md).

## Por qué importa

En [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md), el tema «Tiempo agotado ambiguo» importa porque hace imposible saber si la operación ocurrió.

## Cómo funciona

Según [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md), en la sección «Tiempo agotado ambiguo»:

Cuando el cliente no recibe respuesta caben tres historias: la petición se perdió y no se ejecutó; se ejecutó y la respuesta se perdió; o se ejecutó y la respuesta llegará tarde. Desde fuera son idénticas. Lo que sí se puede es repartir la incertidumbre: con pérdidas simétricas, más de la mitad de los tiempos agotados corresponde a una operación ya ejecutada. La consecuencia es de diseño: reintentar solo es seguro si la operación es idempotente o va con una clave que permita al servidor reconocer el duplicado (`SE-392`), y si no lo es, el cliente debe consultar el estado en lugar de repetir.

## Ejemplo

Caso medido en la sección «Tiempo agotado ambiguo» de [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md):

Cuando el cliente no recibe respuesta caben tres historias: la petición se perdió y no se ejecutó; se ejecutó y la respuesta se perdió; o se ejecutó y la respuesta llegará tarde. Desde fuera son idénticas. Lo que sí se puede es repartir la incertidumbre: con pérdidas simétricas, más de la mitad de los tiempos agotados corresponde a una operación ya ejecutada.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md)) son:

- **Registros duplicados tras una lentitud** — causa: reintento de una operación ya ejecutada. Corrección: clave de idempotencia o consulta del estado.
- **El servicio de abajo cae cuando el de arriba se recupera** — causa: reintentos multiplicados por varias capas. Corrección: reintentar en una sola capa con presupuesto.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ninguna red, servicio ni tiempo de respuesta reales: las probabilidades, la distribución lognormal y los parámetros de los reintentos son construcciones del autor, y no se evaluaron detectores adaptativos. La siguiente clase usa estas incertidumbres para preguntar qué garantías se pueden mantener cuando la red se parte.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-388](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Operación](../o/operacion.md), [Detector de fallos](../d/detector-de-fallos.md), [Fallo parcial](../f/fallo-parcial.md), [Modelo de fallos](../m/modelo-de-fallos.md), [Presupuesto de reintentos](../p/presupuesto-de-reintentos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-395](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fischer, Lynch y Paterson, «Impossibility of distributed consensus with one faulty process»](https://doi.org/10.1145/3149.214121) — indistinguibilidad de un nodo lento y uno caído; autoridad: artículo original (1985).
- [Chandra y Toueg, «Unreliable failure detectors…»](https://doi.org/10.1145/226643.226647) — detectores de fallos no fiables; autoridad: artículo original (1996).
- [AWS Builders' Library: timeouts, reintentos y retroceso con jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — amplificación y jitter; autoridad: Amazon Web Services.
- [Google SRE: fallos en cascada](https://sre.google/sre-book/addressing-cascading-failures/) — propagación de la sobrecarga; autoridad: Google.
- [Kleppmann, «Designing Data-Intensive Applications»](https://dataintensive.net/) — modelos de fallo y de sistema; autoridad: autor del libro.

---

[↑ Glosario](../../README.md) · [← Throughput](./throughput.md) · [Tiempo de ciclo o plazo →](./tiempo-de-ciclo-o-plazo.md)
