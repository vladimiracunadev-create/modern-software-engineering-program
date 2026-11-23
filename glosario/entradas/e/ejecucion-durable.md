# Ejecución durable

[↑ Glosario](../../README.md) · [← Eficiencia de un bus](./eficiencia-de-un-bus.md) · [Ejecución en sombra →](./ejecucion-en-sombra.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Ejecución cuyo progreso se persiste para poder reanudarla tras una interrupción.

Definición de trabajo de [SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md).

## Por qué importa

La clase donde se define, [SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md), existe con este propósito: la clase existe para que un sistema con LLM **sobreviva a sus propias interrupciones sin repetir ni perder efectos**.

## Cómo funciona

Según [SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md):

Un workflow con modelos dura segundos o minutos y depende de procesos que se reinician (despliegues, escalado, fallos) y de servicios que fallan. Sin persistencia del progreso, cada interrupción obliga a empezar de cero: se pierde el tiempo, se vuelve a pagar el modelo y, peor, se repiten efectos. Los motores de **ejecución durable** (Temporal es un ejemplo documentado) resuelven esto persistiendo un historial de eventos y reanudando tras una caída reproduciendo el código hasta el punto donde se quedó. No hace falta un motor para entender el principio: un diario de pasos en una base transaccional ya lo ilustra.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md)) son: El diario es una base SQLite en memoria con un solo paso con efecto; el servicio externo es simulado y respeta la clave; la tormenta de reintentos usa clientes sincronizados sin cola ni limitación de tasa; no se probó ningún motor de ejecución durable ni ningún proveedor real. El siguiente paso, `SE-597`, trata cómo se mide un sistema con LLM: evaluaciones, ruido, jueces, trazas y puertas de release.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-595](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Interrupción](../i/interrupcion.md), [Progreso](../p/progreso.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Diario de pasos](../d/diario-de-pasos.md), [Dispersión](../d/dispersion.md), [Idempotencia](../i/idempotencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-595](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md), [SE-411](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md), [SE-417](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md), [SE-418](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md), [SE-592](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md), [SE-597](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Eficiencia de un bus](./eficiencia-de-un-bus.md) · [Ejecución en sombra →](./ejecucion-en-sombra.md)
