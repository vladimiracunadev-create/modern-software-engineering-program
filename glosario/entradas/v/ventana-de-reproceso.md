# Ventana de reproceso

[↑ Glosario](../../README.md) · [← Ventana de gracia](./ventana-de-gracia.md) · [Ventana de retención →](./ventana-de-retencion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Número de días anteriores que se vuelven a calcular en cada ejecución.

Definición de trabajo de [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md).

## Por qué importa

En [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md), el tema «Datos tardíos» importa porque la ventana de reproceso los recoge a un costo.

## Cómo funciona

[SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: consulta la clase para el mecanismo completo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md)) son: Las particiones, el fallo y los retrasos son construcciones del autor; no se ejecutó ningún orquestador ni se midió una carga con millones de filas, y el tiempo de reemplazar una partición grande no se midió. El resultado «reemplazar y fusionar son idempotentes» vale con transacción o con una clave bien definida, y se comprobó solo para esos casos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-363](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md), [SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Backfill](../b/backfill.md), [Dato tardío](../d/dato-tardio.md), [Determinismo](../d/determinismo.md), [Fusión por clave](../f/fusion-por-clave.md), [Idempotencia](../i/idempotencia.md), [Orden topológico](../o/orden-topologico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-370](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md), [SE-371](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Ventana de gracia](./ventana-de-gracia.md) · [Ventana de retención →](./ventana-de-retencion.md)
