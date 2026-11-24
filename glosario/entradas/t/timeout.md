# Timeout

[↑ Glosario](../../README.md) · [← Time to first success](./time-to-first-success.md) · [Tipo →](./tipo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Un **timeout** (tiempo límite) es el tiempo máximo que un cliente espera una respuesta antes de rendirse ([SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md), [SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md)). Todo llamado por red debería tener uno: sin él, una dependencia colgada puede retener recursos del llamador indefinidamente.

## Por qué importa

El timeout decide cuánto trabajo desperdicia el sistema y cuánto tarda en liberarse ante un fallo. La decisión que cambia es que el valor no se copia de un ejemplo ni se deja por defecto: se deriva de la distribución de latencias del servicio y del plazo total disponible.

## Cómo funciona

[SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md) señala que no existe un valor correcto en abstracto. Hay dos fallos opuestos:

- **Demasiado corto** (por debajo de la cola normal de la latencia): los clientes se rinden ante respuestas que iban a llegar y el servidor hace el trabajo de todas formas. Es trabajo desperdiciado y, si además se reintenta, carga extra.
- **Demasiado largo**: los clientes retienen un trabajador, una conexión y memoria mientras esperan una respuesta que quizá no llegue; una dependencia colgada agota los recursos del llamador.

La elección razonable ancla el timeout a un **percentil alto de la latencia sana** (por ejemplo, un múltiplo del p99,9) y lo ajusta con el **plazo total** disponible: si el usuario espera como máximo dos segundos de punta a punta, la suma de los timeouts en cadena no puede superar ese plazo; por eso se propaga el plazo y no solo se fija un valor local.

La clase añade un problema adicional: el timeout del cliente **no cancela el trabajo del servidor**; el servidor puede seguir ejecutando. Eso lo une al tiempo agotado ambiguo y obliga a que los reintentos sean idempotentes. Se combina con el presupuesto de reintentos, el interruptor y la espera con retroceso.

## Ejemplo

El servicio de correos de confirmación responde normalmente en 80 ms y su p99,9 sano es de 400 ms. Se fija un timeout de 1 s, ajustado al plazo total de la petición. Si el correo se retrasa, el cliente se rinde y degrada («te enviaremos la confirmación»), sin retener un hilo durante 30 s. Ejercicio de transferencia de [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md).

## Errores y confusiones comunes

- **Se duplican entregas tras un timeout**: reintento de una operación no idempotente; se corrige con clave de idempotencia o no reintentando.
- **Los clientes agotan sus hilos esperando**: timeout demasiado largo; se ancla a la cola sana y al plazo total.
- **Un mismo valor para todas las dependencias**.
- **Creer que el timeout cancela el trabajo remoto**.

## Límites y cuándo no aplica

Un timeout no distingue lentitud de caída: solo declara que el tiempo pasó. Para operaciones de duración legítimamente larga (informes, cargas) un timeout corto de petición no corresponde y se usa un patrón asíncrono con consulta de estado. Y los números de las clases son de ejemplos con datos sintéticos, no valores recomendados.

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
