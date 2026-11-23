# Patrón de traza

[↑ Glosario](../../README.md) · [← Patrón de diseño](./patron-de-diseno.md) · [Patrón oscuro →](./patron-oscuro.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

Forma característica que un fallo deja en el registro.

Definición de trabajo de [SE-587 — Taller: diagnosticar el fallo de un harness](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md).

## Por qué importa

En [SE-587 — Taller: diagnosticar el fallo de un harness](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md), el tema «Patrón de traza por fallo» importa porque convierte síntomas en hipótesis.

## Cómo funciona

Según [SE-587 — Taller: diagnosticar el fallo de un harness](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md):

Toma tres fallos reales de tu agente de los últimos meses y escribe, para cada uno, el patrón de traza que dejó, el campo que le habría ayudado a diagnosticarlo y la tarea de regresión que lo cubriría. Si no puedes escribir el patrón porque no hay traza, el primer arreglo es el registro.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-587 — Taller: diagnosticar el fallo de un harness](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-587 — Taller: diagnosticar el fallo de un harness](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md)) son: Se inyectaron seis fallos del autor en un harness mínimo con política guionizada y se diagnosticaron 30 ejecuciones, en Windows 11 con CPython 3.12.9. El 30 de 30 es un resultado sobre un conjunto cerrado, conocido por quien escribió el diagnosticador. No se diagnosticó ningún fallo real ni se midió el diagnóstico de una persona. El siguiente paso, `SE-588`, construye el harness mínimo gobernado y lo evalúa contra escenarios adversos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md), [SE-586](../../../classes/part-48-harness-y-agentic-engineering/se-586-ai-dlc-gobierno-y-vibe-coding-frente-a-agentic-engineering/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Característica](../c/caracteristica.md), [Registro](../r/registro.md), [Fallo inyectado](../f/fallo-inyectado.md), [Hipótesis refutable](../h/hipotesis-refutable.md), [Matriz de confusión](../m/matriz-de-confusion.md), [Regresión](../r/regresion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-587 — Taller: diagnosticar el fallo de un harness](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Patrón de diseño](./patron-de-diseno.md) · [Patrón oscuro →](./patron-oscuro.md)
