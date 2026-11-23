# Paquete de migración

[↑ Glosario](../../README.md) · [← Paquete de integración](./paquete-de-integracion.md) · [Paquete del dispositivo →](./paquete-del-dispositivo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Conjunto de artefactos (plan, ejecutor, verificación, ensayo, límites) que permite a otra persona comprobar la migración.

Definición de trabajo de [SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md).

## Por qué importa

La clase donde se define, [SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md), existe con este propósito: el proyecto existe para que ejecutes de principio a fin una migración incremental reversible y entregues un paquete que otra persona pueda comprobar, repetir y desmontar.

## Cómo funciona

[SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Ejemplo de [SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md) (sección «Caso conductor»):

El módulo de calificaciones es el caso conductor de la [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md). Este proyecto deja el último artefacto: el paquete de migración incremental reversible, que reúne las clasificaciones, el mapa de riesgo, la caracterización, la política de dependencias, el plan de rebanadas, el catálogo de la plataforma, el plan de datos, el contrato de coexistencia, la secuencia de retiro, el modelo económico y la puerta de entrada de las clases anteriores. La [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md) lleva la mirada a la gestión, el liderazgo y la práctica profesional. Cambia después un solo dato, las escrituras diarias de 60 a 600, y observa cuánto se acorta la ventana en que volver es barato.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md)) son:

- **Se vuelve atrás y se pierden notas** — causa: la vuelta no reconstruye lo escrito solo en el nuevo. Corrección: medir las filas distintas antes de volver y reconstruir.
- **Se contrae y un defecto aparece después** — causa: reposo menor que el tiempo de descubrimiento. Corrección: calcular el reposo con la distribución de defectos y el calendario.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutó la migración y los dos cálculos con datos sintéticos en Windows y Ubuntu (WSL2) con cifras idénticas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md), [SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md), [SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md), [SE-525](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Artefacto](../a/artefacto.md), [Conjunto](../c/conjunto.md), [Ensayo](../e/ensayo.md), [Límite](../l/limite.md), [Ensayo de vuelta atrás](../e/ensayo-de-vuelta-atras.md), [Fase reversible](../f/fase-reversible.md).
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

[↑ Glosario](../../README.md) · [← Paquete de integración](./paquete-de-integracion.md) · [Paquete del dispositivo →](./paquete-del-dispositivo.md)
