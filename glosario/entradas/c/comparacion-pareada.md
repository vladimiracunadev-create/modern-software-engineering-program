# Comparación pareada

[↑ Glosario](../../README.md) · [← Comparación en sombra](./comparacion-en-sombra.md) · [Compatibilidad entre versiones →](./compatibilidad-entre-versiones.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Comparación de dos versiones sobre los mismos casos.

Definición de trabajo de [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-603 — Experimentos y entrenamiento reproducible](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md): Comparación de dos configuraciones sobre los mismos datos y las mismas particiones.

## Por qué importa

En [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md), el tema «Comparación pareada» importa porque reduce la varianza al usar los mismos casos.

En [SE-603 — Experimentos y entrenamiento reproducible](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md), el tema «Comparación pareada» importa porque reduce el ruido de la comparación.

## Cómo funciona

Según [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md):

Comparar dos versiones sobre los mismos casos es una comparación **pareada**: interesan los casos donde las versiones discrepan. Sea *b* el número de casos que v2 acierta y v1 falla, y *c* el de los que v1 acierta y v2 falla; el estadístico z de McNemar, (b − c) / √(b + c), mide cuánto se aparta de cero esa diferencia. Si se exige z > 1,645 (una cola, 5 %), la tasa de **falsos positivos** (declarar mejor una versión idéntica) queda cerca del 5 %: en el experimento, 5,6 %, 5,1 %, 4,8 % y 6,8 % con 50, 100, 400 y 1 600 casos. La **potencia** (detectar una mejora real de unos 4 puntos) es otra cosa: 10,1 %, 15,2 %, 37,2 % y 81,8 %.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md)) son: Los sistemas, la dificultad por caso, el sesgo del juez y la traza son sintéticos; la puerta usa una prueba z de McNemar de una cola con 800 evaluaciones por celda; no se evaluó ningún modelo real ni ninguna herramienta de evaluación. El siguiente paso, `SE-598`, trata las tres restricciones que decide un sistema en operación: cuánto cuesta, cuánto tarda y cómo se protege.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-596](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Partición](../p/particion.md), [Sobre](../s/sobre.md), [Versión](../v/version.md), [Calificador](./calificador.md), [Corrida](./corrida.md), [Dispersión](../d/dispersion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.
- [SE-603 — Experimentos y entrenamiento reproducible](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-563](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md), [SE-585](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md), [SE-605](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Lee et al., «Deduplicating training data makes language models better»](https://arxiv.org/abs/2107.06499) — duplicados en los datos de entrenamiento y memorización; autoridad: artículo de investigación (arXiv).
- [Kirkpatrick et al., «Overcoming catastrophic forgetting in neural networks»](https://arxiv.org/abs/1612.00796) — pérdida de capacidades previas al entrenar en una tarea nueva; autoridad: artículo de investigación (arXiv).

---

[↑ Glosario](../../README.md) · [← Comparación en sombra](./comparacion-en-sombra.md) · [Compatibilidad entre versiones →](./compatibilidad-entre-versiones.md)
