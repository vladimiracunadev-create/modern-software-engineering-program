# Tope de vueltas

[↑ Glosario](../../README.md) · [← Tope de solicitudes en curso](./tope-de-solicitudes-en-curso.md) · [Tópico →](./topico.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Número máximo de iteraciones del bucle de revisión.

Definición de trabajo de [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md).

## Por qué importa

La clase donde se define, [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md), existe con este propósito: la clase existe para que sepas cuándo un sistema necesita que un componente **decida en tiempo de ejecución cómo dividir el trabajo** (orquestador-trabajadores) y cuándo la calidad se consigue **iterando contra un criterio** (evaluador-optimizador).

## Cómo funciona

Según [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md):

Un bucle de revisión necesita una condición de parada que no dependa de que el modelo se declare satisfecho: pasa el verificador, o se llega al tope de vueltas (aquí 3), o el costo acumulado supera el presupuesto. Al agotarse sin pasar, la acción correcta es **escalar** con el último borrador y las fallas pendientes, no entregar el borrador. También conviene registrar qué restricción falla más a menudo: si es siempre la misma, el defecto está en el prompt del generador y no en la falta de iteraciones.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un bucle de revisión necesita una condición de parada que no dependa de que el modelo se declare satisfecho: pasa el verificador, o se llega al tope de vueltas (aquí 3), o el costo acumulado supera el presupuesto. ([SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md), [SE-590](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Revisión](../r/revision.md), [Evaluador](../e/evaluador.md), [LPT](../l/lpt.md), [Orquestador](../o/orquestador.md), [Síntesis](../s/sintesis.md), [Trabajador](./trabajador.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-592](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Tope de solicitudes en curso](./tope-de-solicitudes-en-curso.md) · [Tópico →](./topico.md)
