# Expandir y contraer

[↑ Glosario](../../README.md) · [← Éxito y no éxito](./exito-y-no-exito.md) · [Expandir, migrar y contraer →](./expandir-migrar-y-contraer.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Patrón que divide un cambio incompatible en fases compatibles: añadir lo nuevo, migrar a los clientes y quitar lo viejo.

Definición de trabajo de [SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md): Patrón que añade la estructura nueva, migra consumidores y datos, y retira la antigua en pasos compatibles.
- En [SE-366 — Contratos de datos y evolución de esquemas](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md): Añadir lo nuevo, migrar y quitar lo viejo en pasos.
- En [SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md): Patrón de cambio de datos en tres fases en el que ambas versiones coexisten.
- En [SE-380 — Compatibilidad de esquemas y registros](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md): Estrategia de cambio incompatible en fases: añadir lo nuevo en paralelo, migrar a los consumidores y retirar lo viejo.

## Por qué importa

En [SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), el tema «Expandir y contraer» importa porque divide un cambio incompatible en pasos compatibles.

## Cómo funciona

Según [SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), en la sección «Expandir y contraer»:

El patrón de cambio en paralelo divide un cambio incompatible en tres fases compatibles. **Expandir:** se añade la columna nueva, se rellena y se mantiene sincronizada con la vieja con una escritura doble (por la aplicación o por un disparador); ambas versiones funcionan. **Migrar:** se despliegan las instancias nuevas, que leen y escriben lo nuevo. **Contraer:** cuando ya no corre ninguna versión vieja, se quita la columna vieja y los disparadores. Cada fase se puede desplegar y revertir por separado, y el tiempo entre ellas lo fija la última instancia vieja, no el calendario.

Según [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md), en la sección «Expandir y contraer»:

El patrón de **cambio paralelo** descompone un cambio incompatible en tres movimientos. En **expandir** se añade la estructura nueva junto a la antigua sin retirar nada: una columna nueva, nula, que ninguna versión de la aplicación necesita todavía. En **migrar** se llevan los consumidores y los datos a la nueva: la aplicación empieza a escribir en ambas, se rellena lo histórico, se verifica y se cambia la lectura. En **contraer** se retira lo antiguo cuando nadie lo usa. La clave es que en cada paso existen versiones de la aplicación válidas con el esquema en ese estado y con el estado anterior, lo que permite desplegar y revertir el código sin tocar los datos.

## Ejemplo

Ejemplo de [SE-476 — Canary, blue-green y rollback](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md) (sección «Ejemplo profesional»):

El equipo de la API de entregas despliega cada versión en cuatro fases: 1 % durante diez minutos, 5 % durante veinte, 25 % durante treinta y 100 % con la versión anterior conservada una hora. Las métricas son la tasa de error y el percentil 99 de la latencia, comparadas en paralelo con la versión anterior; el umbral es z = 4 con un mínimo de 2 000 solicitudes por fase, una barandilla automática que revierte si el error absoluto del canario supera el 5 % y la regla de que cualquier persona de guardia puede abortar.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Tras revertir hay datos ilegibles** — causa: migración destructiva con el despliegue. Corrección: expandir y contraer en despliegues separados. ([SE-476](../../../classes/part-39-build-release-y-cadena-de-suministro/se-476-canary-blue-green-y-rollback/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Mira primero que renombrar en un solo paso deja en rojo a una versión en cada fase, mientras que expandir y contraer solo deja en rojo a la versión 2 antes del cambio y a la 1 tras quitar la columna vieja. ([SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md))

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
