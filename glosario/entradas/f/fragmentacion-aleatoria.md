# Fragmentación aleatoria

[↑ Glosario](../../README.md) · [← Fragmentación](./fragmentacion.md) · [Fragmento →](./fragmento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Asignar a cada cliente un subconjunto aleatorio de recursos.

Definición de trabajo de [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md).

## Por qué importa

En [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md), el tema «Fragmentación aleatoria» importa porque reduce el radio sin particionar por completo.

## Cómo funciona

Según [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md):

Tras el incidente del martes, el equipo de *Avisos* calcula el radio de impacto de cada opción. Con ocho celdas, el 12,5 %; con fragmentación aleatoria sobre la flota existente, un 3,6 % caído del todo con un venenoso. El equipo descarta empezar con celdas completas porque el costo de capacidad del 20 % y la operación de ocho copias superan lo que puede asumir este año, y elige un camino por etapas: primero un tope de reintentos por inquilino y un cortacircuitos (para que el cliente que reintenta no tumbe trabajadores), después fragmentación aleatoria de dos trabajadores de ocho para los envíos, y celdas solo para el cliente más grande, que se aísla en una celda propia.

## Ejemplo

Ejemplo de [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md) (sección «Ejemplo profesional»):

Tras el incidente del martes, el equipo de *Avisos* calcula el radio de impacto de cada opción. Con ocho celdas, el 12,5 %; con fragmentación aleatoria sobre la flota existente, un 3,6 % caído del todo con un venenoso.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md)) son: Los inquilinos, la carga y el comportamiento del venenoso son construcciones del autor, y el 100 % de la flota compartida es un supuesto de peor caso. No se midió ningún sistema celular ni el costo operativo de mantener ocho copias.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Recurso](../r/recurso.md), [Celda](../c/celda.md), [Enrutador](../e/enrutador.md), [Enrutador de celdas](../e/enrutador-de-celdas.md), [Hash por encuentro](../h/hash-por-encuentro.md), [Inquilino venenoso](../i/inquilino-venenoso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «shuffle sharding».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Fragmentación](./fragmentacion.md) · [Fragmento →](./fragmento.md)
