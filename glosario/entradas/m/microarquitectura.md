# Microarquitectura

[↑ Glosario](../../README.md) · [← Métricas interpretadas](./metricas-interpretadas.md) · [Microkernel →](./microkernel.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Organización concreta que implementa una ISA.

Definición de trabajo de [SE-013 — Arquitectura básica de un computador moderno](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md).

## Por qué importa

En [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), el tema «Microarquitectura» importa porque solapa y reordena trabajo internamente

## Cómo funciona

Según [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md):

El rendimiento se resume en la ecuación clásica: *tiempo de CPU = instrucciones × ciclos por instrucción (CPI) × periodo del reloj*. Reducir instrucciones ayuda solo si el CPI no empeora; subir la frecuencia ayuda solo si no aumentan las esperas de memoria. Los saltos añaden otra dependencia: la CPU predice el resultado para no detenerse, y si se equivoca descarta el trabajo especulativo. La semántica se conserva, pero el estado interno (por ejemplo, qué hay en las cachés) no vuelve exactamente al anterior, y esa diferencia puede observarse como tiempo. Los ataques de ejecución especulativa conocidos como Spectre explotaron precisamente esa brecha entre lo que garantiza la ISA y lo que revela la microarquitectura; es un recordatorio de que «no cambia el resultado» no equivale a «no deja rastro».

Según [SE-013 — Arquitectura básica de un computador moderno](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md):

La arquitectura describe propiedades que un consumidor puede usar sin conocer toda la implementación. Una ISA especifica instrucciones, registros y efectos visibles para el software de bajo nivel. RISC-V, por ejemplo, separa deliberadamente la ISA de una microarquitectura particular. Dos procesadores pueden ejecutar el mismo binario y organizar internamente pipeline, cachés o unidades de ejecución de modo distinto.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md):

Dos procesadores ejecutan el mismo binario con tiempos distintos. La corrección se evalúa por ISA/ABI; el rendimiento se mide por entorno. No se cambia algoritmo basándose solo en frecuencia anunciada.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **una instrucción = un ciclo** — causa: modelo simplificado literal. Corrección: separa ISA y microarquitectura. ([SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md))
- **misma ISA implica mismo rendimiento** — causa: arquitectura confundida con implementación. Corrección: mide cada entorno y declara microarquitectura desconocida. ([SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Los ataques de ejecución especulativa conocidos como Spectre explotaron precisamente esa brecha entre lo que garantiza la ISA y lo que revela la microarquitectura; es un recordatorio de que «no cambia el resultado» no equivale a «no deja rastro». ([SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Organización](../o/organizacion.md), [ABI](../a/abi.md), [Arquitectura](../a/arquitectura.md), [Dispositivo](../d/dispositivo.md), [Estado](../e/estado.md), [Excepción](../e/excepcion.md).
- **Se confunde con:** Los ataques de ejecución especulativa conocidos como Spectre explotaron precisamente esa brecha entre lo que garantiza la ISA y lo que revela la microarquitectura; es un recordatorio de que «no cambia el resultado» no equivale a «no deja rastro».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-013 — Arquitectura básica de un computador moderno](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Métricas interpretadas](./metricas-interpretadas.md) · [Microkernel →](./microkernel.md)
