# Techo de prioridad

[↑ Glosario](../../README.md) · [← Technical Writer / Documentation Engineer](./technical-writer-documentation-engineer.md) · [Teclado y foco →](./teclado-y-foco.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

El poseedor corre con la prioridad máxima de las tareas que usan el recurso.

Definición de trabajo de [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md).

## Por qué importa

En [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md), el tema «Herencia y techo de prioridad» importa porque acotan el bloqueo.

## Cómo funciona

Según [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md):

Con **herencia de prioridad**, la tarea que tiene el mutex hereda la prioridad más alta de las que esperan por él; así M no puede desplazar a L mientras H espera. El bloqueo de H queda acotado por la sección crítica restante de L. Con **techo de prioridad**, cada mutex tiene un techo igual a la prioridad más alta de las tareas que lo usan y quien lo toma corre con esa prioridad desde el momento de tomarlo: evita además los interbloqueos por orden de toma y acota el bloqueo a una sección crítica, a costa de subir la prioridad aun cuando nadie espera. En el laboratorio, con herencia H se bloquea 25 ticks y con techo 0 porque H nunca llega a esperar.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md)) son: El simulador es de ticks con un solo mutex, sin interrupciones ni caché; los tiempos son del autor y el WCET se mide en pasos de un algoritmo; el relato del Pathfinder es de segunda mano. Los dos artículos clásicos se citan por su DOI, que responde con bloqueo a clientes automáticos, y no se reproducen.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md), [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Recurso](../r/recurso.md), [Tarea](./tarea.md), [Herencia de prioridad](../h/herencia-de-prioridad.md), [Inversión de prioridad](../i/inversion-de-prioridad.md), [Peor caso de ejecución](../p/peor-caso-de-ejecucion.md), [Prioridad fija](../p/prioridad-fija.md).
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

[↑ Glosario](../../README.md) · [← Technical Writer / Documentation Engineer](./technical-writer-documentation-engineer.md) · [Teclado y foco →](./teclado-y-foco.md)
