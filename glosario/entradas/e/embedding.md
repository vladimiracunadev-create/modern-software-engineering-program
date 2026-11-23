# Embedding

[↑ Glosario](../../README.md) · [← Embedded & IoT Engineer](./embedded-iot-engineer.md) · [Embudo →](./embudo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Vector que representa un texto de modo que la cercanía aproxima la similitud.

Definición de trabajo de [SE-594 — Embeddings, recuperación y agentic RAG](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md).

## Por qué importa

En [SE-594 — Embeddings, recuperación y agentic RAG](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md), el tema «Embeddings» importa porque aportan similitud tolerante a variaciones.

## Cómo funciona

Según [SE-594 — Embeddings, recuperación y agentic RAG](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md):

Un **embedding** convierte un texto en un vector de números de modo que textos con significado parecido queden cerca (por ejemplo, con coseno). Los modelos de oraciones como Sentence-BERT se entrenan para que esa cercanía refleje similitud semántica, lo que permite encontrar «reintento» desde «volver a intentar». El experimento **no** usa un modelo de ese tipo: usa un vector disperso por trigramas de caracteres con hashing, que capta similitud ortográfica (tolera erratas y raíces) pero no sinonimia. Sirve para ver el mecanismo (indexar vectores, comparar por coseno, combinar con BM25) sin descargar un modelo, y se declara como sustituto. Con consultas exactas acierta en primer lugar el 65,0 %; con erratas y raíces, el 59,2 %.

Según [SE-594 — Embeddings, recuperación y agentic RAG](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md):

El equipo indexa los 300 documentos del programa, fragmentados por encabezado, con título y ruta como metadatos. Escribe 60 preguntas reales de docentes con el fragmento que las responde y mide BM25, un modelo de embeddings y su fusión. Elige BM25 más embeddings con RRF porque el híbrido gana en las preguntas con paráfrasis y no pierde en las exactas. Fija un umbral con las preguntas fuera del corpus que recogió de los registros, de modo que el sistema responda «no lo encontré» en el 80 % de ellas y acepte el 92 % de las válidas. La respuesta cita siempre los fragmentos usados con enlace, y una prueba rechaza respuestas con afirmaciones sin cita.

## Ejemplo

Ejemplo de [SE-594 — Embeddings, recuperación y agentic RAG](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md) (sección «Ejemplo profesional»):

El equipo indexa los 300 documentos del programa, fragmentados por encabezado, con título y ruta como metadatos. Escribe 60 preguntas reales de docentes con el fragmento que las responde y mide BM25, un modelo de embeddings y su fusión. Elige BM25 más embeddings con RRF porque el híbrido gana en las preguntas con paráfrasis y no pierde en las exactas. Fija un umbral con las preguntas fuera del corpus que recogió de los registros, de modo que el sistema responda «no lo encontré» en el 80 % de ellas y acepte el 92 % de las válidas.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** las consultas salen del propio texto (ocho palabras elegidas al azar), lo que favorece la coincidencia léxica; con paráfrasis de personas reales y un modelo de embeddings semántico, el orden entre BM25 y el vector podría cambiar. ([SE-594](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md))
- Una base vectorial aporta escalabilidad, filtros y actualización, no calidad por sí misma: la calidad la determina el modelo de embeddings y la fragmentación. ([SE-594](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-593](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Abstención](../a/abstencion.md), [Acierto@k](../a/acierto-k.md), [BM25](../b/bm25.md), [Fragmentación](../f/fragmentacion.md), [Fragmento](../f/fragmento.md), [MRR](../m/mrr.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-594 — Embeddings, recuperación y agentic RAG](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-593](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md), [SE-595](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Embeddings».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Embedded & IoT Engineer](./embedded-iot-engineer.md) · [Embudo →](./embudo.md)
