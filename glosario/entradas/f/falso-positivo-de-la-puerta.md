# Falso positivo de la puerta

[↑ Glosario](../../README.md) · [← Falso positivo](./falso-positivo.md) · [Falso rechazo →](./falso-rechazo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Declarar mejor una versión que no lo es.

Definición de trabajo de [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md).

## Por qué importa

En [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md), el tema «Falsos positivos de la puerta» importa porque se publica una versión que no mejora.

## Cómo funciona

[SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md)) son: Los sistemas, la dificultad por caso, el sesgo del juez y la traza son sintéticos; la puerta usa una prueba z de McNemar de una cola con 800 evaluaciones por celda; no se evaluó ningún modelo real ni ninguna herramienta de evaluación. El siguiente paso, `SE-598`, trata las tres restricciones que decide un sistema en operación: cuánto cuesta, cuánto tarda y cómo se protege.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-596](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Versión](../v/version.md), [Calificador](../c/calificador.md), [Comparación pareada](../c/comparacion-pareada.md), [Evaluación](../e/evaluacion.md), [Potencia](../p/potencia.md), [Sesgo de posición](../s/sesgo-de-posicion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Lee et al., «Deduplicating training data makes language models better»](https://arxiv.org/abs/2107.06499) — duplicados en los datos de entrenamiento y memorización; autoridad: artículo de investigación (arXiv).
- [Kirkpatrick et al., «Overcoming catastrophic forgetting in neural networks»](https://arxiv.org/abs/1612.00796) — pérdida de capacidades previas al entrenar en una tarea nueva; autoridad: artículo de investigación (arXiv).

---

[↑ Glosario](../../README.md) · [← Falso positivo](./falso-positivo.md) · [Falso rechazo →](./falso-rechazo.md)
