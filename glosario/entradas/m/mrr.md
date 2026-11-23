# MRR

[↑ Glosario](../../README.md) · [← Motor](./motor.md) · [MSB/LSB →](./msb-lsb.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Suma de lo que los clientes activos pagan por mes, normalizado a un mes.

Definición de trabajo de [SE-409 — Qué hace distinto a un producto SaaS](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-594 — Embeddings, recuperación y agentic RAG](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md): Media del inverso de la posición del fragmento correcto.

## Por qué importa

La clase donde se define, [SE-409 — Qué hace distinto a un producto SaaS](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), existe con este propósito: la clase existe para que dejes de tratar un producto SaaS como «una aplicación web con suscripción» y lo analices como lo que es: un sistema que se entrega continuamente a muchos clientes a la vez desde una sola operación, y cuyo ingreso no ocurre en la venta sino cada ciclo.

## Cómo funciona

Según [SE-409 — Qué hace distinto a un producto SaaS](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md):

El ingreso recurrente mensual (MRR) es la suma de lo que cada cliente activo paga por mes, normalizado a un mes. Su variación entre dos meses se explica con cuatro movimientos: clientes nuevos, expansión (clientes que pagan más: más puestos, plan superior), contracción (pagan menos sin irse) y bajas. En el experimento, con 366 clientes de pago en septiembre y 440 en octubre, el ingreso pasó de 61 034 a 78 808: **61 034 + 3 610 (nuevos) + 19 850 (expansión) − 3 300 (contracción) − 2 386 (bajas) = 78 808**.

Según [SE-409 — Qué hace distinto a un producto SaaS](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md):

El equipo de *Tablero* quiere decidir si el siguiente trimestre invierte en un aislamiento de datos más fuerte o en una función que los clientes piden. Antes de discutir, calcula con datos propios cuatro números: la descomposición del MRR de los últimos seis meses, la retención neta y bruta, la distribución de bajas por motivo declarado y el costo por cliente de su infraestructura. Encuentra que la retención neta es 118 % pero la bruta es 88 %: los clientes que se quedan amplían su plan lo suficiente para ocultar que uno de cada ocho clientes se va, y que el motivo más frecuente de baja (31 %) es «lentitud en cuentas grandes».

## Ejemplo

Ejemplo de [SE-409 — Qué hace distinto a un producto SaaS](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md) (sección «Ejemplo mínimo»):

Dados los registros de suscripción de dos meses, descomponer la variación del MRR y comprobar que cuadra:

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- (2) Se compara el MRR con el cobrado, que no son lo mismo: el MRR normaliza a un mes los planes anuales y el procesador cobra el año completo el mes de la renovación. ([SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-133](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md), [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md), [SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md), [SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Activo](../a/activo.md), [Fragmento](../f/fragmento.md), [Abstención](../a/abstencion.md), [Acierto@k](../a/acierto-k.md), [Baja](../b/baja.md), [BM25](../b/bm25.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-409 — Qué hace distinto a un producto SaaS](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.
- [SE-594 — Embeddings, recuperación y agentic RAG](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «ingreso recurrente mensual».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Motor](./motor.md) · [MSB/LSB →](./msb-lsb.md)
