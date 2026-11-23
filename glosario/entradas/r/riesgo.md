# Riesgo

[↑ Glosario](../../README.md) · [← RFC](./rfc.md) · [Riesgo aceptado →](./riesgo-aceptado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Un **riesgo** es, en el programa, un evento incierto que, si ocurre, afecta a lo que se persigue. La palabra cambia de escala según la clase, siempre con la idea de incertidumbre más consecuencia:

- **En un proyecto** ([SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md)): un evento incierto futuro con una causa, un efecto, una probabilidad, un impacto, un disparador y una respuesta.
- **En la estrategia de pruebas** ([SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md)): la pérdida esperada de un componente, estimada como probabilidad de defecto por impacto.
- **En sistemas críticos** ([SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md)): la combinación de la gravedad de un daño posible y la probabilidad de que ocurra.
- **En una restricción de diseño** ([SE-008](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md)): una cadena causal con señal, mitigación y contingencia; la clase advierte que un riesgo escrito como sustantivo («rendimiento») no sirve.

## Por qué importa

Decide dónde se gasta el esfuerzo limitado. [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md) usa el riesgo para priorizar pruebas: no todo componente merece la misma inversión, y la pérdida esperada ordena las decisiones. [SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md) lo usa para gobernar un proyecto: Boehm propuso ordenar los riesgos por exposición, el producto de probabilidad y pérdida, y revisar la lista de los principales cada vez.

## Cómo funciona

Para que un riesgo sirva, se describe como cadena causal, no como etiqueta. [SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md) pide escribirlo con una **causa**, un **evento** y un **efecto** («si el proveedor de identidad cambia su contrato, la integración se retrasa»), estimarlo con probabilidad e impacto y acompañarlo de un **disparador** (la señal de que se está materializando), una **respuesta** (reducir, evitar, aceptar o transferir) y un **responsable**. Se mantiene separado de otros registros: tareas (se hacen), problemas o *issues* (ya ocurrieron), supuestos (se creen) y decisiones. En una pérdida esperada ([SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md)), la cuenta es probabilidad de defecto por impacto; en seguridad funcional ([SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md)), se combinan gravedad y probabilidad para clasificar el daño posible.

## Ejemplo

En [SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md), «el proveedor de identidad cambia su contrato» tiene una causa (cambio del proveedor), un evento (cambio del contrato), un efecto (retraso de la integración), un disparador (aviso del proveedor), una respuesta y un responsable. En [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md), un componente con alta probabilidad de defecto y alto impacto recibe más pruebas que uno de impacto bajo, aunque tenga el mismo tamaño.

## Errores y confusiones comunes

- **Una hoja de riesgos que mezcla tareas, problemas y creencias.** Todo se llama «riesgo»; corrección ([SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md)): clasificar en cuatro registros con campos distintos.
- **La contingencia se agota con un único evento.** Riesgos con causa común tratados como independientes; corrección: registrar las causas comunes y reservar por percentil.
- **Un riesgo escrito como sustantivo.** Faltan causa y consecuencia; corrección ([SE-008](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md)): formular cadena causal, señal, mitigación y contingencia.

## Límites y cuándo no aplica

Las tres definiciones no son intercambiables: la pérdida esperada de [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md) es una estimación numérica para priorizar pruebas, mientras que la combinación de gravedad y probabilidad de [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md) clasifica daños con normas de seguridad, donde el producto de números no basta por sí solo. Las cifras de probabilidad e impacto son estimaciones y la exposición de Boehm ordena, no predice. Al usar la palabra hay que confirmar a qué escala se refiere.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md), [SE-007](../../../classes/part-00-ingenieria-de-software-como-profesion/se-007-calidad-interna-externa-y-calidad-en-uso/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Combinación](../c/combinacion.md), [Componente](../c/componente.md), [Daño](../d/dano.md), [Disparador](../d/disparador.md), [Contingencia](../c/contingencia.md), [Exposición](../e/exposicion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-008 — Restricciones, riesgos y compromisos entre atributos](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-187 — Riesgos, supuestos, issues y decisiones](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-421 — Calidad por riesgo y propósito de las pruebas](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-445 — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (355 clases más lo mencionan; las que más):

[SE-534](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md), [SE-552](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-552-proyecto-politica-metodologica-de-equipo-con-evidencia/README.md), [SE-299](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md), [SE-586](../../../classes/part-48-harness-y-agentic-engineering/se-586-ai-dlc-gobierno-y-vibe-coding-frente-a-agentic-engineering/README.md), [SE-610](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md), [SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md), [SE-196](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md), [SE-449](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Riesgos».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Boehm, «Software risk management: principles and practices» (IEEE Software, 1991)](https://doi.org/10.1109/52.62930) — identificación y priorización de riesgos de proyecto; autoridad: IEEE Software.
- [SEI: Software risk management](https://www.sei.cmu.edu/library/software-risk-management/) — recursos de gestión de riesgos de software; autoridad: Software Engineering Institute, Carnegie Mellon University.
- [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) — evaluación de riesgos; autoridad: NIST.
- [Nygard, «Documenting architecture decisions» (2011)](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — registros breves de decisiones; autoridad: autor de la práctica.
- [Architectural Decision Records](https://adr.github.io/) — plantillas y vocabulario de registros de decisión; autoridad: comunidad ADR.

---

[↑ Glosario](../../README.md) · [← RFC](./rfc.md) · [Riesgo aceptado →](./riesgo-aceptado.md)
