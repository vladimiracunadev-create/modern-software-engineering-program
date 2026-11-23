# Punto de no retorno

[↑ Glosario](../../README.md) · [← Punto de extensión](./punto-de-extension.md) · [Punto de sensibilidad →](./punto-de-sensibilidad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Paso desde el cual volver atrás exige un respaldo anterior.

Definición de trabajo de [SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md): Paso a partir del cual volver atrás es imposible o destruye datos.

## Por qué importa

En [SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), el tema «Punto de no retorno» importa porque hay un paso desde el que solo un respaldo permite volver.

## Cómo funciona

Según [SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), en la sección «Punto de no retorno»:

Toda migración que pierde información tiene un paso a partir del cual volver exige un respaldo anterior a él (`SE-357`). Identificarlo y nombrarlo es parte del plan: «el paso 4 (quitar `nombre`) es el punto de no retorno; antes de él se toma un respaldo verificado y se espera una semana sin instancias viejas». Las migraciones que mezclan pasos reversibles e irreversibles en un solo despliegue esconden ese punto y obligan a decidir bajo presión.

## Ejemplo

Ejemplo de [SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma documenta el renombrado como cuatro migraciones numeradas, cada una desplegable por separado. La 0042 añade `nombre_completo` y los disparadores de copia; la 0043 rellena por lotes de 1 000 filas con un script idempotente y reanudable que registra el último identificador procesado; la 0044 se aplica cuando el monitor no muestra instancias de la versión 1 desde hace siete días y despliega el código que solo usa la columna nueva; la 0045 quita la columna vieja y los disparadores, y está marcada como punto de no retorno: exige un respaldo verificado reciente (`SE-357`) y la aprobación de la persona responsable.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md)) son:

- **Errores en las instancias viejas durante un despliegue** — causa: cambio incompatible hecho en un solo paso. Corrección: expandir, migrar y contraer en despliegues separados.
- **El panel se congela al ejecutar una migración** — causa: actualización de muchas filas en una transacción. Corrección: relleno por lotes idempotente y reanudable.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- «el paso 4 (quitar `nombre`) es el punto de no retorno; antes de él se toma un respaldo verificado y se espera una semana sin instancias viejas». ([SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md))
- Traslada el análisis a otro cambio (por ejemplo, partir una columna `direccion` en varias): descompónlo en fases compatibles, construye la matriz de versiones contra estados, mide un relleno por lotes y marca el punto de no retorno. ([SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Respaldo](../r/respaldo.md), [Compatibilidad hacia atrás](../c/compatibilidad-hacia-atras.md), [Ensayo de vuelta atrás](../e/ensayo-de-vuelta-atras.md), [Expandir y contraer](../e/expandir-y-contraer.md), [Fase reversible](../f/fase-reversible.md), [Migración](../m/migracion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md), [SE-525](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md), [SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), [SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md).

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

[↑ Glosario](../../README.md) · [← Punto de extensión](./punto-de-extension.md) · [Punto de sensibilidad →](./punto-de-sensibilidad.md)
