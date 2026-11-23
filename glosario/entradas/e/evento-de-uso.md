# Evento de uso

[↑ Glosario](../../README.md) · [← Evento de telemetría](./evento-de-telemetria.md) · [Evento privilegiado →](./evento-privilegiado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Registro inmutable de un hecho medible, con identidad, inquilino, cantidad y tiempo de ocurrencia.

Definición de trabajo de [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md).

## Por qué importa

La clase donde se define, [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md), existe con este propósito: la clase existe para que conviertas «lo que el cliente usó» en un importe que el cliente pueda verificar, que contabilidad pueda conciliar y que sobreviva a que los mensajes se repitan, lleguen tarde o se pierdan.

## Cómo funciona

[SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: consulta la clase para el mecanismo completo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md):

*Escenario ilustrativo: las cifras y los resultados de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md)) son: Se midieron 30 000 eventos sintéticos con duplicados y tardíos simulados con semilla 34 y se compararon dos reglas de precios con tramos de ejemplo; no se usó una cola real, ni un reloj distribuido, ni un procesador de pagos. Los precios y las tasas de duplicados y de tardíos son del autor.

## Relación con otros conceptos

- **Prerrequisito:** [Inquilino](../i/inquilino.md).
- **Ver también:** [Hecho](../h/hecho.md), [Registro](../r/registro.md), [Ajuste](../a/ajuste.md), [Deduplicación](../d/deduplicacion.md), [Métrica facturable](../m/metrica-facturable.md), [Tiempo de ocurrencia / de procesamiento](../t/tiempo-de-ocurrencia-de-procesamiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-413 — Medición de uso y facturación por consumo](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Evento de telemetría](./evento-de-telemetria.md) · [Evento privilegiado →](./evento-privilegiado.md)
