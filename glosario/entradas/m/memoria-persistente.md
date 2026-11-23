# Memoria persistente

[↑ Glosario](../../README.md) · [← Memoria lineal](./memoria-lineal.md) · [Memoria virtual →](./memoria-virtual.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Información guardada entre sesiones que la herramienta incorpora al contexto.

Definición de trabajo de [SE-555 — Contexto, archivos, memoria y recuperación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md).

## Por qué importa

En [SE-555 — Contexto, archivos, memoria y recuperación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md), el tema «Memoria persistente» importa porque se desactualiza sin que nadie lo note

## Cómo funciona

Según [SE-555 — Contexto, archivos, memoria y recuperación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md):

El modelo solo usa lo que está en su ventana en el momento de responder, y esa información llega por cuatro vías. El **contexto inmediato** es lo que escribes y lo que la herramienta añade (la conversación, el archivo abierto). Los **archivos aportados** son documentos que decides incluir completos. La **memoria persistente** es un almacén que la herramienta alimenta entre sesiones, ya sean notas que el modelo guardó o archivos de convenciones que el equipo mantiene. Y la **recuperación** es una búsqueda que, ante una pregunta, trae fragmentos de un índice. Cada vía falla de un modo propio: el contexto inmediato se llena, los archivos completos desbordan, la memoria envejece y la recuperación trae lo parecido en vez de lo correcto.

## Ejemplo

Caso medido en la sección «La memoria persistente se desactualiza» de [SE-555 — Contexto, archivos, memoria y recuperación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md):

Una memoria que guarda lo que se aprendió ayer responde hoy con ayer. Si un hecho cambia con probabilidad *c* por día, la probabilidad de que un hecho guardado hace *t* días ya no valga es 1 − (1 − *c*)^t. Eso se agrava porque el modelo no distingue lo vigente de lo vencido: ambos aparecen como texto en el contexto. Las defensas son técnicas y organizativas. Técnicas: fechar cada entrada, asignar una caducidad y refrescar o descartar al vencer, y preferir las fuentes primarias (el código, el esquema) sobre las notas sobre ellas.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-555 — Contexto, archivos, memoria y recuperación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md)) son:

- **El fragmento recuperado empieza a mitad de frase** — causa: fragmentación por número fijo de caracteres. Corrección: fragmentar por estructura y con solapamiento.
- **Se recupera un documento de una versión anterior** — causa: falta el filtro por versión o fecha. Corrección: conservar metadatos y filtrar por vigente.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-555 — Contexto, archivos, memoria y recuperación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: una recuperación BM25 real sobre texto sintético, una simulación de caducidad de memoria y un empaquetado con relevancias del autor. No se usó ningún sistema de recuperación comercial, ningún modelo de vectores ni documentos reales; las consultas con clave única son el caso más favorable y los resultados con paráfrasis o corpus reales serían peores.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-554](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-554-prompting-instrucciones-y-criterios-de-salida/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](../c/contextos.md), [Herramientas](../h/herramientas.md), [BM25](../b/bm25.md), [Fragmentación](../f/fragmentacion.md), [Presupuesto de contexto](../p/presupuesto-de-contexto.md), [Recuperación](../r/recuperacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-555 — Contexto, archivos, memoria y recuperación](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md), [SE-550](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md), [SE-593](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md).

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

[↑ Glosario](../../README.md) · [← Memoria lineal](./memoria-lineal.md) · [Memoria virtual →](./memoria-virtual.md)
