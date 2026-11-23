# Handler idempotente

[↑ Glosario](../../README.md) · [← Hallazgo](./hallazgo.md) · [Handoff →](./handoff.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Función de trabajo cuyo efecto no se repite si se ejecuta varias veces con el mismo trabajo.

Definición de trabajo de [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md).

## Por qué importa

La clase donde se define, [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md), existe con este propósito: la clase existe para que diseñes el trabajo que ocurre fuera de la solicitud: una cola con visibilidad, trabajadores que pueden caer, reintentos acotados y un lugar para lo que nunca termina.

## Cómo funciona

Según [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md):

Como propiedad del efecto sí, como garantía de la cola no. Se consigue con entrega al menos una vez y un handler idempotente; algunos sistemas lo llaman procesamiento efectivamente único.

## Ejemplo

Ejemplo de [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) (sección «Preguntas frecuentes»):

Como propiedad del efecto sí, como garantía de la cola no. Se consigue con entrega al menos una vez y un handler idempotente; algunos sistemas lo llaman procesamiento efectivamente único.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md)) son:

- **La nota se registra dos veces** — causa: handler no idempotente con entrega al menos una vez. Corrección: restricción única por identificador de trabajo.
- **Un trabajo se ejecuta dos veces sin caídas** — causa: tiempo de visibilidad menor que la duración del trabajo. Corrección: ajustar la visibilidad al máximo razonable y renovarla.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún corredor de mensajes ni se midió a ninguna persona: los tiempos de servicio, las caídas y los venenosos son construcciones del autor. La siguiente clase aborda un caso exigente de trabajo: los archivos extensos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Efecto](../e/efecto.md), [Función](../f/funcion.md), [Trabajo](../t/trabajo.md), [Backpressure](../b/backpressure.md), [Cola de muertos](../c/cola-de-muertos.md), [Entrega al menos una vez](../e/entrega-al-menos-una-vez.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE Book: Handling Overload](https://sre.google/sre-book/handling-overload/) — sobrecarga, rechazo y degradación; autoridad: Google.
- [Timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — reintentos con retroceso; autoridad: Amazon Builders' Library.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — tablas y transacciones del experimento; autoridad: Python Software Foundation.
- [Python: queue](https://docs.python.org/3/library/queue.html) — colas de la biblioteca estándar; autoridad: Python Software Foundation.

---

[↑ Glosario](../../README.md) · [← Hallazgo](./hallazgo.md) · [Handoff →](./handoff.md)
