# Timeout

[↑ Glosario](../../README.md) · [← Time to first success](./time-to-first-success.md) · [Tipo →](./tipo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Tiempo máximo que un cliente espera una respuesta antes de rendirse.

Definición de trabajo de [SE-438 — Timeouts, retries, backoff y jitter](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md): Tiempo máximo que se espera una respuesta.

## Por qué importa

En [SE-438 — Timeouts, retries, backoff y jitter](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md), el tema «Timeouts» importa porque un timeout corto crea carga y uno largo retiene recursos.

## Cómo funciona

Según [SE-438 — Timeouts, retries, backoff y jitter](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md), en la sección «Timeouts»:

Un **timeout** es el tiempo que un cliente espera una respuesta antes de rendirse. No existe un valor correcto en abstracto: depende de la distribución de latencias del servicio. Si es más corto que la cola normal, los clientes se rinden ante respuestas que iban a llegar y el servidor hace el trabajo de todas formas: es trabajo desperdiciado. Si es mucho más largo, los clientes retienen un trabajador, una conexión y memoria mientras esperan una respuesta que quizá no llegue, y una dependencia colgada agota los recursos del llamador. La elección razonable ancla el timeout a un percentil alto de la latencia sana (por ejemplo, un múltiplo del p99,9) y lo ajusta con el plazo total disponible.

## Ejemplo

Ejemplo de [SE-438 — Timeouts, retries, backoff y jitter](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md) (sección «Ejemplo profesional»):

El equipo define la política de la API. La llamada de lectura a la base de datos (consultar una calificación) es idempotente y tiene un timeout de 500 ms; se reintenta una vez, con espera de 100 ms más jitter, solo en el cliente del servicio de lectura. La creación de una entrega lleva una clave de idempotencia generada en el cliente y se reintenta como máximo dos veces con un presupuesto del 10 % por minuto. El plazo total de la solicitud es de 1,5 s y se propaga en una cabecera: cada servicio resta el tiempo consumido y falla sin intentar si queda menos de 100 ms.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se duplican entregas tras un timeout** — causa: reintento de una operación no idempotente. Corrección: clave de idempotencia o no reintentar. ([SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md))
- **Los clientes agotan sus hilos esperando** — causa: timeout demasiado largo. Corrección: anclarlo a la cola sana y al plazo total. ([SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Hay un problema adicional: el timeout del cliente no cancela el trabajo del servidor. ([SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md))
- Traslada el análisis a otra dependencia (por ejemplo, el envío de correos de confirmación): cambia el servicio y conserva el procedimiento de clasificar el fallo, elegir el timeout con la distribución, reintentar en una capa con presupuesto y propagar el plazo. ([SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), [SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Espera](../e/espera.md), [Backoff exponencial](../b/backoff-exponencial.md), [Circuit breaker](../c/circuit-breaker.md), [Dispersión](../d/dispersion.md), [Fallo metaestable](../f/fallo-metaestable.md), [Idempotencia](../i/idempotencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-438 — Timeouts, retries, backoff y jitter](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (48 clases más lo mencionan; las que más):

[SE-040](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md), [SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md), [SE-215](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md), [SE-048](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md), [SE-045](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md), [SE-115](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md), [SE-031](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Shopify](../../../casos/exito/shopify.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Timeouts».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [AWS Builders' Library: Timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — reintentos, espera exponencial y jitter; autoridad: Amazon Web Services.
- [Google SRE: Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) — cascadas y presupuestos de reintentos; autoridad: Google, libro de ingeniería de confiabilidad.
- [Bronson et al., «Metastable failures in distributed systems»](https://doi.org/10.1145/3458336.3465286) — estados de sobrecarga que se sostienen; autoridad: HotOS 2021.
- [Microsoft Azure Architecture: patrón Retry](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry) — reintento y fallos transitorios; autoridad: documentación de Microsoft.
- [Python: heapq](https://docs.python.org/3/library/heapq.html) — cola de eventos del simulador; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Time to first success](./time-to-first-success.md) · [Tipo →](./tipo.md)
