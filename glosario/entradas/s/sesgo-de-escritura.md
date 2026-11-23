# Sesgo de escritura

[↑ Glosario](../../README.md) · [← Sesgo de automatización](./sesgo-de-automatizacion.md) · [Sesgo de lo ya sabido →](./sesgo-de-lo-ya-sabido.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Anomalía en la que dos transacciones leen lo mismo, escriben filas distintas y juntas rompen una invariante.

Definición de trabajo de [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md).

## Por qué importa

En [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), el tema «Sesgo de escritura» importa porque dos transacciones sanas pueden romper una invariante conjunta.

## Cómo funciona

Según [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), en la sección «Sesgo de escritura»:

Dos transacciones leen lo mismo, deciden por separado y escriben filas distintas. Ningún conflicto de escritura las detiene, pero la combinación rompe una invariante que implica a ambas filas: «siempre queda un docente de guardia». Es la anomalía característica de las instantáneas. Se evita con un nivel serializable, con un bloqueo explícito sobre lo que se lee o convirtiendo la invariante en algo que una sola fila resume (un contador que se actualiza en ambas transacciones y por eso las serializa).

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md):

El equipo de la plataforma clasifica sus operaciones por la invariante que protegen. Para el contador de cupos usa `UPDATE n = n + 1 WHERE n < limite` y comprueba las filas afectadas: si es cero, no hay cupo. Para la transferencia entre cursos envuelve los cuatro pasos en una transacción y la hace idempotente con una clave de operación única.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Dos operaciones sanas rompen una regla conjunta** — causa: sesgo de escritura bajo instantánea. Corrección: serializable, bloqueo explícito o resumen en una fila. ([SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos. Las intercalaciones se forzaron en un solo hilo con SQLite; los niveles de aislamiento son un modelo del autor y no se ejecutó PostgreSQL ni otro motor con instantáneas; no se midió rendimiento, contención ni durabilidad ante apagones. Las cifras describen enumeraciones, no frecuencias.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-350](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Invariante](../i/invariante.md), [Transacción](../t/transaccion.md), [Actualización perdida](../a/actualizacion-perdida.md), [Atomicidad](../a/atomicidad.md), [Intercalación](../i/intercalacion.md), [Serializable](./serializable.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

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

[↑ Glosario](../../README.md) · [← Sesgo de automatización](./sesgo-de-automatizacion.md) · [Sesgo de lo ya sabido →](./sesgo-de-lo-ya-sabido.md)
