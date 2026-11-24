# Expandir y contraer

[↑ Glosario](../../README.md) · [← Éxito y no éxito](./exito-y-no-exito.md) · [Expandir, migrar y contraer →](./expandir-migrar-y-contraer.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

**Expandir y contraer** (también llamado cambio paralelo) es el patrón que divide un cambio incompatible en fases compatibles: añadir lo nuevo, migrar a los clientes y quitar lo viejo ([SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md)). El programa lo usa en varios contextos con el mismo núcleo: esquemas de base de datos ([SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), [SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md)), datos analíticos ([SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md)), interfaces entre sistemas ([SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md)) y releases ([SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md)), donde ambas versiones coexisten durante el cambio.

## Por qué importa

Un cambio incompatible hecho en un solo paso exige que todas las piezas cambien a la vez, y eso no ocurre en un sistema con varias instancias, versiones desplegadas y clientes. La decisión que cambia es cómo se renombra o reestructura algo compartido: en varios pasos pequeños, cada uno reversible, en lugar de uno solo irreversible.

## Cómo funciona

[SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md) lo explica con un renombrado de columna. Tres fases:

1. **Expandir**: se añade la columna nueva, se rellena y se mantiene sincronizada con la vieja mediante una escritura doble (por la aplicación o por un disparador). Ambas versiones funcionan.
2. **Migrar**: se despliegan las instancias nuevas, que leen y escriben lo nuevo.
3. **Contraer**: cuando ya no corre ninguna versión vieja, se quita la columna vieja y los disparadores.

La clave, según [SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md), es que en cada paso existen versiones de la aplicación válidas tanto con el esquema en ese estado como con el estado anterior; esto permite desplegar y revertir el código **sin tocar los datos**. Cada fase se despliega y se revierte por separado, y el tiempo entre ellas lo fija la última instancia vieja, no el calendario.

La ventaja se ve contando fallos: renombrar en un solo paso deja en rojo a una versión en cada fase, mientras que expandir y contraer solo deja en rojo a la versión 2 antes del cambio y a la 1 tras quitar la columna vieja, es decir, en los extremos que se evitan por orden de despliegue.

## Ejemplo

Para renombrar `nota` a `calificacion`: se añade `calificacion`, se rellena desde `nota` y se mantiene sincronizada; se despliega la aplicación que lee y escribe `calificacion`; cuando la última instancia vieja se apaga y no quedan lecturas de `nota`, se elimina `nota`. Si algo falla en cualquier fase, se revierte el código y los datos siguen legibles. Ejemplo de [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md).

## Errores y confusiones comunes

- **Tras revertir hay datos ilegibles**: migración destructiva con el despliegue; se corrige expandiendo y contrayendo en despliegues separados ([SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md)).
- **Contraer antes de tiempo**: se quita lo viejo mientras alguien aún lo usa.
- **Olvidar contraer**: la estructura vieja y la doble escritura se quedan para siempre.
- **Creer que sirve solo para bases de datos**: es un patrón de compatibilidad general.

## Límites y cuándo no aplica

Tiene un costo: más pasos, más despliegues, escritura doble y un periodo en que conviven dos estructuras; para un cambio compatible o en un sistema que se puede detener y actualizar entero, es excesivo. Exige disciplina para completar la fase final. Y no resuelve cambios de significado sin cambio de forma (cambio semántico), que requieren además coordinación con los consumidores.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cambio incompatible](../c/cambio-incompatible.md), [Estrategia](./estrategia.md), [Estructura](./estructura.md), [Patrón](../p/patron.md), [Cambio semántico](../c/cambio-semantico.md), [Compatibilidad hacia adelante](../c/compatibilidad-hacia-adelante.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-366 — Contratos de datos y evolución de esquemas](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-380 — Compatibilidad de esquemas y registros](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.
- [SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.
- [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-346](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md), [SE-477](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md), [SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «ParallelChange»](https://martinfowler.com/bliki/ParallelChange.html) — patrón expandir y contraer; autoridad: autor del texto.
- [Fowler y Sadalage, «Evolutionary Database Design»](https://martinfowler.com/articles/evodb.html) — diseño evolutivo del esquema; autoridad: autores del artículo.
- [SQLite: ALTER TABLE](https://www.sqlite.org/lang_altertable.html) — cambios admitidos y reconstrucción; autoridad: documentación oficial de SQLite.
- [PostgreSQL: ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html) — bloqueos y reescrituras; autoridad: documentación oficial de PostgreSQL.
- [PostgreSQL: CREATE INDEX](https://www.postgresql.org/docs/current/sql-createindex.html) — creación concurrente de índices; autoridad: documentación oficial de PostgreSQL.

---

[↑ Glosario](../../README.md) · [← Éxito y no éxito](./exito-y-no-exito.md) · [Expandir, migrar y contraer →](./expandir-migrar-y-contraer.md)
