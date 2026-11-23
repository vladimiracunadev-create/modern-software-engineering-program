# Deduplicación

[↑ Glosario](../../README.md) · [← Decorator](./decorator.md) · [Deduplicación de peticiones →](./deduplicacion-de-peticiones.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Descartar eventos repetidos mediante su identificador.

Definición de trabajo de [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md).

## Por qué importa

La clase donde se define, [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md), existe con este propósito: la clase existe para que conviertas «lo que el cliente usó» en un importe que el cliente pueda verificar, que contabilidad pueda conciliar y que sobreviva a que los mensajes se repitan, lleguen tarde o se pierdan.

## Cómo funciona

Según [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md):

La deduplicación falla en silencio. Por eso el identificador debe derivarse del hecho (por ejemplo, el identificador de la petición) y no de la entrega, y se prueba reemitiendo un lote y comprobando que los totales no cambian.

## Ejemplo

Ejemplo de [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md) (sección «Preguntas frecuentes»):

La deduplicación falla en silencio. Por eso el identificador debe derivarse del hecho (por ejemplo, el identificador de la petición) y no de la entrega, y se prueba reemitiendo un lote y comprobando que los totales no cambian.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md)) son: Se midieron 30 000 eventos sintéticos con duplicados y tardíos simulados con semilla 34 y se compararon dos reglas de precios con tramos de ejemplo; no se usó una cola real, ni un reloj distribuido, ni un procesador de pagos. Los precios y las tasas de duplicados y de tardíos son del autor.

## Relación con otros conceptos

- **Prerrequisito:** [Evento](../e/evento.md).
- **Ver también:** [Ajuste](../a/ajuste.md), [Evento de uso](../e/evento-de-uso.md), [Métrica facturable](../m/metrica-facturable.md), [Tiempo de ocurrencia / de procesamiento](../t/tiempo-de-ocurrencia-de-procesamiento.md), [Tramos graduales / por volumen](../t/tramos-graduales-por-volumen.md), [Ventana de gracia](../v/ventana-de-gracia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (19 clases más lo mencionan; las que más):

[SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md), [SE-362](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md), [SE-232](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-232-estado-componentes-y-gestion-de-datos/README.md), [SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md), [SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md), [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md).

**Aparece en los casos de estudio:** [Spotify](../../../casos/exito/spotify.md), [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Decorator](./decorator.md) · [Deduplicación de peticiones →](./deduplicacion-de-peticiones.md)
