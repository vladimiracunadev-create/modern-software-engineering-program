# Cancelación

[↑ Glosario](../../README.md) · [← Canario](./canario.md) · [Cancelación cooperativa →](./cancelacion-cooperativa.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Cancelación pierde información al restar valores cercanos.

Tomado del glosario de [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md).

## Por qué importa

La clase donde se define, [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md), existe con este propósito: la clase existe para evaluar precisión según representación, propagación del error y tolerancia ligada a la escala.

## Cómo funciona

Según [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md):

La segunda es la *cancelación*: restar valores casi iguales borra los dígitos en común y deja el error de redondeo como resultado dominante. `(1 + 1e-16) - 1` es `0.0` en lugar de `1e-16`, y `0.1 + 0.2 - 0.3` es `5.551115123125783e-17` en lugar de cero. La tercera es que la suma de floats no es asociativa: `(a + b) + c` puede diferir de `a + (b + c)`. Un acumulador que suma `1e16` y luego diez veces `1.0` con un bucle simple vuelve a `1e16`; `math.fsum` devuelve `1.000000000000001e+16`, el valor correcto. Por eso los resultados de una reducción en paralelo pueden diferir según el número de hilos, y por eso las pruebas numéricas comparan con tolerancia y no con igualdad exacta.

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
- **Ver también:** [Valor](../v/valor.md), [NaN](../n/nan.md), [Precisión](../p/precision.md), [Rango](../r/rango.md), [Redondeo](../r/redondeo.md), [ULP](../u/ulp.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (68 clases más lo mencionan; las que más):

[SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md), [SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md), [SE-113](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-113-cli-flags-configuracion-y-codigos-de-salida/README.md), [SE-079](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md), [SE-080](../../../classes/part-06-paradigmas-de-programacion/se-080-programacion-reactiva-y-flujos/README.md), [SE-057](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md), [SE-232](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-232-estado-componentes-y-gestion-de-datos/README.md), [SE-536](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md).

**Aparece en los casos de estudio:** [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Canario](./canario.md) · [Cancelación cooperativa →](./cancelacion-cooperativa.md)
