# Mensaje venenoso

[↑ Glosario](../../README.md) · [← Mensaje veneno](./mensaje-veneno.md) · [Mensajes y despacho →](./mensajes-y-despacho.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Trabajo que falla siempre, por ejemplo por un dato corrupto.

Definición de trabajo de [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-382 — Observabilidad y seguridad de integraciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md): Mensaje que un consumidor no puede procesar y que, reintentado sin fin, impide avanzar a los siguientes.

## Por qué importa

La clase donde se define, [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md), existe con este propósito: la clase existe para que diseñes el trabajo que ocurre fuera de la solicitud: una cola con visibilidad, trabajadores que pueden caer, reintentos acotados y un lugar para lo que nunca termina.

## Cómo funciona

Según [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md):

Reproduce el fallo de la clase: **un mensaje venenoso que acapara a los trabajadores**. Con la política de reintento sin límite al frente de la cola, introduce 10 trabajos que siempre fallan entre 1 000. **Síntoma:** la espera de los trabajos buenos crece sin tope y la cola no baja. **Hipótesis rivales:** (a) faltan trabajadores; (b) los mismos trabajos fallan una y otra vez. **Prueba:** cuenta intentos por identificador y comprueba que diez identificadores acumulan miles. **Causa:** reintento sin límite. **Corrección:** tres intentos con retroceso y cola de muertos. **Regresión:** una prueba que inyecta un venenoso y exige que los demás terminen y que el venenoso aparezca en la cola de muertos.

Según [SE-382 — Observabilidad y seguridad de integraciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md):

Un flujo asíncrono falla de formas que una alarma sola no ve. La **profundidad** de la cola crece cuando el consumidor es lento o está colgado, pero no cuando el productor se detiene. La **edad del mensaje más viejo** detecta un mensaje atascado aunque la cola sea corta. La **tasa de procesados** cae cuando el consumidor se cuelga, pero también cuando simplemente no hay trabajo: da falsas alarmas fuera del horario de uso. La **tasa de errores** detecta un mensaje venenoso que se reintenta sin fin, pero no a un consumidor colgado que no produce errores. La práctica es vigilar varias señales, definir para cada alarma qué acción exige y qué falla cubre, y evitar alarmas que despierten a alguien sin que haya nada que hacer.

## Ejemplo

Caso medido en la sección «El mensaje venenoso» de [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md):

Mil trabajos de 1 s con dos trabajadores; uno de cada cien (10 en total) falla siempre. Tres políticas: reintentar sin límite devolviendo el trabajo al frente de la cola, tres intentos y cola de muertos, y tres intentos con reintento al final de la cola. Se cuenta cuántos de los 990 trabajos buenos se completan (con un tope de 20 000 ejecuciones).

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md)) son:

- **La nota se registra dos veces** — causa: handler no idempotente con entrega al menos una vez. Corrección: restricción única por identificador de trabajo.
- **Un trabajo se ejecuta dos veces sin caídas** — causa: tiempo de visibilidad menor que la duración del trabajo. Corrección: ajustar la visibilidad al máximo razonable y renovarla.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **tasa de errores** detecta un mensaje venenoso que se reintenta sin fin, pero no a un consumidor colgado que no produce errores. ([SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Trabajo](../t/trabajo.md), [Backpressure](../b/backpressure.md), [Cola de muertos](../c/cola-de-muertos.md), [Entrega al menos una vez](../e/entrega-al-menos-una-vez.md), [Handler idempotente](../h/handler-idempotente.md), [Identificador de correlación](../i/identificador-de-correlacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-382 — Observabilidad y seguridad de integraciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-223](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE Book: Handling Overload](https://sre.google/sre-book/handling-overload/) — sobrecarga, rechazo y degradación; autoridad: Google.
- [Timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — reintentos con retroceso; autoridad: Amazon Builders' Library.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — tablas y transacciones del experimento; autoridad: Python Software Foundation.
- [Python: queue](https://docs.python.org/3/library/queue.html) — colas de la biblioteca estándar; autoridad: Python Software Foundation.
- [W3C Trace Context](https://www.w3.org/TR/trace-context/) — encabezados para propagar el contexto de una traza; autoridad: W3C.

---

[↑ Glosario](../../README.md) · [← Mensaje veneno](./mensaje-veneno.md) · [Mensajes y despacho →](./mensajes-y-despacho.md)
