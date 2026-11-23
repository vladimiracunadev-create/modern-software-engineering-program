# Fecha de revisión

[↑ Glosario](../../README.md) · [← Fatiga de aprobación](./fatiga-de-aprobacion.md) · [Feedback, telemetría y privacidad →](./feedback-telemetria-y-privacidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Momento o condición en que se vuelve a comprobar que las suposiciones siguen valiendo.

Definición de trabajo de [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md).

## Por qué importa

La clase donde se define, [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md), existe con este propósito: la clase existe para que dejes por escrito por qué el sistema es como es, de forma que otra persona pueda revisar la decisión, saber cuándo dejó de valer y cambiarla sin repetir una discusión que ya se tuvo.

## Cómo funciona

Según [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md):

Toda decisión descansa en suposiciones: el volumen esperado, el número de escritores, el presupuesto, una restricción legal. Cuando una cambia, la decisión puede dejar de valer sin que nadie lo note. Por eso un ADR útil las enumera y fija una condición o una fecha de revisión. La probabilidad de que al menos una haya cambiado crece con el número de suposiciones y con el tiempo: no se puede prevenir, pero sí vigilar. Una decisión con seis suposiciones y una tasa de cambio del 25 % anual tiene, a los doce meses, más de 8 de cada 10 probabilidades de haber perdido alguna.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md):

El portal de la plataforma de entregas guarda sus decisiones en `docs/decisiones/` con un ADR por archivo. ADR-007 registra «SQLite en el prototipo» con suposiciones («un solo proceso escritor», «menos de 5 000 entregas por semana») y la condición de revisión «cuando aparezca un segundo escritor». ADR-019 sustituye a ADR-007 cuando la secretaría empieza a importar notas en paralelo. Un RFC previo, publicado una semana antes, recibió dos objeciones que quedaron recogidas en las alternativas de ADR-019.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una decisión parece vigente y sus suposiciones ya no se cumplen** — causa: no se enumeraron suposiciones ni se fijó revisión. Corrección: añadir suposiciones y fecha de revisión, y listar los ADR vencidos. ([SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La tabla justifica fijar una fecha de revisión y enumerar las suposiciones, no una periodicidad concreta. ([SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Suposición](../s/suposicion.md), [ADR](../a/adr.md), [RFC](../r/rfc.md), [Sustitución](../s/sustitucion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (31 clases más lo mencionan; las que más):

[SE-082](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md), [SE-214](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md), [SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md), [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md), [SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md), [SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md), [SE-216](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md), [SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md).

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

[↑ Glosario](../../README.md) · [← Fatiga de aprobación](./fatiga-de-aprobacion.md) · [Feedback, telemetría y privacidad →](./feedback-telemetria-y-privacidad.md)
