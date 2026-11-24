# Ventana de retención

[↑ Glosario](../../README.md) · [← Ventana de reproceso](./ventana-de-reproceso.md) · [Ventana de reversión limpia →](./ventana-de-reversion-limpia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

La **ventana de retención** es el tiempo durante el cual el servidor recuerda una clave de idempotencia y su respuesta. Es el sentido de [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) (idempotencia, reintentos y deduplicación). [SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md) usa la misma idea para los identificadores de mensaje de un receptor idempotente, con una ventana finita (por ejemplo, 7 días). No es un periodo de conservación legal de datos, aunque comparta el nombre con él.

## Por qué importa

Una clave que caduca antes del reintento más tardío deja pasar el duplicado. El servidor no puede recordar claves para siempre, y de la ventana depende que la protección contra duplicados sea real.

## Cómo funciona

[SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md): el servidor guarda, por cada clave, la huella de la carga y la respuesta, y las retiene un tiempo. El tiempo de vida debe cubrir **el reintento más tardío que un cliente legítimo pueda hacer**. Una aplicación móvil sin conexión puede reintentar horas o días después. Si la clave caduca antes, el reintento crea un duplicado indistinguible de una solicitud nueva.

Alargar la ventana cuesta almacenamiento, y se compensa con claves compactas y limpieza periódica. Por eso la decisión es un cálculo de dos extremos: el reintento legítimo más tardío (cota inferior) y el costo de guardar (cota superior).

En un receptor idempotente ([SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md)), la misma lógica fija cuánto tiempo se conservan los identificadores vistos y exige que el canal no reenvíe un mensaje más tarde que esa ventana.

## Ejemplo

La plataforma de [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) exige `Idempotency-Key` en `POST /entregas` y en `POST /entregas/{id}/apelaciones`; guarda la clave, la huella de la carga y la respuesta en la misma transacción que el efecto; devuelve 422 si la clave llega con otra carga; y la retiene 7 días, que es el reintento más tardío del cliente móvil. El cliente reintenta solo 429, 503 y tiempos agotados, con retroceso exponencial, jitter total, un máximo de 5 intentos y respeto de `Retry-After`.

## Errores y confusiones comunes

- **Entregas duplicadas tras un error de red:** POST sin clave de idempotencia; corrección, clave por intención y restricción única ([SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md)).
- **Ventana menor que el reintento más tardío.**
- **Guardar la clave sin la huella de la carga:** una clave reutilizada con otra carga pasa inadvertida.
- **Confundirla con el TTL de una caché:** aquí un olvido produce un duplicado, no un dato viejo.

## Límites y cuándo no aplica

La ventana no protege contra un reintento posterior a ella; hace falta que el cliente deje de reintentar antes. Si el cliente puede reenviar indefinidamente (una cola persistente), la ventana debe alinearse con esa política. El valor de 7 días es de la plataforma de la clase, no una recomendación general.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md), [SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Clave de idempotencia](../c/clave-de-idempotencia.md), [Dispersión](../d/dispersion.md), [Huella de la carga](../h/huella-de-la-carga.md), [Idempotencia](../i/idempotencia.md), [Idempotente](../i/idempotente.md), [Intención](../i/intencion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md), [SE-596](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md).

**Aparece en los casos de estudio:** [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — retroceso exponencial y jitter; autoridad: Amazon Builders' Library.
- [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110) — métodos idempotentes y reintentos; autoridad: IETF.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — restricciones únicas y transacciones; autoridad: Python Software Foundation.
- [Python: threading](https://docs.python.org/3/library/threading.html) — hilos de la prueba de carrera; autoridad: Python Software Foundation.

---

[↑ Glosario](../../README.md) · [← Ventana de reproceso](./ventana-de-reproceso.md) · [Ventana de reversión limpia →](./ventana-de-reversion-limpia.md)
