# ADR

[↑ Glosario](../../README.md) · [← Adopción](./adopcion.md) · [ADR retrospectivo →](./adr-retrospectivo.md)

> **Tipo:** sigla · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Un **ADR** (*Architecture Decision Record*, registro de decisión arquitectónica) es un documento breve que registra una decisión con su contexto, sus alternativas, la decisión tomada, sus consecuencias y su estado. Es la definición que comparten [SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md), [SE-324](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md), [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md) y [SE-348](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md); [SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md) añade el **estado** (vigente, sustituida) como parte del registro.

## Por qué importa

Una decisión de arquitectura se toma una vez y se sufre durante años; si no se registra, quien llega después ve el efecto sin la razón y la discute o la deshace sin saber qué se descartó. El ADR conserva el *porqué*: el contexto que había y las alternativas que se descartaron. Convierte «así se hizo» en una decisión que se puede revisar cuando cambian las suposiciones.

## Cómo funciona

Un ADR útil tiene los componentes de la definición, y su valor depende de que cada uno sea real ([SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md)):

1. **Contexto:** qué fuerzas empujaban.
2. **Alternativas:** al menos dos, cada una con una razón de descarte.
3. **Decisión:** lo que se eligió.
4. **Consecuencias:** lo que se gana y lo que se paga.
5. **Estado y suposiciones:** si está vigente o fue sustituida, qué suposiciones sostiene y cuándo se revisa.

El registro se trata como un conjunto: los ADR forman un grafo en que una decisión sustituye a otra. [SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md) pide comprobar ese grafo y exigir que el ADR sustituido cambie su estado a «sustituida»; cuando las suposiciones dejan de cumplirse, se abre un RFC de sustitución en vez de editar el original, de modo que la historia se conserva.

## Ejemplo

[SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md) plantea tres casos límite para decidir cuándo basta un ADR: la decisión pequeña y reversible que solo tiene ADR, la decisión que afecta a otros equipos y exige además un RFC, y el ADR cuyas suposiciones ya no se cumplen, que da lugar a un RFC de sustitución. El criterio práctico que propone para no saturar el registro es limitar los ADR a decisiones difíciles de revertir o con impacto externo.

## Errores y confusiones comunes

- **Plantilla completa y sin alternativas reales.** Se llenaron las secciones sin considerar opciones; corrección: exigir al menos dos alternativas con una razón de descarte cada una ([SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md)).
- **Decisión que parece vigente con suposiciones vencidas.** No se enumeraron suposiciones ni se fijó revisión; corrección: añadir suposiciones y fecha de revisión, y listar los ADR vencidos.
- **Dos ADR contradictorios vigentes.** El estado no se actualizó al sustituir; corrección: comprobar el grafo.
- **Nadie lee el registro.** Tiene demasiadas entradas triviales; corrección: limitarlo a decisiones difíciles de revertir o con impacto externo.

## Límites y cuándo no aplica

Un ADR registra una decisión; no la justifica por sí solo ni garantiza que fuera acertada. No sustituye a un RFC cuando la decisión afecta a otros equipos y necesita discusión previa ([SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md)), y su valor se pierde si no se mantiene como un conjunto con estado y revisión. Y es una práctica de documentación, no una herramienta concreta: el formato exacto lo decide el equipo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Arquitectura](./arquitectura.md), [Consecuencia](../c/consecuencia.md), [Contextos](../c/contextos.md), [Documento](../d/documento.md), [Candidato descartado](../c/candidato-descartado.md), [Catálogo de patrones de un sistema](../c/catalogo-de-patrones-de-un-sistema.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.
- [SE-324 — Proyecto: catálogo de patrones de un sistema real](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-333 — Trade-offs, ADR y evaluación de alternativas](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «registro de decisión arquitectónica».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MADR: Markdown Architectural Decision Records](https://adr.github.io/madr/) — plantilla Markdown con alternativas y resultado; autoridad: comunidad ADR.
- [Nygard, «Documenting Architecture Decisions»](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — origen de los ADR; autoridad: Michael Nygard.
- [Fowler, «Architecture Decision Record»](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html) — práctica de ADR; autoridad: Martin Fowler.
- [Nygard, «Documenting Architecture Decisions» (2011)](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — formato breve de registro de decisiones; autoridad: autor del formato.
- [Tyree y Akerman, «Architecture Decisions: Demystifying Architecture» (IEEE Software, 2005)](https://doi.org/10.1109/MS.2005.27) — decisiones como elementos de primer orden y plantilla con suposiciones; autoridad: IEEE Software.

---

[↑ Glosario](../../README.md) · [← Adopción](./adopcion.md) · [ADR retrospectivo →](./adr-retrospectivo.md)
