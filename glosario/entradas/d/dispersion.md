# Dispersión

[↑ Glosario](../../README.md) · [← Disparador de revisión](./disparador-de-revision.md) · [Disponibilidad →](./disponibilidad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Componente aleatorio de la espera que desincroniza a los clientes.

Definición de trabajo de [SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-239 — Taller: construir un flujo web resiliente](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md): Componente aleatorio añadido a una espera para que los clientes no reintenten sincronizados.
- En [SE-270 — Protocolos IoT y conectividad intermitente](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md): Variación aleatoria añadida al intervalo de reintento para evitar que varios clientes coincidan.
- En [SE-438 — Timeouts, retries, backoff y jitter](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md): Variación aleatoria del tiempo de espera entre reintentos para evitar la sincronización.
- En [SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md): Aleatoriedad añadida a la espera entre reintentos para evitar que los clientes se sincronicen.

## Por qué importa

En [SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md), el tema «Jitter» importa porque reparte los reintentos en el tiempo

## Cómo funciona

Según [SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md):

El experimento simula 1000 clientes cuyo primer intento ocurre en el instante 0 y que reintentan hasta 12 veces; el servicio falla hasta 1000 ms y luego acepta 60 peticiones por cada 100 ms. Con **intervalo fijo de 100 ms**, los 1000 clientes siguen sincronizados: el pico es de **1000 peticiones por 100 ms** en cada ronda, se hacen 11.940 intentos y **880 clientes se rinden** tras 12 intentos. Con **exponencial sin aleatoriedad**, siguen sincronizados pero cada vez más espaciados: pico de **1000**, 10.320 intentos, último éxito a los **38.300 ms** y 520 abandonados. Con **jitter completo** (espera uniforme entre 0 y el valor exponencial), el pico tras el arranque baja a **537**, se hacen 6230 intentos, el último éxito llega a los 7179 ms y **nadie** se rinde.

Según [SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md):

El equipo de *Avisos* mide durante una semana la latencia del proveedor: p50 de 60 ms, p99 de 410 ms. Fija un timeout por intento de 500 ms (cerca del p99,5, corta menos de una llamada sana en doscientas), un plazo total de 1,5 s (menos que el de la petición del usuario), dos reintentos con jitter completo y un presupuesto del 10 % por instancia, y un interruptor que se abre con cinco fallos consecutivos durante 10 s. Documenta la pila (plazo total, interruptor, reintento, plazo por intento) y la prueba que simula un proveedor lento y comprueba que la duración máxima de una petición no supera 1,5 s. Registra tres métricas con alarma: tasa de timeouts, tasa de reintentos y estado del interruptor.

## Ejemplo

Ejemplo de [SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* mide durante una semana la latencia del proveedor: p50 de 60 ms, p99 de 410 ms. Fija un timeout por intento de 500 ms (cerca del p99,5, corta menos de una llamada sana en doscientas), un plazo total de 1,5 s (menos que el de la petición del usuario), dos reintentos con jitter completo y un presupuesto del 10 % por instancia, y un interruptor que se abre con cinco fallos consecutivos durante 10 s. Documenta la pila (plazo total, interruptor, reintento, plazo por intento) y la prueba que simula un proveedor lento y comprueba que la duración máxima de una petición no supera 1,5 s.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Mil clientes agotan al servidor al recuperarse** — causa: reintentos sincronizados sin dispersión. Corrección: retroceso exponencial con dispersión, máximo de intentos y límite de tasa. ([SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md))
- **El servidor cae al volver la red** — causa: reintentos sincronizados. Corrección: espera exponencial con jitter completo y retardo inicial aleatorio. ([SE-270](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md))
- **La carga se triplica tras un fallo breve** — causa: reintento inmediato sin límite. Corrección: presupuesto de reintentos y espera con jitter. ([SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Mira cómo el jitter baja el pico a 537 y 759 y elimina los abandonos, mientras el intervalo fijo y el exponencial sin jitter dejan el pico en 1 000. ([SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md))
- Depende del contexto; en la comparación del experimento, el jitter completo da el menor pico y el equilibrado termina antes. ([SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md))

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
