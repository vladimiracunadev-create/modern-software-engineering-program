# ISA

[↑ Glosario](../../README.md) · [← IR](./ir.md) · [ISBN →](./isbn.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Contrato de instrucciones y estado visible para software de máquina.

Definición de trabajo de [SE-013 — Arquitectura básica de un computador moderno](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md).

## Por qué importa

En [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), el tema «ISA» importa porque define operaciones y estado visibles

## Cómo funciona

Según [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md):

Una ISA define instrucciones, registros, formatos y efectos observables. La misma ISA puede tener implementaciones simples, segmentadas o fuera de orden. El software confía en el resultado arquitectónico, no en cada señal interna.

Según [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md):

Dos procesadores ejecutan el mismo binario con tiempos distintos. La corrección se evalúa por ISA/ABI; el rendimiento se mide por entorno. No se cambia algoritmo basándose solo en frecuencia anunciada.

## Ejemplo

Ejemplo de [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md) (sección «Ejemplo profesional»):

Dos procesadores ejecutan el mismo binario con tiempos distintos. La corrección se evalúa por ISA/ABI; el rendimiento se mide por entorno. No se cambia algoritmo basándose solo en frecuencia anunciada.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **una instrucción = un ciclo** — causa: modelo simplificado literal. Corrección: separa ISA y microarquitectura. ([SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md))
- **misma ISA implica mismo rendimiento** — causa: arquitectura confundida con implementación. Corrección: mide cada entorno y declara microarquitectura desconocida. ([SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Otras ISA usan longitudes distintas (x86 tiene instrucciones de 1 a 15 bytes) y RISC-V incluye una extensión comprimida de 16 bits; la idea común es que la ISA define cómo se interpretan los bits, no que todas las instrucciones midan igual. ([SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Contrato](../c/contrato.md), [Estado](../e/estado.md), [Instrucción](./instruccion.md), [ABI](../a/abi.md), [Arquitectura](../a/arquitectura.md), [Dispositivo](../d/dispositivo.md).
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

[↑ Glosario](../../README.md) · [← IR](./ir.md) · [ISBN →](./isbn.md)
