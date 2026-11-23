# Petición condicional

[↑ Glosario](../../README.md) · [← Perturbación](./perturbacion.md) · [Petición de decisión →](./peticion-de-decision.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Petición que incluye el validador de una respuesta anterior para que el servidor responda sin cuerpo si no hay cambios.

Definición de trabajo de [SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md).

## Por qué importa

La clase donde se define, [SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md), existe con este propósito: la clase existe para que decidas cómo se entera tu sistema de lo que ocurre en otro que no controlas, con el costo de cada opción a la vista: aprenderás a medir cuántas peticiones vacías cuesta sondear a un intervalo dado y cuánto retrasa un evento, qué ataques cierra cada capa de verificación de un webhook y cuántos eventos se pierden o se repiten según la política de reintentos del emisor.

## Cómo funciona

Según [SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md):

El equipo de la plataforma documenta el contrato de recepción del webhook del sistema académico. **Verificación:** el manejador lee el cuerpo crudo, comprueba la firma HMAC con comparación de tiempo constante, rechaza marcas de tiempo con más de cinco minutos de diferencia y rechaza identificadores ya vistos, y acepta la firma del secreto vigente y del anterior durante la rotación. **Respuesta:** guarda el evento en una tabla de entrada con el identificador como clave única y responde 204 en milisegundos; ningún trabajo pesado ocurre en el manejador. **Procesamiento:** un trabajador lee la tabla, aplica la nota con guarda de versión y marca el evento.

## Ejemplo

Ejemplo de [SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma documenta el contrato de recepción del webhook del sistema académico. **Verificación:** el manejador lee el cuerpo crudo, comprueba la firma HMAC con comparación de tiempo constante, rechaza marcas de tiempo con más de cinco minutos de diferencia y rechaza identificadores ya vistos, y acepta la firma del secreto vigente y del anterior durante la rotación. **Respuesta:** guarda el evento en una tabla de entrada con el identificador como clave única y responde 204 en milisegundos; ningún trabajo pesado ocurre en el manejador. **Procesamiento:** un trabajador lee la tabla, aplica la nota con guarda de versión y marca el evento.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md)) son:

- **Alguien crea eventos falsos con una herramienta** — causa: la dirección del webhook no verifica firma. Corrección: firma HMAC con secreto y comparación de tiempo constante.
- **Se reprocesa una entrega capturada** — causa: firma sin marca de tiempo ni identificador. Corrección: marca de tiempo firmada con tolerancia corta e identificadores vistos.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún proveedor, dominio externo ni red más allá del bucle local: la tasa de eventos, la pérdida de respuestas, la ventana de 300 s y los calendarios de reintento son construcciones del autor, y los resultados no se extrapolan a ningún servicio.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [HMAC](../h/hmac.md), [Reconciliación](../r/reconciliacion.md), [Sondeo](../s/sondeo.md), [Webhook](../w/webhook.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-379 — Webhooks, polling y suscripciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-042](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md).

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

[↑ Glosario](../../README.md) · [← Perturbación](./perturbacion.md) · [Petición de decisión →](./peticion-de-decision.md)
