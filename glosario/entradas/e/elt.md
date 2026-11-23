# ELT

[↑ Glosario](../../README.md) · [← Elicitación](./elicitacion.md) · [Embedded & IoT Engineer →](./embedded-iot-engineer.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Modelo en el que los datos se extraen, se cargan crudos y se transforman dentro del destino.

Definición de trabajo de [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md).

## Por qué importa

En [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), el tema «ETL y ELT» importa porque decide si el dato crudo sobrevive para recalcular.

## Cómo funciona

Según [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md):

En **ETL** los datos se transforman antes de cargarse al destino, de modo que el destino guarda solo el resultado limpio; en **ELT** se cargan crudos y se transforman dentro del destino. ETL ahorra espacio y mantiene fuera del destino lo que no debe estar (datos personales que no hacen falta), pero cualquier error en la transformación obliga a volver a extraer del origen, que quizá ya cambió. ELT conserva el crudo y permite recalcular tras corregir una regla, pero guarda más y sitúa datos sensibles en más lugares. La decisión depende de cuánto cambian las reglas, de qué datos pueden salir del origen y de quién paga el almacenamiento y la privacidad.

Según [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md):

El equipo de la plataforma decide por destino. **Portal de reportes:** consulta una vista del propio origen, sin copia, porque tolera la carga y necesita el valor actual. **Analítica:** captura de cambios sobre el registro de la base con instantánea inicial, carga cruda (ELT) en una zona sin datos de contacto y transformación posterior, con la versión de cada fila como guarda; el flujo se aplica de forma idempotente y se descarta cualquier cambio con versión menor. **Búsqueda de entregas:** los eventos de negocio del outbox de `SE-377`, porque solo le interesan los cambios con significado de negocio. Cada día una tarea de reconciliación compara el conteo y la suma de control de las notas por curso entre origen y analítica, y reporta cualquier diferencia con el rango afectado.

## Ejemplo

Ejemplo de [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma decide por destino. **Portal de reportes:** consulta una vista del propio origen, sin copia, porque tolera la carga y necesita el valor actual. **Analítica:** captura de cambios sobre el registro de la base con instantánea inicial, carga cruda (ELT) en una zona sin datos de contacto y transformación posterior, con la versión de cada fila como guarda; el flujo se aplica de forma idempotente y se descarta cualquier cambio con versión menor. **Búsqueda de entregas:** los eventos de negocio del outbox de `SE-377`, porque solo le interesan los cambios con significado de negocio.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **No se puede recalcular tras corregir una regla** — causa: ETL sin conservar el dato crudo. Corrección: ELT, o conservar el dato crudo en una zona controlada. ([SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En **ETL** los datos se transforman antes de cargarse al destino, de modo que el destino guarda solo el resultado limpio; en **ELT** se cargan crudos y se transforman dentro del destino. ([SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Modelo](../m/modelo.md), [Captura de cambios](../c/captura-de-cambios.md), [Consistencia eventual](../c/consistencia-eventual.md), [ETL](./etl.md), [Instantánea](../i/instantanea.md), [Lápida](../l/lapida.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft: ETL y ELT](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/etl) — transformar antes o después de cargar; autoridad: documentación de Microsoft.
- [PostgreSQL: decodificación lógica](https://www.postgresql.org/docs/current/logicaldecoding.html) — extracción de cambios desde el registro de escritura anticipada; autoridad: documentación oficial de PostgreSQL.
- [Debezium: conector de PostgreSQL](https://debezium.io/documentation/reference/stable/connectors/postgresql.html) — instantánea y flujo de cambios con entrega al menos una vez; autoridad: proyecto Debezium.
- [SQLite: CREATE TRIGGER](https://www.sqlite.org/lang_createtrigger.html) — disparadores en la misma transacción; autoridad: documentación oficial de SQLite.
- [Kleppmann, «Designing Data-Intensive Applications»](https://dataintensive.net/) — captura de cambios y sistemas derivados; autoridad: autor del libro.

---

[↑ Glosario](../../README.md) · [← Elicitación](./elicitacion.md) · [Embedded & IoT Engineer →](./embedded-iot-engineer.md)
