# RRF

[↑ Glosario](../../README.md) · [← RPO (objetivo de punto de recuperación)](./rpo-objetivo-de-punto-de-recuperacion.md) · [RTO →](./rto.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Fusión de listas ordenadas que suma 1/(k + posición) por lista.

Definición de trabajo de [SE-594 — Embeddings, recuperación y agentic RAG](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md).

## Por qué importa

La clase donde se define, [SE-594 — Embeddings, recuperación y agentic RAG](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md), existe con este propósito: la clase existe para que construyas la recuperación de información de un sistema con LLM **como un componente que se mide**, no como un paso de moda.

## Cómo funciona

Según [SE-594 — Embeddings, recuperación y agentic RAG](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md):

La tabla de resultados tiene una lección más sutil que «gana BM25». Con consultas exactas, BM25 (98,3 %) supera con mucho al vector de trigramas (65,0 %). Con erratas y raíces, BM25 cae a 75,0 % porque las palabras mal escritas no puntúan, pero el vector de trigramas no mejora (59,2 %) porque su señal global es más ruidosa. La **fusión por rango recíproco (RRF)** combina las dos listas: cada documento suma 1/(60 + posición) en cada lista. Con consultas exactas el híbrido (85,0 %) queda **por debajo** de BM25 solo (98,3 %) porque el recuperador débil arrastra; con erratas y raíces queda por encima (77,5 % frente a 75,0 %) y mejora el acierto entre los cinco primeros respecto del vector (90,0 % frente a 77,5 %).

Según [SE-594 — Embeddings, recuperación y agentic RAG](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md):

El equipo indexa los 300 documentos del programa, fragmentados por encabezado, con título y ruta como metadatos. Escribe 60 preguntas reales de docentes con el fragmento que las responde y mide BM25, un modelo de embeddings y su fusión. Elige BM25 más embeddings con RRF porque el híbrido gana en las preguntas con paráfrasis y no pierde en las exactas. Fija un umbral con las preguntas fuera del corpus que recogió de los registros, de modo que el sistema responda «no lo encontré» en el 80 % de ellas y acepte el 92 % de las válidas. La respuesta cita siempre los fragmentos usados con enlace, y una prueba rechaza respuestas con afirmaciones sin cita.

## Ejemplo

Ejemplo de [SE-594 — Embeddings, recuperación y agentic RAG](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md) (sección «Ejemplo profesional»):

El equipo indexa los 300 documentos del programa, fragmentados por encabezado, con título y ruta como metadatos. Escribe 60 preguntas reales de docentes con el fragmento que las responde y mide BM25, un modelo de embeddings y su fusión. Elige BM25 más embeddings con RRF porque el híbrido gana en las preguntas con paráfrasis y no pierde en las exactas. Fija un umbral con las preguntas fuera del corpus que recogió de los registros, de modo que el sistema responda «no lo encontré» en el 80 % de ellas y acepte el 92 % de las válidas.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-594 — Embeddings, recuperación y agentic RAG](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md)) son: El vector del experimento no es un modelo de embeddings semántico; las consultas son sintéticas y salen del propio corpus; solo hay seis consultas ajenas; no se evaluó ningún modelo de embeddings, ninguna base vectorial ni ningún producto de RAG. El siguiente paso, `SE-595`, sale del proceso: cómo un agente descubre y llama herramientas de otros y cómo se comunican entre sí agentes distintos con protocolos como MCP y A2A.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-593](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Fusión](../f/fusion.md), [Abstención](../a/abstencion.md), [Acierto@k](../a/acierto-k.md), [BM25](../b/bm25.md), [Embedding](../e/embedding.md), [Fragmentación](../f/fragmentacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-594 — Embeddings, recuperación y agentic RAG](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← RPO (objetivo de punto de recuperación)](./rpo-objetivo-de-punto-de-recuperacion.md) · [RTO →](./rto.md)
