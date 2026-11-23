# Réplica

[↑ Glosario](../../README.md) · [← Replanificación](./replanificacion.md) · [Réplica asíncrona →](./replica-asincrona.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Copia de un dato que un dispositivo edita de forma independiente y se reconcilia después con las demás.

Definición de trabajo de [SE-260 — Offline-first y resolución de conflictos](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md).

## Por qué importa

La clase donde se define, [SE-260 — Offline-first y resolución de conflictos](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md), existe con este propósito: la clase existe para que diseñes el cliente para trabajar sin conexión como caso normal, elijas una estructura de datos y una política de conflicto sabiendo qué intención sacrifica cada una, y hagas que reintentar sea seguro con operaciones idempotentes.

## Cómo funciona

Según [SE-260 — Offline-first y resolución de conflictos](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md):

Un conjunto con marcas únicas conserva una alta aunque otra copia haya borrado un elemento previo que no vio, y se dice que gana la alta. Un conjunto en el que la baja es definitiva impide volver a añadir un elemento borrado. Un registro de último escritor gana según una marca de tiempo. Un contador por réplica suma las partes de cada una. Shapiro y colaboradores formalizan las condiciones para que las copias converjan; la convergencia no garantiza que el resultado sea lo que la persona quería.

Según [SE-260 — Offline-first y resolución de conflictos](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md):

El equipo del cliente documenta una política de conflicto por tipo de dato. Los comentarios son un conjunto con marcas únicas: nunca se pierde uno añadido, a costa de que una baja concurrente a un alta no gane. El título del borrador usa último escritor con un contador por réplica para decidir y guarda la versión descartada 30 días con un aviso. El contador de revisiones se calcula a partir del registro de operaciones, no se sincroniza como número. Cada operación lleva un identificador y el servidor recuerda los de las últimas dos semanas.

## Ejemplo

Ejemplo de [SE-260 — Offline-first y resolución de conflictos](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md) (sección «Ejemplo profesional»):

El equipo del cliente documenta una política de conflicto por tipo de dato. Los comentarios son un conjunto con marcas únicas: nunca se pierde uno añadido, a costa de que una baja concurrente a un alta no gane. El título del borrador usa último escritor con un contador por réplica para decidir y guarda la versión descartada 30 días con un aviso. El contador de revisiones se calcula a partir del registro de operaciones, no se sincroniza como número. Cada operación lleva un identificador y el servidor recuerda los de las últimas dos semanas.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un comentario añadido sin conexión desaparece** — causa: se copió el estado de la última réplica en llegar. Corrección: fusionar operaciones y usar una estructura que conserve altas. ([SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md))
- **Un contador cuenta la mitad de los cambios** — causa: se sincroniza el valor con «el último gana». Corrección: contador por réplica o recalcular del registro de operaciones. ([SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Se comparan un conjunto con marcas únicas (la baja elimina solo las marcas vistas), un conjunto con baja definitiva y un registro de último escritor gana, con el reloj de una réplica adelantado 0, 10 o 40 pasos. ([SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md), [SE-259](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dispositivo](../d/dispositivo.md), [Conflicto](../c/conflicto.md), [Idempotencia](../i/idempotencia.md), [Offline-first](../o/offline-first.md), [Operaciones idempotentes](../o/operaciones-idempotentes.md), [Reloj lógico](./reloj-logico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-260 — Offline-first y resolución de conflictos](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

**También se usa en** (55 clases más lo mencionan; las que más):

[SE-440](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-440-disponibilidad-durabilidad-y-recuperacion/README.md), [SE-390](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md), [SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), [SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md), [SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md), [SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md), [SE-399](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md), [SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md), [Slack](../../../casos/exito/slack.md).

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

[↑ Glosario](../../README.md) · [← Replanificación](./replanificacion.md) · [Réplica asíncrona →](./replica-asincrona.md)
