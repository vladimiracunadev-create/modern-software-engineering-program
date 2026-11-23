# Tramos graduales / por volumen

[↑ Glosario](../../README.md) · [← Tramo revisable](./tramo-revisable.md) · [Trampa →](./trampa.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Cada tramo a su precio frente a toda la cantidad al precio de su tramo.

Definición de trabajo de [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md).

## Por qué importa

La clase donde se define, [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md), existe con este propósito: la clase existe para que conviertas «lo que el cliente usó» en un importe que el cliente pueda verificar, que contabilidad pueda conciliar y que sobreviva a que los mensajes se repitan, lleguen tarde o se pierdan.

## Cómo funciona

[SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md):

*Escenario ilustrativo: las cifras y los resultados de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md)) son: Se midieron 30 000 eventos sintéticos con duplicados y tardíos simulados con semilla 34 y se compararon dos reglas de precios con tramos de ejemplo; no se usó una cola real, ni un reloj distribuido, ni un procesador de pagos. Los precios y las tasas de duplicados y de tardíos son del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md), [SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md), [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ajuste](../a/ajuste.md), [Deduplicación](../d/deduplicacion.md), [Evento de uso](../e/evento-de-uso.md), [Métrica facturable](../m/metrica-facturable.md), [Tiempo de ocurrencia / de procesamiento](./tiempo-de-ocurrencia-de-procesamiento.md), [Ventana de gracia](../v/ventana-de-gracia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Tramo revisable](./tramo-revisable.md) · [Trampa →](./trampa.md)
