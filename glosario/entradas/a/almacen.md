# Almacén

[↑ Glosario](../../README.md) · [← Aliasing](./aliasing.md) · [Almacén de características →](./almacen-de-caracteristicas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Sistema que gestiona el almacenamiento, el esquema y las transacciones de datos analíticos.

Definición de trabajo de [SE-368 — Warehouse, lake, lakehouse y formatos columnares](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md): Estado de una ejecución: memoria, combustible, límites y datos del anfitrión.

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

- Un almacén (warehouse) gestiona los datos internamente: esquema, transacciones, concurrencia y optimizador son suyos, y el costo es depender de su formato y de su motor. ([SE-368](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md))
- En `wasmtime`, `Engine` es la configuración y el compilador, `Module` es el binario ya compilado a código nativo, `Store` es el estado de una ejecución (memoria, combustible, límites) e `Instance` es el módulo con su memoria enlazada. ([SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Combustible](../c/combustible.md).
- **Ver también:** [Anfitrión](./anfitrion.md), [Esquema](../e/esquema.md), [Estado](../e/estado.md), [Límite](../l/limite.md), [Borde](../b/borde.md), [Codificación por diccionario](../c/codificacion-por-diccionario.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-368 — Warehouse, lake, lakehouse y formatos columnares](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (57 clases más lo mencionan; las que más):

[SE-593](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md), [SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md), [SE-043](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md), [SE-345](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md), [SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md), [SE-602](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-602-datos-de-entrenamiento-etiquetas-y-feature-stores/README.md), [SE-350](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md), [SE-418](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Store», «warehouse».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Aliasing](./aliasing.md) · [Almacén de características →](./almacen-de-caracteristicas.md)
