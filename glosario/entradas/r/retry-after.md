# Retry-After

[↑ Glosario](../../README.md) · [← Retry y operaciones inciertas](./retry-y-operaciones-inciertas.md) · [Reuse y verificación →](./reuse-y-verificacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Encabezado con el que el servidor indica cuánto esperar antes de reintentar.

Definición de trabajo de [SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md).

## Por qué importa

La clase donde se define, [SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md), existe con este propósito: la clase existe para que diseñes una operación que se pueda repetir sin duplicar su efecto, midas cuántos duplicados produce un reintento tras perder la respuesta, elijas una política de reintento que no agrave una caída y fijes cuánto tiempo recuerda el servicio una clave.

## Cómo funciona

Según [SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md):

El cliente que reintenta debe esperar, y esperar mal es peor que no reintentar. Un intervalo fijo concentra a todos los clientes en los mismos instantes; el retroceso exponencial (1, 2, 4, 8 s) los dispersa en el tiempo pero mantiene el sincronismo si todos fallaron a la vez; añadir **jitter** (aleatoriedad en cada espera) rompe la sincronía. Se limita además el número de intentos y el tiempo total, y se respeta `Retry-After` cuando el servidor lo envía.

Según [SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md):

La plataforma exige `Idempotency-Key` en `POST /entregas` y en `POST /entregas/{id}/apelaciones`; guarda la clave, la huella de la carga y la respuesta en la misma transacción que el efecto; devuelve 422 si la clave llega con otra carga; la retiene 7 días, el reintento más tardío del cliente móvil. El cliente reintenta solo 429, 503 y tiempos agotados, con retroceso exponencial, jitter total, un máximo de 5 intentos y respeto de `Retry-After`. Compara este diseño con el original en tres casos: respuesta perdida, caída de cinco segundos con miles de clientes y reintento tres días después.

## Ejemplo

Ejemplo de [SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) (sección «Ejemplo profesional»):

La plataforma exige `Idempotency-Key` en `POST /entregas` y en `POST /entregas/{id}/apelaciones`; guarda la clave, la huella de la carga y la respuesta en la misma transacción que el efecto; devuelve 422 si la clave llega con otra carga; la retiene 7 días, el reintento más tardío del cliente móvil. El cliente reintenta solo 429, 503 y tiempos agotados, con retroceso exponencial, jitter total, un máximo de 5 intentos y respeto de `Retry-After`. Compara este diseño con el original en tres casos: respuesta perdida, caída de cinco segundos con miles de clientes y reintento tres días después.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md)) son:

- **Entregas duplicadas tras un error de red** — causa: POST sin clave de idempotencia. Corrección: clave por intención y restricción única.
- **El servicio vuelve a caer al recuperarse** — causa: reintentos sincronizados sin jitter. Corrección: retroceso exponencial con jitter y límite de intentos.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ningún servicio, cliente ni red reales: las pérdidas, la capacidad y los retardos son construcciones del autor. La siguiente clase pregunta qué pasa cuando el trabajo ocurre fuera de la solicitud y se entrega al menos una vez.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md), [SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Clave de idempotencia](../c/clave-de-idempotencia.md), [Dispersión](../d/dispersion.md), [Huella de la carga](../h/huella-de-la-carga.md), [Idempotencia](../i/idempotencia.md), [Idempotente](../i/idempotente.md), [Intención](../i/intencion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-042](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md), [SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md), [SE-048](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md), [SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — retroceso exponencial y jitter; autoridad: Amazon Builders' Library.
- [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110) — métodos idempotentes y reintentos; autoridad: IETF.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — restricciones únicas y transacciones; autoridad: Python Software Foundation.
- [Python: threading](https://docs.python.org/3/library/threading.html) — hilos de la prueba de carrera; autoridad: Python Software Foundation.

---

[↑ Glosario](../../README.md) · [← Retry y operaciones inciertas](./retry-y-operaciones-inciertas.md) · [Reuse y verificación →](./reuse-y-verificacion.md)
