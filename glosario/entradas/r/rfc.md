# RFC

[↑ Glosario](../../README.md) · [← Revocación](./revocacion.md) · [Riesgo →](./riesgo.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Propuesta publicada para revisión antes de decidir, con un proceso de estados y criterios de aceptación.

Definición de trabajo de [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md).

## Por qué importa

En [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md), el tema «RFC y ADR» importa porque un RFC propone antes y se revisa; un ADR registra después; confundirlos retrasa o deja decisiones sin rastro.

## Cómo funciona

Según [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md):

Un RFC es una propuesta que se publica para recibir revisión antes de decidir; un ADR es el registro de lo decidido. Procesos como los PEP de Python o los RFC de Rust usan el primero para cambios con impacto en muchas personas, con estados, plazos y criterios de aceptación. Para decisiones locales y reversibles, el ADR basta. La regla práctica: si el coste de equivocarse recae en gente que no está en la conversación, publica un RFC; si recae en el equipo y se puede deshacer en un día, registra un ADR. El riesgo de usar solo RFC es la lentitud; el de usar solo ADR, que la revisión llegue cuando ya no puede cambiar nada.

Según [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md):

El portal de la plataforma de entregas guarda sus decisiones en `docs/decisiones/` con un ADR por archivo. ADR-007 registra «SQLite en el prototipo» con suposiciones («un solo proceso escritor», «menos de 5 000 entregas por semana») y la condición de revisión «cuando aparezca un segundo escritor». ADR-019 sustituye a ADR-007 cuando la secretaría empieza a importar notas en paralelo. Un RFC previo, publicado una semana antes, recibió dos objeciones que quedaron recogidas en las alternativas de ADR-019. La integración continua ejecuta el linter de forma y la comprobación del grafo en cada cambio.

## Ejemplo

Ejemplo de [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md) (sección «Ejemplo profesional»):

El portal de la plataforma de entregas guarda sus decisiones en `docs/decisiones/` con un ADR por archivo. ADR-007 registra «SQLite en el prototipo» con suposiciones («un solo proceso escritor», «menos de 5 000 entregas por semana») y la condición de revisión «cuando aparezca un segundo escritor». ADR-019 sustituye a ADR-007 cuando la secretaría empieza a importar notas en paralelo. Un RFC previo, publicado una semana antes, recibió dos objeciones que quedaron recogidas en las alternativas de ADR-019. La integración continua ejecuta el linter de forma y la comprobación del grafo en cada cambio.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un RFC lleva meses abierto** — causa: no hay plazo ni criterio de cierre. Corrección: fijar plazo de revisión y quién decide. ([SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La regla práctica: si el coste de equivocarse recae en gente que no está en la conversación, publica un RFC; si recae en el equipo y se puede deshacer en un día, registra un ADR. ([SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Criterio de aceptación](../c/criterio-de-aceptacion.md), [Estado](../e/estado.md), [Proceso](../p/proceso.md), [Revisión](./revision.md), [ADR](../a/adr.md), [Cita de proximidad](../c/cita-de-proximidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-010 — Cómo leer estándares, documentación y literatura técnica](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Rust RFCs](https://github.com/rust-lang/rfcs) — proceso de RFC de un proyecto abierto; autoridad: equipo de Rust.
- [Nygard, «Documenting Architecture Decisions» (2011)](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — formato breve de registro de decisiones; autoridad: autor del formato.
- [Tyree y Akerman, «Architecture Decisions: Demystifying Architecture» (IEEE Software, 2005)](https://doi.org/10.1109/MS.2005.27) — decisiones como elementos de primer orden y plantilla con suposiciones; autoridad: IEEE Software.
- [MADR: Markdown Architectural Decision Records](https://adr.github.io/madr/) — plantilla Markdown con alternativas y resultado; autoridad: comunidad ADR.
- [Fowler, «Architecture Decision Record» (bliki)](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html) — descripción del registro y de su carácter inmutable; autoridad: martinfowler.com.

---

[↑ Glosario](../../README.md) · [← Revocación](./revocacion.md) · [Riesgo →](./riesgo.md)
