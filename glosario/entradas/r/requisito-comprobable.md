# Requisito comprobable

[↑ Glosario](../../README.md) · [← Requirements Engineer / Business Systems Analyst](./requirements-engineer-business-systems-analyst.md) · [Requisito derivado →](./requisito-derivado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Frase con un disparador y una respuesta para la que existe una observación que podría refutarla.

Definición de trabajo de [SE-565 — De la intención a la especificación durable](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md).

## Por qué importa

La clase donde se define, [SE-565 — De la intención a la especificación durable](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md), existe con este propósito: la clase existe para que dejes de tratar la intención como si ya fuera una especificación.

## Cómo funciona

[SE-565 — De la intención a la especificación durable](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-565 — De la intención a la especificación durable](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo toma la frase «avisa a los estudiantes antes de que venzan las entregas, rápido y sin molestar» y la convierte en seis requisitos con identificador: `RF-01` (avisos a las 72, 24 y 1 hora antes), `RF-02` (no repetir un aviso ya enviado), `RF-03` (no avisar si la entrega está `ENTREGADA`), `RF-04` (no avisar si está `SILENCIADA`), `RF-05` (no avisar después del vencimiento) y `RF-06` (tras una caída del servicio, enviar solo el aviso del umbral más cercano).

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-565 — De la intención a la especificación durable](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md)) son:

- **El agente entrega algo que funciona y no es lo que se quería** — causa: ambigüedades sin resolver que el agente resolvió. Corrección: resolver las de mayor costo y declarar las que se delegan.
- **Las pruebas pasan pero el comportamiento es otro** — causa: las pruebas las escribió quien implementó, a partir de su propia lectura. Corrección: escribir los criterios en la especificación antes de implementar.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-565 — De la intención a la especificación durable](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md)) son: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos; no se invocó ningún modelo de lenguaje ni se observó ningún equipo o sistema reales. Las 125 frases, las ocho decisiones abiertas, la independencia entre ellas, los 24 requisitos y los 12 defectos son construcciones del autor, y el revisor se escribió conociendo las frases que lo evalúan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-564](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Disparador](../d/disparador.md), [Observación](../o/observacion.md), [Ambigüedad](../a/ambiguedad.md), [Deriva](../d/deriva.md), [Especificación](../e/especificacion.md), [Intención](../i/intencion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-565 — De la intención a la especificación durable](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) — significado de DEBE, NO DEBE y DEBERÍA en especificaciones; autoridad: IETF.
- [Mavin et al., «Easy Approach to Requirements Syntax (EARS)»](https://doi.org/10.1109/RE.2009.9) — plantillas de requisitos; autoridad: IEEE International Requirements Engineering Conference, 2009.
- [Cucumber: Gherkin](https://cucumber.io/docs/gherkin/) — sintaxis de criterios de aceptación ejecutables; autoridad: documentación del proyecto.

---

[↑ Glosario](../../README.md) · [← Requirements Engineer / Business Systems Analyst](./requirements-engineer-business-systems-analyst.md) · [Requisito derivado →](./requisito-derivado.md)
