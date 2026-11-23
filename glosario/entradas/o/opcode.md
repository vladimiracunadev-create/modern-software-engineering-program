# Opcode

[↑ Glosario](../../README.md) · [← Opción de refactorizar](./opcion-de-refactorizar.md) · [Open Source & InnerSource Engineer →](./open-source-innersource-engineer.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Opcode identifica operación.

Tomado del glosario de [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md).

## Por qué importa

La clase donde se define, [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), existe con este propósito: la clase existe para explicar instrucciones como transiciones de estado sin confundir bytecode con ISA.

## Cómo funciona

Según [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md):

**Cómo leer la figura.** Una instrucción es *datos*: treinta y dos bits repartidos en campos. El `opcode` (`0110011`) dice que es una operación entre registros; `funct7` y `funct3` precisan cuál (aquí, una suma); `rs1` y `rs2` nombran los registros fuente (`x1` y `x2`) y `rd`, el destino (`x3`). El hexadecimal `0x002081B3` es esa misma secuencia agrupada de a cuatro bits. **Dónde deja de valer:** es el formato de una familia de instrucciones de RISC-V. Otras ISA usan longitudes distintas (x86 tiene instrucciones de 1 a 15 bytes) y RISC-V incluye una extensión comprimida de 16 bits; la idea común es que la ISA define cómo se interpretan los bits, no que todas las instrucciones midan igual.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md):

Dos procesadores ejecutan el mismo binario con tiempos distintos. La corrección se evalúa por ISA/ABI; el rendimiento se mide por entorno. No se cambia algoritmo basándose solo en frecuencia anunciada.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md)) son:

- **variable = registro** — causa: abstracciones mezcladas. Corrección: documenta decisiones de compilador/runtime.
- **una instrucción = un ciclo** — causa: modelo simplificado literal. Corrección: separa ISA y microarquitectura.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md)) son: No mide ciclos físicos ni cubre ensamblador completo. `SE-018` añade jerarquías y localidad.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md), [SE-016](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Operación](./operacion.md), [Excepción](../e/excepcion.md), [Instrucción](../i/instruccion.md), [ISA](../i/isa.md), [Microarquitectura](../m/microarquitectura.md), [PC](../p/pc.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Opción de refactorizar](./opcion-de-refactorizar.md) · [Open Source & InnerSource Engineer →](./open-source-innersource-engineer.md)
