# Criticidad

[↑ Glosario](../../README.md) · [← Criterio delegado](./criterio-delegado.md) · [Cronología y hechos →](./cronologia-y-hechos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Importancia relativa de una solicitud para el negocio, usada para decidir a quién se atiende primero.

Definición de trabajo de [SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md).

## Por qué importa

La clase donde se define, [SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md), existe con este propósito: la clase existe para que decidas cómo se comporta un servicio cuando una de sus dependencias falla o se vuelve lenta y no se recupera pronto: cuándo dejar de llamarla (interruptor de circuito), cómo evitar que arrastre al resto (mamparos) y qué respuesta más barata y menos completa ofrecer mientras tanto (degradación).

## Cómo funciona

Según [SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md):

Cada defensa tiene un precio. El interruptor rechaza solicitudes que quizá habrían funcionado y añade un estado que puede estar mal configurado: un interruptor atascado en abierto convierte una caída corta en una larga. Los mamparos dejan capacidad ociosa y una dimensión equivocada convierte un compartimento pequeño en un cuello de botella permanente. El descarte rechaza personas y exige que la clasificación de criticidad sea correcta. La degradación puede esconder un fallo: un sistema que responde siempre «bien» con datos viejos puede estar roto durante horas sin que nadie lo note, de modo que cada defensa necesita su propia señal observable (cuántas veces se abrió, cuántas respuestas degradadas se sirvieron, cuántos rechazos hubo) y una alerta sobre ella.

Según [SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md):

Traslada el análisis a otro sistema (por ejemplo, una tienda con pasarela de pago y recomendador): cambia las dependencias y la criticidad y conserva el procedimiento de medir el interruptor, separar los recursos, elegir qué se descarta y definir la respuesta degradada. La transferencia está lograda cuando puedes decir qué solicitud se rechaza primero y por qué, no cuando la biblioteca tiene los mismos parámetros.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md):

El equipo hace un mapa de las dependencias de la API de entregas. Para la base de datos (crítica), no hay interruptor con respaldo posible: se reserva un pool propio de trabajadores para entregar tareas y se acota la cola; si la base cae, la API responde con un error claro. Para el servicio de miniaturas (secundario) se pone un interruptor con apertura por cinco fallos seguidos y 10 s abierto, un compartimento de 5 trabajadores y una respuesta degradada (un icono genérico) marcada con una cabecera.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una dependencia secundaria tumba la función principal** — causa: pool compartido. Corrección: mamparos por dependencia o por criticidad. ([SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md))
- **Se rechaza a quien no debía** — causa: criticidad mal clasificada. Corrección: definir la criticidad con negocio y probarla. ([SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** la criticidad es un dato conocido y fiable en el modelo (en la práctica hay que clasificar), el costo de 5 ms de la respuesta degradada es un supuesto y los clientes no reintentan; con reintentos, los rechazados volverían y la carga efectiva sería mayor. ([SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md))
- Traslada el análisis a otro sistema (por ejemplo, una tienda con pasarela de pago y recomendador): cambia las dependencias y la criticidad y conserva el procedimiento de medir el interruptor, separar los recursos, elegir qué se descarta y definir la respuesta degradada. ([SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Bulkhead](../b/bulkhead.md), [Circuit breaker](./circuit-breaker.md), [Degradación elegante](../d/degradacion-elegante.md), [Descarte de carga](../d/descarte-de-carga.md), [Interruptor de circuito](../i/interruptor-de-circuito.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md), [SE-215](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE: Handling Overload](https://sre.google/sre-book/handling-overload/) — sobrecarga, criticidad y degradación; autoridad: Google, libro de ingeniería de confiabilidad.
- [Fowler, «CircuitBreaker»](https://martinfowler.com/bliki/CircuitBreaker.html) — interruptor de circuito y sus estados; autoridad: autor del texto.
- [Microsoft Azure Architecture: patrón Bulkhead](https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead) — aislamiento de recursos; autoridad: documentación de Microsoft.
- [AWS Builders' Library: Using load shedding to avoid overload](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/) — descarte de carga; autoridad: Amazon Web Services.
- [Microsoft Azure Architecture: patrón Circuit Breaker](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker) — estados y parámetros del interruptor; autoridad: documentación de Microsoft.

---

[↑ Glosario](../../README.md) · [← Criterio delegado](./criterio-delegado.md) · [Cronología y hechos →](./cronologia-y-hechos.md)
