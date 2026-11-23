# Fallo parcial

[↑ Glosario](../../README.md) · [← Fallo metaestable](./fallo-metaestable.md) · [Fallo permanente →](./fallo-permanente.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Fallo de una parte de un sistema mientras el resto sigue funcionando.

Definición de trabajo de [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md).

## Por qué importa

La clase donde se define, [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md), existe con este propósito: la clase existe para que dejes de leer un tiempo agotado como un «no funcionó» y aprendas a razonar con la incertidumbre que introduce una red: una operación pudo ejecutarse, perderse o estar en camino, y desde fuera no se distingue.

## Cómo funciona

[SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md):

El equipo de entregas escribe su modelo de fallos en media página: los servicios pueden pararse y recuperarse, los mensajes pueden perderse o retrasarse, no hay nodos bizantinos y el sistema es parcialmente síncrono con una cota de red razonable pero no garantizada. De ahí salen tres decisiones. El registro de una entrega lleva una clave de idempotencia generada por el cliente (`SE-392`), de modo que reintentar es seguro.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md)) son:

- **Registros duplicados tras una lentitud** — causa: reintento de una operación ya ejecutada. Corrección: clave de idempotencia o consulta del estado.
- **El servicio de abajo cae cuando el de arriba se recupera** — causa: reintentos multiplicados por varias capas. Corrección: reintentar en una sola capa con presupuesto.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ninguna red, servicio ni tiempo de respuesta reales: las probabilidades, la distribución lognormal y los parámetros de los reintentos son construcciones del autor, y no se evaluaron detectores adaptativos. La siguiente clase usa estas incertidumbres para preguntar qué garantías se pueden mantener cuando la red se parte.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-388](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Detector de fallos](../d/detector-de-fallos.md), [Modelo de fallos](../m/modelo-de-fallos.md), [Presupuesto de reintentos](../p/presupuesto-de-reintentos.md), [Tiempo agotado ambiguo](../t/tiempo-agotado-ambiguo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md), [SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md), [SE-395](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md), [SE-093](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), [SE-220](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md), [SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md), [SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md).

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

[↑ Glosario](../../README.md) · [← Fallo metaestable](./fallo-metaestable.md) · [Fallo permanente →](./fallo-permanente.md)
