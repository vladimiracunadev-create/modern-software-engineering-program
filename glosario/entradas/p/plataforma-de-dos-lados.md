# Plataforma de dos lados

[↑ Glosario](../../README.md) · [← Plataforma de datos gobernada](./plataforma-de-datos-gobernada.md) · [Plataforma de ejecución aislada →](./plataforma-de-ejecucion-aislada.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Producto que conecta a dos grupos que se necesitan entre sí y cuyo valor para cada uno depende del tamaño del otro.

Definición de trabajo de [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md).

## Por qué importa

La clase donde se define, [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md), existe con este propósito: la clase existe para que entiendas qué cambia cuando un producto deja de servir a un tipo de cliente y pasa a conectar a dos o más tipos que se necesitan entre sí: compradores y vendedores, huéspedes y anfitriones, quienes piden un viaje y quienes lo ofrecen.

## Cómo funciona

Según [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md):

En un producto SaaS clásico, un cliente adicional no mejora el servicio para los demás (salvo por la economía de escala). En una plataforma de dos lados, cada comprador adicional mejora el servicio para los vendedores y cada vendedor adicional para los compradores. Ese efecto es la razón de ser de la plataforma y su mayor riesgo: sin masa en un lado no hay valor en el otro. Hay plataformas de más de dos lados (Uber conecta a quien pide, a quien conduce y, en el reparto, a los comercios) y la misma lógica se aplica con más relaciones cruzadas. Cada lado tiene sus propios incentivos, su propio costo de entrar y su propia sensibilidad al precio.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md):

*Escenario ilustrativo: las cifras y los resultados de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md)) son: Se simuló la liquidez con semilla 34 y se calculó el reparto con porcentajes del autor; no se midió ningún mercado, no se modelaron efectos de red completos ni precios, y el flujo del dinero es un diseño sin dinero real. Las obligaciones regulatorias dependen de cada jurisdicción y no se resuelven aquí.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-133](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md), [SE-294](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-415](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Producto](./producto.md), [Valor](../v/valor.md), [Arranque en frío](../a/arranque-en-frio.md), [Comisión](../c/comision.md), [Custodia](../c/custodia.md), [Desintermediación](../d/desintermediacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Plataforma de datos gobernada](./plataforma-de-datos-gobernada.md) · [Plataforma de ejecución aislada →](./plataforma-de-ejecucion-aislada.md)
