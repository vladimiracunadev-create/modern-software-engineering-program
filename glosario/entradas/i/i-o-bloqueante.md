# I/O bloqueante

[↑ Glosario](../../README.md) · [← Huérfano](../h/huerfano.md) · [I/o y red →](./i-o-y-red.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Operación que suspende la unidad llamante hasta progreso.

Definición de trabajo de [SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md).

## Por qué importa

La clase donde se define, [SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), existe con este propósito: la clase existe para atribuir concurrencia y espera a procesos, hilos, interrupciones e I/O según su mecanismo.

## Cómo funciona

[SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md):

Un servidor atiende muchas conexiones con I/O asíncrono para evitar un hilo bloqueado por conexión. Si el cuello es cálculo, se consideran procesos o trabajo vectorizado, siempre midiendo costos de coordinación.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md)) son:

- **programa = proceso** — causa: archivo confundido con ejecución. Corrección: distingue descripción e instancia.
- **hilos duplican velocidad** — causa: concurrencia = paralelismo. Corrección: identifica carga, núcleos y runtime.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md)) son: No administra servicios ni señales del SO; eso corresponde a la [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md). `SE-020` abre la traducción del programa.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), [SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Operación](../o/operacion.md), [Progreso](../p/progreso.md), [Concurrencia](../c/concurrencia.md), [Hilo](../h/hilo.md), [Interrupción](./interrupcion.md), [Proceso](../p/proceso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Huérfano](../h/huerfano.md) · [I/o y red →](./i-o-y-red.md)
