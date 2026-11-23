# Objetivo de punto de recuperación

[↑ Glosario](../../README.md) · [← Objetivo de nivel de servicio](./objetivo-de-nivel-de-servicio.md) · [Objetivo de seguridad →](./objetivo-de-seguridad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Cantidad máxima de datos que se acepta perder, medida como intervalo de tiempo o número de escrituras.

Definición de trabajo de [SE-393 — Replicación, sharding y balanceo](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md): Cantidad máxima de trabajo reciente que se acepta perder tras una restauración.
- En [SE-357 — Backups, restauración y pruebas de recuperación](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md): Cantidad máxima de datos, medida en tiempo, que la institución acepta perder.
- En [SE-440 — Disponibilidad, durabilidad y recuperación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md): Cantidad máxima de datos recientes que se acepta perder, expresada como tiempo.

## Por qué importa

La clase donde se define, [SE-393 — Replicación, sharding y balanceo](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md), existe con este propósito: la clase existe para que decidas, con números, cómo repartir el trabajo y los datos de un servicio entre varias máquinas: qué política de balanceo mantiene bajo el percentil 99 cuando los trabajos son de tamaños muy distintos, cuántas escrituras confirmadas puedes perder al conmutar según cuántas réplicas esperes, y qué clave de reparto conviene a las consultas de la plataforma sin crear un fragmento caliente.

## Cómo funciona

Según [SE-393 — Replicación, sharding y balanceo](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md):

Una réplica asíncrona recibe los cambios después de que el primario confirma; si el primario cae antes de enviar los últimos, esos cambios, ya confirmados a las personas, se pierden al conmutar. El **objetivo de punto de recuperación** (RPO) es cuánto se acepta perder; con replicación asíncrona es el retraso de la réplica. La replicación **síncrona** espera la confirmación de la réplica antes de responder: RPO cero, a cambio de latencia (el tiempo de ida y vuelta) y de disponibilidad (si la réplica cae, el primario espera o degrada). La **semisíncrona** exige confirmar con al menos una réplica y mantiene las demás asíncronas. Elegir es dato por dato: lo que no puede perderse, síncrono; lo reconstruible, asíncrono.

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

Lo que las clases dicen sobre dónde deja de valer este término:

- De ellos se deduce la estrategia: un RPO de un día se cumple con una copia diaria; uno de 15 minutos exige archivar el registro de cambios; uno de segundos exige replicación, que no sustituye al respaldo. ([SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Intervalo](../i/intervalo.md), [Medida](../m/medida.md), [Restauración](../r/restauracion.md), [Trabajo](../t/trabajo.md), [Balanceo de carga](../b/balanceo-de-carga.md), [Copia consistente](../c/copia-consistente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-357 — Backups, restauración y pruebas de recuperación](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-393 — Replicación, sharding y balanceo](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.
- [SE-440 — Disponibilidad, durabilidad y recuperación](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.
- [SE-576 — Proyecto final: producto operable construido desde SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md), [SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «RPO».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Mitzenmacher, «The power of two choices…»](https://doi.org/10.1109/71.963420) — dos opciones al azar; autoridad: artículo original (2001).
- [Karger et al., «Consistent hashing and random trees»](https://doi.org/10.1145/258533.258660) — hash consistente; autoridad: artículo original (1997).
- [PostgreSQL: servidores en espera](https://www.postgresql.org/docs/current/warm-standby.html) — replicación síncrona y asíncrona; autoridad: documentación oficial de PostgreSQL.
- [DeCandia et al., «Dynamo»](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf) — hash consistente y cuórums configurables; autoridad: artículo de los autores (2007).
- [Chang et al., «Bigtable»](https://doi.org/10.1145/1365815.1365816) — reparto por rango; autoridad: artículo de los autores (2008).

---

[↑ Glosario](../../README.md) · [← Objetivo de nivel de servicio](./objetivo-de-nivel-de-servicio.md) · [Objetivo de seguridad →](./objetivo-de-seguridad.md)
