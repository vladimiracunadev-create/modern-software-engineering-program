# Abstención

[↑ Glosario](../../README.md) · [← Abreviatura de flag](./abreviatura-de-flag.md) · [Abstracción →](./abstraccion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Decisión de no responder porque la evidencia recuperada no alcanza un umbral.

Definición de trabajo de [SE-594 — Embeddings, recuperación y agentic RAG](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md).

## Por qué importa

En [SE-594 — Embeddings, recuperación y agentic RAG](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md), el tema «Abstención» importa porque evita responder con algo irrelevante.

## Cómo funciona

Según [SE-594 — Embeddings, recuperación y agentic RAG](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md):

**Diagnóstico paso a paso.** (1) Se revisa la consulta: no está en el corpus. (2) Se ve que el recuperador devolvió el fragmento más parecido con una puntuación baja. (3) Se comprueba que no había umbral de abstención. (4) Se identifica que la cita era correcta como origen pero no respaldaba la afirmación.

Según [SE-594 — Embeddings, recuperación y agentic RAG](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md):

Reúne 20 preguntas reales de tu sistema y el documento que las responde. Fragmenta tu corpus, mide BM25 y, si lo tienes, un modelo de embeddings, y decide la política: recuperador, número de fragmentos, umbral de abstención, citas. Registra cuántas consultas válidas pierdes por el umbral y cuántas ajenas se cuelan.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-594 — Embeddings, recuperación y agentic RAG](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- (3) Se comprueba que no había umbral de abstención. ([SE-594](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-593](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evidencia](../e/evidencia.md), [Acierto@k](./acierto-k.md), [BM25](../b/bm25.md), [Embedding](../e/embedding.md), [Fragmentación](../f/fragmentacion.md), [Fragmento](../f/fragmento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-594 — Embeddings, recuperación y agentic RAG](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-520](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-520-dependencias-obsoletas-y-riesgo-acumulado/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Abreviatura de flag](./abreviatura-de-flag.md) · [Abstracción →](./abstraccion.md)
