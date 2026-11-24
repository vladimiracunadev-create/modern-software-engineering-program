# Replicación asíncrona

[↑ Glosario](../../README.md) · [← Replicación](./replicacion.md) · [Replicación semisíncrona →](./replicacion-semisincrona.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

La **replicación asíncrona** es la copia de los datos a otras máquinas sin esperar su confirmación antes de responder al cliente ([SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md)). [SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md) la formula desde el efecto: el primario confirma la escritura antes de que la réplica la reciba. Se contrapone a la replicación síncrona, donde el líder espera a una o más réplicas.

## Por qué importa

Replicar datos protege contra la caída de una máquina, pero cómo se replica decide qué se puede perder. La decisión que cambia es qué se sacrifica: velocidad y disponibilidad, o seguridad de no perder datos confirmados. [SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md) lo resume: elegir es elegir qué se sacrifica, y cada institución decide según el costo de perder o de retrasar.

## Cómo funciona

El líder acepta las escrituras y las envía a las réplicas, que las aplican con retardo. En la modalidad **asíncrona**, el líder confirma al cliente sin esperar a las réplicas. Ventajas: es rápido y tolera que una réplica esté lenta o caída. Costos, según [SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md):

- Si el líder se cae **antes de enviar**, esa escritura se pierde, aunque ya se había confirmado al cliente.
- Una lectura en una réplica puede devolver un **valor viejo**, por el retardo de replicación.

En la **síncrona**, el líder espera a una o más réplicas: no pierde lo confirmado, pero cobra latencia y disponibilidad (si la réplica no responde, la escritura espera). Existe un punto intermedio, la semisíncrona, que exige confirmar con al menos una réplica y mantiene las demás asíncronas.

La consecuencia cuantificable es el objetivo de punto de recuperación: con replicación asíncrona, el RPO es el retraso de la réplica. [SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md) lo prueba con ingeniería del caos: si se declara RPO cero con replicación asíncrona, una conmutación hace desaparecer escrituras confirmadas; la corrección es medir la pérdida y elegir replicación semisíncrona o ajustar el RPO declarado.

## Ejemplo

El primario confirma una entrega al estudiante y la envía a la réplica un instante después. El primario cae justo entre ambos momentos. Al conmutar a la réplica, la entrega ya confirmada no existe. Con replicación semisíncrona, el acuse solo se emite tras la confirmación de la réplica y la entrega sobrevive. Contraste de [SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md) y [SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md).

## Errores y confusiones comunes

- **Escrituras confirmadas desaparecen tras una conmutación**: replicación asíncrona con RPO declarado de cero; se corrige midiendo la pérdida y eligiendo semisíncrona o ajustando el RPO ([SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md)).
- **Leer de una réplica esperando el último valor**: puede ser viejo.
- **Confundirla con un respaldo**: replica también los errores y borrados.
- **Elegirla sin declarar cuánto se puede perder**.

## Límites y cuándo no aplica

No aplica cuando lo confirmado no puede perderse nunca: ahí hace falta síncrona o semisíncrona, con su costo de latencia. Tampoco sirve como única protección: no sustituye copias consistentes con prueba de restauración. Y el retraso depende de la red y la carga; solo medirlo en el sistema real da el RPO efectivo.

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
