# Reposo

[↑ Glosario](../../README.md) · [← Repository](./repository.md) · [Representación →](./representacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Periodo durante el cual ambos esquemas se conservan antes de retirar el antiguo.

Definición de trabajo de [SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md).

## Por qué importa

En [SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md), el tema «Reposo antes de contraer» importa porque los defectos tardan en aparecer.

## Cómo funciona

Según [SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md):

Una migración incremental es una secuencia de estados del sistema en cada uno de los cuales funciona. Las seis fases del proyecto son: **expandir** (se crea la estructura nueva vacía), **rellenar** (se copian los datos históricos por lotes), **doble escritura** (cada escritura nueva va a los dos esquemas), **lectura del nuevo** (las consultas leen el esquema nuevo), **escritura solo en el nuevo** (se deja de escribir en el antiguo) y **contraer** (se retira el antiguo).

Según [SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo entrega un paquete con seis directorios. `plan/` describe las seis fases con su condición de paso y su reversibilidad (sin pérdida hasta la fase 3; con reconstrucción de unas 177 filas hasta el día 3 de la fase 4; sin vuelta tras contraer). `ejecutor/` contiene el relleno condicional reanudable y la doble escritura con bandeja. `verificacion/` compara contenido por rangos y escribe, por fase, qué significa una diferencia. `ensayo/` incluye el script que cronometra la vuelta atrás y cuenta lo perdido.

## Ejemplo

Ejemplo de [SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo entrega un paquete con seis directorios. `plan/` describe las seis fases con su condición de paso y su reversibilidad (sin pérdida hasta la fase 3; con reconstrucción de unas 177 filas hasta el día 3 de la fase 4; sin vuelta tras contraer). `ejecutor/` contiene el relleno condicional reanudable y la doble escritura con bandeja. `verificacion/` compara contenido por rangos y escribe, por fase, qué significa una diferencia. `ensayo/` incluye el script que cronometra la vuelta atrás y cuenta lo perdido.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se contrae y un defecto aparece después** — causa: reposo menor que el tiempo de descubrimiento. Corrección: calcular el reposo con la distribución de defectos y el calendario. ([SE-528](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Para pasar de una fase a la siguiente se exige una **condición medible**: tras rellenar, cero diferencias en la verificación; tras la doble escritura, tres reconciliaciones seguidas sin diferencias; tras leer del nuevo, la tasa de errores y la latencia dentro de objetivo durante un periodo; antes de contraer, un reposo cumplido y una copia restaurada. ([SE-528](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md), [SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md), [SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md), [SE-525](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Esquema](../e/esquema.md), [Ensayo de vuelta atrás](../e/ensayo-de-vuelta-atras.md), [Fase reversible](../f/fase-reversible.md), [Paquete de migración](../p/paquete-de-migracion.md), [Punto de no retorno](../p/punto-de-no-retorno.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-267](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md), [SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), [SE-461](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-461-criptografia-aplicada-y-gestion-de-claves/README.md), [SE-525](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md), [SE-535](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-535-compras-proveedores-y-evaluacion-tecnica/README.md), [SE-022](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md), [SE-285](../../../classes/part-23-runtimes-y-plataformas-modernas/se-285-criptografia-poscuantica-y-migracion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «ParallelChange»](https://martinfowler.com/bliki/ParallelChange.html) — expandir, migrar y contraer; autoridad: autor del texto.
- [Fowler, «StranglerFigApplication»](https://martinfowler.com/bliki/StranglerFigApplication.html) — reemplazo incremental; autoridad: autor del texto.
- [Fowler y Sadalage, «Evolutionary Database Design»](https://martinfowler.com/articles/evodb.html) — cambios de esquema pequeños y automatizados; autoridad: autores del texto.
- [Patrón Transactional Outbox](https://microservices.io/patterns/data/transactional-outbox.html) — dos copias alineadas con eventos; autoridad: catálogo de patrones.
- [DORA: las cuatro claves](https://dora.dev/guides/dora-metrics-four-keys/) — tasa de cambios fallidos y tiempo de recuperación; autoridad: DORA.

---

[↑ Glosario](../../README.md) · [← Repository](./repository.md) · [Representación →](./representacion.md)
