# Reintentos

[↑ Glosario](../../README.md) · [← Reidentificación](./reidentificacion.md) · [Relación →](./relacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Los **reintentos** consisten en repetir una llamada fallida con la esperanza de que una falla transitoria no se repita. El programa lo trata en varios contextos: en pruebas ([SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md), flakiness), en códigos de salida y errores ([SE-220](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md)) y en ejecución durable ([SE-596](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md)). La palabra no implica por sí sola ninguna política: cuántas veces, con qué espera y para qué errores son las decisiones que importan.

## Por qué importa

Es la primera defensa contra fallos transitorios, y también una fuente de problemas: reintentar lo permanente gasta recursos y retrasa el aviso ([SE-220](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md)); reintentar sin retroceso aleatorio daña al servicio ([SE-596](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md)); y reintentar una prueba silencia el defecto real intermitente ([SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md)).

## Cómo funciona

[SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md) da los números del costo en pruebas. Para una prueba con 2 % de fallo espurio, un reintento la deja en verde el 99,96 % de las veces: el ruido desaparece. Pero un defecto real que ocurre en el 30 % de las ejecuciones también termina en verde el 91,2 % de las veces con un reintento y el 97,3 % con dos. El reintento no distingue entre los dos. Si se reintenta, se registra cada reintento y se revisa la tasa.

Para llamadas a servicios, la política mínima es:

1. **Reintentar solo errores transitorios** (tiempo agotado, servicio no disponible), no los permanentes (petición inválida, no autorizado).
2. **Limitar intentos** y tiempo total.
3. **Espera creciente con dispersión** (retroceso exponencial con jitter), para no sincronizar a los clientes.
4. **Idempotencia** de lo que se repite, porque un reintento puede duplicar un efecto.

## Ejemplo

El equipo de [SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md) guarda el historial de cada prueba y calcula cada semana la tasa de fallo espurio por prueba y suite. Una prueba con más de 0,1 % de fallo espurio entra en cuarentena: sigue ejecutándose pero no bloquea, con responsable, fecha de revisión a 14 días y criterio de salida de 300 ejecuciones sin fallo tras la corrección. Los reintentos están desactivados para no esconder defectos reales.

## Errores y confusiones comunes

- **Reintentar errores permanentes.**
- **Reintentar sin dispersión,** provocando oleadas sincronizadas.
- **Reintentar operaciones no idempotentes** (cobros, envíos).
- **Usar el reintento de pruebas como solución a la inestabilidad,** en lugar de diagnosticarla.

## Límites y cuándo no aplica

No ayuda cuando la dependencia está caída por un periodo largo: ahí actúa el circuit breaker. Multiplica la carga sobre un servicio ya saturado. Los porcentajes de [SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md) suponen intentos independientes; si la causa es persistente, el reintento no ayuda.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-219](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Backoff exponencial](../b/backoff-exponencial.md), [Circuit breaker](../c/circuit-breaker.md), [Código de salida](../c/codigo-de-salida.md), [Dispersión](../d/dispersion.md), [Estado de una tubería](../e/estado-de-una-tuberia.md), [Fallo permanente](../f/fallo-permanente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-220 — Códigos de salida, errores y diagnóstico](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-320 — Resiliencia: timeout, retry con jitter y circuit breaker](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-430 — Flakiness, diagnóstico y mantenimiento](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (152 clases más lo mencionan; las que más):

[SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md), [SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md), [SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md), [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md), [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-270](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md), [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Reintento».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Luo et al., «An empirical analysis of flaky tests»](https://doi.org/10.1145/2635868.2635920) — causas de las pruebas inestables; autoridad: artículo revisado de FSE 2014.
- [Lam et al., «iDFlakies»](https://doi.org/10.1109/ICST.2019.00038) — detección de pruebas inestables; autoridad: artículo revisado de ICST 2019.
- [Google Testing Blog: Flaky Tests at Google and How We Mitigate Them](https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html) — mitigación en una organización; autoridad: equipo de pruebas de Google.
- [Micco, «The State of Continuous Integration Testing @Google»](https://research.google/pubs/the-state-of-continuous-integration-testing-google/) — integración continua a gran escala; autoridad: Google Research.
- [Martin Fowler, «Eradicating Non-Determinism in Tests»](https://martinfowler.com/articles/nonDeterminism.html) — causas y tratamiento; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Reidentificación](./reidentificacion.md) · [Relación →](./relacion.md)
