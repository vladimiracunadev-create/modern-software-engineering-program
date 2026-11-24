# Tiempo agotado ambiguo

[↑ Glosario](../../README.md) · [← Throughput](./throughput.md) · [Tiempo de ciclo o plazo →](./tiempo-de-ciclo-o-plazo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Un **tiempo agotado ambiguo** es la ausencia de respuesta que no permite saber si la operación se ejecutó ([SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md)). Cuando el cliente espera y no recibe nada, no puede distinguir entre varias historias posibles, y la decisión de qué hacer a continuación se toma a ciegas.

## Por qué importa

Es la raíz de muchos duplicados y de muchas pérdidas en sistemas distribuidos. Reintentar «por si acaso» puede ejecutar dos veces una acción que ya ocurrió; no reintentar puede dejar sin hacer una que nunca llegó. La decisión que cambia es que los reintentos solo se hacen sobre operaciones que lo toleran, y que de las demás se consulta el estado.

## Cómo funciona

[SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md) enumera las tres historias que caben cuando no hay respuesta:

1. La petición se perdió y **no se ejecutó**.
2. Se ejecutó y **la respuesta se perdió**.
3. Se ejecutó y **la respuesta llegará tarde**.

Desde fuera son idénticas. La clase no las distingue, las reparte: con pérdidas simétricas, **más de la mitad** de los tiempos agotados corresponde a una operación ya ejecutada. Por eso reintentar sin precaución es peligroso.

La consecuencia de diseño: reintentar es seguro solo si la operación es **idempotente** o va con una **clave de idempotencia** que permita al servidor reconocer el duplicado ([SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md)). Si no lo es, el cliente debe **consultar el estado** en lugar de repetir. Esto conecta con el detector de fallos, que tiene la misma incertidumbre a nivel de nodo (¿caído o lento?), con el presupuesto de reintentos, que acota el efecto de insistir, y con el timeout, que decide cuánto esperar antes de declarar la ambigüedad.

## Ejemplo

Un cliente envía el cobro de una inscripción y el tiempo se agota. Si reintenta sin clave de idempotencia, puede cobrar dos veces. Con una clave de idempotencia, el servidor reconoce el segundo envío como duplicado y devuelve el resultado del primero. Alternativamente, el cliente consulta si la inscripción ya figura como pagada antes de repetir. Resolución descrita en [SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md).

## Errores y confusiones comunes

- **Registros duplicados tras una lentitud**: reintento de una operación ya ejecutada; se corrige con clave de idempotencia o consulta del estado.
- **El servicio de abajo cae cuando el de arriba se recupera**: reintentos multiplicados por varias capas; se corrige reintentando en una sola capa con presupuesto.
- **Interpretar el timeout como fallo seguro**: solo dice que no hubo respuesta a tiempo.
- **Suponer que «no hubo respuesta» equivale a «no se ejecutó»**.

## Límites y cuándo no aplica

[SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md) indica que no midió ninguna red ni servicio real: las probabilidades, la distribución lognormal y los parámetros de reintentos son construcciones del autor. La cifra de «más de la mitad» depende del supuesto de pérdidas simétricas. En operaciones puramente de lectura, o idempotentes por naturaleza, la ambigüedad no causa daño y reintentar es seguro.

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
