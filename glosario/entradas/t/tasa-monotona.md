# Tasa monótona

[↑ Glosario](../../README.md) · [← Tasa interna de retorno](./tasa-interna-de-retorno.md) · [Team topology →](./team-topology.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Asignación de prioridad según el periodo: menor periodo, mayor prioridad.

Definición de trabajo de [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md).

## Por qué importa

La clase donde se define, [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md), existe con este propósito: la clase existe para que entiendas por qué, en un sistema crítico, una función correcta que llega tarde es una función que falló, y qué herramientas permiten **argumentar** que llega a tiempo: el análisis de planificación de prioridades fijas, los protocolos que acotan la inversión de prioridad y el tiempo de ejecución en el peor caso (WCET).

## Cómo funciona

Según [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md):

En un planificador apropiativo de prioridades fijas, cada tarea tiene una prioridad que no cambia y la que está lista con mayor prioridad corre. Si las prioridades se asignan por tasa monótona (menor periodo, mayor prioridad), Liu y Layland demostraron en 1973 que n tareas periódicas independientes cumplen sus plazos si la utilización total no supera n(2^(1/n) − 1): 0,780 para tres tareas y, con muchas tareas, el logaritmo natural de 2, unos 0,693. Es una condición **suficiente**, no necesaria. En el laboratorio, un conjunto con utilización 0,841 supera la cota y es planificable por análisis (la tarea más lenta responde en 77 ms de 100); otro con 0,950 supera la cota y no lo es (113 ms de 100).

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Si las prioridades se asignan por tasa monótona (menor periodo, mayor prioridad), Liu y Layland demostraron en 1973 que n tareas periódicas independientes cumplen sus plazos si la utilización total no supera n(2^(1/n) − 1): 0,780 para tres tareas y, con muchas tareas, el logaritmo natural de 2, unos 0,693. ([SE-451](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md), [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Herencia de prioridad](../h/herencia-de-prioridad.md), [Inversión de prioridad](../i/inversion-de-prioridad.md), [Peor caso de ejecución](../p/peor-caso-de-ejecucion.md), [Prioridad fija](../p/prioridad-fija.md), [Techo de prioridad](./techo-de-prioridad.md), [Utilización](../u/utilizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Tasa interna de retorno](./tasa-interna-de-retorno.md) · [Team topology →](./team-topology.md)
