# Métrica de valor

[↑ Glosario](../../README.md) · [← Métrica contraria](./metrica-contraria.md) · [Métrica de vanidad →](./metrica-de-vanidad.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Unidad con la que se cobra, que escala con lo que obtiene el cliente.

Definición de trabajo de [SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md).

## Por qué importa

En [SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md), el tema «Métrica de valor» importa porque un cobro que escala con el valor se acepta; uno que no, se percibe como castigo.

## Cómo funciona

Según [SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md):

Toma el plan de precios de un producto que uses y reconstruye su lógica: cuál es la métrica de valor, qué límites separan los planes, qué porcentaje de clientes crees que supera cada límite y qué haría el proveedor si ese porcentaje cambiara. Anota qué datos necesitarías para comprobar tu hipótesis; son los que pedirías a tu propia base.

## Ejemplo

Caso medido en la sección «La métrica de valor es lo que escala con lo que el cliente obtiene» de [SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md):

Cobrar por algo que no se relaciona con el valor genera fricción: el cliente siente que paga por el hecho de usar, no por obtener. Las métricas habituales son el número de puestos (usuarios con acceso), el volumen de uso (llamadas, mensajes, gigabytes), los resultados (cobros procesados, correos entregados) y la capacidad (entornos, núcleos). Una buena métrica reúne cuatro propiedades: el cliente la entiende, crece cuando el cliente obtiene más valor, se puede medir con exactitud (`SE-413`) y se puede predecir (el cliente sabe más o menos cuánto pagará).

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Toma el plan de precios de un producto que uses y reconstruye su lógica: cuál es la métrica de valor, qué límites separan los planes, qué porcentaje de clientes crees que supera cada límite y qué haría el proveedor si ese porcentaje cambiara. ([SE-415](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-133](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md), [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Disposición a pagar](../d/disposicion-a-pagar.md), [Empaquetado](../e/empaquetado.md), [Excedente del cliente](../e/excedente-del-cliente.md), [Grandfathering](../g/grandfathering.md), [Meseta](./meseta.md), [Valla](../v/valla.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-415 — Precios, empaquetado y límites por plan](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Métrica contraria](./metrica-contraria.md) · [Métrica de vanidad →](./metrica-de-vanidad.md)
