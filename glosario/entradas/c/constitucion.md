# Constitución

[↑ Glosario](../../README.md) · [← Consistencia y presión del buzón](./consistencia-y-presion-del-buzon.md) · [Construcción reproducible →](./construccion-reproducible.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Conjunto corto de principios obligatorios y comprobables contra los que se evalúa cada fase posterior del proceso.

Definición de trabajo de [SE-566 — Constitución, specify, clarify, plan y tasks](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md).

## Por qué importa

En [SE-566 — Constitución, specify, clarify, plan y tasks](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md), el tema «La constitución del proyecto» importa porque fija lo que ningún plan puede decidir por comodidad.

## Cómo funciona

Según [SE-566 — Constitución, specify, clarify, plan y tasks](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md):

Una constitución es la lista corta de principios que todo plan debe respetar y que no se discuten en cada función. Spec Kit la trata como el conjunto de principios contra los que se evalúa cada fase posterior. Para *Avisos* bastan tres: `C1`, no se guardan datos personales fuera de la base del servicio; `C2`, no se usa telemetría de terceros; `C3`, toda tarea de código tiene antes una prueba. Dos propiedades las hacen útiles. Son **obligaciones, no aspiraciones**: «DEBE» y no «se procurará», con el sentido que fija RFC 2119. Y son **comprobables**: cada una se acompaña de una observación que podría refutarla, por ejemplo «ninguna decisión del plan menciona almacenamiento externo con datos de estudiantes».

Según [SE-566 — Constitución, specify, clarify, plan y tasks](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* escribe la constitución con tres principios, genera la especificación de diez requisitos y ejecuta una ronda de clarificación. Estima el impacto de las ambigüedades abiertas y elige las cinco más caras: qué ocurre con el aviso de una hora si el de 24 no se envió, si el silencio vale por entrega o global, si el cambio de vencimiento reabre umbrales, qué cuenta como «entregada» cuando el docente revierte una entrega y si el canal que falla se reintenta indefinidamente. Las respuestas se codifican en la especificación.

## Ejemplo

Ejemplo de [SE-566 — Constitución, specify, clarify, plan y tasks](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md) (sección «Ejemplo mínimo»):

El fragmento muestra una puerta mecánica entre plan y constitución. Antes de ejecutarlo, predice cuántas decisiones marca.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El plan introduce tecnología que la organización no permite** — causa: la constitución no existe o no se comprueba. Corrección: escribir tres principios comprobables y evaluarlos al generar el plan. ([SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una constitución es la lista corta de principios que todo plan debe respetar y que no se discuten en cada función. ([SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md))
- Traslada el análisis a otro dominio (por ejemplo, un sistema de turnos para una biblioteca con avisos de devolución): cambia la constitución, los requisitos y las tareas y conserva el procedimiento de comprobar el plan contra los principios, ordenar las preguntas por costo esperado y planificar las tareas por dependencias. ([SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](./conjunto.md), [Proceso](../p/proceso.md), [Análisis entre artefactos](../a/analisis-entre-artefactos.md), [Clarificación](./clarificacion.md), [Plan](../p/plan.md), [Ruta crítica](../r/ruta-critica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-566 — Constitución, specify, clarify, plan y tasks](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md), [SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md), [SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md), [SE-568](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Stripe](../../../casos/exito/stripe.md), [Slack](../../../casos/exito/slack.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Spec Kit — referencia del proceso agentic](https://github.github.io/spec-kit/reference/agentic-sdd.html) — secuencia de comandos, clarificación, análisis y tareas; autoridad: GitHub y mantenedores de la comunidad.
- [Spec Kit — repositorio](https://github.com/github/spec-kit) — plantillas, extensiones y catálogos; autoridad: GitHub y mantenedores.
- [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) — vocabulario normativo; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Consistencia y presión del buzón](./consistencia-y-presion-del-buzon.md) · [Construcción reproducible →](./construccion-reproducible.md)
