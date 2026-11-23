# Solicitud de cobertura

[↑ Glosario](../../README.md) · [← Solicitud de cambio](./solicitud-de-cambio.md) · [Solo lectura →](./solo-lectura.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Copia de una llamada lenta cuya primera respuesta se usa.

Definición de trabajo de [SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md).

## Por qué importa

La clase donde se define, [SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md), existe con este propósito: la clase existe para que trates **costo, latencia y seguridad** de un sistema con LLM como restricciones de diseño que se calculan y se miden, no como propiedades que aparecen sueltas al final.

## Cómo funciona

Según [SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md):

Paralelizar reduce la mediana (cinco llamadas simultáneas toman la más lenta en lugar de la suma) pero **hereda la cola**: la mediana del máximo de cinco es 2,36 s y su p95, 4,76 s, ambos mayores que los de una sola llamada. Dean y Barroso explican que, cuanto más componentes participan en una respuesta, más probable es que alguno sea lento. Una técnica es la **solicitud de cobertura**: enviar una copia de una llamada lenta y usar la primera respuesta. En la simulación, enviar dos copias reduce el p99 de una llamada de 4,89 s a 2,61 s, a costa de duplicar las llamadas en ese tramo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md)) son: Las unidades de costo son supuestos y no precios; la latencia es una distribución sintética; las probabilidades de obediencia, de éxito del atacante y de fatiga humana son supuestos del autor; no se atacó ningún modelo real ni se midió ningún proveedor. El siguiente paso, `SE-599`, es un taller: elegir un patrón agéntico para tareas distintas y degradarlo con un interruptor cuando el proveedor falla.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-597](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Caché de prefijo](../c/cache-de-prefijo.md), [Cola larga](../c/cola-larga.md), [Inyección de prompt](../i/inyeccion-de-prompt.md), [Percentil 95](../p/percentil-95.md), [Presupuesto](../p/presupuesto.md), [Regla de las tres condiciones](../r/regla-de-las-tres-condiciones.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Solicitud de cambio](./solicitud-de-cambio.md) · [Solo lectura →](./solo-lectura.md)
