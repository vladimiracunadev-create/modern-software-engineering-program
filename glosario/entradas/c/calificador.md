# Calificador

[↑ Glosario](../../README.md) · [← Calificación de herramienta](./calificacion-de-herramienta.md) · [Callbacks, promesas y corrutinas →](./callbacks-promesas-y-corrutinas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Componente que decide si una respuesta es correcta: código, persona o modelo.

Definición de trabajo de [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md).

## Por qué importa

La clase donde se define, [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md), existe con este propósito: la clase existe para que **midas** un sistema con LLM con el mismo rigor con que mides cualquier otro componente que decide cosas: con un conjunto de casos, un criterio de calificación, una comparación entre versiones que tenga en cuenta el ruido y una puerta que decida si una versión sale.

## Cómo funciona

Según [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md):

Lo que una evaluación mide es lo que sus casos cubren. Un conjunto útil mezcla casos reales (tomados de solicitudes de usuarios, anonimizadas), casos difíciles (los que fallaron antes, los límites, las ambigüedades) y casos adversariales (intentos de inyección, entradas vacías, texto en otro idioma). Cada caso tiene una **señal de calificación**: código cuando el resultado es verificable (la fecha coincide con la tabla), una persona cuando requiere criterio, un juez basado en modelo cuando el volumen lo exige y se ha calibrado. La documentación de Anthropic sobre evaluaciones de agentes distingue justo esos tres tipos de calificador y subraya que el comportamiento no determinista exige repetir. Un conjunto sin dueño ni fecha se pudre: los casos nuevos entran desde los fallos de producción.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La documentación de Anthropic sobre evaluaciones de agentes distingue justo esos tres tipos de calificador y subraya que el comportamiento no determinista exige repetir. ([SE-597](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-596](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](./componente.md), [Modelo](../m/modelo.md), [Comparación pareada](./comparacion-pareada.md), [Evaluación](../e/evaluacion.md), [Falso positivo de la puerta](../f/falso-positivo-de-la-puerta.md), [Potencia](../p/potencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md), [SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md), [SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md), [SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md), [SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md), [SE-383](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Lee et al., «Deduplicating training data makes language models better»](https://arxiv.org/abs/2107.06499) — duplicados en los datos de entrenamiento y memorización; autoridad: artículo de investigación (arXiv).
- [Kirkpatrick et al., «Overcoming catastrophic forgetting in neural networks»](https://arxiv.org/abs/1612.00796) — pérdida de capacidades previas al entrenar en una tarea nueva; autoridad: artículo de investigación (arXiv).

---

[↑ Glosario](../../README.md) · [← Calificación de herramienta](./calificacion-de-herramienta.md) · [Callbacks, promesas y corrutinas →](./callbacks-promesas-y-corrutinas.md)
