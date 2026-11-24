# Operaciones idempotentes

[↑ Glosario](../../README.md) · [← Operación](./operacion.md) · [Operadores como álgebra de flujos →](./operadores-como-algebra-de-flujos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Una **operación idempotente** es aquella cuyo efecto en el estado es el mismo al aplicarla una vez o varias ([SE-171](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md), [SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md), [SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md)). «Fijar la nota del estudiante 17 en 6,0» es idempotente; «sumar 0,5 a la nota» no. En HTTP, `PUT` y `DELETE` se definen como idempotentes porque describen un estado destino.

## Por qué importa

Permite reintentar sin miedo. Cuando la red falla, el cliente no sabe si el servidor recibió la operación; reintentar es la única opción, y solo es segura si aplicar la operación dos veces equivale a aplicarla una. Una repetición inofensiva además evita coordinar: no hace falta un protocolo para saber si ya se hizo.

## Cómo funciona

[SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md) explica que el cliente, ante un error de red, no distingue entre «la petición no llegó» y «llegó y se perdió la respuesta». Reintentar sin idempotencia puede aplicar el efecto dos veces. RFC 9110 define la idempotencia de los métodos HTTP como propiedad **del efecto**, no de la forma de la petición: `PUT` lo es, `POST` no por defecto.

Hay dos caminos para lograrla. **Cambiar qué se envía**: en lugar de «incrementa el contador» (no idempotente), se envía «la entrega 42 fue recibida» (idempotente: registrar el hecho dos veces deja el mismo estado), o «fija la nota en 6,0» en lugar de «suma 0,5». **Añadir un identificador único por operación** que el servidor recuerda: una clave de idempotencia permite que operaciones no idempotentes por naturaleza (crear, cobrar) se reintenten con seguridad. Del lado del receptor de mensajes, el equivalente es el consumidor idempotente.

[SE-171](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md) y [SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md) sitúan esto en el contexto de un cliente que sincroniza con conflictos: la política de conflicto por dato (último escritor, conservar ambas versiones, fusionar operaciones) interactúa con la idempotencia. Un fallo que aparece sin ella: un comentario añadido sin conexión desaparece porque se copió el estado de la última réplica en llegar; fusionar operaciones, no estados, lo evita.

## Ejemplo

El cliente envía `PUT /entregas/42/nota {valor: 6.0}`. La respuesta se pierde y reintenta. El servidor aplica «nota = 6,0» dos veces: el estado es el mismo. Con `POST /entregas/42/ajustes {suma: 0.5}`, el mismo reintento daría 7,0 en lugar de 6,5; la corrección es o cambiar el mensaje a «nota = 6,5» o enviar con una clave de idempotencia. (Ilustración del principio de [SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md) y [SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md).)

## Errores y confusiones comunes

- **Creer que reintentar es siempre seguro.**
- **Confundir idempotente con «sin efectos»**: tiene efecto, una vez.
- **Asumir que `POST` es idempotente.**
- **Idempotente respecto del estado, no de la respuesta**: el segundo `DELETE` puede devolver otro código sin cambiar el estado.

## Límites y cuándo no aplica

No todas las operaciones se pueden reformular como idempotentes (enviar un correo, cobrar); ahí se usan claves de idempotencia y deduplicación. La idempotencia no resuelve el orden ni la concurrencia: dos operaciones idempotentes distintas pueden interferir entre sí.

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
