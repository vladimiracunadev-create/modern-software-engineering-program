# Bit

[↑ Glosario](../../README.md) · [← Bisección](./biseccion.md) · [Bitácora de cambios →](./bitacora-de-cambios.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Unidad con dos estados distinguibles.

Definición de trabajo de [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md).

## Por qué importa

En [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md), el tema «Bit y byte» importa porque agrupan estados discretos

## Cómo funciona

Según [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md):

Un bit modela dos estados, usualmente escritos 0 y 1. Ocho bits forman un byte en las plataformas estudiadas. Con `n` bits existen `2**n` patrones. Eso no decide qué representan: el mismo patrón puede interpretarse como entero, flags o fragmento de un formato.

Según [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md):

No. Existieron otras, como el complemento a uno y signo-magnitud, que complican la aritmética (dos ceros, por ejemplo). Casi todos los procesadores actuales usan complemento a dos para enteros; los formatos de coma flotante usan signo-magnitud con un bit de signo independiente, tema de `SE-016`.

## Ejemplo

Ejemplo de [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md) (sección «Preguntas frecuentes»):

No. Existieron otras, como el complemento a uno y signo-magnitud, que complican la aritmética (dos ceros, por ejemplo). Casi todos los procesadores actuales usan complemento a dos para enteros; los formatos de coma flotante usan signo-magnitud con un bit de signo independiente, tema de `SE-016`.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md)) son:

- **conversión aprendida de memoria** — causa: falta modelo posicional. Corrección: reconstruye pesos y suma.
- **overflow no aparece en Python** — causa: entero arbitrario oculta ancho. Corrección: valida rango o usa serialización fija.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un entero sin signo de `n` bits cubre `0` a `2**n - 1`. ([SE-014](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Estado](../e/estado.md).
- **Ver también:** [Base](./base.md), [Byte](./byte.md), [Endianess](../e/endianess.md), [Overflow](../o/overflow.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Bisección](./biseccion.md) · [Bitácora de cambios →](./bitacora-de-cambios.md)
