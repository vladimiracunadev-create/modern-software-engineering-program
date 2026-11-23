# Evento de dominio

[↑ Glosario](../../README.md) · [← Evento ancho](./evento-ancho.md) · [Evento de telemetría →](./evento-de-telemetria.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Hecho pasado, con nombre del negocio, que otros contextos pueden consumir.

Definición de trabajo de [SE-330 — Event-driven, CQRS y event sourcing](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md).

## Por qué importa

En [SE-330 — Event-driven, CQRS y event sourcing](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md), el tema «Eventos de dominio y notificaciones» importa porque desacoplan contextos en el tiempo a costa de garantías de entrega.

## Cómo funciona

[SE-330 — Event-driven, CQRS y event sourcing](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-330 — Event-driven, CQRS y event sourcing](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md):

El equipo de la plataforma publica tres eventos entre contextos (`EntregaRecibida`, `EntregaRevisada`, `EntregaCalificada`) con identificador, identificador de la entrega, secuencia por entrega y marca de tiempo. Los consumidores guardan los identificadores vistos con caducidad de 7 días y aplican solo secuencias mayores. La vista «mis entregas» se alimenta con un proyector cuya capacidad se dimensiona con 1,5 veces el pico previsto (60 por segundo); el cliente guarda la versión que escribió y muestra la entrega de forma optimista hasta que la vista la alcanza.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-330 — Event-driven, CQRS y event sourcing](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md)) son:

- **Contadores mayores que la realidad** — causa: consumidor que suma cada mensaje con entrega al-menos-una-vez. Corrección: idempotencia con identificador de evento.
- **Un estado antiguo sobrescribe a uno nuevo** — causa: desorden sin secuencia por entidad. Corrección: aplicar solo eventos con secuencia mayor a la vista.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-330 — Event-driven, CQRS y event sourcing](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún agente de mensajería, almacén de eventos ni base de datos; los duplicados, el desorden, el pico y los tiempos de servicio son construcciones del autor. La siguiente clase mira dónde corren los consumidores: serverless, el borde y redes entre pares.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](../c/contextos.md), [Hecho](../h/hecho.md), [Consumidor idempotente](../c/consumidor-idempotente.md), [Instantánea](../i/instantanea.md), [Lectura de la propia escritura](../l/lectura-de-la-propia-escritura.md), [Proyector](../p/proyector.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-330 — Event-driven, CQRS y event sourcing](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «What do you mean by Event-Driven?»](https://martinfowler.com/articles/201701-event-driven.html) — cuatro patrones que suelen confundirse; autoridad: Martin Fowler.
- [Fowler, «CQRS»](https://martinfowler.com/bliki/CQRS.html) — separación de modelos de lectura y escritura; autoridad: Martin Fowler.
- [Fowler, «Event Sourcing»](https://martinfowler.com/eaaDev/EventSourcing.html) — estado como secuencia de eventos; autoridad: Martin Fowler.
- [Hohpe y Woolf, «Idempotent Receiver»](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html) — receptor que tolera duplicados; autoridad: Enterprise Integration Patterns.
- [Vogels, «Eventually consistent» (CACM, 2009)](https://doi.org/10.1145/1435417.1435432) — consistencia eventual y lectura de la propia escritura; autoridad: Communications of the ACM.

---

[↑ Glosario](../../README.md) · [← Evento ancho](./evento-ancho.md) · [Evento de telemetría →](./evento-de-telemetria.md)
