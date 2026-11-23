# Hash por encuentro

[↑ Glosario](../../README.md) · [← Hash consistente](./hash-consistente.md) · [Hashable →](./hashable.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Función de asignación que elige el elemento de mayor puntaje por clave y elemento.

Definición de trabajo de [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md).

## Por qué importa

La clase donde se define, [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md), existe con este propósito: la clase existe para que puedas tratar el radio de impacto de un fallo como una propiedad que se diseña y se mide, no como un resultado de la suerte.

## Cómo funciona

Según [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md):

El enrutador necesita una función que, dado un inquilino, devuelva su celda y que sea estable. La opción ingenua es el módulo: la celda es el hash del inquilino módulo el número de celdas. Funciona hasta que se añade una celda. Con 100 000 inquilinos y el paso de 8 a 9 celdas, el módulo reubicó 88 985, el 89,0 %: casi todos cambian de celda, y cada cambio es una migración de datos. El hash por encuentro (rendezvous) calcula para cada inquilino un puntaje con cada celda y elige la de mayor puntaje; al añadir una celda nueva, solo se mueven los inquilinos para los que la nueva obtiene el puntaje más alto: 11 176, el 11,2 %, cercano al mínimo teórico de un noveno (11,1 %).

Según [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md):

Tras el incidente del martes, el equipo de *Avisos* calcula el radio de impacto de cada opción. Con ocho celdas, el 12,5 %; con fragmentación aleatoria sobre la flota existente, un 3,6 % caído del todo con un venenoso. El equipo descarta empezar con celdas completas porque el costo de capacidad del 20 % y la operación de ocho copias superan lo que puede asumir este año, y elige un camino por etapas: primero un tope de reintentos por inquilino y un cortacircuitos (para que el cliente que reintenta no tumbe trabajadores), después fragmentación aleatoria de dos trabajadores de ocho para los envíos, y celdas solo para el cliente más grande, que se aísla en una celda propia.

## Ejemplo

Ejemplo de [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md) (sección «Ejemplo mínimo»):

La asignación por hash por encuentro en seis líneas:

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El hash por encuentro (rendezvous) calcula para cada inquilino un puntaje con cada celda y elige la de mayor puntaje; al añadir una celda nueva, solo se mueven los inquilinos para los que la nueva obtiene el puntaje más alto: 11 176, el 11,2 %, cercano al mínimo teórico de un noveno (11,1 %). ([SE-344](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Función](../f/funcion.md), [Celda](../c/celda.md), [Enrutador](../e/enrutador.md), [Enrutador de celdas](../e/enrutador-de-celdas.md), [Fragmentación aleatoria](../f/fragmentacion-aleatoria.md), [Inquilino venenoso](../i/inquilino-venenoso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «rendezvous».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Hash consistente](./hash-consistente.md) · [Hashable →](./hashable.md)
