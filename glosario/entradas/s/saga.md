# Saga

[↑ Glosario](../../README.md) · [← Safety-Critical Software Engineer](./safety-critical-software-engineer.md) · [Sal →](./sal.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Una **saga** es una secuencia de transacciones locales, cada una en un servicio distinto, en la que cada paso tiene una **compensación** que contrarresta su efecto si un paso posterior falla. Sustituye a una transacción atómica global entre servicios, que en un sistema distribuido o no existe o es demasiado cara. [SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md) la desarrolla con ese sentido; [SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md) y [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md) la nombran como la alternativa a la transacción atómica cuando un monolito se divide en servicios, y [SE-411](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md) la usa en el alta y el aprovisionamiento de clientes de un producto SaaS.

## Por qué importa

Cuando un proceso cruza servicios con bases de datos propias, no hay una transacción única que garantice «todo o nada». Sin un mecanismo explícito, un fallo a mitad de camino deja un cobro sin pedido o un pedido sin envío. La saga no devuelve la atomicidad: sustituye la promesa de «todo o nada» por la de **consistencia eventual con reparación**, y obliga a diseñar de antemano qué significa deshacer cada paso.

## Cómo funciona

Según [SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md), una saga divide el proceso en pasos locales; cada uno confirma su propia transacción y publica el siguiente. No hay bloqueos entre servicios ni aislamiento: mientras la saga corre, otros observan estados intermedios. Si un paso falla, la saga ejecuta las **compensaciones** de los pasos ya completados **en orden inverso**.

Hay dos formas de coordinarla:

- **Coreografiada:** cada servicio reacciona a los eventos de los demás, sin coordinador. Reduce el acoplamiento y dificulta saber en qué estado va un proceso.
- **Orquestada:** un coordinador conoce el flujo y ordena cada paso. Concentra ese conocimiento en un lugar que hay que operar y proteger.

La compensación no es un «deshacer» exacto: es una acción de negocio que contrarresta el efecto (reembolsar un cobro, liberar un cupo), y por eso también puede fallar y se reintenta, lo que la obliga a ser idempotente (véase idempotencia en [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md)).

## Ejemplo

En la simulación de [SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md) se ejecutan sagas sobre un corredor en memoria con tres fuentes de fallo: caídas entre pasos (3 %), fallos de un paso (8 %) y fallos de compensación (10 % por intento, hasta tres intentos), con semilla fija. El ejercicio muestra por qué la compensación necesita reintentos y por qué una saga puede quedar en un estado intermedio observable. Las tasas son supuestos del autor de la clase, no mediciones de un sistema real.

## Errores y confusiones comunes

- **Pensar que la saga es una transacción distribuida.** No tiene aislamiento: otros procesos ven estados intermedios y hay que diseñar para ello ([SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md)).
- **Compensaciones que no son idempotentes.** Una compensación reintentada dos veces puede reembolsar dos veces.
- **Olvidar que la compensación no siempre es posible.** Un correo enviado no se «desenvía»: una compensación es una acción de negocio que contrarresta el efecto, no un deshacer exacto.
- **Confundir coreografía con ausencia de diseño.** Sin coordinador, saber en qué estado va un proceso exige observabilidad explícita.

## Límites y cuándo no aplica

Las clases declaran los límites del experimento: las tasas de fallo son iguales y constantes para todos los pasos, mientras que en un sistema real el cobro falla más que el envío de un correo; además no se modelan sagas concurrentes ni lecturas de estados intermedios ([SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md)). Una saga se justifica cuando el proceso cruza servicios con almacenes propios; si todo cabe en una base de datos con una transacción local, la transacción ordinaria es más simple y ofrece más garantías. Tampoco deshace por sí sola un efecto externo irreversible, como un correo ya enviado.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Compensación](../c/compensacion.md), [Efecto](../e/efecto.md), [Locale](../l/locale.md), [Secuencia](./secuencia.md), [Camino crítico](../c/camino-critico.md), [Contrato compatible](../c/contrato-compatible.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.
- [SE-411 — Alta, aprovisionamiento y configuración por cliente](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.
- [SE-573 — Human-in-the-loop, aprobación y acciones reversibles](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md), [SE-572](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Sagas».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Garcia-Molina y Salem, «Sagas»](https://dl.acm.org/doi/10.1145/38713.38742) — subtransacciones con compensaciones; autoridad: artículo original (SIGMOD 1987; metadatos verificados con Crossref, el editor bloquea las peticiones automáticas).
- [Microsoft: patrón Saga](https://learn.microsoft.com/en-us/azure/architecture/patterns/saga) — sagas coreografiadas y orquestadas; autoridad: documentación de Microsoft.
- [García-Molina y Salem, «Sagas» (SIGMOD, 1987)](https://doi.org/10.1145/38713.38742) — transacciones largas con compensación; autoridad: ACM SIGMOD.
- [microservices.io: Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html) — patrón del outbox y su relevo; autoridad: Chris Richardson, autor del catálogo.
- [Debezium: Outbox Event Router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html) — implementación del outbox sobre el registro de cambios; autoridad: proyecto Debezium.

---

[↑ Glosario](../../README.md) · [← Safety-Critical Software Engineer](./safety-critical-software-engineer.md) · [Sal →](./sal.md)
