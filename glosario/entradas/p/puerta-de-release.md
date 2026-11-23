# Puerta de release

[↑ Glosario](../../README.md) · [← Puerta de liberación](./puerta-de-liberacion.md) · [Puerta trasera →](./puerta-trasera.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

Regla de decisión que usa una evaluación para publicar o retener.

Definición de trabajo de [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md).

## Por qué importa

La clase donde se define, [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md), existe con este propósito: la clase existe para que trates una evaluación como lo que es, un **instrumento de medida con ruido**, y no como una prueba determinista con otro nombre.

## Cómo funciona

[SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Caso medido en la sección «La puerta de release y sus dos errores» de [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md):

Una puerta decide con una cifra. Puede equivocarse de dos maneras: dejar pasar una versión peor (**falso pase**) o rechazar una versión sana (**falso rechazo**). El costo no es simétrico: un falso pase publica una regresión; un falso rechazo retrasa un cambio y cuesta una investigación. Un umbral de 0,825 entre una versión sana de 0,85 y una regresada de 0,80 está justo en medio, así que los dos errores son igual de probables con cualquier ruido. Mover el umbral cambia uno a costa del otro; reducir el ruido mejora ambos.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md)) son: La simulación modela casos como lanzamientos independientes con probabilidades supuestas; no se evaluó ningún modelo ni producto real. El siguiente paso, `SE-550`, trata un flujo de trabajo concreto para agentes de código, ODD, con su evidencia declarada y los límites de su documentación.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-548](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Regla de decisión](../r/regla-de-decision.md), [Evaluación](../e/evaluacion.md), [Regla](../r/regla.md), [Conjunto curado](../c/conjunto-curado.md), [Falso pase](../f/falso-pase.md), [Falso rechazo](../f/falso-rechazo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-597](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md), [SE-598](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md), [SE-548](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md), [SE-550](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md), [SE-594](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md), [SE-596](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md), [SE-600](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Puerta de liberación](./puerta-de-liberacion.md) · [Puerta trasera →](./puerta-trasera.md)
