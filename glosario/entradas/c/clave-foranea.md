# Clave foránea

[↑ Glosario](../../README.md) · [← Clave del mensaje](./clave-del-mensaje.md) · [Clave sustituta →](./clave-sustituta.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Restricción que obliga a que un valor referencie una fila existente de otra tabla.

Definición de trabajo de [SE-352 — Restricciones, invariantes y consistencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md).

## Por qué importa

En [SE-352 — Restricciones, invariantes y consistencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md), el tema «Claves foráneas y borrado» importa porque el borrado elige entre rechazar, propagar y dejar huérfano.

## Cómo funciona

Según [SE-352 — Restricciones, invariantes y consistencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md):

Una **invariante** es una afirmación que debe ser verdadera siempre que no haya una operación en curso: «una nota está entre 1 y 7», «cada entrega pertenece a un estudiante que existe», «un estudiante entrega una tarea una vez». Se clasifican por su alcance porque el alcance decide el mecanismo: lo que afecta a una columna lo expresa un `CHECK`; a una tabla, un `UNIQUE`; a dos tablas, una clave foránea; a varias filas o a una secuencia de estados («una entrega calificada tiene nota y docente»), un disparador o un servicio. Cuanto más amplia, más cara de imponer y más tentador dejarla a la aplicación.

Según [SE-352 — Restricciones, invariantes y consistencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md):

El equipo de la plataforma escribe cada invariante en una línea con su alcance, su mecanismo y su prueba. «La nota está entre 1 y 7» es un `CHECK`; «un estudiante entrega una tarea una vez» es un `UNIQUE`; «una entrega pertenece a un curso existente» es una clave foránea con `RESTRICT` (borrar un curso con entregas es decisión humana); «una entrega calificada tiene nota y docente» es un disparador con una prueba que intenta insertar la entrega incompleta; y «las notas coinciden con el sistema de la institución» es una reconciliación nocturna con un desfase máximo de 24 horas y una alarma. En el arranque de cada conexión se activa `foreign_keys` y una prueba de humo verifica el rechazo de un dato inválido.

## Ejemplo

Ejemplo de [SE-352 — Restricciones, invariantes y consistencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma escribe cada invariante en una línea con su alcance, su mecanismo y su prueba. «La nota está entre 1 y 7» es un `CHECK`; «un estudiante entrega una tarea una vez» es un `UNIQUE`; «una entrega pertenece a un curso existente» es una clave foránea con `RESTRICT` (borrar un curso con entregas es decisión humana); «una entrega calificada tiene nota y docente» es un disparador con una prueba que intenta insertar la entrega incompleta; y «las notas coinciden con el sistema de la institución» es una reconciliación nocturna con un desfase máximo de 24 horas y una alarma.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Quedan filas que apuntan a un registro inexistente** — causa: clave foránea sin activar o ausente. Corrección: activarla por conexión y probar el rechazo. ([SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Además, en SQLite la clave foránea declarada no se aplica salvo que se active en cada conexión; un motor con la restricción apagada acepta el borrado y deja filas huérfanas sin error. ([SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Restricciones](../r/restricciones.md), [Valor](../v/valor.md), [Disparador](../d/disparador.md), [Invariante](../i/invariante.md), [Reconciliación](../r/reconciliacion.md), [Restricción de integridad](../r/restriccion-de-integridad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-352 — Restricciones, invariantes y consistencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md), [SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md), [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SQLite: claves foráneas](https://www.sqlite.org/foreignkeys.html) — activación y acciones de borrado; autoridad: documentación oficial de SQLite.
- [SQLite: disparadores](https://www.sqlite.org/lang_createtrigger.html) — rechazo de operaciones con `RAISE`; autoridad: documentación oficial de SQLite.
- [PostgreSQL: restricciones](https://www.postgresql.org/docs/current/ddl-constraints.html) — restricciones declarativas y diferidas; autoridad: documentación oficial de PostgreSQL.
- [Kleppmann, «Designing Data-Intensive Applications»](https://dataintensive.net/) — integridad de extremo a extremo; autoridad: autor del libro.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — excepciones de integridad usadas en las pruebas; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Clave del mensaje](./clave-del-mensaje.md) · [Clave sustituta →](./clave-sustituta.md)
