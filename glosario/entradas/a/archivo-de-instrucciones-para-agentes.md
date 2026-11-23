# Archivo de instrucciones para agentes

[↑ Glosario](../../README.md) · [← Archivo de gestión de riesgos](./archivo-de-gestion-de-riesgos.md) · [Archivo de límites →](./archivo-de-limites.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Documento de contexto y convenciones que un agente puede leer antes de trabajar en un proyecto.

Definición de trabajo de [SE-214 — Documentación para humanos, máquinas y LLM](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md).

## Por qué importa

La clase donde se define, [SE-214 — Documentación para humanos, máquinas y LLM](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md), existe con este propósito: la clase existe para que escribas documentación que lean también programas y modelos de lenguaje sin perjudicar a las personas, y para que sepas qué cambia al diseñarla: metadatos que una máquina valida, fragmentos que no separan una regla de su excepción y una postura clara ante el texto que un agente leerá y podría obedecer.

## Cómo funciona

Según [SE-214 — Documentación para humanos, máquinas y LLM](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md):

El portal de la plataforma de entregas exige a cada página un bloque de metadatos con responsable, estado, fecha de revisión, audiencia y tipo, validado en la integración continua con la regla de antigüedad de 180 días. Los documentos se fragmentan por encabezado y cada sección que enuncia una regla incluye sus excepciones. Un archivo de instrucciones para agentes explica cómo ejecutar los comprobadores y qué no modificar. El asistente que responde preguntas tiene acceso de solo lectura al portal; no puede ejecutar acciones ni escribir. Ante un texto recuperado que contiene instrucciones, el diseño no depende de detectarlo: no tiene nada peligroso que ejecutar.

## Ejemplo

Ejemplo de [SE-214 — Documentación para humanos, máquinas y LLM](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md) (sección «Ejemplo profesional»):

El portal de la plataforma de entregas exige a cada página un bloque de metadatos con responsable, estado, fecha de revisión, audiencia y tipo, validado en la integración continua con la regla de antigüedad de 180 días. Los documentos se fragmentan por encabezado y cada sección que enuncia una regla incluye sus excepciones. Un archivo de instrucciones para agentes explica cómo ejecutar los comprobadores y qué no modificar. El asistente que responde preguntas tiene acceso de solo lectura al portal; no puede ejecutar acciones ni escribir. Ante un texto recuperado que contiene instrucciones, el diseño no depende de detectarlo: no tiene nada peligroso que ejecutar.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-214 — Documentación para humanos, máquinas y LLM](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md)) son:

- **El asistente da respuestas correctas a medias** — causa: fragmentos que separan reglas y excepciones. Corrección: fragmentar por estructura y escribir la excepción junto a la regla.
- **La auditoría no encuentra páginas sin responsable** — causa: los metadatos no se validan con un esquema. Corrección: añadir el esquema y exigirlo en la integración continua.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-214 — Documentación para humanos, máquinas y LLM](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md)) son: Las definiciones son operativas para el portal; no reemplazan las de las fuentes enlazadas abajo. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún modelo de lenguaje ni agente, y no se midió ningún sistema de recuperación: los documentos de 40 secciones, los 140 registros de metadatos y los 22 textos del filtro son construcciones del autor. La siguiente clase pasa al taller: reconstruir conocimiento perdido a partir de lo que sobrevive en el historial.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-213](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Agente](./agente.md), [Contextos](../c/contextos.md), [Documento](../d/documento.md), [Fragmentación](../f/fragmentacion.md), [Fragmento](../f/fragmento.md), [Inyección indirecta](../i/inyeccion-indirecta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-214 — Documentación para humanos, máquinas y LLM](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-560](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [llms.txt: propuesta de Jeremy Howard](https://llmstxt.org/) — archivo de información para agentes en un sitio; autoridad: autor de la propuesta.
- [AGENTS.md](https://agents.md/) — formato abierto de instrucciones para agentes de código; autoridad: proyecto AGENTS.md.
- [Lewis et al., «Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks» (2020)](https://arxiv.org/abs/2005.11401) — generación aumentada por recuperación; autoridad: arXiv.
- [Greshake et al., «Not what you've signed up for» (2023)](https://arxiv.org/abs/2302.12173) — inyección indirecta de instrucciones; autoridad: arXiv.
- [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — riesgos de aplicaciones con modelos de lenguaje; autoridad: OWASP.

---

[↑ Glosario](../../README.md) · [← Archivo de gestión de riesgos](./archivo-de-gestion-de-riesgos.md) · [Archivo de límites →](./archivo-de-limites.md)
