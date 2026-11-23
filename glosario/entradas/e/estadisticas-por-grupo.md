# Estadísticas por grupo

[↑ Glosario](../../README.md) · [← Estabilidad de segmentos](./estabilidad-de-segmentos.md) · [Estado →](./estado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Mínimo y máximo de cada columna en un grupo de filas.

Definición de trabajo de [SE-368 — Warehouse, lake, lakehouse y formatos columnares](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md).

## Por qué importa

En [SE-368 — Warehouse, lake, lakehouse y formatos columnares](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md), el tema «Estadísticas por grupo» importa porque saltar grupos sin leerlos.

## Cómo funciona

Según [SE-368 — Warehouse, lake, lakehouse y formatos columnares](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md):

Las estadísticas por grupo (el mínimo y el máximo de `day` de cada grupo de 10 000 filas) permiten saltar grupos que no pueden contener el rango pedido. Funcionan cuando cada grupo cubre un intervalo estrecho de la columna filtrada. Con los mismos datos mezclados al azar, cada grupo cubre casi todo el año, la consulta leyó los 20 grupos de 20 y 0,945 MB: el archivo era más grande (2,35 MB frente a 2,00) porque el orden también favorecía la compresión. La decisión de diseño es elegir la columna por la que se ordena (o se particiona) según los filtros más frecuentes; no es gratis, porque ordenar por una columna perjudica a las consultas que filtran por otra.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-368 — Warehouse, lake, lakehouse y formatos columnares](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Las estadísticas por grupo (el mínimo y el máximo de `day` de cada grupo de 10 000 filas) permiten saltar grupos que no pueden contener el rango pedido. ([SE-368](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md), [SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-367](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Almacén](../a/almacen.md), [Codificación por diccionario](../c/codificacion-por-diccionario.md), [Compactación](../c/compactacion.md), [Formato columnar](../f/formato-columnar.md), [Lago](../l/lago.md), [Lakehouse](../l/lakehouse.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-368 — Warehouse, lake, lakehouse y formatos columnares](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Estabilidad de segmentos](./estabilidad-de-segmentos.md) · [Estado →](./estado.md)
