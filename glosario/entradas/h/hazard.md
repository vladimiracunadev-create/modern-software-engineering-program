# Hazard

[↑ Glosario](../../README.md) · [← Hashable](./hashable.md) · [Health check →](./health-check.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Hazard es una condición
que impide avanzar sin control.

Tomado del glosario de [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md).

## Por qué importa

La clase donde se define, [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), existe con este propósito: la clase existe para explicar instrucciones como transiciones de estado sin confundir bytecode con ISA.

## Cómo funciona

[SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

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
- **Ver también:** [Condición](../c/condicion.md), [Control](../c/control.md), [Excepción](../e/excepcion.md), [Instrucción](../i/instruccion.md), [ISA](../i/isa.md), [Microarquitectura](../m/microarquitectura.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-017 — CPU, instrucciones, registros y ciclos de ejecución](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Hashable](./hashable.md) · [Health check →](./health-check.md)
