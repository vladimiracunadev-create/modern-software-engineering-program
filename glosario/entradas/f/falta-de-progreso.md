# Falta de progreso

[↑ Glosario](../../README.md) · [← Falso verde](./falso-verde.md) · [Familias de ordenamiento →](./familias-de-ordenamiento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

Repetición del mismo resultado sin mejora observable.

Definición de trabajo de [SE-581 — Loops de agentes y criterios de parada](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md).

## Por qué importa

En [SE-581 — Loops de agentes y criterios de parada](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md), el tema «Falta de progreso» importa porque detecta el atasco mirando resultados, no vueltas.

## Cómo funciona

Según [SE-581 — Loops de agentes y criterios de parada](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md):

Un detector de falta de progreso mira si el resultado cambia. La señal más simple es repetir la misma observación (el mismo mensaje de error, la misma salida de las pruebas) varias veces seguidas. En el modelo se usa tres. No requiere entender la tarea y detecta el atasco típico del agente que reintenta lo mismo con variaciones superficiales. Sus fallos son dos: la falsa alarma (dos errores distintos con el mismo mensaje genérico) y la omisión (un agente que alterna entre dos errores y nunca repite el mismo tres veces). Se mejora con una señal más fina (por ejemplo, el conjunto de pruebas que fallan), siempre con un costo de diseño.

## Ejemplo

Ejemplo de [SE-581 — Loops de agentes y criterios de parada](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md) (sección «Ejemplo mínimo»):

El detector de falta de progreso en seis líneas:

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cuando se detecta la falta de progreso, la primera respuesta no es escalar sino forzar un cambio de enfoque: reiniciar el contexto de la subtarea, pedir un plan alternativo, volver a leer el código desde cero. ([SE-581](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md), [SE-580](../../../classes/part-48-harness-y-agentic-engineering/se-580-gestion-de-contexto-resets-y-handoffs/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Repetición](../r/repeticion.md), [Resultado](../r/resultado.md), [Cambio de plan](../c/cambio-de-plan.md), [Criterio de parada](../c/criterio-de-parada.md), [Escalada](../e/escalada.md), [Presupuesto](../p/presupuesto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-581 — Loops de agentes y criterios de parada](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-588](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md), [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Falso verde](./falso-verde.md) · [Familias de ordenamiento →](./familias-de-ordenamiento.md)
