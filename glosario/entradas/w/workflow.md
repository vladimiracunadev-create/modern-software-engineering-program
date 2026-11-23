# Workflow

[↑ Glosario](../../README.md) · [← WIT](./wit.md) · [Working set →](./working-set.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Sistema donde el código fija los pasos y el modelo se usa dentro de ellos.

Definición de trabajo de [SE-589 — Workflows frente a agentes: cuándo no usar un agente](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md).

## Por qué importa

En [SE-589 — Workflows frente a agentes: cuándo no usar un agente](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md), el tema «Workflow frente a agente» importa porque es la primera decisión de costo, latencia y riesgo del sistema.

## Cómo funciona

Según [SE-589 — Workflows frente a agentes: cuándo no usar un agente](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md):

La definición operativa es una pregunta: **¿qué componente elige la próxima acción?** En un workflow la elige el código: un `if`, una tabla de rutas, una secuencia fija en la que el modelo rellena huecos (clasificar, redactar, extraer). En un agente la elige el modelo en cada vuelta, a partir de lo que ha visto hasta ese momento. Esa frase contiene todas las consecuencias: el workflow es predecible y barato porque su grafo de ejecución existe antes de la entrada; el agente es flexible porque su grafo se construye sobre la marcha, y por eso mismo no se puede revisar de antemano, solo acotar.

Según [SE-589 — Workflows frente a agentes: cuándo no usar un agente](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md):

La coordinación de un programa con 40 cursos decide el asistente de *Avisos*. Registra durante dos semanas las solicitudes reales sin automatizar nada y las clasifica en tres grupos: consultas de política, cambios de configuración e investigaciones. Para las dos primeras escribe workflows con un solo paso de modelo (redactar con datos ya consultados) y pone una prueba por camino. Para las investigaciones diseña un agente con tres herramientas de solo lectura, un presupuesto de ocho pasos y una salida obligatoria: o devuelve un informe con las evidencias que citó, o escala a una persona con lo reunido. El enrutador es una clasificación con umbral: lo que no clasifica con confianza va a la persona. El equipo fija la condición de revisión:

## Ejemplo

Ejemplo de [SE-589 — Workflows frente a agentes: cuándo no usar un agente](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md) (sección «Ejemplo mínimo»):

El workflow gasta dos llamadas siempre; el agente gasta al menos dos (una acción y la respuesta final) y puede gastar diez. Para este tipo de solicitud, la segunda versión paga flexibilidad que no usa.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Esa frase contiene todas las consecuencias: el workflow es predecible y barato porque su grafo de ejecución existe antes de la entrada; el agente es flexible porque su grafo se construye sobre la marcha, y por eso mismo no se puede revisar de antemano, solo acotar. ([SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md))
- Un `while` donde el código decide la condición con reglas es un workflow; uno donde la decide el modelo es un agente. ([SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-551](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-551-taller-un-mismo-cambio-con-cinco-metodologias/README.md), [SE-552](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-552-proyecto-politica-metodologica-de-equipo-con-evidencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Modelo](../m/modelo.md), [Agencia excesiva](../a/agencia-excesiva.md), [Agente](../a/agente.md), [Escalar](../e/escalar.md), [Híbrido](../h/hibrido.md), [Presupuesto de pasos](../p/presupuesto-de-pasos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-589 — Workflows frente a agentes: cuándo no usar un agente](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-599](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-599-taller-elegir-y-degradar-un-patron-agentico/README.md), [SE-596](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md), [SE-600](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md), [SE-590](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md), [SE-586](../../../classes/part-48-harness-y-agentic-engineering/se-586-ai-dlc-gobierno-y-vibe-coding-frente-a-agentic-engineering/README.md), [SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md), [SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md), [SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← WIT](./wit.md) · [Working set →](./working-set.md)
