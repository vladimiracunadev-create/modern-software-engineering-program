# Baja

[↑ Glosario](../../README.md) · [← Backtracking](./backtracking.md) · [Balance y rotaciones →](./balance-y-rotaciones.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Cliente o ingreso que deja de pagar en un periodo.

Definición de trabajo de [SE-409 — Qué hace distinto a un producto SaaS](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md).

## Por qué importa

La clase donde se define, [SE-409 — Qué hace distinto a un producto SaaS](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), existe con este propósito: la clase existe para que dejes de tratar un producto SaaS como «una aplicación web con suscripción» y lo analices como lo que es: un sistema que se entrega continuamente a muchos clientes a la vez desde una sola operación, y cuyo ingreso no ocurre en la venta sino cada ciclo.

## Cómo funciona

Según [SE-409 — Qué hace distinto a un producto SaaS](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md):

Compartir infraestructura entre clientes es lo que permite cobrar 49 por un servicio que, dedicado, costaría cientos. Esa economía existe porque el costo fijo se reparte: en el modelo de la clase, el costo mensual por cliente de una solución totalmente compartida baja de 62 con diez clientes a 2,6 con mil, mientras que la dedicada se queda en 90. La contrapartida es que los clientes dejan de estar separados por construcción: uno puede ver datos de otro por un filtro olvidado o puede consumir tanta capacidad que los demás esperen. `SE-342` explica los modelos de aislamiento y sus fallos; `SE-410` mide el vecino ruidoso con y sin cuotas.

Según [SE-409 — Qué hace distinto a un producto SaaS](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md):

El equipo de *Tablero* quiere decidir si el siguiente trimestre invierte en un aislamiento de datos más fuerte o en una función que los clientes piden. Antes de discutir, calcula con datos propios cuatro números: la descomposición del MRR de los últimos seis meses, la retención neta y bruta, la distribución de bajas por motivo declarado y el costo por cliente de su infraestructura. Encuentra que la retención neta es 118 % pero la bruta es 88 %: los clientes que se quedan amplían su plan lo suficiente para ocultar que uno de cada ocho clientes se va, y que el motivo más frecuente de baja (31 %) es «lentitud en cuentas grandes».

## Ejemplo

Ejemplo de [SE-409 — Qué hace distinto a un producto SaaS](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md) (sección «Ejemplo profesional»):

El equipo de *Tablero* quiere decidir si el siguiente trimestre invierte en un aislamiento de datos más fuerte o en una función que los clientes piden. Antes de discutir, calcula con datos propios cuatro números: la descomposición del MRR de los últimos seis meses, la retención neta y bruta, la distribución de bajas por motivo declarado y el costo por cliente de su infraestructura.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Su variación entre dos meses se explica con cuatro movimientos: clientes nuevos, expansión (clientes que pagan más: más puestos, plan superior), contracción (pagan menos sin irse) y bajas. ([SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-133](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md), [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md), [SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md), [SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [CAC (costo de adquisición de cliente)](../c/cac-costo-de-adquisicion-de-cliente.md), [Expansión y contracción](../e/expansion-y-contraccion.md), [Inquilino](../i/inquilino.md), [MRR](../m/mrr.md), [Plano de control](../p/plano-de-control.md), [Retención](../r/retencion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-409 — Qué hace distinto a un producto SaaS](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (276 clases más lo mencionan; las que más):

[SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), [SE-390](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md), [SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md), [SE-446](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md), [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md), [SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md), [SE-293](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md), [SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «churn».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Backtracking](./backtracking.md) · [Balance y rotaciones →](./balance-y-rotaciones.md)
