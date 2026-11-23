# Graduador

[↑ Glosario](../../README.md) · [← Gobierno](./gobierno.md) · [Grafema →](./grafema.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

Programa o regla que decide si una tarea se resolvió.

Definición de trabajo de [SE-585 — Observabilidad y evals del propio harness](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md).

## Por qué importa

La clase donde se define, [SE-585 — Observabilidad y evals del propio harness](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md), existe con este propósito: la clase existe para que puedas responder dos preguntas sobre tu propio harness:

## Cómo funciona

Según [SE-585 — Observabilidad y evals del propio harness](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md):

Anthropic describe las evaluaciones de agentes como un conjunto de tareas con un criterio de éxito (un graduador), ejecutadas varias veces porque el resultado no es determinista. Aplicado al harness, cada versión (instrucciones, permisos, parada, verificación) se ejecuta sobre las mismas tareas y se compara. SWE-bench es un ejemplo de conjunto de tareas reales con pruebas como criterio; para un equipo, el conjunto útil es el propio: las tareas que su agente hace de verdad, con las pruebas del repositorio como graduador.

Según [SE-585 — Observabilidad y evals del propio harness](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md):

El equipo quiere saber si un archivo de instrucciones más corto mejora al asistente. Reúne las ochenta tareas más frecuentes del último trimestre, cada una con su prueba como graduador, y ejecuta las dos versiones tres veces cada una. La versión corta resuelve 61 en promedio y la larga 58. Con la regla de discordancias, la diferencia no supera el umbral. El equipo no concluye «son iguales»: calcula que con ochenta tareas solo habría detectado una mejora de más de diez puntos, y decide mantener la versión corta por su menor costo de contexto, con la salvedad escrita de que no se probó mejora. La lección es separar la decisión de adoptar (por costo) de la afirmación de mejorar (no demostrada).

## Ejemplo

Ejemplo de [SE-585 — Observabilidad y evals del propio harness](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md) (sección «Ejemplo profesional»):

El equipo quiere saber si un archivo de instrucciones más corto mejora al asistente. Reúne las ochenta tareas más frecuentes del último trimestre, cada una con su prueba como graduador, y ejecuta las dos versiones tres veces cada una. La versión corta resuelve 61 en promedio y la larga 58. Con la regla de discordancias, la diferencia no supera el umbral. El equipo no concluye «son iguales»: calcula que con ochenta tareas solo habría detectado una mejora de más de diez puntos, y decide mantener la versión corta por su menor costo de contexto, con la salvedad escrita de que no se probó mejora.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Anthropic describe las evaluaciones de agentes como un conjunto de tareas con un criterio de éxito (un graduador), ejecutadas varias veces porque el resultado no es determinista. ([SE-585](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-549](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md), [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md), [SE-584](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Regla](../r/regla.md), [Tarea](../t/tarea.md), [Evaluación del harness](../e/evaluacion-del-harness.md), [Observabilidad](../o/observabilidad.md), [Potencia](../p/potencia.md), [Tarea de regresión](../t/tarea-de-regresion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-585 — Observabilidad y evals del propio harness](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Gobierno](./gobierno.md) · [Grafema →](./grafema.md)
