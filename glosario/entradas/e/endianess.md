# Endianess

[↑ Glosario](../../README.md) · [← Encoding](./encoding.md) · [Endurecimiento →](./endurecimiento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Orden de bytes en un valor multibyte.

Definición de trabajo de [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md).

## Por qué importa

En [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md), el tema «Endianess» importa porque ordena bytes de valores multibyte

## Cómo funciona

[SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Caso medido en la sección «Endianess ordena bytes, no bits dentro de una explicación informal» de [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md):

**Cómo leer la figura.** Las dos filas guardan *el mismo valor* en las mismas cuatro direcciones; solo cambia cuál byte va primero. La flecha roja muestra el error del problema auténtico: bytes escritos en un orden y leídos en el contrario no se corrompen, pero significan otra cosa. `struct.pack('<I', 1)` produce `01000000` y `struct.pack('>I', 1)` produce `00000001`. **Dónde deja de valer:** el diagrama trata los bytes como indivisibles. Dentro de un byte el orden de los bits es otra cuestión que casi nunca importa en software, pero sí en ciertos buses y protocolos serie; no mezcles ambas preguntas.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **bytes invertidos entre sistemas** — causa: endianess implícito. Corrección: fija orden y vector de prueba. ([SE-014](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md)) son: No cubre álgebra booleana ni formatos de archivo completos. `SE-015` asigna texto a secuencias de bytes.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Byte](../b/byte.md), [Valor](../v/valor.md), [Base](../b/base.md), [Bit](../b/bit.md), [Overflow](../o/overflow.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Encoding](./encoding.md) · [Endurecimiento →](./endurecimiento.md)
