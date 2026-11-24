# Agente

[↑ Glosario](../../README.md) · [← Agencia excesiva](./agencia-excesiva.md) · [Agente en cuarentena →](./agente-en-cuarentena.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Un **agente** es un sistema donde el modelo decide el siguiente paso y el uso de herramientas en cada vuelta. [SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md) lo define con una pregunta operativa: ¿qué componente elige la próxima acción? Si la elige el código (un `if`, una tabla de rutas, una secuencia fija en la que el modelo rellena huecos), es un *workflow*; si la elige el modelo a partir de lo que ha visto hasta ese momento, es un agente.

## Por qué importa

De esa frase salen todas las consecuencias de diseño. El workflow es predecible y barato porque su grafo de ejecución existe antes de la entrada; el agente es flexible porque su grafo se construye sobre la marcha, y por eso mismo no se puede revisar de antemano, solo acotar. Elegir entre uno y otro decide cuánto control, costo y capacidad de prueba se tiene.

## Cómo funciona

El agente repite un ciclo: observa el estado, el modelo elige una acción (normalmente una herramienta), el arnés la ejecuta y el resultado vuelve al contexto. Termina por convergencia o por una condición de parada. Como el camino no está fijado, se controla desde fuera: herramientas disponibles, permisos, presupuesto de pasos y salida obligatoria. Un `while` donde el código decide la condición con reglas es un workflow; uno donde la decide el modelo es un agente ([SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md)).

## Ejemplo

[SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md): la coordinación de un programa con 40 cursos decide el asistente de *Avisos*. Clasifica dos semanas de solicitudes reales en consultas de política, cambios de configuración e investigaciones. Para las dos primeras escribe workflows con un solo paso de modelo y una prueba por camino. Para las investigaciones diseña un agente con tres herramientas de solo lectura, un presupuesto de ocho pasos y una salida obligatoria: un informe con las evidencias que citó, o escalada a una persona. Lo que no se clasifica con confianza va a la persona.

## Errores y confusiones comunes

Llamar «agente» a cualquier uso de un modelo: si el código fija la secuencia, es un workflow. Dar a un agente más autonomía de la que su verificación permite.

## Límites y cuándo no aplica

Donde el camino es conocido de antemano, un workflow es más barato, predecible y fácil de probar; el agente solo se justifica cuando la tarea exige decidir el camino sobre la marcha. Las cifras del caso (40 cursos, ocho pasos) son del ejemplo de la clase, no de una medición.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-551](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-551-taller-un-mismo-cambio-con-cinco-metodologias/README.md), [SE-552](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-552-proyecto-politica-metodologica-de-equipo-con-evidencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Siguiente paso](../s/siguiente-paso.md), [Herramientas](../h/herramientas.md), [Modelo](../m/modelo.md), [Agencia excesiva](./agencia-excesiva.md), [Escalar](../e/escalar.md), [Híbrido](../h/hibrido.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-589 — Workflows frente a agentes: cuándo no usar un agente](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (611 clases más lo mencionan; las que más):

[SE-572](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md), [SE-584](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md), [SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md), [SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md), [SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md), [SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md), [SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md), [SE-595](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Uber](../../../casos/exito/uber.md), [Stripe](../../../casos/exito/stripe.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Agencia excesiva](./agencia-excesiva.md) · [Agente en cuarentena →](./agente-en-cuarentena.md)
