# Actualización perdida

[↑ Glosario](../../README.md) · [← Actualización inalámbrica](./actualizacion-inalambrica.md) · [Actualización y rollback →](./actualizacion-y-rollback.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Una **actualización perdida** (*lost update*) ocurre cuando una escritura se pisa con otra que se basó en una lectura anterior, sin que ninguna de las dos falle. [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) la presenta como una anomalía de concurrencia en transacciones; [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md) usa el mismo término en HTTP: una escritura posterior sobrescribe otra sin haberla visto. El rasgo que la hace peligrosa es el silencio: ningún cliente recibe un error.

## Por qué importa

Es de los defectos de datos más difíciles de ver, porque el sistema «funciona»: cada petición tiene éxito y aun así el estado final no corresponde a ninguna ejecución ordenada. [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) muestra el síntoma típico: un contador queda por debajo de las operaciones confirmadas. La decisión que cambia es dónde se hace el cálculo y qué mecanismo protege el ciclo leer-calcular-escribir.

## Cómo funciona

Leer un valor, calcular el nuevo y escribirlo son tres pasos. Si dos clientes los intercalan:

1. A lee 10. B lee 10.
2. A escribe 11. B escribe 11.
3. Debían ser 12; la escritura de A se perdió.

[SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) da tres remedios con costos distintos:

- **Que la base calcule:** `UPDATE ... SET n = n + 1`. Es la más barata cuando el cálculo cabe en una expresión, porque lectura y escritura ocurren en una sola sentencia.
- **Comprobar la versión al escribir y reintentar** si cambió. Conviene cuando el cálculo ocurre en la aplicación y los conflictos son raros. En HTTP es la misma idea que [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md) enseña con una precondición sobre la versión del recurso.
- **Bloquear la fila** mientras se calcula. Conviene cuando los conflictos son frecuentes, a costa de esperas.

## Ejemplo

El ejemplo mínimo de [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) ejecuta dos clientes que leen el mismo valor y escriben, y pide predecir el valor final antes de correrlo. Un esbozo ilustrativo (no es código de la clase):

```sql
-- Cliente A y B, intercalados: ambos leen n = 10
UPDATE cuenta SET n = 11 WHERE id = 1; -- A
UPDATE cuenta SET n = 11 WHERE id = 1; -- B (debía ser 12)
-- Corrección: UPDATE cuenta SET n = n + 1 WHERE id = 1;
```

## Errores y confusiones comunes

- **Contador por debajo de lo confirmado** por leer-modificar-escribir sin control ([SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md)).
- **Creer que una transacción lo impide siempre.** Depende del nivel de aislamiento y del motor; la clase modela niveles de aislamiento, pero no ejecutó un motor con instantáneas.
- **Confundirla con una lectura sucia o una condición de carrera en memoria:** aquí cada escritura es válida; lo que falla es la base de la que partió.

## Límites y cuándo no aplica

Solo existe cuando hay lectura previa que alimenta la escritura; una escritura que no depende de lo leído («fija el estado en cerrado») no la sufre, aunque puede decidirse si la última escritura debe ganar. Los experimentos de [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) forzaron intercalaciones en un solo hilo con SQLite y no midieron rendimiento ni contención; las cifras describen enumeraciones, no frecuencias reales.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Efecto](../e/efecto.md), [Atomicidad](./atomicidad.md), [Colección](../c/coleccion.md), [ETag](../e/etag.md), [Intercalación](../i/intercalacion.md), [Keyset](../k/keyset.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-227](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), [SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md), [SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md), [SE-305](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md), [SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md).

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

[↑ Glosario](../../README.md) · [← Actualización inalámbrica](./actualizacion-inalambrica.md) · [Actualización y rollback →](./actualizacion-y-rollback.md)
