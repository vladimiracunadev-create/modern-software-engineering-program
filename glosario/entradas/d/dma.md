# DMA

[↑ Glosario](../../README.md) · [← Divulgación coordinada](./divulgacion-coordinada.md) · [Doble →](./doble.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

DMA permite transferencias de dispositivo a memoria con intervención acotada de CPU.

Tomado del glosario de [SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md).

## Por qué importa

La clase donde se define, [SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), existe con este propósito: la clase existe para atribuir concurrencia y espera a procesos, hilos, interrupciones e I/O según su mecanismo.

## Cómo funciona

Según [SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md):

El programa solicita operaciones mediante APIs que llegan a llamadas del sistema. El kernel valida y coordina controladores. Dispositivos pueden avisar completado mediante interrupciones; DMA puede mover datos sin que la CPU copie cada byte. Una llamada bloqueante suspende al hilo hasta una condición, no necesariamente ocupa CPU todo el tiempo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md):

Un servidor atiende muchas conexiones con I/O asíncrono para evitar un hilo bloqueado por conexión. Si el cuello es cálculo, se consideran procesos o trabajo vectorizado, siempre midiendo costos de coordinación.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md)) son:

- **programa = proceso** — causa: archivo confundido con ejecución. Corrección: distingue descripción e instancia.
- **hilos duplican velocidad** — causa: concurrencia = paralelismo. Corrección: identifica carga, núcleos y runtime.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- DMA puede mover datos sin que la CPU copie cada byte. ([SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), [SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dispositivo](./dispositivo.md), [Transferencia](../t/transferencia.md), [Concurrencia](../c/concurrencia.md), [Hilo](../h/hilo.md), [I/O bloqueante](../i/i-o-bloqueante.md), [Interrupción](../i/interrupcion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Divulgación coordinada](./divulgacion-coordinada.md) · [Doble →](./doble.md)
