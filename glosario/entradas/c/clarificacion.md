# Clarificación

[↑ Glosario](../../README.md) · [← Cita de proximidad](./cita-de-proximidad.md) · [Clase base frágil →](./clase-base-fragil.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Ronda de preguntas dirigidas sobre las partes insuficientemente especificadas cuyas respuestas se codifican en la especificación.

Definición de trabajo de [SE-566 — Constitución, specify, clarify, plan y tasks](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md).

## Por qué importa

La clase donde se define, [SE-566 — Constitución, specify, clarify, plan y tasks](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md), existe con este propósito: la clase existe para que veas el proceso de especificación como una cadena de artefactos con puertas entre ellos y no como un único documento que se escribe de una vez.

## Cómo funciona

Según [SE-566 — Constitución, specify, clarify, plan y tasks](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md):

La especificación (`SE-565`) declara el qué y el porqué. La clarificación es la fase en que el proceso formula preguntas dirigidas a las partes insuficientemente especificadas; Spec Kit limita cada ronda a cinco y codifica las respuestas en la propia especificación, de modo que el artefacto resultante ya no depende de la conversación. El límite no es un detalle de la herramienta sino una restricción útil: obliga a elegir. La pregunta no es «qué falta» sino «qué falta que, si se supone mal, sale más caro». Una ambigüedad tiene dos propiedades que importan: cuántas lecturas plausibles admite y cuánto cuesta equivocarse. La probabilidad de equivocarse al suponer es 1 menos la inversa del número de lecturas y el costo esperado es el producto de ambos.

Según [SE-566 — Constitución, specify, clarify, plan y tasks](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* escribe la constitución con tres principios, genera la especificación de diez requisitos y ejecuta una ronda de clarificación. Estima el impacto de las ambigüedades abiertas y elige las cinco más caras: qué ocurre con el aviso de una hora si el de 24 no se envió, si el silencio vale por entrega o global, si el cambio de vencimiento reabre umbrales, qué cuenta como «entregada» cuando el docente revierte una entrega y si el canal que falla se reintenta indefinidamente. Las respuestas se codifican en la especificación.

## Ejemplo

Ejemplo de [SE-566 — Constitución, specify, clarify, plan y tasks](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* escribe la constitución con tres principios, genera la especificación de diez requisitos y ejecuta una ronda de clarificación. Estima el impacto de las ambigüedades abiertas y elige las cinco más caras: qué ocurre con el aviso de una hora si el de 24 no se envió, si el silencio vale por entrega o global, si el cambio de vencimiento reabre umbrales, qué cuenta como «entregada» cuando el docente revierte una entrega y si el canal que falla se reintenta indefinidamente. Las respuestas se codifican en la especificación.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-566 — Constitución, specify, clarify, plan y tasks](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md)) son:

- **El plan introduce tecnología que la organización no permite** — causa: la constitución no existe o no se comprueba. Corrección: escribir tres principios comprobables y evaluarlos al generar el plan.
- **Se hacen veinte preguntas y se contestan tres** — causa: no hay presupuesto ni orden. Corrección: limitar la ronda y ordenar por costo esperado.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-566 — Constitución, specify, clarify, plan y tasks](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md)) son: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos; no se ejecutó ninguna herramienta de Spec Kit, no se invocó ningún modelo de lenguaje ni se observó ningún equipo o sistema reales. Los artefactos, las incoherencias inyectadas, los impactos, las lecturas por ambigüedad, las duraciones y las dependencias son construcciones del autor, y el analizador se escribió conociendo los defectos que debe encontrar.

## Relación con otros conceptos

- **Prerrequisito:** [Especificación](../e/especificacion.md).
- **Ver también:** [Sobre](../s/sobre.md), [Análisis entre artefactos](../a/analisis-entre-artefactos.md), [Constitución](./constitucion.md), [Plan](../p/plan.md), [Ruta crítica](../r/ruta-critica.md), [Tarea](../t/tarea.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-566 — Constitución, specify, clarify, plan y tasks](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md), [SE-568](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Spec Kit — referencia del proceso agentic](https://github.github.io/spec-kit/reference/agentic-sdd.html) — secuencia de comandos, clarificación, análisis y tareas; autoridad: GitHub y mantenedores de la comunidad.
- [Spec Kit — repositorio](https://github.com/github/spec-kit) — plantillas, extensiones y catálogos; autoridad: GitHub y mantenedores.
- [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) — vocabulario normativo; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Cita de proximidad](./cita-de-proximidad.md) · [Clase base frágil →](./clase-base-fragil.md)
