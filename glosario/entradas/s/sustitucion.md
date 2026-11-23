# Sustitución

[↑ Glosario](../../README.md) · [← Suscripción](./suscripcion.md) · [Syscall →](./syscall.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Relación entre dos ADR por la que el segundo reemplaza al primero sin borrarlo.

Definición de trabajo de [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md).

## Por qué importa

En [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md), el tema «Estado y sustitución» importa porque las decisiones cambian: un registro útil dice cuál es la vigente y enlaza la historia.

## Cómo funciona

Según [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md):

Se generan 200 registros de 40 ADR con sustituciones aleatorias (cada ADR sustituye, con probabilidad 0,35, a uno anterior que aún no tenía sucesor) y se aplica una mutación a cada uno: enlace a un ADR inexistente (45), dos ADR que sustituyen al mismo (41), un ADR que se sustituye a sí mismo (39), un ADR sustituido que sigue declarándose vigente (39) o un ADR que sustituye a otro estructuralmente válido pero equivocado (36).

Según [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md):

Compara el caso normal con tres casos límite: la decisión pequeña y reversible que solo tiene ADR, la decisión que afecta a otros equipos y exige RFC, y el ADR cuyas suposiciones ya no se cumplen (se abre un RFC de sustitución, no se edita el original).

## Ejemplo

Ejemplo de [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md) (sección «Ejemplo profesional»):

Compara el caso normal con tres casos límite: la decisión pequeña y reversible que solo tiene ADR, la decisión que afecta a otros equipos y exige RFC, y el ADR cuyas suposiciones ya no se cumplen (se abre un RFC de sustitución, no se edita el original).

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md)) son:

- **Los ADR tienen secciones pero ninguna alternativa real** — causa: se completó la plantilla sin considerar opciones. Corrección: exigir al menos dos alternativas con una razón de descarte cada una.
- **Una decisión parece vigente y sus suposiciones ya no se cumplen** — causa: no se enumeraron suposiciones ni se fijó revisión. Corrección: añadir suposiciones y fecha de revisión, y listar los ADR vencidos.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md)) son: Las definiciones son operativas para el portal; no reemplazan las de las fuentes enlazadas abajo. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se revisó ningún registro real ni se midió el ahorro de un ADR: los 300 registros, los 200 grafos y las tasas de cambio de suposiciones son construcciones del autor, y las frases vacías que escapan al linter se sembraron a propósito.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Relación](../r/relacion.md), [ADR](../a/adr.md), [Fecha de revisión](../f/fecha-de-revision.md), [RFC](../r/rfc.md), [Suposición](./suposicion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (29 clases más lo mencionan; las que más):

[SE-078](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md), [SE-522](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md), [SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md), [SE-075](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md), [SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md), [SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md), [SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md), [SE-010](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Nygard, «Documenting Architecture Decisions» (2011)](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — formato breve de registro de decisiones; autoridad: autor del formato.
- [Tyree y Akerman, «Architecture Decisions: Demystifying Architecture» (IEEE Software, 2005)](https://doi.org/10.1109/MS.2005.27) — decisiones como elementos de primer orden y plantilla con suposiciones; autoridad: IEEE Software.
- [MADR: Markdown Architectural Decision Records](https://adr.github.io/madr/) — plantilla Markdown con alternativas y resultado; autoridad: comunidad ADR.
- [Fowler, «Architecture Decision Record» (bliki)](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html) — descripción del registro y de su carácter inmutable; autoridad: martinfowler.com.
- [PEP 1, propósito y guía de los PEP](https://peps.python.org/pep-0001/) — proceso de propuestas con estados para cambios en Python; autoridad: Python Software Foundation.

---

[↑ Glosario](../../README.md) · [← Suscripción](./suscripcion.md) · [Syscall →](./syscall.md)
