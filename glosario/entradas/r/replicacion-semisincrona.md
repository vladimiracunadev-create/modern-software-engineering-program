# Replicación semisíncrona

[↑ Glosario](../../README.md) · [← Replicación asíncrona](./replicacion-asincrona.md) · [Replication →](./replication.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Replicación en que el primario espera la confirmación de al menos una réplica antes de responder.

Definición de trabajo de [SE-393 — Replicación, sharding y balanceo](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md).

## Por qué importa

La clase donde se define, [SE-393 — Replicación, sharding y balanceo](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md), existe con este propósito: la clase existe para que decidas, con números, cómo repartir el trabajo y los datos de un servicio entre varias máquinas: qué política de balanceo mantiene bajo el percentil 99 cuando los trabajos son de tamaños muy distintos, cuántas escrituras confirmadas puedes perder al conmutar según cuántas réplicas esperes, y qué clave de reparto conviene a las consultas de la plataforma sin crear un fragmento caliente.

## Cómo funciona

Según [SE-393 — Replicación, sharding y balanceo](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md):

El equipo del servicio de entregas cambia el balanceador de turnos a «dos opciones al azar» con una métrica de conexiones activas, y fija la cola máxima por servidor para rechazar rápido antes de que la espera crezca (`SE-396`). La base de entregas usa replicación semisíncrona hacia una réplica en el mismo centro de datos, con RPO cero, y asíncrona hacia otra región, con un RPO declarado de 30 segundos; los acuses de recibo solo se emiten tras la confirmación semisíncrona. Para los archivos y metadatos de entregas elige reparto por hash del identificador de entrega, porque la consulta principal es por entrega; para los informes por fecha mantiene una tabla aparte con reparto por rango y un fragmento más pequeño al final.

## Ejemplo

Ejemplo de [SE-393 — Replicación, sharding y balanceo](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md) (sección «Ejemplo profesional»):

El equipo del servicio de entregas cambia el balanceador de turnos a «dos opciones al azar» con una métrica de conexiones activas, y fija la cola máxima por servidor para rechazar rápido antes de que la espera crezca (`SE-396`). La base de entregas usa replicación semisíncrona hacia una réplica en el mismo centro de datos, con RPO cero, y asíncrona hacia otra región, con un RPO declarado de 30 segundos; los acuses de recibo solo se emiten tras la confirmación semisíncrona.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-393 — Replicación, sharding y balanceo](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md)) son:

- **Algunos servidores saturados y otros ociosos** — causa: balanceo por turnos con tamaños de cola pesada. Corrección: dos opciones al azar o menos conexiones.
- **Estudiantes con acuse y sin registro tras una conmutación** — causa: replicación asíncrona con acuse previo. Corrección: confirmar con una réplica antes del acuse.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-393 — Replicación, sharding y balanceo](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ningún balanceador, ninguna base replicada ni ninguna red: los tamaños, la carga, los retrasos y los ocho fragmentos son construcciones del autor. La siguiente clase pregunta cómo comprobar que todo esto resiste fallos reales: caos controlado y pruebas de distribución.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), [SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Confirmación](../c/confirmacion.md), [Espera](../e/espera.md), [Réplica](./replica.md), [Replicación](./replicacion.md), [Balanceo de carga](../b/balanceo-de-carga.md), [Fragmento caliente](../f/fragmento-caliente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-393 — Replicación, sharding y balanceo](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Mitzenmacher, «The power of two choices…»](https://doi.org/10.1109/71.963420) — dos opciones al azar; autoridad: artículo original (2001).
- [Karger et al., «Consistent hashing and random trees»](https://doi.org/10.1145/258533.258660) — hash consistente; autoridad: artículo original (1997).
- [PostgreSQL: servidores en espera](https://www.postgresql.org/docs/current/warm-standby.html) — replicación síncrona y asíncrona; autoridad: documentación oficial de PostgreSQL.
- [DeCandia et al., «Dynamo»](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf) — hash consistente y cuórums configurables; autoridad: artículo de los autores (2007).
- [Chang et al., «Bigtable»](https://doi.org/10.1145/1365815.1365816) — reparto por rango; autoridad: artículo de los autores (2008).

---

[↑ Glosario](../../README.md) · [← Replicación asíncrona](./replicacion-asincrona.md) · [Replication →](./replication.md)
