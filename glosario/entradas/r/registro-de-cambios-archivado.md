# Registro de cambios archivado

[↑ Glosario](../../README.md) · [← Registro de cambios](./registro-de-cambios.md) · [Registro de decisiones →](./registro-de-decisiones.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Secuencia de registros de escritura que permite avanzar una copia hasta un instante posterior.

Definición de trabajo de [SE-357 — Backups, restauración y pruebas de recuperación](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md).

## Por qué importa

La clase donde se define, [SE-357 — Backups, restauración y pruebas de recuperación](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md), existe con este propósito: la clase existe para que definas cuánto dato puedes perder y cuánto tardas en volver, que midas si una copia se puede restaurar y no solo si existe, y que conozcas lo que cada nivel de verificación de una restauración ve y lo que deja pasar.

## Cómo funciona

Según [SE-357 — Backups, restauración y pruebas de recuperación](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md):

El equipo de la plataforma fija con la dirección un RPO de 15 minutos para entregas y calificaciones y de 24 horas para registros de acceso, y un RTO de 2 horas. De ahí deriva la estrategia: una copia completa diaria con la API del motor, el registro de cambios archivado cada 5 minutos a un almacén en otra región, y una retención de 14 días para las copias y de 7 para el registro. Cada noche, un trabajo restaura la última copia en un entorno aislado, ejecuta la verificación completa (integridad, conteos del manifiesto, suma de notas y claves foráneas) y publica el resultado y el tiempo; si falla, avisa y prueba la copia anterior.

## Ejemplo

Ejemplo de [SE-357 — Backups, restauración y pruebas de recuperación](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma fija con la dirección un RPO de 15 minutos para entregas y calificaciones y de 24 horas para registros de acceso, y un RTO de 2 horas. De ahí deriva la estrategia: una copia completa diaria con la API del motor, el registro de cambios archivado cada 5 minutos a un almacén en otra región, y una retención de 14 días para las copias y de 7 para el registro.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-357 — Backups, restauración y pruebas de recuperación](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md)) son:

- **La restauración termina bien y los datos son erróneos** — causa: copia ingenua con la base en uso. Corrección: API de copia consistente y verificación de negocio.
- **Se pierden horas de trabajo tras un borrado accidental** — causa: solo copia diaria y sin registro de cambios. Corrección: archivar el registro para recuperar a un instante.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-357 — Backups, restauración y pruebas de recuperación](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. Las bases son pequeñas y de SQLite; las 200 mutaciones son construcciones del autor y los fallos de la primera simulación son uniformes con una escritura constante. No se midió el tiempo de restauración ni se probó cifrado, almacenamiento remoto, otro motor o datos de producción.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Instante](../i/instante.md), [Registro](./registro.md), [Secuencia](../s/secuencia.md), [Copia consistente](../c/copia-consistente.md), [Objetivo de punto de recuperación](../o/objetivo-de-punto-de-recuperacion.md), [Prueba de restauración](../p/prueba-de-restauracion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-357 — Backups, restauración y pruebas de recuperación](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

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

[↑ Glosario](../../README.md) · [← Registro de cambios](./registro-de-cambios.md) · [Registro de decisiones →](./registro-de-decisiones.md)
