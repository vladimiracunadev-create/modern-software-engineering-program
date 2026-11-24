# Captura de cambios

[↑ Glosario](../../README.md) · [← Captura](./captura.md) · [Característica →](./caracteristica.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

La **captura de cambios** (CDC, por *change data capture*) es el mecanismo que produce un flujo ordenado de altas, cambios y bajas de filas de una base de datos: «se insertó la fila X», «se actualizó la fila Y de este valor a este», «se borró la fila Z» ([SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md)).

## Por qué importa

Sincronizar una base con un almacén analítico u otro sistema puede hacerse copiando todo cada vez, o detectando qué cambió. La captura de cambios decide si el destino se entera de **todo** lo ocurrido, incluidas las bajas y los cambios intermedios, o solo de una foto. Para quien diseña integración, es la diferencia entre un destino que converge con el origen y uno que conserva filas que ya no existen.

## Cómo funciona

[SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md) presenta dos formas de producir el flujo:

- **Disparadores**: cada escritura inserta una fila en una tabla de cambios dentro de la misma transacción. Son simples y se ven en el esquema, pero añaden una escritura a cada operación.
- **Lectura del registro de escritura anticipada** del motor, como la decodificación lógica de PostgreSQL o conectores como Debezium. No toca las operaciones de la aplicación, pero exige permisos y operar el conector.

La causa de que la captura exista es una limitación de la alternativa: la detección por marca de tiempo solo ve filas que existen y cuya marca cambió. Un borrado no deja fila que comparar, así que el destino conserva lo que el origen ya eliminó; y una comparación estricta con la última marca pierde las filas modificadas en el mismo instante. Un flujo de eventos de fila evita ambos fallos porque registra el cambio como hecho, incluida la baja.

## Ejemplo

Una plataforma replica su tabla de entregas a un almacén analítico. Con detección por marca, una entrega eliminada sigue apareciendo en el almacén. Con captura de cambios, el flujo trae un evento de baja y el destino la retira. Como el consumidor puede recibir un evento repetido, aplica los eventos de forma idempotente. Es el patrón que enseña [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md) con datos sintéticos.

## Errores y confusiones comunes

- **El destino tiene filas que ya no existen en el origen**: la detección por marca no ve las bajas; corrección, registro de cambios o lápidas con borrado lógico.
- **Faltan filas modificadas en el último segundo**: comparación estricta con la última marca; corrección, comparar con mayor o igual y aplicar de forma idempotente.
- **Creer que los disparadores son gratis**: añaden escritura a cada operación.
- **Confundirla con replicación del motor**: la captura produce eventos de fila reutilizables, no una copia física.

## Límites y cuándo no aplica

[SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md) declara que sus experimentos son sintéticos, sin motor con registro lógico, conector, almacén ni red; los ritmos y porcentajes son construcciones del autor, por lo que no son una medición de un sistema real. En la práctica, la captura no resuelve por sí sola el orden entre tablas ni la evolución del esquema, y la lectura del registro exige operar el conector. Para volúmenes pequeños con cambios poco frecuentes, una recarga completa puede bastar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Baja](../b/baja.md), [Base](../b/base.md), [Flujo](../f/flujo.md), [Mecanismo](../m/mecanismo.md), [Consistencia eventual](./consistencia-eventual.md), [ELT](../e/elt.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-362](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md).

**Aparece en los casos de estudio:** [Shopify](../../../casos/exito/shopify.md).

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
