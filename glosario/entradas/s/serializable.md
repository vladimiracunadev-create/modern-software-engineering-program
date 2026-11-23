# Serializable

[↑ Glosario](../../README.md) · [← Separación de funciones](./separacion-de-funciones.md) · [Serialización →](./serializacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Nivel que garantiza un resultado equivalente a alguna ejecución una tras otra.

Definición de trabajo de [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md).

## Por qué importa

La clase donde se define, [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), existe con este propósito: la clase existe para que razones sobre qué puede observar una operación mientras otras escriben, y para que elijas el nivel de aislamiento y el patrón de escritura por la invariante que hay que proteger, no por el valor por defecto del motor.

## Cómo funciona

Según [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md):

El aislamiento define qué ve una transacción de lo que otras hacen en paralelo. **Leer lo confirmado** deja que una segunda lectura de la misma fila vea otro valor. **Instantánea** fija lo que se ve al comenzar, de modo que las lecturas repetidas coinciden, y a cambio permite anomalías que implican a varias filas. **Serializable** garantiza un resultado equivalente a alguna ejecución en serie y lo logra con bloqueos o con abortos. El estándar SQL definió los niveles con una lista de anomalías que, como mostraron Berenson y colaboradores, es ambigua y deja fuera varias; por eso el nivel por defecto de cada motor importa y se consulta en su documentación.

Según [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md):

El equipo de la plataforma clasifica sus operaciones por la invariante que protegen. Para el contador de cupos usa `UPDATE n = n + 1 WHERE n < limite` y comprueba las filas afectadas: si es cero, no hay cupo. Para la transferencia entre cursos envuelve los cuatro pasos en una transacción y la hace idempotente con una clave de operación única. Para el relevo de guardia, que implica a varias filas, escribe en la misma fila de un resumen (`guardia_activos`) que ambas transacciones actualizan, de modo que se serialicen; documenta que el mismo patrón en PostgreSQL con nivel por defecto necesitaría `SERIALIZABLE` o un bloqueo explícito. Cada cliente maneja el rechazo con un reintento acotado y con jitter.

## Ejemplo

Ejemplo de [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma clasifica sus operaciones por la invariante que protegen. Para el contador de cupos usa `UPDATE n = n + 1 WHERE n < limite` y comprueba las filas afectadas: si es cero, no hay cupo. Para la transferencia entre cursos envuelve los cuatro pasos en una transacción y la hace idempotente con una clave de operación única. Para el relevo de guardia, que implica a varias filas, escribe en la misma fila de un resumen (`guardia_activos`) que ambas transacciones actualizan, de modo que se serialicen; documenta que el mismo patrón en PostgreSQL con nivel por defecto necesitaría `SERIALIZABLE` o un bloqueo explícito.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Dos operaciones sanas rompen una regla conjunta** — causa: sesgo de escritura bajo instantánea. Corrección: serializable, bloqueo explícito o resumen en una fila. ([SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Evitar una anomalía no sale gratis: un nivel serializable con detección de conflictos aborta transacciones que luego hay que reintentar, y un bloqueo hace esperar. ([SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-350](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Resultado](../r/resultado.md), [Actualización perdida](../a/actualizacion-perdida.md), [Atomicidad](../a/atomicidad.md), [Intercalación](../i/intercalacion.md), [Sesgo de escritura](./sesgo-de-escritura.md), [Transacción](../t/transaccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-067](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md).

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

[↑ Glosario](../../README.md) · [← Separación de funciones](./separacion-de-funciones.md) · [Serialización →](./serializacion.md)
