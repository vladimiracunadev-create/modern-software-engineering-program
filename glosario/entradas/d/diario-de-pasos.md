# Diario de pasos

[↑ Glosario](../../README.md) · [← Diagrama como código](./diagrama-como-codigo.md) · [Diferencias de plataforma →](./diferencias-de-plataforma.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Registro transaccional de los pasos completados de una ejecución.

Definición de trabajo de [SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md).

## Por qué importa

En [SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md), el tema «Diario de pasos» importa porque permite reanudar sin rehacer lo hecho.

## Cómo funciona

Según [SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md):

Un workflow con modelos dura segundos o minutos y depende de procesos que se reinician (despliegues, escalado, fallos) y de servicios que fallan. Sin persistencia del progreso, cada interrupción obliga a empezar de cero: se pierde el tiempo, se vuelve a pagar el modelo y, peor, se repiten efectos. Los motores de **ejecución durable** (Temporal es un ejemplo documentado) resuelven esto persistiendo un historial de eventos y reanudando tras una caída reproduciendo el código hasta el punto donde se quedó. No hace falta un motor para entender el principio: un diario de pasos en una base transaccional ya lo ilustra.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- No hace falta un motor para entender el principio: un diario de pasos en una base transaccional ya lo ilustra. ([SE-596](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-595](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Registro](../r/registro.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Dispersión](./dispersion.md), [Ejecución durable](../e/ejecucion-durable.md), [Idempotencia](../i/idempotencia.md), [Reconciliación](../r/reconciliacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Diagrama como código](./diagrama-como-codigo.md) · [Diferencias de plataforma →](./diferencias-de-plataforma.md)
