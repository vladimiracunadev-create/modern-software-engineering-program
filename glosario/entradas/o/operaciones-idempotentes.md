# Operaciones idempotentes

[↑ Glosario](../../README.md) · [← Operación](./operacion.md) · [Operadores como álgebra de flujos →](./operadores-como-algebra-de-flujos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Operación cuyo efecto en el estado es el mismo al aplicarla una vez o varias.

Definición de trabajo de [SE-171 — Interacción, affordances y retroalimentación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md).

## Por qué importa

En [SE-260 — Offline-first y resolución de conflictos](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md), el tema «Operaciones idempotentes» importa porque una operación que se puede aplicar dos veces sin cambiar el resultado permite reintentar sin miedo.

En [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), el tema «Operaciones idempotentes» importa porque una repetición inofensiva evita coordinar.

## Cómo funciona

Según [SE-260 — Offline-first y resolución de conflictos](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md), en la sección «Operaciones idempotentes»:

Cuando la red falla, el cliente no sabe si el servidor recibió la operación. Reintentar es la única opción, y solo es segura si aplicar la misma operación dos veces equivale a aplicarla una. Se logra con un identificador único por operación que el servidor recuerda. RFC 9110 define la idempotencia de los métodos HTTP como propiedad del efecto, no de la forma de la petición: `PUT` lo es, `POST` no por defecto.

Según [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), en la sección «Operaciones idempotentes»:

Una operación es **idempotente** si repetirla produce el mismo estado que ejecutarla una vez. «Fijar la nota del estudiante 17 en 6,0» lo es; «sumar 0,5 a la nota» no. Los métodos PUT y DELETE de HTTP se definen como idempotentes porque describen un estado destino. Convertir una operación no idempotente en idempotente suele consistir en cambiar *qué* se envía: no «incrementa el contador» sino «la entrega 8 301 del curso 12 existe», de modo que contar entregas distintas da lo mismo aunque el mensaje llegue tres veces. Cuando eso no es posible, se añade una clave que permite reconocer la repetición.

## Ejemplo

Ejemplo de [SE-260 — Offline-first y resolución de conflictos](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md) (sección «Caso conductor»):

El cliente de entregas de la [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md) deja aquí su política de conflicto por dato y su regla de operaciones idempotentes. `SE-261` mide el coste en recursos de sincronizar, `SE-262` firma y valida lo que viaja, y `SE-264` integra el protocolo en el proyecto. Cambia después una sola decisión, el título pasa de último escritor a conservar ambas versiones, y revisa qué pantallas y qué pruebas cambian.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-260 — Offline-first y resolución de conflictos](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md)) son:

- **Un comentario añadido sin conexión desaparece** — causa: se copió el estado de la última réplica en llegar. Corrección: fusionar operaciones y usar una estructura que conserve altas.
- **Un contador cuenta la mitad de los cambios** — causa: se sincroniza el valor con «el último gana». Corrección: contador por réplica o recalcular del registro de operaciones.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** la operación «sumar uno» es la más sensible a la duplicación; una operación idempotente por naturaleza (asignar un valor) no lo sería. ([SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-170](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Efecto](../e/efecto.md), [Estado](../e/estado.md), [Operación](./operacion.md), [Affordance percibida](../a/affordance-percibida.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Conflicto](../c/conflicto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-171 — Interacción, affordances y retroalimentación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.
- [SE-260 — Offline-first y resolución de conflictos](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-040](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md), [SE-048](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md), [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md), [SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md), [SE-172](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md), [SE-264](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md), [SE-383](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md), [SE-411](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «operación idempotente».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Shapiro et al., «Conflict-Free Replicated Data Types» (SSS 2011)](https://doi.org/10.1007/978-3-642-24550-3_29) — tipos de datos replicados que convergen; autoridad: Lecture Notes in Computer Science.
- [Lamport, «Time, clocks, and the ordering of events in a distributed system» (CACM, 1978)](https://doi.org/10.1145/359545.359563) — relojes lógicos y orden causal; autoridad: Communications of the ACM.
- [Kleppmann et al., «Local-first software» (Onward! 2019)](https://doi.org/10.1145/3359591.3359737) — propuesta de aplicaciones con datos locales primero; autoridad: ACM SIGPLAN Onward!.
- [Ink & Switch, «Local-first software»](https://www.inkandswitch.com/local-first/) — versión extendida del ensayo con siete ideales; autoridad: Ink & Switch.
- [IETF, «RFC 9110: HTTP Semantics» (métodos idempotentes)](https://www.rfc-editor.org/rfc/rfc9110) — definición de idempotencia de los métodos HTTP; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Operación](./operacion.md) · [Operadores como álgebra de flujos →](./operadores-como-algebra-de-flujos.md)
