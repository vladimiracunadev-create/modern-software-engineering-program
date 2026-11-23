# Lakehouse

[↑ Glosario](../../README.md) · [← Lago](./lago.md) · [Language server protocol →](./language-server-protocol.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Lago con una capa de metadatos que da transacciones, versiones y esquema.

Definición de trabajo de [SE-368 — Warehouse, lake, lakehouse y formatos columnares](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md).

## Por qué importa

En [SE-368 — Warehouse, lake, lakehouse y formatos columnares](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md), el tema «Almacén, lago y lakehouse» importa porque definen garantías y quién opera el almacenamiento.

## Cómo funciona

Según [SE-368 — Warehouse, lake, lakehouse y formatos columnares](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md):

Un almacén (warehouse) gestiona los datos internamente: esquema, transacciones, concurrencia y optimizador son suyos, y el costo es depender de su formato y de su motor. Un lago (lake) guarda archivos en almacenamiento barato y deja el esquema para la lectura: máxima flexibilidad y almacenamiento económico a cambio de que nadie garantice atomicidad, versiones ni calidad. Un lakehouse añade al lago una capa de metadatos (la lista de archivos de cada versión de una tabla) que da transacciones, instantáneas y evolución de esquema; propuestas como Apache Iceberg y Delta Lake definen esa capa. Ninguna es «la correcta»: cambian el equilibrio entre garantías, costo y control. Fowler advierte que un lago sin curaduría se vuelve un pantano de datos que nadie sabe leer.

Según [SE-368 — Warehouse, lake, lakehouse y formatos columnares](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md):

Depende del volumen, del equipo y del nivel de operación que se acepte. Un lakehouse reduce copias entre lago y almacén pero exige operar la capa de metadatos y la compactación. Un almacén gestionado delega esa operación.

## Ejemplo

Ejemplo de [SE-368 — Warehouse, lake, lakehouse y formatos columnares](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md) (sección «Preguntas frecuentes»):

Depende del volumen, del equipo y del nivel de operación que se acepte. Un lakehouse reduce copias entre lago y almacén pero exige operar la capa de metadatos y la compactación. Un almacén gestionado delega esa operación.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una tabla de un lakehouse no es una carpeta de archivos: es la lista de archivos de una versión, guardada en un manifiesto. ([SE-368](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Capa](../c/capa.md), [Metadatos](../m/metadatos.md).
- **Ver también:** [Esquema](../e/esquema.md), [Lago](./lago.md), [Transacción](../t/transaccion.md), [Versión](../v/version.md), [Almacén](../a/almacen.md), [Codificación por diccionario](../c/codificacion-por-diccionario.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-368 — Warehouse, lake, lakehouse y formatos columnares](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-367](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Lago](./lago.md) · [Language server protocol →](./language-server-protocol.md)
