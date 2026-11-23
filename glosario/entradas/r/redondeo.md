# Redondeo

[↑ Glosario](../../README.md) · [← Redirección permanente](./redireccion-permanente.md) · [Reducción →](./reduccion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Selección de un valor representable.

Definición de trabajo de [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md).

## Por qué importa

En [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md), el tema «Redondeo» importa porque asigna resultados no representables

## Cómo funciona

Según [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md):

IEEE 754 representa valores mediante signo, exponente y significando. Entre valores representables hay huecos que crecen con la magnitud. `0.1` no tiene expansión binaria finita, por lo que se guarda el valor representable más cercano bajo una regla de redondeo. La salida corta de Python es una representación decimal conveniente, no los bits exactos.

Según [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md):

Un segundo fallo controlado es la acumulación. Escribe un bucle que sume 0,1 un millón de veces y compara el resultado con `math.fsum`, con `sum` y con `Decimal`, registrando la versión de Python. **Síntoma:** el bucle da `100000.00000133288` mientras `sum` y `fsum` dan `100000.0`. **Causa:** errores de redondeo acumulados que `sum` compensa desde Python 3.12. **Corrección:** decide si el cálculo requiere exactitud (entero escalado o `Decimal`) o tolerancia (compara con `math.isclose` y una tolerancia relativa y absoluta justificadas), y escribe una prueba que *no* dependa de la versión del intérprete. Documenta qué dato mostraría que tu tolerancia es demasiado laxa o demasiado estricta.

## Ejemplo

Caso medido en la sección «Redondeo: modos, empates y el caso de 2,675» de [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md):

Redondear exige elegir un *modo*. Python usa por defecto «redondeo al par más cercano» (a veces llamado bancario): `round(0.5)` es 0, `round(1.5)` es 2 y `round(2.5)` es 2, porque los empates van al entero par. Esto evita sesgo acumulado, pero choca con las reglas legales que exigen «medio hacia arriba». Un caso aparente de error es `round(2.675, 2)`, que devuelve `2.67` y no `2.68`: el `float` 2,675 en realidad vale 2,67499999999999982236…, de modo que *no hay empate* y el redondeo es correcto.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **centavos faltantes** — causa: float usado sin política decimal. Corrección: usa entero escalado o Decimal con redondeo. ([SE-016](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- `0.1` no tiene expansión binaria finita, por lo que se guarda el valor representable más cercano bajo una regla de redondeo. ([SE-016](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-014](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Valor](../v/valor.md), [NaN](../n/nan.md), [Precisión](../p/precision.md), [Rango](./rango.md), [ULP](../u/ulp.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-016 — Enteros, coma flotante, precisión y errores numéricos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (47 clases más lo mencionan; las que más):

[SE-522](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md), [SE-294](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md), [SE-311](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md), [SE-312](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md), [SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md), [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md), [SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md), [SE-560](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Redirección permanente](./redireccion-permanente.md) · [Reducción →](./reduccion.md)
