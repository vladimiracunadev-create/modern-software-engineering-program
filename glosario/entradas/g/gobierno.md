# Gobierno

[↑ Glosario](../../README.md) · [← Gobernanza federada y computacional](./gobernanza-federada-y-computacional.md) · [Graduador →](./graduador.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

Conjunto de decisiones sobre quién aprueba qué y con qué evidencia.

Definición de trabajo de [SE-586 — AI-DLC, gobierno y vibe coding frente a agentic engineering](../../../classes/part-48-harness-y-agentic-engineering/se-586-ai-dlc-gobierno-y-vibe-coding-frente-a-agentic-engineering/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md): Conjunto de controles (enrutamiento, permisos, diario, trazas, evaluación, degradación) que rodean a la calidad.

## Por qué importa

La clase donde se define, [SE-586 — AI-DLC, gobierno y vibe coding frente a agentic engineering](../../../classes/part-48-harness-y-agentic-engineering/se-586-ai-dlc-gobierno-y-vibe-coding-frente-a-agentic-engineering/README.md), existe con este propósito: la clase existe para que puedas explicar a una organización qué significa trabajar con agentes *con gobierno* y qué lo separa del *vibe coding*.

## Cómo funciona

Según [SE-586 — AI-DLC, gobierno y vibe coding frente a agentic engineering](../../../classes/part-48-harness-y-agentic-engineering/se-586-ai-dlc-gobierno-y-vibe-coding-frente-a-agentic-engineering/README.md):

AWS publicó AI-DLC (AI-Driven Development Life Cycle) como un flujo que parte de una intención del desarrollador y organiza el trabajo en tres fases (Inception, Construction y Operations), con la profundidad de cada etapa adaptada al problema, aprobaciones humanas en los puntos de decisión y trazabilidad de artefactos, decisiones y conversaciones. Es un ejemplo de un flujo con control proporcional y registro de decisiones. La fuente es una publicación del proveedor que presenta el diseño y no mide su efecto en productividad ni en calidad; se estudia como forma de organizar el gobierno, no como evidencia de que funcione.

Según [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md):

La tabla de la puerta cuenta una historia que ninguna columna aislada cuenta. El **agente solo** tiene 97,5 % de calidad (pasa), pero gasta 1 862 tokens (excede los 1 500), tiene un 19,23 % de ataques exitosos (excede el 0,5 %) y un envío duplicado tras la caída: **no pasa**. El **workflow solo** gasta 774 tokens y responde en unos 6 s, pero su calidad es 85,0 % porque escala las incidencias: **no pasa**. El **híbrido sin gobierno** tiene la mejor calidad (99,0 %) y gasta 1 421 tokens, pero hereda el 19,23 % de ataques y los envíos duplicados: **no pasa**.

## Ejemplo

Ejemplo de [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md) (sección «Preguntas frecuentes»):

Al menos dos, que difieran en la decisión más importante (agente frente a workflow, con o sin gobierno). Medir uno no deja ver qué aporta cada pieza.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La fuente es una publicación del proveedor que presenta el diseño y no mide su efecto en productividad ni en calidad; se estudia como forma de organizar el gobierno, no como evidencia de que funcione. ([SE-586](../../../classes/part-48-harness-y-agentic-engineering/se-586-ai-dlc-gobierno-y-vibe-coding-frente-a-agentic-engineering/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Traza](../t/traza.md), [Traza](../t/traza.md).
- **Ver también:** [Conjunto](../c/conjunto.md), [Degradación](../d/degradacion.md), [Evaluación](../e/evaluacion.md), [Evidencia](../e/evidencia.md), [Agentic engineering](../a/agentic-engineering.md), [Aprobación humana](../a/aprobacion-humana.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-586 — AI-DLC, gobierno y vibe coding frente a agentic engineering](../../../classes/part-48-harness-y-agentic-engineering/se-586-ai-dlc-gobierno-y-vibe-coding-frente-a-agentic-engineering/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.
- [SE-600 — Proyecto: sistema con LLM evaluado y operable](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (23 clases más lo mencionan; las que más):

[SE-610](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md), [SE-200](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md), [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md), [SE-369](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md), [SE-609](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-609-seguridad-y-robustez-de-sistemas-de-ml/README.md), [SE-372](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md), [SE-343](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [Airbnb](../../../casos/exito/airbnb.md), [Knight Capital](../../../casos/fallo/knight-capital.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [TSB Bank](../../../casos/fallo/tsb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Gobernanza federada y computacional](./gobernanza-federada-y-computacional.md) · [Graduador →](./graduador.md)
