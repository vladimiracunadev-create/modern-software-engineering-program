# Retroceso exponencial

[↑ Glosario](../../README.md) · [← Retroceso catastrófico](./retroceso-catastrofico.md) · [Retrospectiva →](./retrospectiva.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Espera que crece de forma exponencial entre reintentos.

Definición de trabajo de [SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md): Estrategia que multiplica la espera entre reintentos por un factor fijo.
- En [SE-239 — Taller: construir un flujo web resiliente](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md): Política de reintento que multiplica la espera tras cada fallo.
- En [SE-270 — Protocolos IoT y conectividad intermitente](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md): Política que duplica el intervalo entre reintentos tras cada fallo hasta un máximo.

## Por qué importa

La clase donde se define, [SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md), existe con este propósito: la clase existe para que un sistema con LLM **sobreviva a sus propias interrupciones sin repetir ni perder efectos**.

## Cómo funciona

Según [SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md):

Cuando una llamada falla de forma transitoria (tiempo de espera, error 503), reintentar es razonable; pero **cuándo** reintentar importa tanto como cuántas veces. Con mil clientes sincronizados y un servicio caído cinco segundos, tres políticas dan resultados distintos. Con intervalo fijo de un segundo: 6 000 solicitudes, picos de 1 000 por medio segundo, y mil clientes golpean a la vez tras la recuperación. Con retroceso exponencial **sin aleatoriedad**: 4 000 solicitudes, pero los clientes siguen sincronizados y el pico tras la recuperación vuelve a ser de 1 000. Con retroceso exponencial y **jitter completo** (esperar un valor aleatorio entre 0 y el tope): 5 061 solicitudes y un pico tras la recuperación de 145.

Según [SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md):

El equipo de *Avisos* revisa su flujo de aviso masivo. Lista los pasos: leer pendientes (idempotente), calcular umbrales (determinista), enviar por correo (efecto), registrar el envío (efecto interno con clave natural) y notificar a coordinación (efecto). Para el envío, la clave es `aviso:{curso}:{estudiante}:{umbral}` y el proveedor de correo la acepta en una cabecera con retención de 24 horas; para la notificación a coordinación, que no admite claves, el diario guarda el identificador devuelto y, antes de repetir, consulta si el mensaje existe. Los reintentos usan retroceso exponencial con jitter completo, un máximo de cinco intentos y un tiempo total de dos minutos; pasado ese límite, la ejecución se marca «pendiente de revisión» y aparece en la cola humana.

## Ejemplo

Ejemplo de [SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* revisa su flujo de aviso masivo. Lista los pasos: leer pendientes (idempotente), calcular umbrales (determinista), enviar por correo (efecto), registrar el envío (efecto interno con clave natural) y notificar a coordinación (efecto). Para el envío, la clave es `aviso:{curso}:{estudiante}:{umbral}` y el proveedor de correo la acepta en una cabecera con retención de 24 horas; para la notificación a coordinación, que no admite claves, el diario guarda el identificador devuelto y, antes de repetir, consulta si el mensaje existe.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El servicio vuelve a caer al recuperarse** — causa: reintentos sincronizados sin jitter. Corrección: retroceso exponencial con jitter y límite de intentos. ([SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md))
- **Mil clientes agotan al servidor al recuperarse** — causa: reintentos sincronizados sin dispersión. Corrección: retroceso exponencial con dispersión, máximo de intentos y límite de tasa. ([SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Con retroceso exponencial **sin aleatoriedad**: 4 000 solicitudes, pero los clientes siguen sincronizados y el pico tras la recuperación vuelve a ser de 1 000. ([SE-596](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md))
- **reintentos con retroceso exponencial sin jitter tras un corte general**. ([SE-270](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md))

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
