# PC

[↑ Glosario](../../README.md) · [← Pause](./pause.md) · [PDU →](./pdu.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Estado que identifica la próxima instrucción.

Definición de trabajo de [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md).

## Por qué importa

En [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), el tema «Registros y PC» importa porque conservan operandos y próxima instrucción

## Cómo funciona

Según [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md):

Comparaciones y branches cambian el PC. Bucles y decisiones surgen de esas transiciones. Una predicción de salto intenta mantener ocupada la máquina; si falla, descarta trabajo especulativo. La semántica correcta permanece, pero tiempo y efectos laterales microarquitectónicos requieren análisis aparte.

Según [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md):

Cambia un salto para usar la condición opuesta. Registra PC y primer estado divergente; corrige la condición, no el resultado final a mano.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md):

Dos procesadores ejecutan el mismo binario con tiempos distintos. La corrección se evalúa por ISA/ABI; el rendimiento se mide por entorno. No se cambia algoritmo basándose solo en frecuencia anunciada.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md)) son:

- **variable = registro** — causa: abstracciones mezcladas. Corrección: documenta decisiones de compilador/runtime.
- **una instrucción = un ciclo** — causa: modelo simplificado literal. Corrección: separa ISA y microarquitectura.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Registra PC y primer estado divergente; corrige la condición, no el resultado final a mano. ([SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Estado](../e/estado.md).
- **Ver también:** [Instrucción](../i/instruccion.md), [Excepción](../e/excepcion.md), [ISA](../i/isa.md), [Microarquitectura](../m/microarquitectura.md), [Pipeline](./pipeline.md), [Registro](../r/registro.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Pause](./pause.md) · [PDU →](./pdu.md)
