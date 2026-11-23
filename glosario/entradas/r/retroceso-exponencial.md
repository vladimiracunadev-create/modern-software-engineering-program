# Retroceso exponencial

[↑ Glosario](../../README.md) · [← Retroceso catastrófico](./retroceso-catastrofico.md) · [Retrospectiva →](./retrospectiva.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

El **retroceso exponencial** (*exponential backoff*) es una política de reintento que multiplica la espera tras cada fallo: [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md) la define como la política que multiplica la espera tras cada fallo, [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) como la estrategia que multiplica la espera entre reintentos por un factor fijo, [SE-270](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md) como la que duplica el intervalo hasta un máximo y [SE-596](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md) como la espera que crece de forma exponencial entre reintentos. Un ejemplo de [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md): esperas de 1, 2, 4 y 8 segundos.

## Por qué importa

El cliente que reintenta debe esperar, y [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) dice que esperar mal es peor que no reintentar. Un intervalo fijo concentra a todos los clientes en los mismos instantes y puede volver a tumbar al servicio justo cuando se recupera. El retroceso exponencial dispersa los reintentos en el tiempo y da margen al servicio para recuperarse.

## Cómo funciona

Cada fallo multiplica la espera por un factor, hasta un máximo. La causa de su efecto es que los clientes que fallaron a la vez dejan de reintentar a la vez. Pero [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) señala su límite: si todos fallaron al mismo tiempo, siguen reintentando en sincronía, solo que en oleadas más espaciadas. Por eso se añade **jitter**, aleatoriedad en cada espera, que rompe la sincronía. Además se limita el número de intentos y el tiempo total, y se respeta `Retry-After` cuando el servidor lo envía. [SE-596](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md) aplica el conjunto en un flujo con agentes: retroceso exponencial con jitter completo, máximo de cinco intentos y dos minutos en total; pasado el límite, la ejecución queda «pendiente de revisión» y llega a una cola humana. [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md) añade un límite de tasa. Los reintentos solo son seguros si la operación es idempotente (véase idempotencia).

## Ejemplo

[SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) simula 2 000 clientes que fallan a la vez durante una caída de 5 s contra un servicio con capacidad de 400 solicitudes por segundo; cada cliente se rinde tras 8 intentos. Tras la caída, el intervalo fijo produce un pico de 2 000 solicitudes por segundo, 3 s por encima de la capacidad y 800 clientes que abandonan; el exponencial sin jitter mantiene el pico en 2 000 y 4 s por encima de la capacidad, sin abandonos; con jitter total el pico baja a 372 y la capacidad no se supera en ningún segundo.

## Errores y confusiones comunes

- **El servicio vuelve a caer al recuperarse.** Reintentos sincronizados sin jitter; corrección ([SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md)): retroceso exponencial con jitter y límite de intentos.
- **Mil clientes agotan al servidor al recuperarse.** Reintentos sincronizados sin dispersión; corrección ([SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md)): dispersión, máximo de intentos y límite de tasa.
- **Creer que exponencial basta.** Sin jitter el pico sigue siendo de 2 000 en la simulación de [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md).

## Límites y cuándo no aplica

El modelo de [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) supone clientes idénticos y capacidad fija; no incluye colas ni que el servicio empeore con la carga. Con 2 000 clientes el efecto es claro; con 20, todas las políticas serían inocuas. El retroceso no sustituye a la idempotencia ni a un interruptor de circuito (véase circuit breaker): dispersa los reintentos, no decide si conviene reintentar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-233](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md), [SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md), [SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md), [SE-238](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Espera](../e/espera.md), [Estrategia](../e/estrategia.md), [Intervalo](../i/intervalo.md), [Reintentos](./reintentos.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Dispersión](../d/dispersion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-239 — Taller: construir un flujo web resiliente](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.
- [SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-270 — Protocolos IoT y conectividad intermitente](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.
- [SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-048](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md), [SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md), [SE-399](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md), [SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md), [SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md), [SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md).

**Aparece en los casos de estudio:** [Caída global de Meta](../../../casos/fallo/meta-2021.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — retroceso exponencial y jitter; autoridad: Amazon Builders' Library.
- [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110) — métodos idempotentes y reintentos; autoridad: IETF.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — restricciones únicas y transacciones; autoridad: Python Software Foundation.
- [Python: threading](https://docs.python.org/3/library/threading.html) — hilos de la prueba de carrera; autoridad: Python Software Foundation.
- [Harel, «Statecharts: a visual formalism for complex systems» (Sci. Comput. Program., 1987)](https://doi.org/10.1016/0167-6423%2887%2990035-9) — estados y transiciones para comportamiento reactivo; autoridad: Science of Computer Programming.

---

[↑ Glosario](../../README.md) · [← Retroceso catastrófico](./retroceso-catastrofico.md) · [Retrospectiva →](./retrospectiva.md)
