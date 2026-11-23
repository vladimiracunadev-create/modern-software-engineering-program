# Semiabierto

[↑ Glosario](../../README.md) · [← Semánticas de entrega](./semanticas-de-entrega.md) · [Semilla →](./semilla.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Estado del interruptor en que pasa una llamada de sondeo.

Definición de trabajo de [SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md).

## Por qué importa

La clase donde se define, [SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md), existe con este propósito: la clase existe para que configures **tres controles de una llamada a una dependencia** (cuánto espera, cuántas veces reintenta, cuándo deja de intentar) sabiendo que cada uno puede ayudar o empeorar un incidente según cómo interactúe con los otros y con las demás capas del sistema.

## Cómo funciona

Según [SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md):

El interruptor tiene tres estados: **cerrado** (las llamadas pasan), **abierto** (se rechazan al instante) y **semiabierto** (se deja pasar una llamada de sondeo). Se abre cuando los fallos consecutivos superan un umbral y se cierra cuando un sondeo tiene éxito. En el experimento, una dependencia está caída entre los 5 y los 12 segundos de una ventana de 20 s, con 100 peticiones por segundo. **Sin** interruptor se hacen 2000 llamadas, todas al servicio, con 1300 éxitos. **Con** interruptor (umbral de 5 fallos, 1 s abierto), se hacen **1307** llamadas, **693** se rechazan al instante y hay **1296** éxitos. El interruptor ahorra 693 llamadas a una dependencia que no podía contestarlas, y a cambio pierde 4 éxitos en la recuperación (las llamadas que habrían salido bien mientras estaba abierto).

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md)) son: La simulación usa un servicio con capacidad fija y una caída total, latencias lognormales elegidas por el autor y un reloj virtual; no se midió una dependencia real ni fallos correlacionados con la carga. El siguiente paso, `SE-321`, pregunta qué ocurre cuando los plazos no bastan y una dependencia lenta agota los recursos que comparte con las sanas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), [SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Sondeo](./sondeo.md), [Backoff exponencial](../b/backoff-exponencial.md), [Circuit breaker](../c/circuit-breaker.md), [Dispersión](../d/dispersion.md), [Presupuesto de reintentos](../p/presupuesto-de-reintentos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Semánticas de entrega](./semanticas-de-entrega.md) · [Semilla →](./semilla.md)
