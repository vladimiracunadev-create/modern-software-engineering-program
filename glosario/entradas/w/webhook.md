# Webhook

[↑ Glosario](../../README.md) · [← WASI](./wasi.md) · [Whistleblowing →](./whistleblowing.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Un **webhook** es una petición HTTP `POST` que un sistema (el proveedor) dirige a una dirección de otro (el receptor) para avisarle de un evento, con un cuerpo que describe lo ocurrido ([SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md)). [SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md) lo usa en el contexto de pagos: el mensaje que el procesador envía al producto para notificar un evento.

## Por qué importa

En lugar de preguntar periódicamente al proveedor si algo cambió, el receptor recibe el aviso cuando ocurre. Pero esa comodidad trae un contrato implícito que, si no se entiende, produce pérdidas, duplicados y eventos falsos. La decisión que cambia es cómo se escribe el receptor: no como una función que aplica el cambio, sino como un buzón que verifica, guarda y responde rápido.

## Cómo funciona

[SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md) describe cuatro partes del contrato implícito:

1. El receptor debe **responder rápido** con un código de éxito: el proveedor considera fallida cualquier respuesta lenta o de error, y reintenta.
2. **No se garantiza orden** entre eventos.
3. Se puede recibir el **mismo evento más de una vez**.
4. **No hay garantía** de haberlos recibido todos.

Por eso el cuerpo debe tratarse como un **aviso**, y el tratamiento real (por ejemplo, aplicar una nota o actualizar una suscripción) hacerse de forma asíncrona e idempotente: el manejador **verifica, guarda en una cola y responde**; un trabajador procesa aparte. La verificación es la **firma**: el proveedor firma el cuerpo con un HMAC y un secreto compartido, y el receptor la comprueba con una comparación de tiempo constante; sin ella, cualquiera que conozca la dirección puede crear eventos falsos.

Como no hay garantía de recibirlos todos, el webhook se combina con una **reconciliación** periódica: el webhook es la pista de baja latencia y el sondeo (listar lo ocurrido desde un punto de control) la red de seguridad. Los dos mecanismos no son excluyentes.

## Ejemplo

Un procesador de pagos envía un webhook «pago confirmado». El manejador verifica la firma HMAC, guarda el evento en una cola y devuelve 200 en milisegundos. Un trabajador lo procesa de forma idempotente, de modo que si el evento llega dos veces no se activa la suscripción dos veces. Cada hora, un trabajo lista los pagos recientes del proveedor y procesa los que faltaron. Mecanismo de [SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md).

## Errores y confusiones comunes

- **Alguien crea eventos falsos con una herramienta**: la dirección del webhook no verifica firma; se corrige con firma HMAC y comparación de tiempo constante.
- **El proveedor desactiva el webhook**: respuestas lentas o de error durante mucho tiempo; se corrige respondiendo rápido, encolando y procesando aparte, con alarma por fallos.
- **Procesar dentro del manejador**: una demora provoca reintentos y duplicados.
- **Asumir orden y entrega exacta**.

## Límites y cuándo no aplica

No sirve como única fuente de verdad: puede perder eventos y no garantiza orden. Para consultas que requieren el estado actual, se pregunta al proveedor. Y exige exponer una dirección pública y operar su seguridad, lo que no siempre es posible detrás de ciertas redes; en ese caso el sondeo es la alternativa.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento](../e/evento.md), [Producto](../p/producto.md), [Ancla del ciclo](../a/ancla-del-ciclo.md), [Dunning](../d/dunning.md), [Factura](../f/factura.md), [HMAC](../h/hmac.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.
- [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (11 clases más lo mencionan; las que más):

[SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), [SE-338](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md), [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md), [SE-298](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md), [SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md), [SE-079](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md), [SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md), [SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md).

**Aparece en los casos de estudio:** [Mercado Libre](../../../casos/exito/mercado-libre.md), [Stripe](../../../casos/exito/stripe.md), [Shopify](../../../casos/exito/shopify.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Webhooks».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Stripe: webhooks](https://docs.stripe.com/webhooks) — firmas, tolerancia de marca de tiempo, reintentos y eventos repetidos; autoridad: documentación oficial de Stripe.
- [GitHub: validar entregas de webhooks](https://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries) — HMAC-SHA256 y comparación de tiempo constante; autoridad: documentación oficial de GitHub.
- [Standard Webhooks](https://www.standardwebhooks.com/) — convención de identificador, marca de tiempo y firma; autoridad: especificación comunitaria.
- [RFC 2104: HMAC](https://www.rfc-editor.org/rfc/rfc2104) — código de autenticación de mensajes; autoridad: IETF.
- [RFC 9110: semántica de HTTP](https://www.rfc-editor.org/rfc/rfc9110) — validadores y peticiones condicionales; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← WASI](./wasi.md) · [Whistleblowing →](./whistleblowing.md)
