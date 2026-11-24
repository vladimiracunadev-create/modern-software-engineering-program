# Presupuesto de reintentos

[↑ Glosario](../../README.md) · [← Presupuesto de recursos](./presupuesto-de-recursos.md) · [Presupuesto de rendimiento →](./presupuesto-de-rendimiento.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Un **presupuesto de reintentos** es un límite global a la fracción de peticiones que pueden ser reintentos ([SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md), [SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md), [SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md), [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md)). En lugar de limitar cuántas veces reintenta cada llamada, limita cuánto del tráfico total puede ser reintento, para que insistir no empeore el fallo.

## Por qué importa

Reintentar parece inocuo: si algo falla, se vuelve a intentar. Pero cuando el servicio está en dificultades, cada reintento añade carga justo donde ya sobra, y puede convertir un fallo breve en una caída prolongada. La decisión que cambia es dónde se pone el límite: no solo por llamada, sino sobre el total, de modo que la insistencia sea acotada pase lo que pase.

## Cómo funciona

[SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md) muestra la amenaza con aritmética. Si el cliente web reintenta 3 veces, el servicio de aplicación que lo atiende reintenta 3 veces y el cliente del proveedor reintenta 3 veces, una sola petición del usuario puede producir 3 × 3 × 3 = **27** intentos sobre el proveedor cuando este falla. El efecto es **multiplicativo** porque cada capa reintenta sin saber que las demás también lo hacen.

El presupuesto acota el total: cada capa puede reintentar como máximo una fracción de sus peticiones. En el ejemplo de la clase, el 10 %, de modo que el factor de amplificación de las tres capas es 1,1³ ≈ **1,33**. El valor del presupuesto es una decisión; lo que el cálculo muestra es la forma de la amenaza (multiplicativa) y de su solución: acotar globalmente, no por llamada.

La clase lo combina con otras defensas: **jitter completo** (aleatorizar la espera para que los clientes no reintenten sincronizados), el interruptor (circuit breaker) y una simulación que reproduce la caída y comprueba el pico. [SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md) simula un presupuesto del 10 % por capa con distintas tasas de fallo, para 1 000 clientes que fallaron a la vez, comparando retroceso con y sin jitter. [SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md) y [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md) aplican la misma idea a integración y a calidad: la regla de reintentar en una sola capa, con retroceso, aleatoriedad y presupuesto.

## Ejemplo

Un proveedor falla durante 30 segundos. Sin presupuesto, cada una de las tres capas reintenta tres veces y el proveedor recibe hasta 27 veces el tráfico habitual, lo que impide su recuperación. Con un presupuesto del 10 % por capa, el exceso nunca pasa de un 33 % y el proveedor puede recuperarse. Cálculo de [SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md).

## Errores y confusiones comunes

- **La carga se triplica tras un fallo breve**: reintento inmediato sin límite; se corrige con presupuesto y espera con jitter ([SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md)).
- **Reintentar en todas las capas**: la amplificación se multiplica.
- **Confundirlo con un número máximo de intentos por llamada**: es un límite sobre la fracción global.
- **Reintentar operaciones no idempotentes** sin protección.

## Límites y cuándo no aplica

El valor del 10 % es un ejemplo, no una recomendación general: se decide según el servicio y su tolerancia. El presupuesto limita la amplificación pero no arregla el fallo: sin un interruptor que deje de llamar y sin degradación, las peticiones simplemente fallan. Y los experimentos de las clases son simulaciones con parámetros del autor, no mediciones de sistemas reales.

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
