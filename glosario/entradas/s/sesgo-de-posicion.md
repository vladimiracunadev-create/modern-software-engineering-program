# Sesgo de posición

[↑ Glosario](../../README.md) · [← Sesgo de participación](./sesgo-de-participacion.md) · [Sesgo de retrospectiva →](./sesgo-de-retrospectiva.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Tendencia de un juez a preferir una respuesta por el orden en que aparece.

Definición de trabajo de [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md).

## Por qué importa

La clase donde se define, [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md), existe con este propósito: la clase existe para que **midas** un sistema con LLM con el mismo rigor con que mides cualquier otro componente que decide cosas: con un conjunto de casos, un criterio de calificación, una comparación entre versiones que tenga en cuenta el ruido y una puerta que decida si una versión sale.

## Cómo funciona

Según [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md):

Usar un modelo como calificador permite evaluar a escala lo que el código no puede (tono, claridad, utilidad). Pero un juez tiene sesgos documentados: prefiere la respuesta que aparece primera, o la más larga, o la que se parece a las suyas. En el experimento, un juez con sesgo de posición de 0,65 elige la primera respuesta el 65,5 % de las veces **aunque sean iguales**, y cuando se le presenta cada par en los dos órdenes, el 54,8 % de las veces su veredicto se **contradice** (dice «A» en un orden y «B» en el otro). La práctica estándar es evaluar en ambos órdenes y contar como empate los desacuerdos.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md)) son: Los sistemas, la dificultad por caso, el sesgo del juez y la traza son sintéticos; la puerta usa una prueba z de McNemar de una cola con 800 evaluaciones por celda; no se evaluó ningún modelo real ni ninguna herramienta de evaluación. El siguiente paso, `SE-598`, trata las tres restricciones que decide un sistema en operación: cuánto cuesta, cuánto tarda y cómo se protege.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-596](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Calificador](../c/calificador.md), [Comparación pareada](../c/comparacion-pareada.md), [Evaluación](../e/evaluacion.md), [Falso positivo de la puerta](../f/falso-positivo-de-la-puerta.md), [Potencia](../p/potencia.md), [Traza](../t/traza.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md), [SE-590](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md).

**Aparece en los casos de estudio:** [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Lee et al., «Deduplicating training data makes language models better»](https://arxiv.org/abs/2107.06499) — duplicados en los datos de entrenamiento y memorización; autoridad: artículo de investigación (arXiv).
- [Kirkpatrick et al., «Overcoming catastrophic forgetting in neural networks»](https://arxiv.org/abs/1612.00796) — pérdida de capacidades previas al entrenar en una tarea nueva; autoridad: artículo de investigación (arXiv).

---

[↑ Glosario](../../README.md) · [← Sesgo de participación](./sesgo-de-participacion.md) · [Sesgo de retrospectiva →](./sesgo-de-retrospectiva.md)
