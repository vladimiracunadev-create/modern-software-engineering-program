# Prioridad fija

[↑ Glosario](../../README.md) · [← Principio ágil](./principio-agil.md) · [Prioridad y conflictos →](./prioridad-y-conflictos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Prioridad de una tarea que no cambia durante la ejecución.

Definición de trabajo de [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md).

## Por qué importa

En [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md), el tema «Prioridades fijas y utilización» importa porque fijan la regla de quién corre.

## Cómo funciona

Según [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md):

En un planificador apropiativo de prioridades fijas, cada tarea tiene una prioridad que no cambia y la que está lista con mayor prioridad corre. Si las prioridades se asignan por tasa monótona (menor periodo, mayor prioridad), Liu y Layland demostraron en 1973 que n tareas periódicas independientes cumplen sus plazos si la utilización total no supera n(2^(1/n) − 1): 0,780 para tres tareas y, con muchas tareas, el logaritmo natural de 2, unos 0,693. Es una condición **suficiente**, no necesaria. En el laboratorio, un conjunto con utilización 0,841 supera la cota y es planificable por análisis (la tarea más lenta responde en 77 ms de 100); otro con 0,950 supera la cota y no lo es (113 ms de 100).

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En un planificador apropiativo de prioridades fijas, cada tarea tiene una prioridad que no cambia y la que está lista con mayor prioridad corre. ([SE-451](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md), [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Tarea](../t/tarea.md), [Herencia de prioridad](../h/herencia-de-prioridad.md), [Inversión de prioridad](../i/inversion-de-prioridad.md), [Peor caso de ejecución](./peor-caso-de-ejecucion.md), [Tasa monótona](../t/tasa-monotona.md), [Techo de prioridad](../t/techo-de-prioridad.md).
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

[↑ Glosario](../../README.md) · [← Principio ágil](./principio-agil.md) · [Prioridad y conflictos →](./prioridad-y-conflictos.md)
