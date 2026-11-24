# Detector de fallos

[↑ Glosario](../../README.md) · [← Detección de secretos](./deteccion-de-secretos.md) · [Detector estructural →](./detector-estructural.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Un **detector de fallos** es el componente que sospecha que un nodo ha fallado a partir de los latidos que recibe, y que puede equivocarse ([SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md)). La palabra clave es «sospecha»: en una red asincrónica no hay forma de distinguir un nodo caído de uno lento, así que el detector emite una opinión, no un hecho.

## Por qué importa

Casi todo mecanismo de recuperación (elegir un nuevo líder, reasignar trabajo, conmutar a otra réplica) arranca con la frase «ese nodo ha fallado». Si el detector se equivoca, el sistema reacciona a un fallo que no existe o tarda en reaccionar a uno real. La decisión que cambia es cómo se fija el tiempo límite y qué se exige a los algoritmos que dependen de él: tolerar sospechas erróneas, no confiar en ellas.

## Cómo funciona

El mecanismo de [SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md) es simple. Con un tiempo límite de *T*, un nodo se sospecha si pasa *T* sin recibir latido. Ahí aparece un compromiso inevitable: un *T* corto detecta rápido y se equivoca a menudo con nodos sanos pero lentos; un *T* largo casi no se equivoca y tarda en detectar el fallo real. Ningún valor da las dos cosas.

De ahí la formalización de Chandra y Toueg que cita la clase: los detectores son **no fiables**, y los algoritmos que los usan deben tolerar sospechas erróneas. El tiempo límite adecuado sale de la distribución del retardo de la red (su cola, no su mediana) y del costo de una falsa alarma frente al de una detección tardía. Una falsa alarma puede provocar, por ejemplo, un cambio de líder innecesario; una detección tardía deja al sistema sirviendo con un nodo caído.

La clase ilustra con simulaciones: retardos con distribución lognormal y un detector por latidos, midiendo falsas sospechas y tiempo de detección según *T*. La consecuencia práctica es la misma que en el tiempo agotado ambiguo: sospechar no equivale a saber, y la operación puede haberse ejecutado aunque el nodo parezca caído.

## Ejemplo

Un servicio envía latidos cada segundo. Con *T* = 2 s detecta una caída real en unos 2 s, pero un pico de latencia de la red marca como caído a un nodo sano varias veces al día. Con *T* = 30 s, casi no hay falsas alarmas, pero una caída real tarda medio minuto en notarse. Quien elige *T* decide cuál de los dos costos prefiere. Ilustración basada en la simulación de [SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md).

## Errores y confusiones comunes

- **Registros duplicados tras una lentitud**: se reintenta una operación ya ejecutada; se corrige con clave de idempotencia o consulta del estado.
- **El servicio de abajo cae cuando el de arriba se recupera**: reintentos multiplicados por varias capas; se corrige reintentando en una sola capa con presupuesto.
- **Tratar la sospecha como certeza**: actuar como si el nodo estuviera muerto cuando solo está lento.
- **Fijar *T* con la mediana del retardo**: lo que importa es la cola.

## Límites y cuándo no aplica

[SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md) declara que no se midió ninguna red ni servicio real: las probabilidades, la distribución lognormal y los parámetros de reintentos son construcciones del autor, y no se evaluaron detectores adaptativos. Un detector por latidos con *T* fijo es el caso más simple; los adaptativos ajustan *T* según lo observado, y su análisis queda fuera de la clase. En un sistema de un solo nodo o con conexión fiable y local, el problema desaparece.

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
