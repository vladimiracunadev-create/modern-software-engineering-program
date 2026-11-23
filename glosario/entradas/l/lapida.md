# Lápida

[↑ Glosario](../../README.md) · [← Lanzamiento por fases](./lanzamiento-por-fases.md) · [Latencia →](./latencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Registro de que una clave fue borrada, con su versión, que impide que un cambio anterior la reviva.

Definición de trabajo de [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md).

## Por qué importa

La clase donde se define, [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), existe con este propósito: la clase existe para que eligas cómo se entera una segunda base de lo que cambió en la primera con criterios medibles y no por costumbre: aprenderás a contar qué filas faltan, cuáles están viejas y cuáles sobran en una réplica según el método de detección, cuánto lee y cuánto escribe cada enfoque, y qué aplica o rompe un flujo de cambios que llega repetido y fuera de orden.

## Cómo funciona

Según [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md):

Hay cuatro formas de enterarse. **Comparar todo** (copia completa) ve cualquier diferencia pero lee todo el origen en cada ciclo. **Sondear por marca de tiempo** lee solo las filas modificadas después de la última marca, barato y fácil, con tres huecos: no ve las filas borradas (ya no están), pierde las filas modificadas en el mismo instante que la marca si la comparación es estricta (`>`), y depende de que cada escritura actualice la marca (una que la olvide es invisible). **Columnas de versión** resuelven el orden pero no las bajas. El **registro de cambios** captura cada alta, cambio y baja en el orden de confirmación, y es el único de los cuatro que ve las bajas sin ayuda de una lápida.

Según [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** el total de entregas de analítica supera al de la plataforma y no se reconoce qué entregas sobran. **Hipótesis rivales:** (a) entregas duplicadas por una carga repetida; (b) entregas de otro curso mal asignadas; (c) entregas borradas en el origen que el destino nunca eliminó. **Prueba:** busca en el destino identificadores que no existan en el origen; si todos los sobrantes tienen un identificador ausente en el origen, la causa es la falta de bajas. **Conclusión:** el sondeo por marca no puede ver los borrados.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md):

El equipo de la plataforma decide por destino. **Portal de reportes:** consulta una vista del propio origen, sin copia, porque tolera la carga y necesita el valor actual. **Analítica:** captura de cambios sobre el registro de la base con instantánea inicial, carga cruda (ELT) en una zona sin datos de contacto y transformación posterior, con la versión de cada fila como guarda; el flujo se aplica de forma idempotente y se descarta cualquier cambio con versión menor.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El destino tiene filas que ya no existen en el origen** — causa: la detección por marca no ve las bajas. Corrección: registro de cambios o lápidas con borrado lógico. ([SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El **registro de cambios** captura cada alta, cambio y baja en el orden de confirmación, y es el único de los cuatro que ve las bajas sin ayuda de una lápida. ([SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Registro](../r/registro.md), [Versión](../v/version.md), [Captura de cambios](../c/captura-de-cambios.md), [Consistencia eventual](../c/consistencia-eventual.md), [ELT](../e/elt.md), [ETL](../e/etl.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-378 — CDC, ETL, ELT y sincronización](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [PostgreSQL: decodificación lógica](https://www.postgresql.org/docs/current/logicaldecoding.html) — extracción de cambios desde el registro de escritura anticipada; autoridad: documentación oficial de PostgreSQL.
- [Debezium: conector de PostgreSQL](https://debezium.io/documentation/reference/stable/connectors/postgresql.html) — instantánea y flujo de cambios con entrega al menos una vez; autoridad: proyecto Debezium.
- [SQLite: CREATE TRIGGER](https://www.sqlite.org/lang_createtrigger.html) — disparadores en la misma transacción; autoridad: documentación oficial de SQLite.
- [Microsoft: ETL y ELT](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/etl) — transformar antes o después de cargar; autoridad: documentación de Microsoft.
- [Kleppmann, «Designing Data-Intensive Applications»](https://dataintensive.net/) — captura de cambios y sistemas derivados; autoridad: autor del libro.

---

[↑ Glosario](../../README.md) · [← Lanzamiento por fases](./lanzamiento-por-fases.md) · [Latencia →](./latencia.md)
