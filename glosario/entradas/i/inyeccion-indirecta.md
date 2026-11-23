# Inyección indirecta

[↑ Glosario](../../README.md) · [← Inyección de scripts](./inyeccion-de-scripts.md) · [Inyección indirecta de instrucciones →](./inyeccion-indirecta-de-instrucciones.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Ataque que coloca instrucciones en datos que un modelo recupera o lee, para que las obedezca como si fueran de su usuario.

Definición de trabajo de [SE-214 — Documentación para humanos, máquinas y LLM](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md).

## Por qué importa

La clase donde se define, [SE-214 — Documentación para humanos, máquinas y LLM](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md), existe con este propósito: la clase existe para que escribas documentación que lean también programas y modelos de lenguaje sin perjudicar a las personas, y para que sepas qué cambia al diseñarla: metadatos que una máquina valida, fragmentos que no separan una regla de su excepción y una postura clara ante el texto que un agente leerá y podría obedecer.

## Cómo funciona

Según [SE-214 — Documentación para humanos, máquinas y LLM](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md):

La inyección indirecta aprovecha que un modelo no distingue de forma fiable entre las instrucciones de quien lo usa y el texto que lee: un documento recuperado puede contener «ignora lo anterior» y el modelo puede obedecer. La defensa no consiste en detectar frases, porque el texto adversarial se reescribe, se codifica o cambia de idioma. Consiste en tratar todo lo recuperado como dato no confiable y en limitar lo que el agente puede hacer con él: permisos mínimos, acciones que requieren confirmación humana, separación entre quien lee y quien ejecuta. Un filtro léxico puede ayudar como alarma; no es un límite.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-214 — Documentación para humanos, máquinas y LLM](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md):

El portal de la plataforma de entregas exige a cada página un bloque de metadatos con responsable, estado, fecha de revisión, audiencia y tipo, validado en la integración continua con la regla de antigüedad de 180 días. Los documentos se fragmentan por encabezado y cada sección que enuncia una regla incluye sus excepciones. Un archivo de instrucciones para agentes explica cómo ejecutar los comprobadores y qué no modificar. El asistente que responde preguntas tiene acceso de solo lectura al portal; no puede ejecutar acciones ni escribir.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-214 — Documentación para humanos, máquinas y LLM](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md)) son:

- **El asistente da respuestas correctas a medias** — causa: fragmentos que separan reglas y excepciones. Corrección: fragmentar por estructura y escribir la excepción junto a la regla.
- **La auditoría no encuentra páginas sin responsable** — causa: los metadatos no se validan con un esquema. Corrección: añadir el esquema y exigirlo en la integración continua.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La inyección indirecta aprovecha que un modelo no distingue de forma fiable entre las instrucciones de quien lo usa y el texto que lee: un documento recuperado puede contener «ignora lo anterior» y el modelo puede obedecer. ([SE-214](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-213](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Instrucción](./instruccion.md), [Modelo](../m/modelo.md), [Archivo de instrucciones para agentes](../a/archivo-de-instrucciones-para-agentes.md), [Fragmentación](../f/fragmentacion.md), [Fragmento](../f/fragmento.md), [Metadatos de documento](../m/metadatos-de-documento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-214 — Documentación para humanos, máquinas y LLM](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md), [SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md), [SE-042](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md), [SE-594](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md), [SE-595](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Greshake et al., «Not what you've signed up for» (2023)](https://arxiv.org/abs/2302.12173) — inyección indirecta de instrucciones; autoridad: arXiv.
- [llms.txt: propuesta de Jeremy Howard](https://llmstxt.org/) — archivo de información para agentes en un sitio; autoridad: autor de la propuesta.
- [AGENTS.md](https://agents.md/) — formato abierto de instrucciones para agentes de código; autoridad: proyecto AGENTS.md.
- [Lewis et al., «Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks» (2020)](https://arxiv.org/abs/2005.11401) — generación aumentada por recuperación; autoridad: arXiv.
- [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — riesgos de aplicaciones con modelos de lenguaje; autoridad: OWASP.

---

[↑ Glosario](../../README.md) · [← Inyección de scripts](./inyeccion-de-scripts.md) · [Inyección indirecta de instrucciones →](./inyeccion-indirecta-de-instrucciones.md)
