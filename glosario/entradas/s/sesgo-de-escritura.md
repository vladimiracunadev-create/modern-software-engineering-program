# Sesgo de escritura

[↑ Glosario](../../README.md) · [← Sesgo de automatización](./sesgo-de-automatizacion.md) · [Sesgo de lo ya sabido →](./sesgo-de-lo-ya-sabido.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

El **sesgo de escritura** (*write skew*) es la anomalía en la que dos transacciones leen lo mismo, escriben filas distintas y juntas rompen una invariante ([SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md)). Ninguna sobrescribe lo que la otra escribió, y sin embargo el resultado combinado viola una regla que implica a ambas filas.

## Por qué importa

Es un error de concurrencia sutil: cada transacción es correcta por separado y no hay conflicto de escritura que la detenga. Sucede en un nivel de aislamiento que muchos sistemas usan por defecto. La decisión que cambia es cómo se protege una regla que abarca varias filas: no alcanza con asumir que las transacciones «aíslan» lo suficiente.

## Cómo funciona

[SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) lo describe con una invariante: «siempre queda un docente de guardia». Dos docentes de guardia piden salir a la vez. Cada transacción lee que hay dos docentes de guardia, decide que puede salir, y actualiza **su propia** fila. Como escriben filas distintas, ningún conflicto de escritura las detiene; al final no queda ninguno.

Es la anomalía característica de las **instantáneas** (aislamiento basado en versiones): cada transacción lee una foto consistente del inicio, y esa foto no refleja lo que la otra está haciendo. La actualización perdida, por contraste, sí es un conflicto de escritura sobre la misma fila y las instantáneas la detectan; el sesgo no.

La clase da tres formas de evitarlo:

1. **Nivel serializable**: el motor detecta y aborta la combinación peligrosa.
2. **Bloqueo explícito** sobre lo que se lee: obliga a esperar al otro.
3. **Convertir la invariante en algo que una sola fila resume**: por ejemplo, un contador de docentes de guardia que ambas transacciones actualizan; al escribir la misma fila, se serializan.

## Ejemplo

Dos transacciones leen «hay 2 docentes de guardia». T1 marca a A como libre; T2 marca a B como libre. Ninguna toca la fila de la otra, ambas confirman y no queda nadie de guardia. Con un contador `guardias` que ambas decrementan solo si es mayor que 1, la segunda transacción entra en conflicto en esa fila y se serializa. Caso de [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md).

## Errores y confusiones comunes

- **Dos operaciones sanas rompen una regla conjunta**: sesgo de escritura bajo instantánea; se corrige con serializable, bloqueo explícito o resumen en una fila.
- **Creer que evitar actualizaciones perdidas basta**: el sesgo ocurre sin escribir la misma fila.
- **Confiar en el aislamiento por defecto** sin conocer su nivel.
- **Validar la invariante solo en la lectura**.

## Límites y cuándo no aplica

[SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) aclara que sus experimentos forzaron las intercalaciones en un solo hilo con SQLite; los niveles de aislamiento son un modelo del autor y no se ejecutó PostgreSQL ni otro motor con instantáneas; no se midió rendimiento, contención ni durabilidad ante apagones, y las cifras describen enumeraciones, no frecuencias. Los motores con aislamiento serializable pagan costo en reintentos y abortos. Si la regla no abarca varias filas, no hay sesgo posible.

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
