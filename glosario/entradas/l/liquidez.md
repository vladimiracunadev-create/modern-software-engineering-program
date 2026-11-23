# Liquidez

[↑ Glosario](../../README.md) · [← Liquidación](./liquidacion.md) · [Lista blanca →](./lista-blanca.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Proporción de intentos (búsquedas, ofertas) que terminan en una transacción.

Definición de trabajo de [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md).

## Por qué importa

En [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md), el tema «Liquidez» importa porque mide si el mercado funciona, más que el número de usuarios.

## Cómo funciona

Según [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md):

El número de usuarios registrados dice poco; lo que importa es la proporción de búsquedas que terminan en una transacción, el tiempo hasta la primera venta de un vendedor nuevo y la tasa de recompra. En el modelo de la clase, un comprador tiene probabilidad de 4 % de encontrar en cada vendedor algo que le sirva. La probabilidad de encontrar al menos una oferta con n vendedores es 1 − 0,96ⁿ, y las simulaciones dan **18,4 % con 5 vendedores, 57,0 % con 20, 95,6 % con 80 y 100 % con 320**. La relación no es lineal: de 5 a 20 vendedores la liquidez triplica y de 80 a 320 casi no cambia.

Según [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md):

El equipo de *Tablero* decide que el lado difícil de «Plantillas» es la oferta y diseña el lanzamiento alrededor de eso. Elige una sola categoría («planes de proyecto para pequeñas empresas»), contrata a veinte autores con una garantía mínima de ingresos durante tres meses, publica sus propias treinta plantillas de base y define la métrica de liquidez: porcentaje de búsquedas con al menos un resultado comprado en siete días. Mide cada semana; solo abre una segunda categoría cuando la primera supera el 40 %.

## Ejemplo

Ejemplo de [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md) (sección «Ejemplo profesional»):

El equipo de *Tablero* decide que el lado difícil de «Plantillas» es la oferta y diseña el lanzamiento alrededor de eso. Elige una sola categoría («planes de proyecto para pequeñas empresas»), contrata a veinte autores con una garantía mínima de ingresos durante tres meses, publica sus propias treinta plantillas de base y define la métrica de liquidez: porcentaje de búsquedas con al menos un resultado comprado en siete días. Mide cada semana; solo abre una segunda categoría cuando la primera supera el 40 %.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La relación no es lineal: de 5 a 20 vendedores la liquidez triplica y de 80 a 320 casi no cambia. ([SE-416](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-133](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md), [SE-294](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-415](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Transacción](../t/transaccion.md), [Arranque en frío](../a/arranque-en-frio.md), [Comisión](../c/comision.md), [Custodia](../c/custodia.md), [Desintermediación](../d/desintermediacion.md), [Efecto de red cruzado](../e/efecto-de-red-cruzado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-416 — Marketplaces y plataformas de dos lados](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Liquidación](./liquidacion.md) · [Lista blanca →](./lista-blanca.md)
