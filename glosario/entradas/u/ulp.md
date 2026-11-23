# ULP

[↑ Glosario](../../README.md) · [← Tutorial](../t/tutorial.md) · [Última escritura gana →](./ultima-escritura-gana.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Distancia local entre valores flotantes consecutivos.

Definición de trabajo de [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md).

## Por qué importa

La clase donde se define, [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md), existe con este propósito: la clase existe para evaluar precisión según representación, propagación del error y tolerancia ligada a la escala.

## Cómo funciona

Según [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md):

Entre dos `double` consecutivos hay un hueco que crece con la magnitud, medido en ULP (*unit in the last place*). Cerca de 1 el hueco es de unos 2,2 × 10⁻¹⁶ (el épsilon de máquina); cerca de 10¹⁶ es 2. La primera consecuencia es la *absorción*: `1e16 + 1` es igual a `1e16`, porque 1 es menor que la mitad del hueco; un acumulador grande ignora sumandos pequeños. Con enteros pasa algo parecido en el límite 2⁵³: `float(2**53) + 1 == float(2**53)` es verdadero, y por encima de 2⁵³ un `float` ya no representa todos los enteros.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md):

Un contador Java de 32 bits se exporta desde Python. Aunque Python no desborde, el contrato sí. Se valida rango antes de serializar y se prueba máximo, máximo+1 y valores negativos.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md)) son:

- **centavos faltantes** — causa: float usado sin política decimal. Corrección: usa entero escalado o Decimal con redondeo.
- **prueba pasa en Python y falla al integrar** — causa: ancho externo omitido. Corrección: valida rango del contrato.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md)) son: No es análisis numérico completo. `SE-017` sigue las operaciones desde instrucciones y registros.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-014](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Valor](../v/valor.md), [NaN](../n/nan.md), [Precisión](../p/precision.md), [Rango](../r/rango.md), [Redondeo](../r/redondeo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Tutorial](../t/tutorial.md) · [Última escritura gana →](./ultima-escritura-gana.md)
