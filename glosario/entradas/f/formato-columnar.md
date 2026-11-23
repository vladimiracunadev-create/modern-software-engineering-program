# Formato columnar

[↑ Glosario](../../README.md) · [← Fork](./fork.md) · [Formatter →](./formatter.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Archivo que guarda cada columna por separado, en grupos de filas.

Definición de trabajo de [SE-368 — Warehouse, lake, lakehouse y formatos columnares](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md).

## Por qué importa

La clase donde se define, [SE-368 — Warehouse, lake, lakehouse y formatos columnares](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md), existe con este propósito: la clase existe para que elijas dónde y cómo se guardan los datos analíticos sabiendo qué hace cada formato con los bytes, y no por el nombre de la categoría.

## Cómo funciona

Según [SE-368 — Warehouse, lake, lakehouse y formatos columnares](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md):

Doscientos mil pedidos con ocho columnas ocuparon 7,33 MB en CSV, 25,93 MB en JSON por líneas (el nombre de cada columna se repite en cada fila), 11,60 MB en un binario por filas de ancho fijo (ocho bytes por entero y por texto reservados aunque sobren) y 2,00 MB en el formato columnar con compresión, un 27 % del CSV. La diferencia no viene de «ser binario» sino de tres decisiones: guardar los valores de una columna juntos (se parecen y se comprimen mejor), codificar el texto repetido con un diccionario de índices de un byte y comprimir cada bloque. La columna de estado, con tres valores distintos, ocupa 1 080 493 bytes como texto sin comprimir y unos 45 000 como índices de un byte comprimidos.

Según [SE-368 — Warehouse, lake, lakehouse y formatos columnares](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md):

El equipo de *Avisos* toma las diez consultas más frecuentes sobre la tabla de lecturas y mide, para cada una, columnas usadas, rango de fechas y bytes leídos. Siete filtran por fecha y usan tres columnas o menos. Con esa evidencia propone un piloto: escribir la tabla en un formato columnar, particionada por mes y ordenada por fecha dentro de cada archivo, con archivos objetivo de 256 MB y una compactación nocturna. Registra la medida de salida: bytes leídos por consulta frente a la línea base y número de archivos por partición.

## Ejemplo

Ejemplo de [SE-368 — Warehouse, lake, lakehouse y formatos columnares](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md) (sección «Ejemplo mínimo»):

El mínimo y el máximo del bloque son lo que guardaría un formato columnar como estadística: una consulta por `importe > 1000` podría saltar este bloque sin descomprimirlo. Con ocho valores la compresión casi no ahorra; el efecto aparece con miles de valores parecidos.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Fallo.** Tras migrar la tabla de lecturas a un formato columnar, las consultas por rango de fechas no mejoran y el costo mensual no baja. ([SE-368](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md), [SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-367](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Guarda](../g/guarda.md), [Almacén](../a/almacen.md), [Codificación por diccionario](../c/codificacion-por-diccionario.md), [Compactación](../c/compactacion.md), [Estadísticas por grupo](../e/estadisticas-por-grupo.md), [Lago](../l/lago.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-368 — Warehouse, lake, lakehouse y formatos columnares](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-370](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Fork](./fork.md) · [Formatter →](./formatter.md)
