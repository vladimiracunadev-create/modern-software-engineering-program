# Ensayo de vuelta atrás

[↑ Glosario](../../README.md) · [← Ensayo](./ensayo.md) · [Ensayo en copia →](./ensayo-en-copia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Ejecución controlada de la reversión para medir su duración y lo que se pierde.

Definición de trabajo de [SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md).

## Por qué importa

La clase donde se define, [SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md), existe con este propósito: el proyecto existe para que ejecutes de principio a fin una migración incremental reversible y entregues un paquete que otra persona pueda comprobar, repetir y desmontar.

## Cómo funciona

Según [SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md):

El entregable no es el script sino el paquete que permite a otra persona comprobar la migración sin confiar en quien la hizo. Debe contener el **plan de fases** con las condiciones de paso, el **ejecutor** idempotente y reanudable, la **verificación de contenido** con su interpretación por fase, el **ensayo de vuelta atrás** con el número de escrituras perdidas, los **criterios de reposo** con su fundamento, los **datos sintéticos** con semilla y un `LIMITES.md` que diga qué no se probó: no hubo concurrencia real, no se usó el motor de producción, las tasas de fallo son supuestas, no se midió ningún proceso periódico real. Un paquete sin límites declarados proyecta una certeza que la evidencia no respalda.

Según [SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md):

Traslada el proyecto a otro dominio (por ejemplo, la migración de una tabla de reservas de un taller con un campo de dirección que se divide en dos): cambia el esquema, la conversión y las tasas y conserva las seis fases, la verificación con interpretación por fase, el ensayo de vuelta atrás cronometrado y el cálculo del reposo. La transferencia está lograda cuando puedes decir en qué fase de ese dominio deja de ser gratuita la vuelta y cuánto cuesta en el día tres, no cuando el paquete se parece al de las notas.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo entrega un paquete con seis directorios. `plan/` describe las seis fases con su condición de paso y su reversibilidad (sin pérdida hasta la fase 3; con reconstrucción de unas 177 filas hasta el día 3 de la fase 4; sin vuelta tras contraer). `ejecutor/` contiene el relleno condicional reanudable y la doble escritura con bandeja. `verificacion/` compara contenido por rangos y escribe, por fase, qué significa una diferencia.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md)) son:

- **Se vuelve atrás y se pierden notas** — causa: la vuelta no reconstruye lo escrito solo en el nuevo. Corrección: medir las filas distintas antes de volver y reconstruir.
- **Se contrae y un defecto aparece después** — causa: reposo menor que el tiempo de descubrimiento. Corrección: calcular el reposo con la distribución de defectos y el calendario.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutó la migración y los dos cálculos con datos sintéticos en Windows y Ubuntu (WSL2) con cifras idénticas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md), [SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md), [SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md), [SE-525](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Retroceso](../r/retroceso.md), [Fase reversible](../f/fase-reversible.md), [Paquete de migración](../p/paquete-de-migracion.md), [Punto de no retorno](../p/punto-de-no-retorno.md), [Reposo](../r/reposo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

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

[↑ Glosario](../../README.md) · [← Ensayo](./ensayo.md) · [Ensayo en copia →](./ensayo-en-copia.md)
