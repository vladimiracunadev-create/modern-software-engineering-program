# NaN

[↑ Glosario](../../README.md) · [← Namespace](./namespace.md) · [Narrativa y verificación →](./narrativa-y-verificacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Valor especial para resultados no numéricos.

Definición de trabajo de [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md).

## Por qué importa

La clase donde se define, [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md), existe con este propósito: la clase existe para evaluar precisión según representación, propagación del error y tolerancia ligada a la escala.

## Cómo funciona

Según [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md):

IEEE 754 incluye infinitos, NaN y ceros con signo. NaN no es igual a sí mismo y puede propagarse; usarlo como dato faltante sin política mezcla ausencia con resultado indefinido. Validar entrada y salida evita que un valor especial atraviese decisiones que esperaban números finitos.

Según [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md):

`NaN` no es igual a sí mismo: `float('nan') == float('nan')` es falso. Para detectarlo usa `math.isnan`. Decide una política: rechazar la entrada, propagarlo y marcar el resultado como inválido, o sustituir un valor documentado. No uses `NaN` como valor faltante sin que el contrato lo diga, porque se mezclará con resultados indefinidos.

## Ejemplo

Ejemplo de [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md) (sección «Preguntas frecuentes»):

`NaN` no es igual a sí mismo: `float('nan') == float('nan')` es falso. Para detectarlo usa `math.isnan`. Decide una política: rechazar la entrada, propagarlo y marcar el resultado como inválido, o sustituir un valor documentado. No uses `NaN` como valor faltante sin que el contrato lo diga, porque se mezclará con resultados indefinidos.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **NaN atraviesa el cálculo** — causa: valores especiales no validados. Corrección: define entrada, propagación y rechazo. ([SE-016](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- NaN no es igual a sí mismo y puede propagarse; usarlo como dato faltante sin política mezcla ausencia con resultado indefinido. ([SE-016](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-014](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Resultado](../r/resultado.md), [Valor](../v/valor.md), [Precisión](../p/precision.md), [Rango](../r/rango.md), [Redondeo](../r/redondeo.md), [ULP](../u/ulp.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Namespace](./namespace.md) · [Narrativa y verificación →](./narrativa-y-verificacion.md)
