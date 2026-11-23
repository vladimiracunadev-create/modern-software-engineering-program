# Restricción de integridad

[↑ Glosario](../../README.md) · [← Restauración](./restauracion.md) · [Restricción dura →](./restriccion-dura.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Regla declarada en el esquema que el motor hace cumplir en cada cambio.

Definición de trabajo de [SE-352 — Restricciones, invariantes y consistencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md).

## Por qué importa

La clase donde se define, [SE-352 — Restricciones, invariantes y consistencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md), existe con este propósito: la clase existe para que decidas qué invariantes del negocio las impone el motor y cuáles quedan en la aplicación, y para que midas cuántos datos inválidos deja pasar cada capa antes de que una persona los encuentre en un informe.

## Cómo funciona

[SE-352 — Restricciones, invariantes y consistencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-352 — Restricciones, invariantes y consistencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md):

El equipo de la plataforma escribe cada invariante en una línea con su alcance, su mecanismo y su prueba. «La nota está entre 1 y 7» es un `CHECK`; «un estudiante entrega una tarea una vez» es un `UNIQUE`; «una entrega pertenece a un curso existente» es una clave foránea con `RESTRICT` (borrar un curso con entregas es decisión humana);

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-352 — Restricciones, invariantes y consistencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md)) son:

- **Aparecen notas fuera de rango en un informe** — causa: validación solo en un cliente. Corrección: `CHECK` en el esquema y prueba de rechazo.
- **Hay entregas duplicadas bajo carga** — causa: comprobar y luego insertar. Corrección: `UNIQUE` y manejo del error de unicidad.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-352 — Restricciones, invariantes y consistencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. Los defectos se generaron conociendo lo que cada capa detecta, por lo que la cobertura real es desconocida; las intercalaciones se forzaron en un hilo con SQLite; no se probó otro motor y el comportamiento de las claves foráneas apagadas es específico de SQLite.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Esquema](../e/esquema.md), [Motor](../m/motor.md), [Regla](./regla.md), [Clave foránea](../c/clave-foranea.md), [Disparador](../d/disparador.md), [Invariante](../i/invariante.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-352 — Restricciones, invariantes y consistencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

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

[↑ Glosario](../../README.md) · [← Restauración](./restauracion.md) · [Restricción dura →](./restriccion-dura.md)
