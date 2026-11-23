# LPT

[↑ Glosario](../../README.md) · [← Low-code](./low-code.md) · [LRU →](./lru.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Regla voraz de reparto que asigna primero las tareas más grandes.

Definición de trabajo de [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md).

## Por qué importa

La clase donde se define, [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md), existe con este propósito: la clase existe para que sepas cuándo un sistema necesita que un componente **decida en tiempo de ejecución cómo dividir el trabajo** (orquestador-trabajadores) y cuándo la calidad se consigue **iterando contra un criterio** (evaluador-optimizador).

## Cómo funciona

Según [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md):

El tiempo de reloj de un reparto entre *k* trabajadores es la carga del más cargado. Un reparto fijo («el curso *i* va al trabajador *i* mod 3») ignora los tamaños. Un orquestador que conoce o estima los tamaños puede aplicar la regla voraz «asigna el trabajo más grande aún sin asignar al trabajador menos cargado» (la heurística LPT). En 500 repasos simulados de cursos de tamaño parecido, un solo agente tarda 57,2 unidades, el reparto fijo entre tres 23,1 y el orquestador 20,8. Con cursos de cola larga, 155,4, 87,1 y 68,5. La ventaja del orquestador sobre el reparto fijo crece del 10 % al 21 % con el desequilibrio. Cuando todo es parecido, la ganancia es pequeña y no compensa las dos llamadas de coordinación.

Según [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md):

Toma una tarea de tu sistema que se reparta entre varias partes y mide, con datos reales o una muestra, la variabilidad del tamaño de las partes. Calcula el tiempo con reparto fijo y con LPT. Para un artefacto que generes (un correo, un informe, un fragmento de código), escribe un verificador de al menos tres restricciones y mide cuántos borradores del generador lo pasan sin revisión.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un orquestador que conoce o estima los tamaños puede aplicar la regla voraz «asigna el trabajo más grande aún sin asignar al trabajador menos cargado» (la heurística LPT). ([SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md), [SE-590](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Regla](../r/regla.md), [Tarea](../t/tarea.md), [Evaluador](../e/evaluador.md), [Orquestador](../o/orquestador.md), [Síntesis](../s/sintesis.md), [Tope de vueltas](../t/tope-de-vueltas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Low-code](./low-code.md) · [LRU →](./lru.md)
