# Punto de no retorno

[↑ Glosario](../../README.md) · [← Punto de extensión](./punto-de-extension.md) · [Punto de sensibilidad →](./punto-de-sensibilidad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

El **punto de no retorno** es el paso de una migración desde el cual volver atrás exige un respaldo anterior a él ([SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md)). [SE-528](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md) lo formula como el paso a partir del cual volver atrás es imposible o destruye datos. Todo cambio que pierde información tiene uno.

## Por qué importa

Una migración con varios pasos mezcla pasos reversibles y otros que no lo son. Si ese límite no se nombra, se cruza sin darse cuenta y la decisión de seguir adelante o de retroceder se toma bajo presión, con el sistema ya roto. La decisión que cambia es que el punto se identifica, se nombra y se prepara antes de ejecutar, con respaldo verificado y criterios de espera.

## Cómo funciona

[SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md) lo ubica dentro del patrón expandir y contraer. Las fases de expandir y migrar son reversibles: se puede volver al código anterior sin perder datos. Contraer, es decir, quitar la columna o estructura vieja, no lo es: una vez eliminada, volver exige restaurar desde un respaldo anterior a ese paso ([SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md)). Por eso la clase pide que el plan lo diga con todas las letras: «el paso 4 (quitar `nombre`) es el punto de no retorno; antes de él se toma un respaldo verificado y se espera una semana sin instancias viejas».

La clase observa el riesgo de ocultarlo: las migraciones que mezclan pasos reversibles e irreversibles en un solo despliegue esconden ese punto y obligan a decidir bajo presión. Separar los pasos en despliegues distintos hace que el punto sea un lugar concreto del calendario, con su preparación: respaldo verificado (con prueba de restauración), un periodo de espera sin versiones viejas y la decisión explícita de cruzarlo.

[SE-528](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md) aplica la misma idea a la modernización de sistemas heredados: identificar el paso desde el cual el sistema antiguo ya no se puede reanudar y preparar el ensayo de vuelta atrás antes.

## Ejemplo

Para separar una columna `direccion` en varias, el plan descompone el cambio en fases compatibles. Las tres primeras (añadir columnas nuevas, escribir en ambas, migrar lecturas) son reversibles. La cuarta, quitar `direccion`, es el punto de no retorno: antes se toma un respaldo verificado y se espera una semana sin instancias de la versión vieja. Ejercicio de transferencia de [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md).

## Errores y confusiones comunes

- **Errores en las instancias viejas durante un despliegue**: cambio incompatible hecho en un solo paso; se corrige expandiendo, migrando y contrayendo en despliegues separados.
- **El panel se congela al ejecutar una migración**: actualización de muchas filas en una transacción; se corrige con un relleno por lotes idempotente y reanudable.
- **No nombrar el punto**: se cruza sin decisión consciente.
- **Respaldo no verificado**: sin prueba de restauración no hay vuelta atrás real.

## Límites y cuándo no aplica

No toda migración lo tiene: un cambio solo aditivo y compatible puede revertirse siempre. El respaldo previo permite volver al estado anterior al paso, pero no recupera los cambios hechos después: los datos nuevos escritos tras cruzarlo se pierden al restaurar. Y la espera de una semana es el ejemplo de la clase, no una regla general: depende de cuánto tarde en salir de circulación la última instancia vieja.

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
