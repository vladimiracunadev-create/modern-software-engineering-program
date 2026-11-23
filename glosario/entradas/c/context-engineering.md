# Context engineering

[↑ Glosario](../../README.md) · [← Contenido no confiable](./contenido-no-confiable.md) · [Context switch →](./context-switch.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Diseño del conjunto de información, su forma y su precedencia que se aporta al modelo en cada llamada.

Definición de trabajo de [SE-560 — Context engineering y reducción de ambigüedad](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md).

## Por qué importa

La clase donde se define, [SE-560 — Context engineering y reducción de ambigüedad](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md), existe con este propósito: la clase existe para que dejes de ajustar el texto de las peticiones y empieces a diseñar el conjunto de información con el que el modelo trabaja.

## Cómo funciona

[SE-560 — Context engineering y reducción de ambigüedad](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Caso medido en la sección «Context engineering: diseñar el espacio de respuestas» de [SE-560 — Context engineering y reducción de ambigüedad](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md):

Escribir una buena petición es una parte del problema; el resto es todo lo que acompaña a la petición. El contexto de una llamada incluye instrucciones del sistema, convenciones del proyecto, el historial de la conversación, archivos, resultados de herramientas y documentos recuperados, y compite por una ventana finita (`SE-553`). La guía de Anthropic lo plantea como la tarea de encontrar el conjunto más pequeño posible de información de alta señal que haga probable el resultado deseado.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-560 — Context engineering y reducción de ambigüedad](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md)) son:

- **Cada ejecución produce una variante distinta** — causa: muchas dimensiones abiertas. Corrección: enumerar dimensiones y fijar las consecuentes.
- **El asistente alterna entre dos estilos** — causa: reglas contradictorias. Corrección: detectar pares y escribir una precedencia.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-560 — Context engineering y reducción de ambigüedad](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: una enumeración exacta de interpretaciones, una simulación de recuperación con versiones y un detector real de contradicciones sobre archivos sintéticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-559](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](./conjunto.md), [Modelo](../m/modelo.md), [Precedencia](../p/precedencia.md), [Contradicción](./contradiccion.md), [Dimensión de decisión](../d/dimension-de-decision.md), [Interpretación](../i/interpretacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-560 — Context engineering y reducción de ambigüedad](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md), [SE-559](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md), [SE-555](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md), [SE-578](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md), [SE-580](../../../classes/part-48-harness-y-agentic-engineering/se-580-gestion-de-contexto-resets-y-handoffs/README.md), [SE-593](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md), [SE-598](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md).

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

[↑ Glosario](../../README.md) · [← Contenido no confiable](./contenido-no-confiable.md) · [Context switch →](./context-switch.md)
