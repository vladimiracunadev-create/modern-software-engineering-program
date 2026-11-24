# Registro de decisiones

[↑ Glosario](../../README.md) · [← Registro de cambios archivado](./registro-de-cambios-archivado.md) · [Registro de esquemas →](./registro-de-esquemas.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Un **registro de decisiones** es un documento breve con contexto, opciones, decisión, responsable, fecha y condición de revisión ([SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md)). En arquitectura se llama ADR (registro de decisión de arquitectura) ([SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md)). [SE-586](../../../classes/part-48-harness-y-agentic-engineering/se-586-ai-dlc-gobierno-y-vibe-coding-frente-a-agentic-engineering/README.md) y [SE-610](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md) lo usan como historial de quién aprobó qué, con qué evidencia, y [SE-557](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md) como la conservación de por qué se eligió una opción y qué se descartó.

## Por qué importa

Conserva el porqué cuando las personas cambian. Sin registro, nadie recuerda por qué se decidió algo y se reinventan o se deshacen decisiones sin conocer las razones. Cambia la gestión del conocimiento: la decisión y su contexto viven junto al código, no en la memoria de quien participó.

## Cómo funciona

[SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md) describe el ADR: un documento corto sobre una **decisión significativa**, con **título, estado** (propuesta, aceptada, reemplazada), **fecha, contexto, decisión, alternativas consideradas y consecuencias**. Se guarda **junto al código**, se numera y **no se edita para borrar el pasado**: si la decisión cambia, un ADR nuevo reemplaza al anterior y este queda con el estado «reemplazada». Así la historia de las decisiones es consultable.

[SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md) sitúa el registro de decisiones junto a otros tres registros de gestión: riesgos, supuestos e issues. En el ejemplo, una hoja de 23 filas se reorganiza en cuatro registros, con siete decisiones tomadas en el trimestre registradas con contexto y disparador de revisión. La **condición de revisión** es parte de la decisión: qué cambio de circunstancias la reabriría.

[SE-610](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md) añade un requisito de integridad: el registro debe poder demostrar que **no se alteró**, por ejemplo con firmas o huellas encadenadas, lo que conecta con los registros de auditoría. [SE-557](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md) lo usa para exploraciones con asistentes de IA: el registro conserva qué opciones se evaluaron, con qué datos y por qué se eligió una. Y un fallo con corrección conocida: el ganador de una matriz de decisión cambia al mover un peso porque la matriz no discrimina; se calcula la sensibilidad y se sostiene la decisión con un escenario, registrando ambos.

## Ejemplo

ADR-007. Título: «Penalización diaria con tope». Estado: aceptada. Fecha: 2026-03-04. Contexto: reclamos por descuentos arbitrarios. Opciones: penalización fija, diaria con tope, sin penalización. Decisión: diaria con tope del 50 %. Responsable: coordinación académica. Consecuencias: reglas más complejas de explicar. Revisar si: los reclamos no bajan en dos periodos. (Registro ilustrativo en el formato de [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md).)

## Errores y confusiones comunes

- **Nadie recuerda por qué se decidió algo**: no hay registro; corrección: escribir un ADR con contexto, alternativas y consecuencias.
- **Editar el ADR para «corregir» el pasado.**
- **Registrar la decisión sin las alternativas descartadas.**
- **Decisiones sin responsable ni condición de revisión.**

## Límites y cuándo no aplica

No toda decisión merece registro: solo las significativas o de difícil reversión. Un registro sin lectores se pudre; se enlaza desde el código afectado. Las decisiones triviales y reversibles no justifican el costo de documentarlas.

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
