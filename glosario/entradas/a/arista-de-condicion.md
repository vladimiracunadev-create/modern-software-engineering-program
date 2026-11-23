# Arista de condición

[↑ Glosario](../../README.md) · [← Argumento](./argumento.md) · [Arista de valor →](./arista-de-valor.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Una columna de origen decide qué filas llegan, sin entrar en el valor.

Definición de trabajo de [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md).

## Por qué importa

La clase donde se define, [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md), existe con este propósito: la clase existe para que puedas responder dos preguntas que una plataforma de datos recibe todos los días y que casi nadie puede contestar con certeza:

## Cómo funciona

Según [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md):

**Corrección.** Se restaura la columna, se añaden las aristas de condición al catálogo y se exige la prueba de perturbación antes de cualquier retiro. La lección es que el linaje de valores subestima el impacto de las columnas de filtro, y que un catálogo que dice «sin consumidores» debe indicar qué método lo dijo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md)) son: El pipeline, el analizador de expresiones regulares y las perturbaciones son construcciones del autor; las 17 salidas y las 9 columnas de origen son un caso de juguete y la medición solo ve lo que los datos de prueba ejercitan. No se ejecutó ninguna herramienta de linaje ni de catálogo. El siguiente paso, `SE-368`, estudia dónde y cómo se guardan los datos: almacén, lago, lakehouse y formatos columnares.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md), [SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md), [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Origen](../o/origen.md), [Valor](../v/valor.md), [Arista de valor](./arista-de-valor.md), [Catálogo de datos](../c/catalogo-de-datos.md), [Condición](../c/condicion.md), [Impacto](../i/impacto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-367 — Linaje, catálogo y metadatos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Argumento](./argumento.md) · [Arista de valor →](./arista-de-valor.md)
