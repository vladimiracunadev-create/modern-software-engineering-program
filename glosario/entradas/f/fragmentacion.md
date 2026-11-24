# Fragmentación

[↑ Glosario](../../README.md) · [← FPR](./fpr.md) · [Fragmentación aleatoria →](./fragmentacion-aleatoria.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

En sistemas de recuperación para modelos, la **fragmentación** (*chunking*) es la división de documentos en unidades indexables, con un tamaño y una solapación. Es el sentido común a [SE-555](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md) (contexto, archivos, memoria y recuperación), [SE-214](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md) (documentación para humanos, máquinas y LLM) y [SE-594](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md) (embeddings, recuperación y agentic RAG). Aquí no se trata de la fragmentación de memoria ni de disco.

## Por qué importa

Cambia qué encuentra el sistema y cuánto cuesta. El tamaño del fragmento condiciona qué se recupera. Según [SE-214](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md), separar una regla de su excepción produce respuestas falsas con apariencia de fuente: el sistema cita un fragmento real que, sin su excepción, lleva a una conclusión equivocada. Y según [SE-594](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md), decide qué unidad se recupera y con qué contexto.

## Cómo funciona

El documento se parte en fragmentos que se indexan (por palabras clave como BM25 o por vectores) y se recuperan por consulta. Dos parámetros dominan: el **tamaño** y la **solapación** entre fragmentos consecutivos. [SE-594](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md) describe el compromiso: un fragmento demasiado corto pierde el contexto que lo hace entendible («el plazo es de 72 horas», ¿de qué?); uno demasiado largo diluye la señal y llena el contexto del modelo.

Dos prácticas reducen el daño. Primera, fragmentar **por estructura** (secciones, funciones) y con solapamiento, no por número fijo de caracteres, para no empezar a mitad de frase ([SE-555](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md)). Segunda, conservar la cita al fragmento exacto con enlace a la fuente, de modo que se pueda verificar. Pero la cita no basta si el fragmento está truncado en una excepción: la respuesta puede ser errónea con una cita real. Por eso [SE-594](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md) añade que una base vectorial aporta escalabilidad, filtros y actualización, no calidad por sí misma: la calidad la determinan el modelo de embeddings y la fragmentación.

## Ejemplo

En el escenario hipotético de [SE-555](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md), el equipo diseña el contexto para tres tareas. Para «explicar la regla de redondeo» no recupera nada: aporta la función entera y la sección de decisiones fechada y exige citar líneas. Para «¿qué decidimos sobre las notas ausentes?» recupera por BM25 con fragmentos de 200 palabras y filtro de versión vigente; la respuesta debe incluir la fecha de la decisión.

## Errores y confusiones comunes

- **El fragmento empieza a mitad de frase.** Fragmentación por número fijo de caracteres; fragmentar por estructura y con solapamiento.
- **Separar la regla de su excepción.** Produce respuestas falsas con apariencia de fuente.
- **Atribuir la calidad a la base vectorial.** Depende de los embeddings y de la fragmentación.
- **Usar el mismo tamaño para todo documento.** Un código y un acta no se parten igual.

## Límites y cuándo no aplica

Si la fuente cabe entera en el contexto y la tarea la necesita, fragmentar es innecesario y arriesga perder relaciones. Ningún tamaño es universalmente correcto: se ajusta evaluando con consultas reales. Los escenarios de [SE-555](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md) son hipotéticos, sin datos reales.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-213](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Documento](../d/documento.md), [Archivo de instrucciones para agentes](../a/archivo-de-instrucciones-para-agentes.md), [BM25](../b/bm25.md), [Fragmento](./fragmento.md), [Inyección indirecta](../i/inyeccion-indirecta.md), [Memoria persistente](../m/memoria-persistente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-214 — Documentación para humanos, máquinas y LLM](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.
- [SE-555 — Contexto, archivos, memoria y recuperación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.
- [SE-594 — Embeddings, recuperación y agentic RAG](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-344](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md), [SE-399](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md), [SE-021](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md), [SE-038](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md), [SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md), [SE-039](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md), [SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [Stripe](../../../casos/exito/stripe.md), [Slack](../../../casos/exito/slack.md), [Shopify](../../../casos/exito/shopify.md), [Instagram](../../../casos/exito/instagram.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Lewis et al., «Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks»](https://arxiv.org/abs/2005.11401) — generación con recuperación de memoria externa; autoridad: NeurIPS 2020.
- [Robertson y Zaragoza, «The Probabilistic Relevance Framework: BM25 and Beyond»](https://doi.org/10.1561/1500000019) — la función de puntuación BM25; autoridad: Foundations and Trends in Information Retrieval.
- [Anthropic: effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — el contexto como recurso finito y la recuperación justo a tiempo; autoridad: Anthropic.
- [Liu et al., «Lost in the Middle»](https://arxiv.org/abs/2307.03172) — uso de la información según su posición; autoridad: Transactions of the ACL.
- [Model Context Protocol](https://modelcontextprotocol.io) — protocolo abierto para exponer datos y herramientas a un modelo; autoridad: especificación del proyecto.

---

[↑ Glosario](../../README.md) · [← FPR](./fpr.md) · [Fragmentación aleatoria →](./fragmentacion-aleatoria.md)
