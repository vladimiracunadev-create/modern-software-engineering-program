# Registro de decisiones

[↑ Glosario](../../README.md) · [← Registro de cambios archivado](./registro-de-cambios-archivado.md) · [Registro de esquemas →](./registro-de-esquemas.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Documento breve con contexto, opciones, decisión, responsable, fecha y condición de revisión.

Definición de trabajo de [SE-187 — Riesgos, supuestos, issues y decisiones](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-586 — AI-DLC, gobierno y vibe coding frente a agentic engineering](../../../classes/part-48-harness-y-agentic-engineering/se-586-ai-dlc-gobierno-y-vibe-coding-frente-a-agentic-engineering/README.md): Historial de quién aprobó qué, con qué evidencia.

## Por qué importa

En [SE-333 — Trade-offs, ADR y evaluación de alternativas](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md), el tema «Registro de decisiones» importa porque conserva el porqué cuando las personas cambian.

En [SE-610 — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md), el tema «Registro de decisiones» importa porque debe poder demostrar que no se alteró.

En [SE-557 — Prototipado, scaffolding y exploración de alternativas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md), el tema «Registro de decisiones» importa porque conserva por qué se eligió y qué se descartó

## Cómo funciona

Según [SE-333 — Trade-offs, ADR y evaluación de alternativas](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md), en la sección «Registro de decisiones»:

Un **ADR** (registro de decisión de arquitectura) es un documento corto sobre una decisión significativa: título, estado (propuesta, aceptada, reemplazada), fecha, contexto, decisión, alternativas consideradas y consecuencias. Se guarda junto al código, se numera y no se edita para borrar el pasado: si la decisión cambia, un ADR nuevo reemplaza al anterior y el anterior queda con el estado «reemplazada». Su valor aparece cuando alguien pregunta por qué: la respuesta está escrita, con las fuerzas que había en ese momento. Registrar todo es ruido; registrar lo costoso de revertir es memoria.

## Ejemplo

Ejemplo de [SE-557 — Prototipado, scaffolding y exploración de alternativas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md) (sección «Caso conductor»):

El módulo de calificaciones es el caso conductor. Esta clase deja el quinto artefacto: la exploración con su registro de decisión. `SE-558` preguntará qué ocurre cuando lo que se genera son pruebas, documentación y migraciones, y `SE-563` comparará flujos con mediciones. Cambia después un solo dato, el ruido del evaluador, y observa a partir de qué valor más alternativas dejan de compensar.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-333 — Trade-offs, ADR y evaluación de alternativas](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md)) son:

- **Nadie recuerda por qué se decidió algo** — causa: no hay registro de la decisión. Corrección: escribir un ADR con contexto, alternativas y consecuencias.
- **El ganador de la matriz cambia al mover un peso** — causa: la matriz no discrimina. Corrección: calcular la sensibilidad y sostener la decisión con un escenario.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-333 — Trade-offs, ADR y evaluación de alternativas](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres cálculos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se evaluó ninguna arquitectura real: los puntajes, los ADR, sus defectos y el modelo de espera son construcciones del autor. La siguiente clase mira a las personas y a los equipos que toman y ejecutan estas decisiones.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición de revisión](../c/condicion-de-revision.md), [Condición](../c/condicion.md), [Contextos](../c/contextos.md), [Documento](../d/documento.md), [ADR](../a/adr.md), [Análisis de sensibilidad](../a/analisis-de-sensibilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-187 — Riesgos, supuestos, issues y decisiones](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-333 — Trade-offs, ADR y evaluación de alternativas](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-557 — Prototipado, scaffolding y exploración de alternativas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.
- [SE-586 — AI-DLC, gobierno y vibe coding frente a agentic engineering](../../../classes/part-48-harness-y-agentic-engineering/se-586-ai-dlc-gobierno-y-vibe-coding-frente-a-agentic-engineering/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.
- [SE-610 — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (24 clases más lo mencionan; las que más):

[SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md), [SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md), [SE-518](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md), [SE-529](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-529-liderazgo-tecnico-sin-autoridad-formal/README.md), [SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md), [SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md), [SE-324](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md), [SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «registro de decisión».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Nygard, «Documenting Architecture Decisions»](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — registro de decisiones; autoridad: autor del texto.
- [Architectural Decision Records](https://adr.github.io/) — plantillas y vocabulario de registros de decisión; autoridad: comunidad ADR.
- [MADR, Markdown Architectural Decision Records](https://adr.github.io/madr/) — plantilla de ADR; autoridad: comunidad ADR.
- [SEI, «The Architecture Tradeoff Analysis Method»](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/) — análisis de compromisos contra escenarios; autoridad: Software Engineering Institute (Carnegie Mellon).
- [Fowler, «Architecture Decision Record»](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html) — práctica de ADR; autoridad: Martin Fowler.

---

[↑ Glosario](../../README.md) · [← Registro de cambios archivado](./registro-de-cambios-archivado.md) · [Registro de esquemas →](./registro-de-esquemas.md)
