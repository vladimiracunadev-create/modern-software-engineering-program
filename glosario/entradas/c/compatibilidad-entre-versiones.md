# Compatibilidad entre versiones

[↑ Glosario](../../README.md) · [← Comparación pareada](./comparacion-pareada.md) · [Compatibilidad hacia adelante →](./compatibilidad-hacia-adelante.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Un despliegue no es instantáneo: mientras las instancias se actualizan, hay clientes de las dos versiones usando la misma base. Una migración es **compatible hacia atrás** si el código viejo sigue funcionando con el esquema nuevo, y **hacia delante** si el código nuevo funciona con el esquema viejo. Los cambios de esquema que rompen la compatibilidad (renombrar, quitar, cambiar un tipo, añadir una restricción más estricta) no se pueden hacer en un solo paso con la aplicación viva.

Explicación de la sección «Compatibilidad entre versiones» de [SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md).

## Por qué importa

En [SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), el tema «Compatibilidad entre versiones» importa porque durante el despliegue conviven dos versiones del código.

En [SE-441 — Compatibilidad, portabilidad e interoperabilidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md), el tema «Compatibilidad entre versiones» importa porque decide cuándo un cambio rompe a quien no cambió.

## Cómo funciona

Según [SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), en la sección «Compatibilidad entre versiones»:

Un despliegue no es instantáneo: mientras las instancias se actualizan, hay clientes de las dos versiones usando la misma base. Una migración es **compatible hacia atrás** si el código viejo sigue funcionando con el esquema nuevo, y **hacia delante** si el código nuevo funciona con el esquema viejo. Los cambios de esquema que rompen la compatibilidad (renombrar, quitar, cambiar un tipo, añadir una restricción más estricta) no se pueden hacer en un solo paso con la aplicación viva. La pregunta de diseño no es «qué script ejecuto» sino «qué versión funciona en cada estado».

Según [SE-441 — Compatibilidad, portabilidad e interoperabilidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md), en la sección «Compatibilidad entre versiones»:

Un cambio es **compatible hacia atrás** si los consumidores existentes siguen funcionando con la nueva versión del productor, y **compatible hacia adelante** si los consumidores nuevos pueden leer lo que produce una versión anterior (o los antiguos leer lo nuevo). Añadir un campo opcional suele ser compatible hacia atrás; quitar un campo, renombrarlo o cambiar su tipo no lo es. Pero la respuesta depende del lector: si el consumidor rechaza los campos desconocidos, añadir un campo lo rompe. De ahí que la compatibilidad no sea una propiedad del cambio sino del par productor-consumidor y de la política de lectura. Los números de versión (por ejemplo, el versionado semántico) comunican una intención, y la intención no sustituye a la prueba: un cambio de versión menor que renombra un campo sigue rompiendo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md):

El equipo de la plataforma documenta el renombrado como cuatro migraciones numeradas, cada una desplegable por separado.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md)) son:

- **Errores en las instancias viejas durante un despliegue** — causa: cambio incompatible hecho en un solo paso. Corrección: expandir, migrar y contraer en despliegues separados.
- **El panel se congela al ejecutar una migración** — causa: actualización de muchas filas en una transacción. Corrección: relleno por lotes idempotente y reanudable.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2); la matriz y las filas alteradas fueron idénticas y los pasos de los lotes difirieron un 7 % entre SQLite 3.45.3 y 3.45.1 con la misma proporción.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Compatibilidad hacia atrás](./compatibilidad-hacia-atras.md), [Expandir y contraer](../e/expandir-y-contraer.md), [Interoperabilidad](../i/interoperabilidad.md), [Lector tolerante](../l/lector-tolerante.md), [Matriz de compatibilidad](../m/matriz-de-compatibilidad.md), [Migración](../m/migracion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-441 — Compatibilidad, portabilidad e interoperabilidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-120](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md), [SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md), [SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler y Sadalage, «Evolutionary Database Design»](https://martinfowler.com/articles/evodb.html) — diseño evolutivo del esquema; autoridad: autores del artículo.
- [Fowler, «Parallel Change»](https://martinfowler.com/bliki/ParallelChange.html) — expandir, migrar y contraer; autoridad: autor del texto.
- [SQLite: ALTER TABLE](https://www.sqlite.org/lang_altertable.html) — cambios admitidos y reconstrucción; autoridad: documentación oficial de SQLite.
- [PostgreSQL: ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html) — bloqueos y reescrituras; autoridad: documentación oficial de PostgreSQL.
- [PostgreSQL: CREATE INDEX](https://www.postgresql.org/docs/current/sql-createindex.html) — creación concurrente de índices; autoridad: documentación oficial de PostgreSQL.

---

[↑ Glosario](../../README.md) · [← Comparación pareada](./comparacion-pareada.md) · [Compatibilidad hacia adelante →](./compatibilidad-hacia-adelante.md)
