# Webhook

[↑ Glosario](../../README.md) · [← WASI](./wasi.md) · [Whistleblowing →](./whistleblowing.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Petición HTTP que un sistema envía a una dirección de otro para avisarle de un evento.

Definición de trabajo de [SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md): Mensaje que el procesador envía al producto para notificar un evento.

## Por qué importa

En [SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md), el tema «Webhooks» importa porque exponen una dirección pública que debe autenticar y tolerar repeticiones.

## Cómo funciona

Según [SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md), en la sección «Webhooks»:

Un **webhook** es una petición HTTP `POST` que el proveedor dirige a una dirección del receptor con un cuerpo que describe el evento. Su contrato implícito tiene cuatro partes: el receptor debe responder rápido con un código de éxito (el proveedor considera fallida cualquier respuesta lenta o de error y reintenta), no se garantiza orden entre eventos, se puede recibir el mismo evento más de una vez y no hay garantía de haber recibido todos. Por eso el cuerpo debe tratarse como un **aviso** y el tratamiento real (aplicar la nota) hacerse de forma asíncrona e idempotente: el manejador verifica, guarda en una cola y responde, y un trabajador procesa.

## Ejemplo

Ejemplo de [SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma documenta el contrato de recepción del webhook del sistema académico. **Verificación:** el manejador lee el cuerpo crudo, comprueba la firma HMAC con comparación de tiempo constante, rechaza marcas de tiempo con más de cinco minutos de diferencia y rechaza identificadores ya vistos, y acepta la firma del secreto vigente y del anterior durante la rotación. **Respuesta:** guarda el evento en una tabla de entrada con el identificador como clave única y responde 204 en milisegundos; ningún trabajo pesado ocurre en el manejador. **Procesamiento:** un trabajador lee la tabla, aplica la nota con guarda de versión y marca el evento.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Alguien crea eventos falsos con una herramienta** — causa: la dirección del webhook no verifica firma. Corrección: firma HMAC con secreto y comparación de tiempo constante. ([SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md))
- **El proveedor desactiva el webhook** — causa: respuestas lentas o de error durante mucho tiempo. Corrección: responder rápido, encolar y procesar aparte; alarmar por fallos. ([SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- No son excluyentes: la combinación habitual usa el webhook como pista de baja latencia y el sondeo como red de seguridad. ([SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md))

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
