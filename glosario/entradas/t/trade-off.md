# Trade-off

[↑ Glosario](../../README.md) · [← Traceability](./traceability.md) · [Traducción →](./traduccion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Pareja de ganancia y sacrificio que implica elegir una alternativa.

Definición de trabajo de [SE-333 — Trade-offs, ADR y evaluación de alternativas](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md).

## Por qué importa

En [SE-008 — Restricciones, riesgos y compromisos entre atributos](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md), el tema «Trade-off» importa porque hace visible ganancia y pérdida

## Cómo funciona

Según [SE-008 — Restricciones, riesgos y compromisos entre atributos](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md):

Un trade-off no significa que toda mejora empeore necesariamente otra cosa. A veces un diseño elimina desperdicio y mejora rendimiento, costo y mantenibilidad. La obligación es buscar alternativas antes de aceptar una pérdida y, cuando permanece, declarar quién la soporta. “CAP”, “seguridad versus usabilidad” o “rápido versus correcto” no reemplazan el mecanismo específico del caso.

Según [SE-333 — Trade-offs, ADR y evaluación de alternativas](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md):

Una decisión elige una alternativa y sacrifica algo: por eso un ADR sin alternativas ni consecuencias negativas es sospechoso de una decisión ya tomada y justificada después. Las alternativas deben ser reales (algo que se habría podido hacer) y deben incluir «no hacer nada» o «hacer menos» cuando corresponde. Un **trade-off** es la pareja ganancia-sacrificio de una alternativa: separar la revisión de archivos gana aislamiento y escalado, y sacrifica la transacción local y suma operación. Escribir el sacrificio es lo que permite reabrir la decisión cuando ese sacrificio deja de ser aceptable.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-008 — Restricciones, riesgos y compromisos entre atributos](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md):

Una entidad evalúa biometría: reduce fraude, pero agrega datos sensibles, exclusión y dependencia. Compara biometría obligatoria, opcional con alternativa y no adopción; incluye borrado y apelación.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-008 — Restricciones, riesgos y compromisos entre atributos](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md)) son:

- **solo existe una opción “viable”** — causa: preferencias se presentaron como restricciones. Corrección: verifica fuente, vigencia y autoridad de cada límite.
- **riesgo escrito como sustantivo** — causa: faltan causa y consecuencia. Corrección: formula cadena causal, señal, mitigación y contingencia.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un trade-off no significa que toda mejora empeore necesariamente otra cosa. ([SE-008](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md), [SE-007](../../../classes/part-00-ingenieria-de-software-como-profesion/se-007-calidad-interna-externa-y-calidad-en-uso/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [ADR](../a/adr.md), [Análisis de sensibilidad](../a/analisis-de-sensibilidad.md), [Contingencia](../c/contingencia.md), [Exposición](../e/exposicion.md), [Mitigación](../m/mitigacion.md), [Preferencia](../p/preferencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-008 — Restricciones, riesgos y compromisos entre atributos](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-333 — Trade-offs, ADR y evaluación de alternativas](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

**También se usa en** (10 clases más lo mencionan; las que más):

[SE-334](../../../classes/part-27-arquitectura-de-software-y-dominio/se-334-arquitectura-socio-tecnica-y-limites-de-equipo/README.md), [SE-009](../../../classes/part-00-ingenieria-de-software-como-profesion/se-009-sostenibilidad-inclusion-y-responsabilidad-social/README.md), [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md), [SE-007](../../../classes/part-00-ingenieria-de-software-como-profesion/se-007-calidad-interna-externa-y-calidad-en-uso/README.md), [SE-059](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md), [SE-093](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Nygard, «Documenting Architecture Decisions»](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — origen de los ADR; autoridad: Michael Nygard.
- [MADR, Markdown Architectural Decision Records](https://adr.github.io/madr/) — plantilla de ADR; autoridad: comunidad ADR.
- [SEI, «The Architecture Tradeoff Analysis Method»](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/) — análisis de compromisos contra escenarios; autoridad: Software Engineering Institute (Carnegie Mellon).
- [Fowler, «Architecture Decision Record»](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html) — práctica de ADR; autoridad: Martin Fowler.
- [Python: `re`](https://docs.python.org/3/library/re.html) — expresiones regulares del comprobador; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Traceability](./traceability.md) · [Traducción →](./traduccion.md)
