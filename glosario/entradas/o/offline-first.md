# Offline-first

[↑ Glosario](../../README.md) · [← ODD](./odd.md) · [Olor de código →](./olor-de-codigo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

**Offline-first** es un estilo de diseño en el que el cliente lee y escribe en su almacenamiento local y la red solo reconcilia las copias. Es el sentido de [SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md) (offline-first y resolución de conflictos). No significa «funciona sin conexión como extra»: significa que el caso sin conexión es el normal y que la conexión es una optimización.

## Por qué importa

Invierte el diseño habitual, donde la red es la fuente de verdad y la caché una ayuda. La aplicación responde sin esperar a la red, y funciona en un tren, en una sala sin cobertura o con una red inestable. El costo es que dos copias pueden divergir, y alguien debe decidir qué hacer cuando lo hacen.

## Cómo funciona

[SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md): un cliente offline-first lee y escribe en su almacenamiento local y sincroniza en segundo plano. La red solo reconcilia. Kleppmann y colaboradores, citados por la clase, describen la propuesta y sus dificultades abiertas.

De eso se siguen tres decisiones:

1. **Dónde vive el estado** (local primero) y cómo se guarda.
2. **Cómo se registra el cambio:** como operaciones (un registro de lo hecho) y no solo como estado final, para poder fusionar.
3. **Qué política de conflicto aplica a cada tipo de dato.**

La política es por tipo de dato, no global.

## Ejemplo

El equipo del cliente en [SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md) documenta una política de conflicto por tipo de dato. Los comentarios son un conjunto con marcas únicas: nunca se pierde uno añadido, a costa de que una baja concurrente a un alta no gane. El título del borrador usa último escritor con un contador por réplica para decidir, y guarda la versión descartada 30 días con un aviso. El contador de revisiones se calcula a partir del registro de operaciones, no se sincroniza como número.

## Errores y confusiones comunes

- **Un comentario añadido sin conexión desaparece:** se copió el estado de la última réplica en llegar. Corrección: fusionar operaciones y usar una estructura que conserve los añadidos ([SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md)).
- **Una política única de «gana el último»** para todo.
- **Confundirlo con una caché sin conexión,** que solo sirve lecturas viejas.
- **Sincronizar contadores como números,** que pierde incrementos concurrentes.

## Límites y cuándo no aplica

No conviene cuando los datos exigen consistencia fuerte inmediata (un saldo, un cupo único): ahí dos copias divergentes son inaceptables. Las dificultades abiertas que cita la clase siguen vigentes: no existe solución general sin decidir políticas por dominio. Añade complejidad de almacenamiento local, migraciones del estado guardado y avisos al usuario.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md), [SE-259](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conflicto](../c/conflicto.md), [Idempotencia](../i/idempotencia.md), [Operaciones idempotentes](./operaciones-idempotentes.md), [Reloj lógico](../r/reloj-logico.md), [Réplica](../r/replica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-260 — Offline-first y resolución de conflictos](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-259](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md), [SE-261](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md), [SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Shapiro et al., «Conflict-Free Replicated Data Types» (SSS 2011)](https://doi.org/10.1007/978-3-642-24550-3_29) — tipos de datos replicados que convergen; autoridad: Lecture Notes in Computer Science.
- [Lamport, «Time, clocks, and the ordering of events in a distributed system» (CACM, 1978)](https://doi.org/10.1145/359545.359563) — relojes lógicos y orden causal; autoridad: Communications of the ACM.
- [Kleppmann et al., «Local-first software» (Onward! 2019)](https://doi.org/10.1145/3359591.3359737) — propuesta de aplicaciones con datos locales primero; autoridad: ACM SIGPLAN Onward!.
- [Ink & Switch, «Local-first software»](https://www.inkandswitch.com/local-first/) — versión extendida del ensayo con siete ideales; autoridad: Ink & Switch.
- [IETF, «RFC 9110: HTTP Semantics» (métodos idempotentes)](https://www.rfc-editor.org/rfc/rfc9110) — definición de idempotencia de los métodos HTTP; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← ODD](./odd.md) · [Olor de código →](./olor-de-codigo.md)
