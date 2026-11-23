# Context switch

[↑ Glosario](../../README.md) · [← Context engineering](./context-engineering.md) · [Contexto de trabajo →](./contexto-de-trabajo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Context switch cambia unidad ejecutada.

Tomado del glosario de [SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md).

## Por qué importa

La clase donde se define, [SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), existe con este propósito: la clase existe para atribuir concurrencia y espera a procesos, hilos, interrupciones e I/O según su mecanismo.

## Cómo funciona

[SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: consulta la clase para el mecanismo completo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md):

Un servidor atiende muchas conexiones con I/O asíncrono para evitar un hilo bloqueado por conexión. Si el cuello es cálculo, se consideran procesos o trabajo vectorizado, siempre midiendo costos de coordinación.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md)) son:

- **programa = proceso** — causa: archivo confundido con ejecución. Corrección: distingue descripción e instancia.
- **hilos duplican velocidad** — causa: concurrencia = paralelismo. Corrección: identifica carga, núcleos y runtime.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md)) son: No administra servicios ni señales del SO; eso corresponde a la [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md). `SE-020` abre la traducción del programa.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), [SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Concurrencia](./concurrencia.md), [Hilo](../h/hilo.md), [I/O bloqueante](../i/i-o-bloqueante.md), [Interrupción](../i/interrupcion.md), [Proceso](../p/proceso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Context engineering](./context-engineering.md) · [Contexto de trabajo →](./contexto-de-trabajo.md)
