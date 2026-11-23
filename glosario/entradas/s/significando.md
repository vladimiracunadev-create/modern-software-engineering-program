# Significando

[↑ Glosario](../../README.md) · [← Signed-off-by](./signed-off-by.md) · [Siguiente paso →](./siguiente-paso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Significando contiene dígitos significativos.

Tomado del glosario de [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md).

## Por qué importa

En [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md), el tema «Coma flotante» importa porque significando y exponente aproximan reales

## Cómo funciona

Según [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md):

IEEE 754 representa valores mediante signo, exponente y significando. Entre valores representables hay huecos que crecen con la magnitud. `0.1` no tiene expansión binaria finita, por lo que se guarda el valor representable más cercano bajo una regla de redondeo. La salida corta de Python es una representación decimal conveniente, no los bits exactos.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md):

Un contador Java de 32 bits se exporta desde Python. Aunque Python no desborde, el contrato sí. Se valida rango antes de serializar y se prueba máximo, máximo+1 y valores negativos.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md)) son:

- **centavos faltantes** — causa: float usado sin política decimal. Corrección: usa entero escalado o Decimal con redondeo.
- **prueba pasa en Python y falla al integrar** — causa: ancho externo omitido. Corrección: valida rango del contrato.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md)) son: No es análisis numérico completo. `SE-017` sigue las operaciones desde instrucciones y registros.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-014](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [NaN](../n/nan.md), [Precisión](../p/precision.md), [Rango](../r/rango.md), [Redondeo](../r/redondeo.md), [ULP](../u/ulp.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Signed-off-by](./signed-off-by.md) · [Siguiente paso →](./siguiente-paso.md)
