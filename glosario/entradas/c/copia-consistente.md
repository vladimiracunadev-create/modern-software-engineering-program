# Copia consistente

[↑ Glosario](../../README.md) · [← Convergencia](./convergencia.md) · [Copia profunda →](./copia-profunda.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Copia que corresponde a un único instante confirmado de la base.

Definición de trabajo de [SE-357 — Backups, restauración y pruebas de recuperación](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md).

## Por qué importa

En [SE-357 — Backups, restauración y pruebas de recuperación](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md), el tema «Copia consistente» importa porque copiar un archivo en uso puede dar un estado a medias.

## Cómo funciona

Según [SE-357 — Backups, restauración y pruebas de recuperación](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md), en la sección «Copia consistente»:

Copiar el archivo de una base mientras otra transacción escribe puede producir una copia con parte de los cambios y no el resto: cada página es válida, el conjunto no corresponde a ningún momento. Hay tres caminos: parar las escrituras, usar un mecanismo del motor que tome una instantánea consistente (la API de copia en línea de SQLite, `pg_dump` o la copia base con archivado de PostgreSQL) o copiar a nivel del sistema de archivos con una instantánea atómica. Lo que no es seguro es la copia ingenua con la base en uso, que además puede dar «éxito» y pasar una comprobación estructural.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-357 — Backups, restauración y pruebas de recuperación](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md):

El equipo de la plataforma fija con la dirección un RPO de 15 minutos para entregas y calificaciones y de 24 horas para registros de acceso, y un RTO de 2 horas. De ahí deriva la estrategia: una copia completa diaria con la API del motor, el registro de cambios archivado cada 5 minutos a un almacén en otra región, y una retención de 14 días para las copias y de 7 para el registro.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La restauración termina bien y los datos son erróneos** — causa: copia ingenua con la base en uso. Corrección: API de copia consistente y verificación de negocio. ([SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-357 — Backups, restauración y pruebas de recuperación](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. Las bases son pequeñas y de SQLite; las 200 mutaciones son construcciones del autor y los fallos de la primera simulación son uniformes con una escritura constante. No se midió el tiempo de restauración ni se probó cifrado, almacenamiento remoto, otro motor o datos de producción.

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
