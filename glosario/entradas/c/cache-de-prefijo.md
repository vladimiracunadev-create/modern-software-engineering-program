# Caché de prefijo

[↑ Glosario](../../README.md) · [← CAC (costo de adquisición de cliente)](./cac-costo-de-adquisicion-de-cliente.md) · [Cache hit/miss →](./cache-hit-miss.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Reutilización del procesamiento de un prefijo estable del prompt entre llamadas.

Definición de trabajo de [SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md).

## Por qué importa

En [SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md), el tema «Caché de prefijo» importa porque ahorra con prefijos estables y bucles largos, y cuesta de más al escribir.

## Cómo funciona

[SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: consulta la clase para el mecanismo completo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md)) son: Las unidades de costo son supuestos y no precios; la latencia es una distribución sintética; las probabilidades de obediencia, de éxito del atacante y de fatiga humana son supuestos del autor; no se atacó ningún modelo real ni se midió ningún proveedor. El siguiente paso, `SE-599`, es un taller: elegir un patrón agéntico para tareas distintas y degradarlo con un interruptor cuando el proveedor falla.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-597](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Prefijo](../p/prefijo.md), [Cola larga](./cola-larga.md), [Inyección de prompt](../i/inyeccion-de-prompt.md), [Percentil 95](../p/percentil-95.md), [Presupuesto](../p/presupuesto.md), [Regla de las tres condiciones](../r/regla-de-las-tres-condiciones.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← CAC (costo de adquisición de cliente)](./cac-costo-de-adquisicion-de-cliente.md) · [Cache hit/miss →](./cache-hit-miss.md)
