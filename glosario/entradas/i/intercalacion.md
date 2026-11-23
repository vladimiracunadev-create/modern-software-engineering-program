# Intercalación

[↑ Glosario](../../README.md) · [← Interbloqueo](./interbloqueo.md) · [Interés →](./interes.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Orden concreto en que se alternan los pasos de operaciones concurrentes.

Definición de trabajo de [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md).

## Por qué importa

La clase donde se define, [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), existe con este propósito: la clase existe para que razones sobre qué puede observar una operación mientras otras escriben, y para que elijas el nivel de aislamiento y el patrón de escritura por la invariante que hay que proteger, no por el valor por defecto del motor.

## Cómo funciona

Según [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md):

Un contador de cupos vale 0 y tres clientes lo suben una vez. Con leer-modificar-escribir cada cliente tiene dos pasos (leer, escribir): hay 90 intercalaciones posibles. Se ejecutan todas sobre SQLite con tres conexiones y un orden forzado, en tres variantes: leer-sumar-escribir, escribir solo si la versión no cambió y `UPDATE n = n + 1`.

Según [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md):

El equipo de la plataforma clasifica sus operaciones por la invariante que protegen. Para el contador de cupos usa `UPDATE n = n + 1 WHERE n < limite` y comprueba las filas afectadas: si es cero, no hay cupo. Para la transferencia entre cursos envuelve los cuatro pasos en una transacción y la hace idempotente con una clave de operación única. Para el relevo de guardia, que implica a varias filas, escribe en la misma fila de un resumen (`guardia_activos`) que ambas transacciones actualizan, de modo que se serialicen; documenta que el mismo patrón en PostgreSQL con nivel por defecto necesitaría `SERIALIZABLE` o un bloqueo explícito. Cada cliente maneja el rechazo con un reintento acotado y con jitter.

## Ejemplo

Ejemplo de [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma clasifica sus operaciones por la invariante que protegen. Para el contador de cupos usa `UPDATE n = n + 1 WHERE n < limite` y comprueba las filas afectadas: si es cero, no hay cupo. Para la transferencia entre cursos envuelve los cuatro pasos en una transacción y la hace idempotente con una clave de operación única. Para el relevo de guardia, que implica a varias filas, escribe en la misma fila de un resumen (`guardia_activos`) que ambas transacciones actualizan, de modo que se serialicen; documenta que el mismo patrón en PostgreSQL con nivel por defecto necesitaría `SERIALIZABLE` o un bloqueo explícito.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Las pruebas pasan y producción falla a veces** — causa: pruebas de un solo hilo. Corrección: enumerar intercalaciones y comprobar invariantes. ([SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Solo 6 de 90 intercalaciones (las que ejecutan los tres clientes en serie) dan 3 con leer-sumar-escribir. ([SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-350](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Operación](../o/operacion.md), [Actualización perdida](../a/actualizacion-perdida.md), [Atomicidad](../a/atomicidad.md), [Serializable](../s/serializable.md), [Sesgo de escritura](../s/sesgo-de-escritura.md), [Transacción](../t/transaccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (16 clases más lo mencionan; las que más):

[SE-305](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md), [SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md), [SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md), [SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md), [SE-395](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md), [SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md), [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md), [SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [PostgreSQL: aislamiento de transacciones](https://www.postgresql.org/docs/current/transaction-iso.html) — niveles y anomalías; autoridad: documentación oficial de PostgreSQL.
- [SQLite: aislamiento](https://www.sqlite.org/isolation.html) — comportamiento entre conexiones; autoridad: documentación oficial de SQLite.
- [SQLite: transacciones](https://www.sqlite.org/lang_transaction.html) — `BEGIN` diferido e inmediato; autoridad: documentación oficial de SQLite.
- [Berenson et al., «A Critique of ANSI SQL Isolation Levels»](https://arxiv.org/abs/cs/0701157) — anomalías no cubiertas por el estándar; autoridad: artículo de los autores.
- [Cahill, Röhm y Fekete (2008)](https://dl.acm.org/doi/10.1145/1376616.1376690) — serializabilidad sobre instantáneas; autoridad: artículo original.

---

[↑ Glosario](../../README.md) · [← Interbloqueo](./interbloqueo.md) · [Interés →](./interes.md)
