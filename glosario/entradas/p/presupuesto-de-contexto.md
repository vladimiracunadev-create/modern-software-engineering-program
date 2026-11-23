# Presupuesto de contexto

[↑ Glosario](../../README.md) · [← Presupuesto de consultas](./presupuesto-de-consultas.md) · [Presupuesto de error →](./presupuesto-de-error.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Número de tokens que se decide enviar al modelo para una tarea.

Definición de trabajo de [SE-555 — Contexto, archivos, memoria y recuperación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md).

## Por qué importa

En [SE-555 — Contexto, archivos, memoria y recuperación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md), el tema «Presupuesto de contexto» importa porque obliga a elegir y a medir qué se sacrifica

## Cómo funciona

[SE-555 — Contexto, archivos, memoria y recuperación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-555 — Contexto, archivos, memoria y recuperación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo diseña el contexto para tres tareas. Para «explicar la regla de redondeo» no recupera nada: aporta la función entera y la sección de decisiones fechada, y exige que la respuesta cite líneas. Para «¿qué decidimos sobre las notas ausentes?» recupera por BM25 con fragmentos de 200 palabras y filtro de versión vigente; la respuesta debe incluir la fecha de la decisión. Para «convenciones de estilo» usa un archivo versionado con dueño, no la memoria de la herramienta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-555 — Contexto, archivos, memoria y recuperación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md)) son:

- **El fragmento recuperado empieza a mitad de frase** — causa: fragmentación por número fijo de caracteres. Corrección: fragmentar por estructura y con solapamiento.
- **Se recupera un documento de una versión anterior** — causa: falta el filtro por versión o fecha. Corrección: conservar metadatos y filtrar por vigente.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-555 — Contexto, archivos, memoria y recuperación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: una recuperación BM25 real sobre texto sintético, una simulación de caducidad de memoria y un empaquetado con relevancias del autor. No se usó ningún sistema de recuperación comercial, ningún modelo de vectores ni documentos reales; las consultas con clave única son el caso más favorable y los resultados con paráfrasis o corpus reales serían peores.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-554](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-554-prompting-instrucciones-y-criterios-de-salida/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Modelo](../m/modelo.md), [Tarea](../t/tarea.md), [Token](../t/token.md), [BM25](../b/bm25.md), [Fragmentación](../f/fragmentacion.md), [Memoria persistente](../m/memoria-persistente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-555 — Contexto, archivos, memoria y recuperación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-593](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md).

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

[↑ Glosario](../../README.md) · [← Presupuesto de consultas](./presupuesto-de-consultas.md) · [Presupuesto de error →](./presupuesto-de-error.md)
