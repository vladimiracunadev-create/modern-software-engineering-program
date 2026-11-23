# Replicación asíncrona

[↑ Glosario](../../README.md) · [← Replicación](./replicacion.md) · [Replicación semisíncrona →](./replicacion-semisincrona.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Copia de los datos a otras máquinas sin esperar su confirmación antes de responder al cliente.

Definición de trabajo de [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-510 — Fallos de datos y de estado: réplicas, particiones y corrupción](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md): El primario confirma la escritura antes de que la réplica la reciba.

## Por qué importa

En [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), el tema «Replicación asíncrona» importa porque una réplica puede ir por detrás del líder.

## Cómo funciona

Según [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), en la sección «Replicación asíncrona»:

El líder acepta las escrituras y las envía a las réplicas, que las aplican con retardo. En la replicación **asíncrona** el líder confirma sin esperar a las réplicas: es rápido y tolera que una réplica esté lenta, pero si el líder se cae antes de enviar, esa escritura se pierde, y una lectura en una réplica puede devolver un valor viejo. En la **síncrona** el líder espera a una o más réplicas: no pierde lo confirmado y cobra latencia y disponibilidad (si la réplica no responde, la escritura espera). Elegir es elegir qué se sacrifica, y cada institución decide según el costo de perder o de retrasar.

## Ejemplo

Ejemplo de [SE-510 — Fallos de datos y de estado: réplicas, particiones y corrupción](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula las escrituras esperadas en vuelo con replicación asíncrona según el retraso y el ritmo. Antes de ejecutarlo, predice cuántas son con 200 escrituras por segundo y 80 ms de retraso.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Escrituras confirmadas desaparecen tras una conmutación** — causa: replicación asíncrona con RPO declarado de cero. Corrección: medir la pérdida y elegir replicación semisíncrona o ajustar el RPO. ([SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En la replicación **asíncrona** el líder confirma sin esperar a las réplicas: es rápido y tolera que una réplica esté lenta, pero si el líder se cae antes de enviar, esa escritura se pierde, y una lectura en una réplica puede devolver un valor viejo. ([SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Confirmación](../c/confirmacion.md), [Réplica](./replica.md), [Almacén de características](../a/almacen-de-caracteristicas.md), [Clave caliente](../c/clave-caliente.md), [Cuórum](../c/cuorum.md), [Escritura confirmada perdida](../e/escritura-confirmada-perdida.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-510 — Fallos de datos y de estado: réplicas, particiones y corrupción](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md), [SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [PostgreSQL: replicación y servidores en espera](https://www.postgresql.org/docs/current/warm-standby.html) — replicación síncrona y asíncrona; autoridad: documentación oficial de PostgreSQL.
- [PostgreSQL: particionado](https://www.postgresql.org/docs/current/ddl-partitioning.html) — particionado por rango, lista y hash; autoridad: documentación oficial de PostgreSQL.
- [Karger et al., «Consistent hashing and random trees»](https://dl.acm.org/doi/10.1145/258533.258660) — hash consistente; autoridad: artículo original (1997).
- [DeCandia et al., «Dynamo»](https://www.allthingsdistributed.com/2007/10/amazons_dynamo.html) — cuórum, nodos virtuales y reparto; autoridad: artículo de los autores.
- [Jepsen: modelos de consistencia](https://jepsen.io/consistency) — mapa de modelos de consistencia; autoridad: proyecto Jepsen.

---

[↑ Glosario](../../README.md) · [← Replicación](./replicacion.md) · [Replicación semisíncrona →](./replicacion-semisincrona.md)
