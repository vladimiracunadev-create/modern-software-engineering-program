# Compensación

[↑ Glosario](../../README.md) · [← Compatibilidad y sintaxis](./compatibilidad-y-sintaxis.md) · [Competencia →](./competencia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Una **compensación** es una acción **nueva** que deshace o neutraliza el efecto de un paso anterior, sin borrarlo del historial ([SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md)). No es una reversión: reembolsar un cobro no «des-cobra», y cancelar un cupo no borra que alguien lo vio ocupado. Es el mecanismo con que una saga se recupera cuando no puede haber una transacción única que abarque varios servicios.

## Por qué importa

En un flujo que cruza sistemas, un fallo a mitad de camino deja efectos reales ya producidos. La decisión que cambia es cómo se diseña el flujo: no se pregunta solo «cómo hago cada paso» sino «cómo se contrarresta cada paso si falla uno posterior» y, sobre todo, «qué pasos no tienen contrapartida». Esa pregunta decide el orden de los pasos.

## Cómo funciona

[SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md) fija las ideas centrales:

- La compensación es otra operación de negocio, visible y registrada, con sus propios efectos (el reembolso aparece en el extracto).
- Algunas acciones **no tienen compensación**: un correo enviado, un archivo publicado. Son pasos irreversibles.
- La regla de diseño: ordenar los pasos de modo que los compensables vayan primero y el irreversible lo más tarde posible. Ese paso se llama **pivote**: tras él la saga solo puede avanzar, y los pasos posteriores deben poder reintentarse hasta lograrse.
- Las compensaciones también fallan. Por eso deben ser **idempotentes**, reintentables y dejar un estado «atascado» observable si no logran terminar, para que alguien actúe.

[SE-573](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md) lleva esto a los flujos con agentes: un flujo queda a medias cuando no hay compensación o las compensaciones fallan, y la corrección es compensar con reintentos y registro. En [SE-411](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md) el término aparece en el contexto de una plataforma SaaS, donde un aprovisionamiento a medias debe poder deshacerse.

## Ejemplo

Una inscripción reserva un cupo, cobra y envía un correo de bienvenida. Si el cobro falla, se compensa el cupo liberándolo. Si el correo es el último paso y es irreversible, se coloca después de los compensables: el cobro, que sí tiene compensación (reembolso), va antes. Si el envío falla tras el pivote, no se deshace el cobro; se reintenta el envío. Ejemplo ilustrativo del orden que enseña [SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md).

## Errores y confusiones comunes

- **Un flujo queda a medias** ([SE-573](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md)): sin compensación o con compensaciones que fallan; se corrige compensando con reintentos y registro.
- **Creer que compensar es revertir**: el efecto original sigue existiendo y visible.
- **Compensación no idempotente**: un reintento reembolsa dos veces.
- **Poner el paso irreversible al principio**: se pierde la posibilidad de deshacer lo demás.

## Límites y cuándo no aplica

No todo se puede compensar, y la compensación no restituye el estado anterior exacto: terceros pudieron haber observado el estado intermedio. Cuando la consistencia inmediata es indispensable y todo ocurre en una sola base, una transacción local es más simple y segura que una saga con compensaciones. Y una compensación mal diseñada añade más fallos de los que evita: requiere reintento, registro y alertas sobre los casos atascados.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Efecto](../e/efecto.md), [Aprovisionamiento](../a/aprovisionamiento.md), [Configuración por capas](./configuracion-por-capas.md), [Doble escritura](../d/doble-escritura.md), [Idempotente](../i/idempotente.md), [Inbox](../i/inbox.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.
- [SE-411 — Alta, aprovisionamiento y configuración por cliente](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.
- [SE-573 — Human-in-the-loop, aprobación y acciones reversibles](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (22 clases más lo mencionan; las que más):

[SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md), [SE-395](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md), [SE-180](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md), [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), [SE-535](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-535-compras-proveedores-y-evaluacion-tecnica/README.md), [SE-293](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md).

**Aparece en los casos de estudio:** [Spotify](../../../casos/exito/spotify.md), [Knight Capital](../../../casos/fallo/knight-capital.md), [TSB Bank](../../../casos/fallo/tsb.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Garcia-Molina y Salem, «Sagas»](https://dl.acm.org/doi/10.1145/38713.38742) — subtransacciones con compensaciones; autoridad: artículo original (SIGMOD 1987; metadatos verificados con Crossref, el editor bloquea las peticiones automáticas).
- [Garcia-Molina y Salem, «Sagas»](https://doi.org/10.1145/38713.38742) — compensaciones; autoridad: ACM SIGMOD, 1987.
- [microservices.io: Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html) — patrón del outbox y su relevo; autoridad: Chris Richardson, autor del catálogo.
- [Debezium: Outbox Event Router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html) — implementación del outbox sobre el registro de cambios; autoridad: proyecto Debezium.
- [Microsoft: patrón Saga](https://learn.microsoft.com/en-us/azure/architecture/patterns/saga) — sagas coreografiadas y orquestadas; autoridad: documentación de Microsoft.

---

[↑ Glosario](../../README.md) · [← Compatibilidad y sintaxis](./compatibilidad-y-sintaxis.md) · [Competencia →](./competencia.md)
