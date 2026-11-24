# Dispersión

[↑ Glosario](../../README.md) · [← Disparador de revisión](./disparador-de-revision.md) · [Disponibilidad →](./disponibilidad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

En este glosario, **dispersión** es el nombre en español de lo que las clases llaman *jitter*: un componente aleatorio añadido a la espera de un reintento para que los clientes no reintenten sincronizados. Lo usan con el mismo sentido [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md), [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md), [SE-270](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md) y [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md); [SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md) lo desarrolla como «jitter». No debe confundirse con la dispersión estadística (varianza) ni con el *jitter* de variación de latencia en redes de tiempo real.

## Por qué importa

Cuando muchos clientes fallan a la vez y reintentan con la misma regla, vuelven a chocar a la vez: una tormenta de reintentos que impide la recuperación del servicio. Añadir aleatoriedad reparte la carga en el tiempo. Es una de esas decisiones de dos líneas de código que deciden si un servicio se recupera o no.

## Cómo funciona

El experimento de [SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md) simula 1000 clientes cuyo primer intento ocurre en el instante 0 y reintentan hasta 12 veces; el servicio falla hasta 1000 ms y luego acepta 60 peticiones por cada 100 ms:

- **Intervalo fijo de 100 ms:** siguen sincronizados; pico de 1000 peticiones por 100 ms en cada ronda, 11 940 intentos y 880 clientes se rinden.
- **Exponencial sin aleatoriedad:** siguen sincronizados, más espaciados; pico de 1000, 10 320 intentos, último éxito a los 38 300 ms, 520 abandonados.
- **Jitter completo** (espera uniforme entre 0 y el valor exponencial): el pico tras el arranque baja a 537, con 6230 intentos y último éxito a los 7179 ms.

El retroceso exponencial alarga las esperas, pero no las desincroniza; la dispersión sí. Por eso se combinan. La idea es la misma en IoT ([SE-270](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md): varias unidades reconectando tras un corte), en el flujo web resiliente de [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md) y en la idempotencia de reintentos de [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md).

## Ejemplo

Esbozo ilustrativo del jitter completo (no código de la clase):

```python
import random
espera = random.uniform(0, min(tope, base * 2 ** intento))
```

Con 1000 clientes reintentando tras un corte de un segundo, el tráfico deja de llegar como un muro y llega como una rampa.

## Errores y confusiones comunes

- **Retroceso exponencial sin aleatoriedad,** que mantiene a los clientes sincronizados.
- **Reintentar sin tope de intentos,** que prolonga la sobrecarga.
- **Reintentar operaciones no idempotentes:** la dispersión reparte la carga, no evita duplicados; hace falta idempotencia ([SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md)).
- **Confundirlo con un cambio de timeout.**

## Límites y cuándo no aplica

Los números de [SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md) vienen de una simulación con parámetros del autor, no de un servicio real. La dispersión no arregla un servicio que sigue caído; solo evita agravarlo. Con pocos clientes, la sincronización no importa. Y retrasa aleatoriamente una parte de los reintentos, lo que alarga la espera de algunos clientes.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-221](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Corrida](../c/corrida.md), [Desviación](./desviacion.md), [Espera](../e/espera.md), [Drenado](./drenado.md), [Escenario de integración](../e/escenario-de-integracion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-239 — Taller: construir un flujo web resiliente](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.
- [SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-270 — Protocolos IoT y conectividad intermitente](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.
- [SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-438 — Timeouts, retries, backoff y jitter](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.
- [SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.
- [SE-603 — Experimentos y entrenamiento reproducible](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (69 clases más lo mencionan; las que más):

[SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md), [SE-185](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md), [SE-048](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md), [SE-171](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md), [SE-289](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md), [SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-391](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «jitter».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [AWS Builders' Library: timeouts, reintentos y retroceso con dispersión](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — por qué sincronizan los reintentos y cómo repartirlos; autoridad: Amazon Web Services.
- [AWS Architecture Blog, «Exponential backoff and jitter»](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/) — comparación de estrategias de reintento; autoridad: Amazon Web Services.
- [Harel, «Statecharts: a visual formalism for complex systems» (Sci. Comput. Program., 1987)](https://doi.org/10.1016/0167-6423%2887%2990035-9) — estados y transiciones para comportamiento reactivo; autoridad: Science of Computer Programming.
- [W3C WAI: evaluación preliminar de accesibilidad](https://www.w3.org/WAI/test-evaluate/preliminary/) — alcance y límites de las comprobaciones rápidas; autoridad: W3C WAI.
- [W3C: Website Accessibility Conformance Evaluation Methodology (WCAG-EM)](https://www.w3.org/TR/WCAG-EM/) — metodología para evaluar la conformidad de un sitio; autoridad: W3C.

---

[↑ Glosario](../../README.md) · [← Disparador de revisión](./disparador-de-revision.md) · [Disponibilidad →](./disponibilidad.md)
