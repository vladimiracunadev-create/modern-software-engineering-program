# Detector de fallos

[↑ Glosario](../../README.md) · [← Detección de secretos](./deteccion-de-secretos.md) · [Detector estructural →](./detector-estructural.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Componente que sospecha que un nodo ha fallado según los latidos que recibe, y que puede equivocarse.

Definición de trabajo de [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md).

## Por qué importa

En [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md), el tema «Detectores de fallos» importa porque todo tiempo límite elige entre rapidez y falsas alarmas.

## Cómo funciona

Según [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md), en la sección «Detectores de fallos»:

Un **detector de fallos** decide si un nodo ha fallado a partir de los latidos que recibe. Con un tiempo límite de *T*, el nodo se sospecha si pasa *T* sin latido. Un *T* corto detecta rápido y se equivoca a menudo con nodos sanos pero lentos; un *T* largo casi no se equivoca y tarda en detectar el fallo real. Ningún valor da las dos cosas, y de ahí la formalización de Chandra y Toueg: los detectores son *no fiables* y los algoritmos que los usan deben tolerar sospechas erróneas. El tiempo límite correcto sale de la distribución del retardo de la red (su cola, no su mediana) y del coste de una falsa alarma frente al de una detección tardía.

## Ejemplo

Ejemplo de [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md) (sección «Ejemplo profesional»):

El equipo de entregas escribe su modelo de fallos en media página: los servicios pueden pararse y recuperarse, los mensajes pueden perderse o retrasarse, no hay nodos bizantinos y el sistema es parcialmente síncrono con una cota de red razonable pero no garantizada. De ahí salen tres decisiones. El registro de una entrega lleva una clave de idempotencia generada por el cliente (`SE-392`), de modo que reintentar es seguro. Solo reintenta la capa más cercana al usuario, con un máximo de dos reintentos, retroceso exponencial con jitter completo y un presupuesto del 10 % por servicio.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md)) son:

- **Registros duplicados tras una lentitud** — causa: reintento de una operación ya ejecutada. Corrección: clave de idempotencia o consulta del estado.
- **El servicio de abajo cae cuando el de arriba se recupera** — causa: reintentos multiplicados por varias capas. Corrección: reintentar en una sola capa con presupuesto.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ninguna red, servicio ni tiempo de respuesta reales: las probabilidades, la distribución lognormal y los parámetros de los reintentos son construcciones del autor, y no se evaluaron detectores adaptativos. La siguiente clase usa estas incertidumbres para preguntar qué garantías se pueden mantener cuando la red se parte.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-388](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Fallo parcial](../f/fallo-parcial.md), [Modelo de fallos](../m/modelo-de-fallos.md), [Presupuesto de reintentos](../p/presupuesto-de-reintentos.md), [Tiempo agotado ambiguo](../t/tiempo-agotado-ambiguo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Detectores de fallos».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Chandra y Toueg, «Unreliable failure detectors…»](https://doi.org/10.1145/226643.226647) — detectores de fallos no fiables; autoridad: artículo original (1996).
- [Fischer, Lynch y Paterson, «Impossibility of distributed consensus with one faulty process»](https://doi.org/10.1145/3149.214121) — indistinguibilidad de un nodo lento y uno caído; autoridad: artículo original (1985).
- [AWS Builders' Library: timeouts, reintentos y retroceso con jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — amplificación y jitter; autoridad: Amazon Web Services.
- [Google SRE: fallos en cascada](https://sre.google/sre-book/addressing-cascading-failures/) — propagación de la sobrecarga; autoridad: Google.
- [Kleppmann, «Designing Data-Intensive Applications»](https://dataintensive.net/) — modelos de fallo y de sistema; autoridad: autor del libro.

---

[↑ Glosario](../../README.md) · [← Detección de secretos](./deteccion-de-secretos.md) · [Detector estructural →](./detector-estructural.md)
