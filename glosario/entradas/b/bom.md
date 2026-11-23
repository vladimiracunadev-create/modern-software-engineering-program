# BOM

[↑ Glosario](../../README.md) · [← BM25](./bm25.md) · [Bomba de descompresión →](./bomba-de-descompresion.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

BOM es U+FEFF al inicio bajo
ciertos protocolos.

Tomado del glosario de [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md).

## Por qué importa

La clase donde se define, [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md), existe con este propósito: la clase existe para distinguir carácter, punto de código, unidades de código, bytes y glifo al diagnosticar texto.

## Cómo funciona

Según [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md):

Unicode asigna puntos de código. UTF-8 los transforma en secuencias de uno a cuatro bytes y conserva ASCII como bytes iguales. Es reversible para secuencias válidas. El orden de bytes del procesador no altera UTF-8 porque se interpreta byte a byte. Un BOM en UTF-8 puede actuar como firma, no como indicador de endianess.

Según [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md):

Normalmente no. El BOM en UTF-8 es la secuencia `EF BB BF` y solo sirve como firma, ya que UTF-8 no tiene orden de bytes. Algunos programas lo exigen para reconocer la codificación y otros lo muestran como un carácter extraño al inicio del archivo. Decide según el consumidor y declara la decisión; Python lo maneja con la codificación `utf-8-sig`.

## Ejemplo

Ejemplo de [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md) (sección «Preguntas frecuentes»):

Normalmente no. El BOM en UTF-8 es la secuencia `EF BB BF` y solo sirve como firma, ya que UTF-8 no tiene orden de bytes. Algunos programas lo exigen para reconocer la codificación y otros lo muestran como un carácter extraño al inicio del archivo. Decide según el consumidor y declara la decisión; Python lo maneja con la codificación `utf-8-sig`.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md)) son:

- **`len()` se interpreta como caracteres visibles** — causa: puntos y grafemas confundidos. Corrección: declara la unidad que cuentas.
- **texto “arreglado” con reemplazos** — causa: se atacó apariencia. Corrección: reconstruye codificación y conserva original.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un BOM en UTF-8 puede actuar como firma, no como indicador de endianess. ([SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-014](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Codificación](../c/codificacion.md), [Grafema](../g/grafema.md), [Mojibake](../m/mojibake.md), [Normalización](../n/normalizacion.md), [Punto de código](../p/punto-de-codigo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← BM25](./bm25.md) · [Bomba de descompresión →](./bomba-de-descompresion.md)
