# Copia consistente

[↑ Glosario](../../README.md) · [← Convergencia](./convergencia.md) · [Copia profunda →](./copia-profunda.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Una **copia consistente** es una copia que corresponde a un único instante confirmado de la base de datos ([SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md)). No basta con que cada página del archivo sea válida: el conjunto debe reflejar un momento en que todas las transacciones confirmadas estaban completas y ninguna a medias.

## Por qué importa

Una copia de seguridad solo vale si se puede restaurar a algo correcto. Copiar el archivo de una base mientras otra transacción escribe puede producir una copia con parte de los cambios y no el resto: cada página es válida, pero el conjunto no corresponde a ningún momento. La decisión que cambia es cómo se hacen las copias: con una técnica que garantice el instante, no con una copia de archivos con la base en uso.

## Cómo funciona

[SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md) presenta tres caminos:

1. **Parar las escrituras** durante la copia.
2. **Usar un mecanismo del motor** que tome una instantánea consistente: la API de copia en línea de SQLite, `pg_dump` o la copia base con archivado de PostgreSQL.
3. **Copiar a nivel del sistema de archivos** con una instantánea atómica.

Lo que no es seguro es la **copia ingenua con la base en uso**. Y su peligro es doble: puede dar «éxito» y además pasar una comprobación estructural, porque cada página individual es válida. El fallo está en la relación entre páginas, que la comprobación de estructura no examina. Por eso [SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md) pide verificar con reglas de negocio (por ejemplo, que los totales cuadren) y no solo con la integridad del archivo; esa verificación se completa con la prueba de restauración.

En el experimento de la clase, con bases de SQLite y 200 mutaciones, se compara la copia ingenua con la copia consistente: la primera produce restauraciones que «terminan bien» con datos erróneos; la segunda, no.

## Ejemplo

Una plataforma copia el archivo de su base cada noche mientras sigue recibiendo entregas. Una noche la copia coincide con una transacción que modifica dos tablas relacionadas: la copia contiene el cambio de una tabla y no el de la otra. La comprobación de integridad pasa. Meses después se restaura y los datos no cuadran. Con la API de copia en línea o con una instantánea atómica, la copia corresponde a un instante confirmado.

## Errores y confusiones comunes

- **La restauración termina bien y los datos son erróneos**: copia ingenua con la base en uso; se corrige con la API de copia consistente y verificación de negocio ([SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md)).
- **Dar por buena una copia porque pasó la comprobación estructural**.
- **Copiar archivos con el motor en marcha** pensando que el sistema de archivos ya es atómico.
- **No restaurar nunca**: una copia que no se ha restaurado es una hipótesis.

## Límites y cuándo no aplica

[SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md) aclara que sus experimentos usan bases pequeñas de SQLite y datos sintéticos; las 200 mutaciones son construcciones del autor y los fallos de la primera simulación son uniformes. No se midió el tiempo de restauración ni se probó cifrado, almacenamiento remoto, otro motor o datos de producción. Una copia consistente da un instante: cuánta información se pierde entre ese instante y el fallo lo define el objetivo de punto de recuperación y, si se necesita menos pérdida, el archivado continuo del registro de cambios.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Base](../b/base.md), [Instante](../i/instante.md), [Objetivo de punto de recuperación](../o/objetivo-de-punto-de-recuperacion.md), [Prueba de restauración](../p/prueba-de-restauracion.md), [Registro de cambios archivado](../r/registro-de-cambios-archivado.md), [RTO](../r/rto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-357 — Backups, restauración y pruebas de recuperación](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), [SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md), [SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SQLite: API de copia en línea](https://www.sqlite.org/backup.html) — copia consistente de una base en uso; autoridad: documentación oficial de SQLite.
- [SQLite: cómo se corrompe una base](https://www.sqlite.org/howtocorrupt.html) — causas de corrupción; autoridad: documentación oficial de SQLite.
- [SQLite: PRAGMA](https://www.sqlite.org/pragma.html) — `integrity_check`, `quick_check` y `foreign_key_check`; autoridad: documentación oficial de SQLite.
- [PostgreSQL: archivado continuo](https://www.postgresql.org/docs/current/continuous-archiving.html) — copia base y registro para recuperar a un instante; autoridad: documentación oficial de PostgreSQL.
- [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) — planes de contingencia, objetivos de recuperación y pruebas; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Convergencia](./convergencia.md) · [Copia profunda →](./copia-profunda.md)
