# Presupuesto de reintentos

[↑ Glosario](../../README.md) · [← Presupuesto de recursos](./presupuesto-de-recursos.md) · [Presupuesto de rendimiento →](./presupuesto-de-rendimiento.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Límite global de reintentos como fracción de las peticiones.

Definición de trabajo de [SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md): Límite de la fracción de tráfico que puede ser reintento.
- En [SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md): Límite a la fracción de llamadas que pueden ser reintentos, para que insistir no empeore el fallo.
- En [SE-438 — Timeouts, retries, backoff y jitter](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md): Límite a la fracción de solicitudes que pueden ser reintentos.

## Por qué importa

En [SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md), el tema «Presupuesto de reintentos» importa porque acota la carga extra

## Cómo funciona

Según [SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md):

Si el cliente web reintenta 3 veces, el servicio de aplicación que lo atiende reintenta 3 veces y el cliente del proveedor reintenta 3 veces, una sola petición del usuario puede producir 3 × 3 × 3 = **27** intentos sobre el proveedor cuando este falla. Un **presupuesto de reintentos** acota el total: cada capa puede reintentar como máximo una fracción de sus peticiones (el ejemplo del experimento usa el 10 %), de modo que el factor de amplificación de las tres capas es 1,1³ ≈ **1,33**. El valor del presupuesto es una decisión; lo que el cálculo muestra es la forma de la amenaza (multiplicativa) y de su solución (acotar globalmente, no por llamada).

Según [SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md):

**Corrección.** Se añade jitter completo, se acota con un presupuesto de reintentos, se añade el interruptor y se prueba con una simulación que reproduce la caída y comprueba el pico.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La carga se triplica tras un fallo breve** — causa: reintento inmediato sin límite. Corrección: presupuesto de reintentos y espera con jitter. ([SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Aparte, se simula un presupuesto de reintentos del 10 % por capa con distintas tasas de fallo del servicio y se compara un retroceso sin jitter con uno con jitter completo, para 1 000 clientes que fallaron a la vez. ([SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), [SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Límite](../l/limite.md), [Reintentos](../r/reintentos.md), [Acoplamiento temporal](../a/acoplamiento-temporal.md), [Amplificación de reintentos](../a/amplificacion-de-reintentos.md), [Backlog](../b/backlog.md), [Backoff exponencial](../b/backoff-exponencial.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.
- [SE-389 — Fallos parciales y modelos de red](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.
- [SE-438 — Timeouts, retries, backoff y jitter](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-048](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE: Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) — cascadas y presupuestos de reintentos; autoridad: Google, libro de ingeniería de confiabilidad.
- [Fischer, Lynch y Paterson, «Impossibility of distributed consensus with one faulty process»](https://doi.org/10.1145/3149.214121) — indistinguibilidad de un nodo lento y uno caído; autoridad: artículo original (1985).
- [Chandra y Toueg, «Unreliable failure detectors…»](https://doi.org/10.1145/226643.226647) — detectores de fallos no fiables; autoridad: artículo original (1996).
- [AWS Builders' Library: timeouts, reintentos y retroceso con jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — amplificación y jitter; autoridad: Amazon Web Services.
- [Kleppmann, «Designing Data-Intensive Applications»](https://dataintensive.net/) — modelos de fallo y de sistema; autoridad: autor del libro.

---

[↑ Glosario](../../README.md) · [← Presupuesto de recursos](./presupuesto-de-recursos.md) · [Presupuesto de rendimiento →](./presupuesto-de-rendimiento.md)
