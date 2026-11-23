# Suposición

[↑ Glosario](../../README.md) · [← Supervisión humana](./supervision-humana.md) · [Supply chain mínima →](./supply-chain-minima.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Condición del entorno que la decisión da por cierta y cuyo cambio podría invalidarla.

Definición de trabajo de [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md).

## Por qué importa

En [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md), el tema «Suposiciones y caducidad» importa porque una decisión vale mientras valgan sus suposiciones; más suposiciones, antes pierde vigencia alguna.

## Cómo funciona

Según [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md):

Toda decisión descansa en suposiciones: el volumen esperado, el número de escritores, el presupuesto, una restricción legal. Cuando una cambia, la decisión puede dejar de valer sin que nadie lo note. Por eso un ADR útil las enumera y fija una condición o una fecha de revisión. La probabilidad de que al menos una haya cambiado crece con el número de suposiciones y con el tiempo: no se puede prevenir, pero sí vigilar. Una decisión con seis suposiciones y una tasa de cambio del 25 % anual tiene, a los doce meses, más de 8 de cada 10 probabilidades de haber perdido alguna.

Según [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md):

El portal de la plataforma de entregas guarda sus decisiones en `docs/decisiones/` con un ADR por archivo. ADR-007 registra «SQLite en el prototipo» con suposiciones («un solo proceso escritor», «menos de 5 000 entregas por semana») y la condición de revisión «cuando aparezca un segundo escritor». ADR-019 sustituye a ADR-007 cuando la secretaría empieza a importar notas en paralelo. Un RFC previo, publicado una semana antes, recibió dos objeciones que quedaron recogidas en las alternativas de ADR-019. La integración continua ejecuta el linter de forma y la comprobación del grafo en cada cambio.

## Ejemplo

Ejemplo de [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md) (sección «Ejemplo profesional»):

El portal de la plataforma de entregas guarda sus decisiones en `docs/decisiones/` con un ADR por archivo. ADR-007 registra «SQLite en el prototipo» con suposiciones («un solo proceso escritor», «menos de 5 000 entregas por semana») y la condición de revisión «cuando aparezca un segundo escritor». ADR-019 sustituye a ADR-007 cuando la secretaría empieza a importar notas en paralelo. Un RFC previo, publicado una semana antes, recibió dos objeciones que quedaron recogidas en las alternativas de ADR-019. La integración continua ejecuta el linter de forma y la comprobación del grafo en cada cambio.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una decisión parece vigente y sus suposiciones ya no se cumplen** — causa: no se enumeraron suposiciones ni se fijó revisión. Corrección: añadir suposiciones y fecha de revisión, y listar los ADR vencidos. ([SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La probabilidad de que al menos una haya cambiado crece con el número de suposiciones y con el tiempo: no se puede prevenir, pero sí vigilar. ([SE-208](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Entorno](../e/entorno.md), [ADR](../a/adr.md), [Fecha de revisión](../f/fecha-de-revision.md), [RFC](../r/rfc.md), [Sustitución](./sustitucion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-208 — ADRs, RFCs y registro de decisiones](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-208-adrs-rfcs-y-registro-de-decisiones/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (58 clases más lo mencionan; las que más):

[SE-133](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md), [SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md), [SE-177](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md), [SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md), [SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md), [SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md), [SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md), [SE-178](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md).

**Aparece en los casos de estudio:** [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Tyree y Akerman, «Architecture Decisions: Demystifying Architecture» (IEEE Software, 2005)](https://doi.org/10.1109/MS.2005.27) — decisiones como elementos de primer orden y plantilla con suposiciones; autoridad: IEEE Software.
- [Nygard, «Documenting Architecture Decisions» (2011)](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — formato breve de registro de decisiones; autoridad: autor del formato.
- [MADR: Markdown Architectural Decision Records](https://adr.github.io/madr/) — plantilla Markdown con alternativas y resultado; autoridad: comunidad ADR.
- [Fowler, «Architecture Decision Record» (bliki)](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html) — descripción del registro y de su carácter inmutable; autoridad: martinfowler.com.
- [PEP 1, propósito y guía de los PEP](https://peps.python.org/pep-0001/) — proceso de propuestas con estados para cambios en Python; autoridad: Python Software Foundation.

---

[↑ Glosario](../../README.md) · [← Supervisión humana](./supervision-humana.md) · [Supply chain mínima →](./supply-chain-minima.md)
