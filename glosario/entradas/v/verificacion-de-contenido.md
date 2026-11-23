# Verificación de contenido

[↑ Glosario](../../README.md) · [← Verificación de comportamiento](./verificacion-de-comportamiento.md) · [Verificación de estado →](./verificacion-de-estado.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Un recuento igual no prueba datos iguales.

Es uno de los temas de [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md), donde se enseña como «Verificación de contenido».

## Por qué importa

En [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md), el tema «Verificación de contenido» importa porque un recuento igual no prueba datos iguales.

En [SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md), el tema «Verificación de contenido» importa porque lo que no se compara no se sabe.

## Cómo funciona

Según [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md):

El relleno típico hace tres pasos: leer un lote, calcular el valor nuevo y escribirlo. Entre la lectura y la escritura, la aplicación puede modificar una fila del lote. Si el relleno escribe sin condiciones, sobrescribe el valor nuevo calculado desde el texto viejo, y la columna nueva queda con un dato obsoleto aunque pasen todas las comprobaciones de recuento. Hay tres defensas combinables. La **escritura condicional** actualiza solo si la fila no cambió desde la lectura (comparando un número de versión o una marca de tiempo). La **escritura en ambos sitios desde la aplicación**, activada antes del relleno, garantiza que las escrituras nuevas van a la columna nueva; pero por sí sola no protege del relleno, que puede sobrescribirlas con valores calculados del texto antiguo.

Según [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md):

Traslada el análisis a otro dominio (por ejemplo, una tabla de pedidos con un campo de dirección que se divide en calle y ciudad): cambia la conversión y el volumen y conserva el procedimiento de expandir, doble escritura, relleno condicional por lotes, verificación de contenido y contracción tras un reposo. La transferencia está lograda cuando puedes decir qué escritura concurrente pisaría tu relleno y cómo lo impides, no cuando el plan se parece al de la nota numérica.

## Ejemplo

Caso medido en la sección «Verificación de contenido en cada fase» de [SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md):

La verificación compara cada fila del esquema antiguo, convertida con la regla de traducción, con la del nuevo. En la fase 0 el nuevo está vacío y todas las filas difieren. Tras el relleno, difieren las filas modificadas en el antiguo mientras se rellenaba. Con la doble escritura activa y tras una pasada de reconciliación, difieren solo las filas donde la segunda escritura falló. En las fases posteriores, las diferencias cambian de sentido: si el antiguo ya no recibe escrituras, las filas que difieren son las que el nuevo tiene más recientes.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md)) son:

- **Las escrituras se detienen durante el relleno** — causa: lote demasiado grande. Corrección: reducir el lote hasta cumplir el objetivo de espera.
- **Recuentos iguales y datos obsoletos** — causa: relleno sin escritura condicional. Corrección: condicionar por versión o marca de tiempo y repasar las nulas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Traslada el análisis a otro dominio (por ejemplo, una tabla de pedidos con un campo de dirección que se divide en calle y ciudad): cambia la conversión y el volumen y conserva el procedimiento de expandir, doble escritura, relleno condicional por lotes, verificación de contenido y contracción tras un reposo. ([SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-522](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ensayo de vuelta atrás](../e/ensayo-de-vuelta-atras.md), [Escritura condicional](../e/escritura-condicional.md), [Expandir y contraer](../e/expandir-y-contraer.md), [Fase reversible](../f/fase-reversible.md), [Idempotencia](../i/idempotencia.md), [Paquete de migración](../p/paquete-de-migracion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.
- [SE-528 — Proyecto: migración incremental reversible](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «ParallelChange»](https://martinfowler.com/bliki/ParallelChange.html) — patrón expandir y contraer; autoridad: autor del texto.
- [Fowler y Sadalage, «Evolutionary Database Design»](https://martinfowler.com/articles/evodb.html) — cambios de esquema en pasos pequeños y automatizados; autoridad: autores del texto.
- [SQLite: ALTER TABLE](https://www.sqlite.org/lang_altertable.html) — qué cambios son de metadatos y cuáles reconstruyen la tabla; autoridad: documentación de SQLite.
- [SQLite: UPDATE](https://www.sqlite.org/lang_update.html) — actualización condicionada; autoridad: documentación de SQLite.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — módulo usado en los experimentos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Verificación de comportamiento](./verificacion-de-comportamiento.md) · [Verificación de estado →](./verificacion-de-estado.md)
