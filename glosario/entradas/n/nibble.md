# Nibble

[↑ Glosario](../../README.md) · [← Negociación por intereses](./negociacion-por-intereses.md) · [NISQ →](./nisq.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Nibble son
cuatro bits.

Tomado del glosario de [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md).

## Por qué importa

La clase donde se define, [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md), existe con este propósito: la clase existe para interpretar un valor binario solo cuando se declaran base, ancho, signo y orden de bytes.

## Cómo funciona

[SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md):

Un encabezado de red fija ancho y orden. El productor que usa orden nativo puede pasar pruebas locales y fallar al interoperar. La solución es contrato explícito y vectores de prueba compartidos, no detectar plataforma en cada extremo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md)) son:

- **conversión aprendida de memoria** — causa: falta modelo posicional. Corrección: reconstruye pesos y suma.
- **overflow no aparece en Python** — causa: entero arbitrario oculta ancho. Corrección: valida rango o usa serialización fija.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md)) son: No cubre álgebra booleana ni formatos de archivo completos. `SE-015` asigna texto a secuencias de bytes.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Base](../b/base.md), [Bit](../b/bit.md), [Byte](../b/byte.md), [Endianess](../e/endianess.md), [Overflow](../o/overflow.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Negociación por intereses](./negociacion-por-intereses.md) · [NISQ →](./nisq.md)
