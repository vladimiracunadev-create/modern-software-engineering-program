# M/M/1

[↑ Glosario](../../README.md) · [← LSB](../l/lsb.md) · [MAD →](./mad.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Modelo de una cola con llegadas aleatorias, servicio exponencial y un servidor.

Definición de trabajo de [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md).

## Por qué importa

La clase donde se define, [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md), existe con este propósito: la clase existe para que diseñes el trabajo que ocurre fuera de la solicitud: una cola con visibilidad, trabajadores que pueden caer, reintentos acotados y un lugar para lo que nunca termina.

## Cómo funciona

Según [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md):

Si llegan λ trabajos por segundo y cada trabajador procesa μ, la utilización es ρ = λ/μ. La espera media de un sistema M/M/1 es ρ/(1−ρ) veces el tiempo de servicio: con ρ = 0,5 espera 1 servicio; con 0,9, 9; con 0,95, 19. La relación no es lineal: pasar de 90 % a 95 % de utilización duplica la espera. La ley de Little relaciona el número medio de trabajos en el sistema con la tasa de llegada y el tiempo en el sistema, y sirve para dimensionar sin simular.

## Ejemplo

Ejemplo de [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula la espera teórica de una cola M/M/1. Antes de ejecutarlo, predice el valor para ρ = 0,9.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md)) son:

- **La nota se registra dos veces** — causa: handler no idempotente con entrega al menos una vez. Corrección: restricción única por identificador de trabajo.
- **Un trabajo se ejecuta dos veces sin caídas** — causa: tiempo de visibilidad menor que la duración del trabajo. Corrección: ajustar la visibilidad al máximo razonable y renovarla.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún corredor de mensajes ni se midió a ninguna persona: los tiempos de servicio, las caídas y los venenosos son construcciones del autor. La siguiente clase aborda un caso exigente de trabajo: los archivos extensos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Modelo](./modelo.md), [Servicio](../s/servicio.md), [Backpressure](../b/backpressure.md), [Cola de muertos](../c/cola-de-muertos.md), [Entrega al menos una vez](../e/entrega-al-menos-una-vez.md), [Handler idempotente](../h/handler-idempotente.md).
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

[↑ Glosario](../../README.md) · [← LSB](../l/lsb.md) · [MAD →](./mad.md)
