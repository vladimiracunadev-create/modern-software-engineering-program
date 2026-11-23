# Actualización perdida

[↑ Glosario](../../README.md) · [← Actualización inalámbrica](./actualizacion-inalambrica.md) · [Actualización y rollback →](./actualizacion-y-rollback.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Escritura que se pisa con otra basada en una lectura anterior sin que ninguna falle.

Definición de trabajo de [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md): Efecto por el que una escritura posterior sobrescribe otra sin haberla visto.

## Por qué importa

En [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), el tema «Actualización perdida» importa porque dos escrituras sobre la misma lectura dejan una sola en silencio.

## Cómo funciona

Según [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), en la sección «Actualización perdida»:

Leer un valor, calcular el nuevo y escribirlo es tres pasos; si dos clientes los intercalan, el segundo escribe sobre una lectura vieja y la primera escritura se pierde. Ninguno recibe un error. Hay tres remedios con costos distintos: hacer que la base calcule (`UPDATE ... SET n = n + 1`), comprobar la versión al escribir y reintentar si cambió, o bloquear la fila mientras se calcula. La primera es la más barata cuando el cálculo cabe en una expresión; la segunda, cuando hay un cálculo del lado de la aplicación y los conflictos son raros; la tercera, cuando son frecuentes.

## Ejemplo

Ejemplo de [SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md) (sección «Ejemplo mínimo»):

El fragmento muestra una actualización perdida con dos clientes. Antes de ejecutarlo, predice el valor final.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md)) son:

- **Un contador queda por debajo de las operaciones confirmadas** — causa: leer-modificar-escribir sin control. Corrección: actualización atómica o comprobación de versión con reintento.
- **Una transferencia cortada deja cupos perdidos** — causa: sentencias confirmadas por separado. Corrección: envolver los pasos en una transacción e idempotencia.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-351 — Transacciones, aislamiento y concurrencia](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos. Las intercalaciones se forzaron en un solo hilo con SQLite; los niveles de aislamiento son un modelo del autor y no se ejecutó PostgreSQL ni otro motor con instantáneas; no se midió rendimiento, contención ni durabilidad ante apagones. Las cifras describen enumeraciones, no frecuencias.

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
