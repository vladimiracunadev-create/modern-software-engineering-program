# Ventana de gracia

[↑ Glosario](../../README.md) · [← Ventana de exposición](./ventana-de-exposicion.md) · [Ventana de reproceso →](./ventana-de-reproceso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Plazo tras el fin del periodo durante el cual aún se aceptan eventos antes de emitir la factura.

Definición de trabajo de [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md).

## Por qué importa

En [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md), el tema «Cierre del periodo» importa porque fija cuándo un número deja de cambiar.

## Cómo funciona

Según [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md):

Un evento tardío puede llegar en cualquier momento, pero la factura debe emitirse en una fecha. La práctica es una *ventana de gracia*: el periodo se cierra N horas después de su fin (por ejemplo 24 horas) y la factura se emite desde ahí. Los eventos que llegan después del cierre no cambian la factura emitida (es inmutable): se registran como ajuste en la factura siguiente, con su concepto. El borrador previo al cierre se puede recalcular las veces que haga falta porque es una consulta determinista sobre los eventos crudos; la factura emitida no.

Según [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md):

**Diagnóstico paso a paso.** (1) Se compara el agregado de la tubería con el recálculo nocturno desde los eventos crudos: coinciden con el panel, no con la factura. (2) La factura se calculó con un agregado por hora que el trabajador regeneró durante una migración y que sumó dos veces un lote de la hora 14 del día 17. (3) La tabla de agregados no tenía restricción de unicidad por (cliente, hora, lote), solo una por (cliente, hora) que el trabajador omitió con una opción de «reemplazar» mal configurada. (4) Se detecta con la comparación de cierre: la diferencia es cero salvo en esa hora.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md):

*Escenario ilustrativo: las cifras y los resultados de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Los eventos que llegan después del cierre no cambian la factura emitida (es inmutable): se registran como ajuste en la factura siguiente, con su concepto. ([SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Evento](../e/evento.md), [Factura](../f/factura.md).
- **Ver también:** [Plazo](../p/plazo.md), [Ajuste](../a/ajuste.md), [Deduplicación](../d/deduplicacion.md), [Evento de uso](../e/evento-de-uso.md), [Métrica facturable](../m/metrica-facturable.md), [Tiempo de ocurrencia / de procesamiento](../t/tiempo-de-ocurrencia-de-procesamiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (156 clases más lo mencionan; las que más):

[SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md), [SE-462](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md), [SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md), [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md), [SE-362](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md), [SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md), [SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md), [SE-218](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md), [Slack](../../../casos/exito/slack.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «cierre».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Ventana de exposición](./ventana-de-exposicion.md) · [Ventana de reproceso →](./ventana-de-reproceso.md)
