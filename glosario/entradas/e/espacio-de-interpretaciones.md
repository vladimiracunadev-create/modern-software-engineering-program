# Espacio de interpretaciones

[↑ Glosario](../../README.md) · [← Espacio de estados](./espacio-de-estados.md) · [Espacio de nombres →](./espacio-de-nombres.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Convierte «ambiguo» en un número.

Es uno de los temas de [SE-560 — Context engineering y reducción de ambigüedad](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md), donde se enseña como «Espacio de interpretaciones».

## Por qué importa

En [SE-560 — Context engineering y reducción de ambigüedad](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md), el tema «Espacio de interpretaciones» importa porque convierte «ambiguo» en un número

En [SE-565 — De la intención a la especificación durable](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md), el tema «Espacio de interpretaciones» importa porque cada ambigüedad multiplica los comportamientos posibles; el agente elige por ti.

## Cómo funciona

[SE-560 — Context engineering y reducción de ambigüedad](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-560 — Context engineering y reducción de ambigüedad](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones rediseña el contexto de sus asistentes. Primero enumera las seis dimensiones de «calcular la nota final» y clasifica cada una: escala, umbral, decimales y promedio ponderado quedan fijadas en el archivo de instrucciones con su fuente (el reglamento y su fecha); el redondeo queda fijado con un ejemplo de frontera; la nota ausente se marca «preguntar»: el asistente no escribe código sin que una persona decida.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-560 — Context engineering y reducción de ambigüedad](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md)) son:

- **Cada ejecución produce una variante distinta** — causa: muchas dimensiones abiertas. Corrección: enumerar dimensiones y fijar las consecuentes.
- **El asistente alterna entre dos estilos** — causa: reglas contradictorias. Corrección: detectar pares y escribir una precedencia.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-560 — Context engineering y reducción de ambigüedad](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: una enumeración exacta de interpretaciones, una simulación de recuperación con versiones y un detector real de contradicciones sobre archivos sintéticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-559](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ambigüedad](../a/ambiguedad.md), [Context engineering](../c/context-engineering.md), [Contradicción](../c/contradiccion.md), [Deriva](../d/deriva.md), [Dimensión de decisión](../d/dimension-de-decision.md), [Especificación](./especificacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-560 — Context engineering y reducción de ambigüedad](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.
- [SE-565 — De la intención a la especificación durable](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Anthropic: effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — conjunto mínimo de información de alta señal; autoridad: Anthropic.
- [Anthropic: context windows](https://docs.anthropic.com/en/docs/build-with-claude/context-windows) — la ventana como recurso finito; autoridad: documentación de Anthropic.
- [AGENTS.md](https://agents.md) — archivo de instrucciones para agentes de programación; autoridad: especificación abierta del proyecto.
- [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) — palabras clave de obligatoriedad; autoridad: IETF.
- [Wallace et al., «The Instruction Hierarchy»](https://arxiv.org/abs/2404.13208) — jerarquía de instrucciones; autoridad: preprint de OpenAI.

---

[↑ Glosario](../../README.md) · [← Espacio de estados](./espacio-de-estados.md) · [Espacio de nombres →](./espacio-de-nombres.md)
