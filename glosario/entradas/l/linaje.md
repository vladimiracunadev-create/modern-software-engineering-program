# Linaje

[↑ Glosario](../../README.md) · [← Limpieza y recuperación](./limpieza-y-recuperacion.md) · [Línea base →](./linea-base.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Grafo de dependencia entre conjuntos de datos, columnas o trabajos.

Definición de trabajo de [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md).

## Por qué importa

En [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md), el tema «Linaje de tablas» importa porque dice qué tablas dependen de cuáles; es grueso.

## Cómo funciona

Según [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md):

El linaje de tablas dice «`mart_city` depende de `fact_sales`». El de columnas, «`mart_city.total_clp` se calcula desde `fact_sales.amount_clp`». El de condiciones añade «`fact_sales` solo contiene filas cuyo `status` no es `cancelled`». Cada nivel responde algo distinto: el primero, «qué se recalcula si cambia esta tabla» (`SE-364`); el segundo, «qué columnas ven esta columna»; el tercero, «qué filas llegan». La respuesta a «¿es seguro quitar esta columna?» necesita los tres.

Según [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md):

El equipo de *Avisos* quiere retirar tres columnas antiguas de la tabla de lecturas. Con el linaje de tablas, el catálogo dice que veinte activos dependen de ella, demasiado para revisar. Con linaje de columnas y condiciones, dos de las tres columnas no tienen consumidores y la tercera aparece en un filtro de un informe de finanzas. El equipo ejecuta la prueba de perturbación sobre la tercera en una copia: cambia cuatro columnas de salida de dos informes. Avisa a los dos dueños con la lista exacta, fija una fecha de retiro de seis semanas y retira las dos columnas sin consumidores esa misma semana. El catálogo registra la decisión y la fecha y comprueba que, al llegar la fecha, el uso en el registro de consultas sea cero.

## Ejemplo

Ejemplo de [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md) (sección «Ejemplo mínimo»):

La columna `status` no está en ninguna salida y determina qué filas existen. Sin la segunda lista, el linaje diría que cambiar `status` no afecta a nadie.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El linaje de tablas dice «`mart_city` depende de `fact_sales`». ([SE-367](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Grafo de dependencias](../g/grafo-de-dependencias.md).
- **Ver también:** [Conjunto](../c/conjunto.md), [Dependencia](../d/dependencia.md), [Grafo](../g/grafo.md), [Trabajo](../t/trabajo.md), [Arista de condición](../a/arista-de-condicion.md), [Arista de valor](../a/arista-de-valor.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), [SE-369](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md), [SE-372](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-372-proyecto-plataforma-de-datos-minima-gobernada/README.md), [SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md), [SE-290](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md), [SE-371](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md), [SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Limpieza y recuperación](./limpieza-y-recuperacion.md) · [Línea base →](./linea-base.md)
