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

[SE-560 — Context engineering y reducción de ambigüedad](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Caso medido en la sección «El espacio de interpretaciones» de [SE-565 — De la intención a la especificación durable](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md):

Cada ambigüedad es una decisión que alguien tomará. Si una especificación deja sin resolver ocho decisiones con dos o tres lecturas plausibles cada una, admite el producto de esas lecturas en comportamientos distintos, no la suma. Esto explica por qué dos implementaciones «correctas» de la misma frase difieren en detalles que nadie discutió: no eligieron mal, eligieron. También explica por qué la sensación de que «el agente se equivoca a veces» es engañosa: con muchas ambigüedades abiertas, el agente rara vez coincide con una intención concreta aunque cada una de sus decisiones sea razonable.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-560 — Context engineering y reducción de ambigüedad](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md)) son:

- **Cada ejecución produce una variante distinta** — causa: muchas dimensiones abiertas. Corrección: enumerar dimensiones y fijar las consecuentes.
- **El asistente alterna entre dos estilos** — causa: reglas contradictorias. Corrección: detectar pares y escribir una precedencia.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-560 — Context engineering y reducción de ambigüedad](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: una enumeración exacta de interpretaciones, una simulación de recuperación con versiones y un detector real de contradicciones sobre archivos sintéticos.

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
