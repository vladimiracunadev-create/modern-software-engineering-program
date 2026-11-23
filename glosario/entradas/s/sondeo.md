# Sondeo

[↑ Glosario](../../README.md) · [← Sonda sintética](./sonda-sintetica.md) · [Sondeo de arranque →](./sondeo-de-arranque.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Consulta periódica de un sistema a otro para saber si hubo cambios.

Definición de trabajo de [SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md).

## Por qué importa

En [SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md), el tema «Sondeo y peticiones condicionales» importa porque cambia peticiones por retraso y puede evitar transferir lo que no cambió.

## Cómo funciona

Según [SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md):

En el modelo de **empujar** (webhook), el proveedor llama al receptor cuando algo ocurre; en el de **tirar** (sondeo), el receptor pregunta cada cierto tiempo. El primero da baja latencia y pocas peticiones, pero obliga al receptor a exponer un punto de entrada, estar disponible cuando el proveedor llama y aceptar el calendario de reintentos del otro. El segundo conserva el control (cuándo, cuánto, qué), no requiere exponer nada y es sencillo de depurar, a cambio de peticiones vacías y de un retraso que depende del intervalo. No son excluyentes: la combinación habitual usa el webhook como pista de baja latencia y el sondeo como red de seguridad.

Según [SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md):

Depende de quién debe soportar el costo y el riesgo. Un webhook da baja latencia pero expone una dirección y exige verificar, tolerar repeticiones y reconciliar; el sondeo cuesta peticiones y retraso pero el receptor controla el ritmo. Para cosas que importan, la combinación (webhook como pista y sondeo de reconciliación) es la más robusta.

## Ejemplo

Ejemplo de [SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md) (sección «Preguntas frecuentes»):

Depende de quién debe soportar el costo y el riesgo. Un webhook da baja latencia pero expone una dirección y exige verificar, tolerar repeticiones y reconciliar; el sondeo cuesta peticiones y retraso pero el receptor controla el ritmo. Para cosas que importan, la combinación (webhook como pista y sondeo de reconciliación) es la más robusta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md)) son:

- **Alguien crea eventos falsos con una herramienta** — causa: la dirección del webhook no verifica firma. Corrección: firma HMAC con secreto y comparación de tiempo constante.
- **Se reprocesa una entrega capturada** — causa: firma sin marca de tiempo ni identificador. Corrección: marca de tiempo firmada con tolerancia corta e identificadores vistos.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- No son excluyentes: la combinación habitual usa el webhook como pista de baja latencia y el sondeo como red de seguridad. ([SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [HMAC](../h/hmac.md), [Petición condicional](../p/peticion-condicional.md), [Reconciliación](../r/reconciliacion.md), [Webhook](../w/webhook.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (14 clases más lo mencionan; las que más):

[SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md), [SE-261](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), [SE-265](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md), [SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md), [SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md), [SE-045](../../../classes/part-03-redes-internet-y-protocolos/se-045-sockets-conexiones-persistentes-y-tiempo-real/README.md), [SE-609](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Stripe: webhooks](https://docs.stripe.com/webhooks) — firmas, tolerancia de marca de tiempo, reintentos y eventos repetidos; autoridad: documentación oficial de Stripe.
- [GitHub: validar entregas de webhooks](https://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries) — HMAC-SHA256 y comparación de tiempo constante; autoridad: documentación oficial de GitHub.
- [Standard Webhooks](https://www.standardwebhooks.com/) — convención de identificador, marca de tiempo y firma; autoridad: especificación comunitaria.
- [RFC 2104: HMAC](https://www.rfc-editor.org/rfc/rfc2104) — código de autenticación de mensajes; autoridad: IETF.
- [RFC 9110: semántica de HTTP](https://www.rfc-editor.org/rfc/rfc9110) — validadores y peticiones condicionales; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Sonda sintética](./sonda-sintetica.md) · [Sondeo de arranque →](./sondeo-de-arranque.md)
