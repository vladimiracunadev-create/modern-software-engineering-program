# RTO

[↑ Glosario](../../README.md) · [← RRF](./rrf.md) · [RTO (objetivo de tiempo de recuperación) →](./rto-objetivo-de-tiempo-de-recuperacion.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Tiempo máximo que la institución acepta que el servicio esté caído.

Definición de trabajo de [SE-357 — Backups, restauración y pruebas de recuperación](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-440 — Disponibilidad, durabilidad y recuperación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md): Tiempo máximo aceptable entre un fallo y el servicio restablecido.

## Por qué importa

En [SE-357 — Backups, restauración y pruebas de recuperación](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md), el tema «RPO y RTO» importa porque definen cuánto se pierde y cuánto se tarda, y por tanto qué estrategia se necesita.

## Cómo funciona

Según [SE-357 — Backups, restauración y pruebas de recuperación](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md):

El **RPO** (objetivo de punto de recuperación) es cuántos datos puede permitirse perder la institución, medido en tiempo: «hasta 15 minutos». El **RTO** (objetivo de tiempo de recuperación) es cuánto puede estar el servicio caído: «hasta 2 horas». No son técnicos sino de negocio, y los fija quien asume el daño (una nota de cierre de semestre no se puede perder; un historial de accesos de hace un mes, sí). De ellos se deduce la estrategia: un RPO de un día se cumple con una copia diaria; uno de 15 minutos exige archivar el registro de cambios; uno de segundos exige replicación, que no sustituye al respaldo.

Según [SE-357 — Backups, restauración y pruebas de recuperación](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md):

El equipo de la plataforma fija con la dirección un RPO de 15 minutos para entregas y calificaciones y de 24 horas para registros de acceso, y un RTO de 2 horas. De ahí deriva la estrategia: una copia completa diaria con la API del motor, el registro de cambios archivado cada 5 minutos a un almacén en otra región, y una retención de 14 días para las copias y de 7 para el registro. Cada noche, un trabajo restaura la última copia en un entorno aislado, ejecuta la verificación completa (integridad, conteos del manifiesto, suma de notas y claves foráneas) y publica el resultado y el tiempo; si falla, avisa y prueba la copia anterior.

## Ejemplo

Ejemplo de [SE-357 — Backups, restauración y pruebas de recuperación](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma fija con la dirección un RPO de 15 minutos para entregas y calificaciones y de 24 horas para registros de acceso, y un RTO de 2 horas. De ahí deriva la estrategia: una copia completa diaria con la API del motor, el registro de cambios archivado cada 5 minutos a un almacén en otra región, y una retención de 14 días para las copias y de 7 para el registro.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El RTO real es el triple del prometido** — causa: falta detección y verificación en la cuenta. Corrección: medir con un ensayo todo el recorrido. ([SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- No mide el tiempo de restauración (el RTO) ni qué pasa si la copia está dañada. ([SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Servicio](../s/servicio.md), [Causa común](../c/causa-comun.md), [Copia consistente](../c/copia-consistente.md), [Disponibilidad](../d/disponibilidad.md), [Durabilidad](../d/durabilidad.md), [Objetivo de punto de recuperación](../o/objetivo-de-punto-de-recuperacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-357 — Backups, restauración y pruebas de recuperación](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-440 — Disponibilidad, durabilidad y recuperación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

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

[↑ Glosario](../../README.md) · [← RRF](./rrf.md) · [RTO (objetivo de tiempo de recuperación) →](./rto-objetivo-de-tiempo-de-recuperacion.md)
