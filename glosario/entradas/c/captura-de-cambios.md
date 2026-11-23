# Captura de cambios

[↑ Glosario](../../README.md) · [← Captura](./captura.md) · [Característica →](./caracteristica.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Mecanismo que produce un flujo ordenado de altas, cambios y bajas de filas de una base de datos.

Definición de trabajo de [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md).

## Por qué importa

En [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), el tema «Captura de cambios» importa porque trae altas, cambios y bajas en orden, a costa de operar el mecanismo.

## Cómo funciona

Según [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), en la sección «Captura de cambios»:

La **captura de cambios** (CDC) produce un flujo de eventos de fila: «se insertó la fila X», «se actualizó la fila Y de este valor a este», «se borró la fila Z». Puede hacerse con **disparadores** (cada escritura inserta en una tabla de cambios en la misma transacción) o leyendo el **registro de escritura anticipada** del motor, como hacen la decodificación lógica de PostgreSQL y conectores como Debezium. Los disparadores son simples y se ven en el esquema, pero añaden escritura a cada operación; el registro del motor no toca las operaciones y exige permisos y operación del conector.

## Ejemplo

Ejemplo de [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma decide por destino. **Portal de reportes:** consulta una vista del propio origen, sin copia, porque tolera la carga y necesita el valor actual. **Analítica:** captura de cambios sobre el registro de la base con instantánea inicial, carga cruda (ELT) en una zona sin datos de contacto y transformación posterior, con la versión de cada fila como guarda; el flujo se aplica de forma idempotente y se descarta cualquier cambio con versión menor. **Búsqueda de entregas:** los eventos de negocio del outbox de `SE-377`, porque solo le interesan los cambios con significado de negocio.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md)) son:

- **El destino tiene filas que ya no existen en el origen** — causa: la detección por marca no ve las bajas. Corrección: registro de cambios o lápidas con borrado lógico.
- **Faltan filas modificadas en el último segundo** — causa: comparación estricta con la última marca. Corrección: comparar con mayor o igual y aplicar de forma idempotente.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos salvo los pasos de la máquina virtual. No se usó ningún motor con registro lógico, conector, almacén analítico ni red: el ritmo de operaciones, la resolución de la marca, los porcentajes de reordenado y duplicado y las tasas de cambio son construcciones del autor, y los resultados no se extrapolan a ningún producto.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Baja](../b/baja.md), [Base](../b/base.md), [Flujo](../f/flujo.md), [Mecanismo](../m/mecanismo.md), [Consistencia eventual](./consistencia-eventual.md), [ELT](../e/elt.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-362](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «CDC».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Kleppmann, «Designing Data-Intensive Applications»](https://dataintensive.net/) — captura de cambios y sistemas derivados; autoridad: autor del libro.
- [PostgreSQL: decodificación lógica](https://www.postgresql.org/docs/current/logicaldecoding.html) — extracción de cambios desde el registro de escritura anticipada; autoridad: documentación oficial de PostgreSQL.
- [Debezium: conector de PostgreSQL](https://debezium.io/documentation/reference/stable/connectors/postgresql.html) — instantánea y flujo de cambios con entrega al menos una vez; autoridad: proyecto Debezium.
- [SQLite: CREATE TRIGGER](https://www.sqlite.org/lang_createtrigger.html) — disparadores en la misma transacción; autoridad: documentación oficial de SQLite.
- [Microsoft: ETL y ELT](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/etl) — transformar antes o después de cargar; autoridad: documentación de Microsoft.

---

[↑ Glosario](../../README.md) · [← Captura](./captura.md) · [Característica →](./caracteristica.md)
