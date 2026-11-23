# Multiplexación estadística

[↑ Glosario](../../README.md) · [← Multi-tenancy](./multi-tenancy.md) · [Mutabilidad →](./mutabilidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Ahorro de capacidad por promediar cargas independientes.

Definición de trabajo de [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md).

## Por qué importa

La clase donde se define, [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md), existe con este propósito: la clase existe para que puedas tratar el radio de impacto de un fallo como una propiedad que se diseña y se mide, no como un resultado de la suerte.

## Cómo funciona

Según [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md):

Una flota compartida absorbe los picos de unos inquilinos con los valles de otros, porque la carga agregada es más estable que la individual. Una celda solo tiene la carga de sus inquilinos y debe dimensionarse para su propio pico. En la simulación, con 1 000 inquilinos cuya carga por minuto es lognormal (semilla 44, 1 000 minutos), cubrir el percentil 99 de la carga total exigió 1 824 unidades en una flota compartida y 2 184 sumando los percentiles 99 de ocho celdas: un 19,8 % más. Esa es la pérdida de multiplexación estadística. Además, cada celda necesita su redundancia mínima (al menos dos instancias de cada cosa), y el costo operativo se multiplica por el número de celdas: ocho copias que desplegar, monitorear y actualizar.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md)) son: Los inquilinos, la carga y el comportamiento del venenoso son construcciones del autor, y el 100 % de la flota compartida es un supuesto de peor caso. No se midió ningún sistema celular ni el costo operativo de mantener ocho copias.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Celda](../c/celda.md), [Enrutador](../e/enrutador.md), [Enrutador de celdas](../e/enrutador-de-celdas.md), [Fragmentación aleatoria](../f/fragmentacion-aleatoria.md), [Hash por encuentro](../h/hash-por-encuentro.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Multi-tenancy](./multi-tenancy.md) · [Mutabilidad →](./mutabilidad.md)
