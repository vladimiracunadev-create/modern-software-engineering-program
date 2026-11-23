# Prorrateo

[↑ Glosario](../../README.md) · [← Propuesta de valor](./propuesta-de-valor.md) · [Protocolos de mensajes →](./protocolos-de-mensajes.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Ajuste de importes proporcional a los días restantes del ciclo cuando algo cambia a mitad de él.

Definición de trabajo de [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md).

## Por qué importa

En [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md), el tema «Prorrateo» importa porque un cambio de plan a mitad de ciclo debe cobrar y acreditar con exactitud.

## Cómo funciona

Según [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md):

El equipo de *Tablero* rediseña su facturación recurrente. Escribe la tabla de nueve transiciones y la convierte en pruebas: una por cada transición válida y una por cada transición inválida importante (un pago sobre una cuenta cancelada pide reactivación explícita). Reemplaza el campo `vence` por un ancla y un periodo actual, con una prueba de renovaciones desde el 29, 30 y 31 en un año bisiesto. Para el prorrateo define la regla («cobro inmediato al subir, crédito en la siguiente factura al bajar; redondeo hacia el centavo más cercano en cada línea») y la escribe también en la página de precios.

## Ejemplo

Ejemplo de [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md) (sección «Ejemplo profesional»):

El equipo de *Tablero* rediseña su facturación recurrente. Escribe la tabla de nueve transiciones y la convierte en pruebas: una por cada transición válida y una por cada transición inválida importante (un pago sobre una cuenta cancelada pide reactivación explícita). Reemplaza el campo `vence` por un ancla y un periodo actual, con una prueba de renovaciones desde el 29, 30 y 31 en un año bisiesto. Para el prorrateo define la regla («cobro inmediato al subir, crédito en la siguiente factura al bajar; redondeo hacia el centavo más cercano en cada línea») y la escribe también en la página de precios.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md)) son: Se ejecutaron una máquina de estados, un ciclo anclado y un prorrateo, y se simularon reintentos con semilla 34 y probabilidades del autor; no se llamó a un procesador, no hubo cobros reales ni se trataron impuestos, facturación electrónica ni reconocimiento contable de ingresos. Las probabilidades de recuperación no son las de ningún procesador.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-057](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md), [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md), [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md), [SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ajuste](../a/ajuste.md), [Ciclo](../c/ciclo.md), [Ancla del ciclo](../a/ancla-del-ciclo.md), [Dunning](../d/dunning.md), [Factura](../f/factura.md), [Máquina de estados](../m/maquina-de-estados.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-412 — Suscripciones, ciclos de facturación y dunning](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Propuesta de valor](./propuesta-de-valor.md) · [Protocolos de mensajes →](./protocolos-de-mensajes.md)
