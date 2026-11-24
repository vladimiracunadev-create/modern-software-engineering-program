# Prueba de restauración

[↑ Glosario](../../README.md) · [← Prueba de resistencia](./prueba-de-resistencia.md) · [Prueba de trabajo →](./prueba-de-trabajo.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

La **prueba de restauración** es el ejercicio que restaura una copia en un entorno aislado y verifica su contenido y su tiempo ([SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md)). Es la única prueba de la hipótesis de que se puede volver: una copia que nunca se restauró es una suposición.

## Por qué importa

Hacer copias de seguridad es fácil; recuperar es lo que cuenta. Las copias pueden estar incompletas, corruptas, inconsistentes o simplemente ser inutilizables con los procedimientos que el equipo conoce. La decisión que cambia es qué se considera «respaldado»: no lo que tiene una copia, sino lo que se ha restaurado con éxito, y en qué tiempo.

## Cómo funciona

[SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md) define el procedimiento: restaurar una copia reciente en un entorno aislado, ejecutar la verificación, medir el tiempo y registrar quién lo hizo y qué falló. Dos reglas de frecuencia:

- **Periódica**: una copia no ensayada en el último trimestre se considera **no verificada**.
- **Tras cada cambio** que afecte al respaldo: una migración, un cambio de proveedor.

La verificación debe ser **de negocio**, no solo estructural: una copia ingenua tomada con la base en uso puede restaurarse «con éxito» y tener datos erróneos, porque cada página es válida pero el conjunto no corresponde a ningún instante. Por eso la clase combina la prueba de restauración con la copia consistente: la primera prueba el camino de vuelta, la segunda garantiza el contenido.

También hay que ensayar el **caso inverso**: qué pasa cuando la última copia está dañada y hay que usar la anterior, y cuántos datos más se pierden. Eso conecta con el objetivo de punto de recuperación: la restauración mide el tiempo realmente necesario (que alimenta el RTO) y revela cuánta información se pierde (el RPO real).

## Ejemplo

Cada trimestre, el equipo restaura la copia más reciente en un entorno aislado, ejecuta consultas de verificación de negocio (totales, conteos, relaciones), mide cuánto tarda y anota quién lo hizo y qué falló. En una prueba descubren que el procedimiento depende de una clave que solo conocía una persona. Lo corrigen antes de necesitarlo. Ilustración del procedimiento de [SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md).

## Errores y confusiones comunes

- **La restauración termina bien y los datos son erróneos**: copia ingenua con la base en uso; se corrige con la API de copia consistente y verificación de negocio.
- **Se pierden horas de trabajo tras un borrado accidental**: solo copia diaria y sin registro de cambios; se corrige archivando el registro para recuperar a un instante.
- **Comprobar solo que el archivo existe o que el motor arranca**.
- **No registrar quién y cómo**: el conocimiento queda en una persona.

## Límites y cuándo no aplica

[SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md) aclara que sus experimentos usan bases pequeñas de SQLite y datos sintéticos; no se midió el tiempo de restauración con volumen real ni se probó cifrado, almacenamiento remoto, otro motor o datos de producción. Una restauración probada en un entorno aislado no garantiza el tiempo en una emergencia real (con otro volumen, otra red y menos calma). Y verifica un momento: la copia de hoy, no las futuras.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Entorno aislado](../e/entorno-aislado.md), [Entorno](../e/entorno.md), [Copia consistente](../c/copia-consistente.md), [Objetivo de punto de recuperación](../o/objetivo-de-punto-de-recuperacion.md), [Registro de cambios archivado](../r/registro-de-cambios-archivado.md), [RTO](../r/rto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-357 — Backups, restauración y pruebas de recuperación](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md), [SE-525](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md), [SE-535](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-535-compras-proveedores-y-evaluacion-tecnica/README.md), [SE-582](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md), [SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md).

**Aparece en los casos de estudio:** [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

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

[↑ Glosario](../../README.md) · [← Prueba de resistencia](./prueba-de-resistencia.md) · [Prueba de trabajo →](./prueba-de-trabajo.md)
