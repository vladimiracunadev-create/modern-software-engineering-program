# Bulkhead

[↑ Glosario](../../README.md) · [← Builder](./builder.md) · [Burn rate →](./burn-rate.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Reparto de un recurso finito en compartimentos para que el fallo de un uso no consuma el de los demás.

Definición de trabajo de [SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-321 — Resiliencia: bulkhead, sidecar, ambassador y degradación](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md): Aislamiento de recursos por dependencia para contener una falla.

## Por qué importa

En [SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md), el tema «Mamparos» importa porque confina el fallo de una dependencia a su compartimento.

En [SE-321 — Resiliencia: bulkhead, sidecar, ambassador y degradación](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md), el tema «Bulkhead» importa porque contiene el daño a la dependencia afectada

## Cómo funciona

Según [SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md):

El nombre viene de los compartimentos estancos de un barco. Un **mamparo** reparte un recurso finito (hilos, conexiones, memoria) en compartimentos, uno por dependencia o por clase de solicitud, de manera que la lentitud de una no pueda consumirlo todo. Si todas las llamadas comparten un único pool de 20 trabajadores y una de las dependencias tarda un segundo en lugar de 50 ms, sus llamadas ocupan los trabajadores mucho más tiempo y dejan sin ellos a las demás. Con pools separados, la dependencia lenta agota su compartimento y las demás siguen. El mamparo no arregla la dependencia lenta: la confina.

Según [SE-321 — Resiliencia: bulkhead, sidecar, ambassador y degradación](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md):

El nombre viene de los mamparos de un barco: una vía de agua llena un compartimento y no el casco. En software, cada dependencia (o clase de dependencias) tiene su propio grupo de recursos. En la simulación, dos dependencias: A (sana, 40 peticiones por segundo, unos 50 ms por llamada) y B (8 por segundo, se degrada a 3 s entre t = 10 y t = 30 de una ventana de 40 s). Con un **grupo compartido de 10 hilos**, el 30,6 % de las peticiones de A terminan dentro de 0,5 s y el 23,4 % de las de B.

## Ejemplo

Caso medido en la sección «Mamparos» de [SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md):

El nombre viene de los compartimentos estancos de un barco. Un **mamparo** reparte un recurso finito (hilos, conexiones, memoria) en compartimentos, uno por dependencia o por clase de solicitud, de manera que la lentitud de una no pueda consumirlo todo. Si todas las llamadas comparten un único pool de 20 trabajadores y una de las dependencias tarda un segundo en lugar de 50 ms, sus llamadas ocupan los trabajadores mucho más tiempo y dejan sin ellos a las demás. Con pools separados, la dependencia lenta agota su compartimento y las demás siguen.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una dependencia secundaria tumba la función principal** — causa: pool compartido. Corrección: mamparos por dependencia o por criticidad. ([SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un **mamparo** reparte un recurso finito (hilos, conexiones, memoria) en compartimentos, uno por dependencia o por clase de solicitud, de manera que la lentitud de una no pueda consumirlo todo. ([SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), [SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md), [SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Aislamiento](../a/aislamiento.md), [Dependencia](../d/dependencia.md), [Recurso](../r/recurso.md), [Ambassador](../a/ambassador.md), [Circuit breaker](../c/circuit-breaker.md), [Criticidad](../c/criticidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-321 — Resiliencia: bulkhead, sidecar, ambassador y degradación](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-439 — Circuit breakers, bulkheads y degradación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (12 clases más lo mencionan; las que más):

[SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md), [SE-344](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md), [SE-443](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md), [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md), [SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md), [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), [SE-322](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md), [SE-341](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md), [Boeing 737 MAX y MCAS](../../../casos/fallo/boeing-737-max-mcas.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «mamparo».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft Azure Architecture: patrón Bulkhead](https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead) — aislamiento de recursos; autoridad: documentación de Microsoft.
- [Fowler, «CircuitBreaker»](https://martinfowler.com/bliki/CircuitBreaker.html) — interruptor de circuito y sus estados; autoridad: autor del texto.
- [AWS Builders' Library: Using load shedding to avoid overload](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/) — descarte de carga; autoridad: Amazon Web Services.
- [Google SRE: Handling Overload](https://sre.google/sre-book/handling-overload/) — sobrecarga, criticidad y degradación; autoridad: Google, libro de ingeniería de confiabilidad.
- [Microsoft Azure Architecture: patrón Circuit Breaker](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker) — estados y parámetros del interruptor; autoridad: documentación de Microsoft.

---

[↑ Glosario](../../README.md) · [← Builder](./builder.md) · [Burn rate →](./burn-rate.md)
