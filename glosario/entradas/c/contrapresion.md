# Contrapresión

[↑ Glosario](../../README.md) · [← Contrafactual](./contrafactual.md) · [Contrato →](./contrato.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

La **contrapresión** (*backpressure*) es la señal o el mecanismo por el que un consumidor lento limita el ritmo del productor, en lugar de dejar que el exceso se acumule sin límite. Es la definición compartida de [SE-305](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md) (flujos reactivos), [SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md) (una señal que frena al productor cuando el consumidor no da abasto) y [SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md) (un consumidor lento hace esperar o rechazar a un productor en lugar de acumular mensajes sin límite).

## Por qué importa

Si el productor es más rápido que el consumidor, el exceso «tiene que ir a algún lado» ([SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md)). Sin contrapresión va a la memoria y a la latencia: la cola crece hasta agotar la memoria y el sistema parece sano hasta que cae ([SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md)). La contrapresión convierte esa sobrecarga escondida en una decisión explícita: quién espera, quién rechaza o qué se pierde.

## Cómo funciona

Un flujo conecta un productor con un consumidor mediante una cola. Si la cola no tiene límite, el desequilibrio se acumula como memoria y como latencia: los mensajes nuevos esperan detrás de todos los anteriores ([SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md)). Si la cola está **acotada**, el exceso se traslada al productor: o se bloquea al emitir, o recibe un rechazo que puede reintentar, degradar o registrar.

[SE-305](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md) ordena las alternativas en cuatro políticas: **dejar crecer** la cola, **bloquear** al productor, **descartar lo nuevo** o **descartar lo viejo**. Cada una compra algo y cuesta algo; elegir es decidir qué se pierde. Si no se puede frenar al productor (un sensor, una persona), algo debe descartarse. La capacidad de la cola no se «calcula»: se elige a partir de la latencia máxima aceptable (con servicio de un mensaje por turno, una cola de 100 implica hasta 100 turnos de espera) y se complementa con la política ante el llenado ([SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md)).

## Ejemplo

En el experimento de [SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md), un productor rápido envía 5 000 mensajes a un consumidor que duerme 50 µs por mensaje (el sueño real es mayor y depende del sistema). Con una cola ilimitada, la profundidad llegó a unos 5 000, todo el lote esperando; con una cola acotada a 100, llegó a exactamente 100: cuando se llena, el `put` del productor se bloquea hasta que el consumidor libera un hueco. La sobrecarga se convirtió en espera del productor.

## Errores y confusiones comunes

- **Colas sin límite «para no perder nada».** Trasladan el problema a la memoria y a la latencia y fallan de golpe ([SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md), [SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md)).
- **Elegir la capacidad por intuición.** Se elige desde la latencia máxima aceptable, no desde un número redondo ([SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md)).
- **Olvidar la política ante el llenado.** Una cola acotada sin decisión de qué hacer cuando se llena solo cambia dónde falla.

## Límites y cuándo no aplica

La contrapresión solo funciona si el productor puede frenar. Con fuentes que no se pueden detener, como un sensor o un usuario, hay que descartar, y [SE-305](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md) pide decidir explícitamente qué (lo nuevo o lo viejo). Las cifras de [SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md) provienen de un experimento local con duraciones de sueño que dependen del sistema: muestran el mecanismo, no tiempos transferibles. Y bloquear al productor traslada la espera hacia atrás en la cadena: es una decisión de diseño, no una solución gratuita.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Límite](../l/limite.md), [Mecanismo](../m/mecanismo.md), [Señal](../s/senal.md), [Cola de rechazos](./cola-de-rechazos.md), [Condición de carrera](./condicion-de-carrera.md), [Filtro](../f/filtro.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-305 — Patrones funcionales, reactivos y concurrentes](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-045](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md), [SE-080](../../../classes/part-06-paradigmas-de-programacion/se-080-programacion-reactiva-y-flujos/README.md), [SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md), [SE-081](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Reactive Streams](https://www.reactive-streams.org/) — flujo asincrónico con contrapresión; autoridad: la iniciativa Reactive Streams.
- [Hughes, «Why Functional Programming Matters» (The Computer Journal, 1989)](https://doi.org/10.1093/comjnl/32.2.98) — modularidad con funciones sin efectos; autoridad: The Computer Journal.
- [Lee, «The Problem with Threads» (IEEE Computer, 2006)](https://doi.org/10.1109/MC.2006.180) — hilos y no determinismo; autoridad: IEEE Computer.
- [The Reactive Manifesto](https://www.reactivemanifesto.org/) — sistemas reactivos y paso de mensajes; autoridad: sus autores.
- [Little, «A Proof for the Queuing Formula: L = λW» (Operations Research, 1961)](https://doi.org/10.1287/opre.9.3.383) — relación entre cola, llegada y espera; autoridad: Operations Research.

---

[↑ Glosario](../../README.md) · [← Contrafactual](./contrafactual.md) · [Contrato →](./contrato.md)
