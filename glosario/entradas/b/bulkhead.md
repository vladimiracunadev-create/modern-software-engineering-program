# Bulkhead

[↑ Glosario](../../README.md) · [← Builder](./builder.md) · [Burn rate →](./burn-rate.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Un **bulkhead** (mamparo) reparte un recurso finito (hilos, conexiones, memoria) en compartimentos, uno por dependencia o por clase de solicitud, para que el fallo o la lentitud de un uso no consuma el recurso de los demás ([SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md)). [SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md) lo presenta como aislamiento de recursos por dependencia para contener una falla. El nombre viene de los compartimentos estancos de un barco.

## Por qué importa

Una dependencia lenta es más peligrosa que una caída: no devuelve error rápido, retiene los hilos. La decisión que cambia es cómo se dimensionan los recursos compartidos: en lugar de un único pool para todo, se decide cuánto del recurso puede perder cada dependencia sin arrastrar a las demás. El mamparo no arregla la dependencia lenta; la **confina**.

## Cómo funciona

El mecanismo, según [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md), es aritmético. Si todas las llamadas comparten un pool de 20 trabajadores y una dependencia pasa de 50 ms a un segundo, sus llamadas ocupan los trabajadores unas veinte veces más tiempo; a la tasa de llegada de ese tráfico, el pool entero termina atendiendo solo a la dependencia lenta y las demás llamadas esperan en cola. Con pools separados, la dependencia lenta agota **su** compartimento; las otras siguen con el suyo. Las llamadas a la lenta fallan o esperan, pero el resto del servicio sigue sirviendo.

[SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md) lo verifica con una simulación: dos dependencias, A sana (40 peticiones por segundo, unos 50 ms) y B que se degrada a 3 s durante 20 s de una ventana de 40 s. Con un grupo compartido de 10 hilos, solo el 30,6 % de las peticiones de A terminan dentro de 0,5 s, aunque A estaba sana; con grupos separados, A queda protegida. Los números son de esa simulación, no una regla general.

## Ejemplo

Un servicio de entregas llama a un sistema de calificaciones (crítico) y a uno de estadísticas (secundario). Con un solo pool, que las estadísticas se pongan lentas deja sin hilos a las calificaciones. Con mamparos por criticidad, las estadísticas tienen, por ejemplo, un pool pequeño; cuando se agota, esa función se degrada y las calificaciones siguen. El tamaño de cada compartimento es una decisión de diseño, no un valor universal.

## Errores y confusiones comunes

- **Una dependencia secundaria tumba la función principal**: es el error de [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md), causado por un pool compartido; se corrige con mamparos por dependencia o por criticidad.
- **Creer que el mamparo cura la lentitud**: solo limita el daño.
- **Confundirlo con el circuit breaker**: el mamparo limita cuánto recurso puede consumir una dependencia; el circuit breaker decide cuándo dejar de llamarla. Se combinan.
- **Compartimentos demasiado pequeños**: una dependencia sana puede quedarse sin capacidad en un pico normal.

## Límites y cuándo no aplica

Repartir un recurso finito lo hace menos eficiente en conjunto: capacidad ociosa en un compartimento no la puede usar otro. Con una sola dependencia, o con recursos holgados respecto al tráfico, no aporta. Y solo protege los recursos que se dividen: si todos los compartimentos comparten, por ejemplo, la misma base de datos, esa base sigue siendo un punto común.

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
