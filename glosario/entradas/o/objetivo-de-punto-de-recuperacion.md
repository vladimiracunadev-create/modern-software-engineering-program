# Objetivo de punto de recuperación

[↑ Glosario](../../README.md) · [← Objetivo de nivel de servicio](./objetivo-de-nivel-de-servicio.md) · [Objetivo de seguridad →](./objetivo-de-seguridad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

El **objetivo de punto de recuperación** (RPO, por *recovery point objective*) es la cantidad máxima de datos recientes que se acepta perder tras una falla o una restauración, expresada como un intervalo de tiempo (o, en algunos casos, como número de escrituras) ([SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md), [SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md), [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md)). [SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md) lo usa en el contexto de agentes: la cantidad máxima de trabajo reciente que se acepta perder tras una restauración.

## Por qué importa

«No perder datos» no es un objetivo: es un deseo. El RPO convierte la tolerancia en un número que condiciona el diseño y su costo. Un RPO de un día se cumple con una copia diaria; uno de segundos exige replicación continua. La decisión que cambia es qué mecanismo de protección se elige y cuánto se paga por él, dato por dato.

## Cómo funciona

[SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md) deduce la estrategia del RPO: un RPO de un día se cumple con una copia diaria; uno de 15 minutos exige archivar el registro de cambios; uno de segundos exige replicación, que **no sustituye al respaldo** (una réplica replica también los errores).

[SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md) desarrolla la parte de replicación. Una réplica asíncrona recibe los cambios después de que el primario confirma; si el primario cae antes de enviar los últimos, esos cambios, ya confirmados a las personas, se pierden al conmutar. Con replicación asíncrona, el RPO es el retraso de la réplica. La replicación **síncrona** espera la confirmación de la réplica antes de responder: RPO cero, a cambio de latencia (el tiempo de ida y vuelta) y de disponibilidad (si la réplica cae, el primario espera o degrada). La **semisíncrona** exige confirmar con al menos una réplica y mantiene las demás asíncronas. Elegir es dato por dato: lo que no puede perderse, síncrono; lo reconstruible, asíncrono.

## Ejemplo

El servicio de entregas de [SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md) usa replicación semisíncrona hacia una réplica del mismo centro de datos (RPO cero) y asíncrona hacia otra región, con un RPO declarado de 30 segundos. Los acuses de recibo se emiten solo tras la confirmación semisíncrona, de modo que ninguna entrega con acuse se pierde en una conmutación local. El de 30 segundos es el precio aceptado para la región remota.

## Errores y confusiones comunes

- **Estudiantes con acuse y sin registro tras una conmutación**: replicación asíncrona con acuse previo; se corrige confirmando con una réplica antes del acuse.
- **Confundirlo con RTO**: el RPO mide cuántos datos se pierden; el RTO, cuánto tarda la recuperación.
- **Creer que la réplica reemplaza el respaldo**: replica también los borrados y la corrupción.
- **Declarar un RPO sin medir el retraso real** de la réplica.

## Límites y cuándo no aplica

Un RPO es un compromiso que se debe comprobar: una copia que nunca se restauró es una hipótesis (de ahí la prueba de restauración). RPO cero tiene un costo de latencia y disponibilidad que no siempre se justifica, y los datos reconstruibles no lo necesitan. El valor numérico depende del negocio; las cifras de los ejemplos (30 segundos, 15 minutos, un día) son de las clases, no valores recomendados.

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
