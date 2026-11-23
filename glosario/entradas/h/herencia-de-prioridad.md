# Herencia de prioridad

[↑ Glosario](../../README.md) · [← Herencia](./herencia.md) · [Herramientas →](./herramientas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

El poseedor de un recurso hereda la prioridad más alta de quienes esperan.

Definición de trabajo de [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md).

## Por qué importa

La clase donde se define, [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md), existe con este propósito: la clase existe para que entiendas por qué, en un sistema crítico, una función correcta que llega tarde es una función que falló, y qué herramientas permiten **argumentar** que llega a tiempo: el análisis de planificación de prioridades fijas, los protocolos que acotan la inversión de prioridad y el tiempo de ejecución en el peor caso (WCET).

## Cómo funciona

Según [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md):

Con **herencia de prioridad**, la tarea que tiene el mutex hereda la prioridad más alta de las que esperan por él; así M no puede desplazar a L mientras H espera. El bloqueo de H queda acotado por la sección crítica restante de L. Con **techo de prioridad**, cada mutex tiene un techo igual a la prioridad más alta de las tareas que lo usan y quien lo toma corre con esa prioridad desde el momento de tomarlo: evita además los interbloqueos por orden de toma y acota el bloqueo a una sección crítica, a costa de subir la prioridad aun cuando nadie espera. En el laboratorio, con herencia H se bloquea 25 ticks y con techo 0 porque H nunca llega a esperar.

Según [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md):

**Diagnóstico paso a paso.** (1) El tiempo de ejecución del limitador, medido aisladamente, es de 8 ms y no explica el retraso. (2) La traza muestra a H bloqueada esperando el mutex que L tenía. (3) Entre medias, la tarea M de registro, de prioridad intermedia, corrió 120 ms porque había una ráfaga de eventos. (4) La herencia de prioridad estaba disponible en el sistema operativo y desactivada en la creación de ese mutex.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Con **herencia de prioridad**, la tarea que tiene el mutex hereda la prioridad más alta de las que esperan por él; así M no puede desplazar a L mientras H espera. ([SE-451](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md), [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Recurso](../r/recurso.md), [Inversión de prioridad](../i/inversion-de-prioridad.md), [Peor caso de ejecución](../p/peor-caso-de-ejecucion.md), [Prioridad fija](../p/prioridad-fija.md), [Tasa monótona](../t/tasa-monotona.md), [Techo de prioridad](../t/techo-de-prioridad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Herencia](./herencia.md) · [Herramientas →](./herramientas.md)
