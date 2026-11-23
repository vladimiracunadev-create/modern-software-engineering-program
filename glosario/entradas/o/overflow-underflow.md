# Overflow/underflow

[↑ Glosario](../../README.md) · [← Overflow](./overflow.md) · [Owner →](./owner.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Overflow/underflow exceden rango
alto o pequeño.

Tomado del glosario de [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md).

## Por qué importa

La clase donde se define, [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md), existe con este propósito: la clase existe para evaluar precisión según representación, propagación del error y tolerancia ligada a la escala.

## Cómo funciona

[SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: consulta la clase para el mecanismo completo.

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

- **Prerrequisito:** [Overflow](./overflow.md).
- **Ver también:** [Rango](../r/rango.md), [NaN](../n/nan.md), [Precisión](../p/precision.md), [Redondeo](../r/redondeo.md), [ULP](../u/ulp.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Overflow](./overflow.md) · [Owner →](./owner.md)
