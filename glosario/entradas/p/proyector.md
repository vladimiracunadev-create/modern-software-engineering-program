# Proyector

[↑ Glosario](../../README.md) · [← Proyecto nuevo](./proyecto-nuevo.md) · [Prueba A/A →](./prueba-a-a.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Componente que construye un modelo de lectura a partir de los eventos.

Definición de trabajo de [SE-330 — Event-driven, CQRS y event sourcing](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md).

## Por qué importa

La clase donde se define, [SE-330 — Event-driven, CQRS y event sourcing](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md), existe con este propósito: la clase existe para que decidas cuándo comunicar contextos por eventos, cuándo separar la escritura de la lectura y cuándo guardar la historia en lugar del estado, y para que midas las garantías que esa decisión exige a quien consume eventos.

## Cómo funciona

Según [SE-330 — Event-driven, CQRS y event sourcing](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md):

**CQRS** separa el modelo que acepta comandos (escritura) del que responde consultas (lectura), a menudo con un proyector que actualiza una vista desde los eventos. Permite optimizar cada lado por separado (consultas rápidas con vistas desnormalizadas) a cambio de una ventana de retraso: la vista no refleja la escritura al instante. Vogels distingue la *consistencia eventual* de garantías más finas como la *lectura de la propia escritura*, que es la que la persona percibe: si acabo de subir mi entrega y no la veo, la tomo por perdida. Fowler advierte que CQRS añade complejidad y solo debe usarse en partes del sistema donde compense.

Según [SE-330 — Event-driven, CQRS y event sourcing](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md):

El equipo de la plataforma publica tres eventos entre contextos (`EntregaRecibida`, `EntregaRevisada`, `EntregaCalificada`) con identificador, identificador de la entrega, secuencia por entrega y marca de tiempo. Los consumidores guardan los identificadores vistos con caducidad de 7 días y aplican solo secuencias mayores. La vista «mis entregas» se alimenta con un proyector cuya capacidad se dimensiona con 1,5 veces el pico previsto (60 por segundo); el cliente guarda la versión que escribió y muestra la entrega de forma optimista hasta que la vista la alcanza. No adopta event sourcing: guarda el estado y un historial de auditoría de solo añadir para Evaluación, porque el escenario de auditoría lo pide y el de reproceso no.

## Ejemplo

Ejemplo de [SE-330 — Event-driven, CQRS y event sourcing](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma publica tres eventos entre contextos (`EntregaRecibida`, `EntregaRevisada`, `EntregaCalificada`) con identificador, identificador de la entrega, secuencia por entrega y marca de tiempo. Los consumidores guardan los identificadores vistos con caducidad de 7 días y aplican solo secuencias mayores. La vista «mis entregas» se alimenta con un proyector cuya capacidad se dimensiona con 1,5 veces el pico previsto (60 por segundo); el cliente guarda la versión que escribió y muestra la entrega de forma optimista hasta que la vista la alcanza.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Personas que no ven su cambio al recargar** — causa: retraso del modelo de lectura sin lectura propia. Corrección: dimensionar el proyector y mostrar la escritura de forma optimista. ([SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** los tiempos de servicio exponenciales y un único proyector son una simplificación; los sistemas reales particionan, reintentan y tienen picos de otra forma. ([SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Evento](../e/evento.md), [Modelo](../m/modelo.md), [Consumidor idempotente](../c/consumidor-idempotente.md), [Evento de dominio](../e/evento-de-dominio.md), [Instantánea](../i/instantanea.md).
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

[↑ Glosario](../../README.md) · [← Proyecto nuevo](./proyecto-nuevo.md) · [Prueba A/A →](./prueba-a-a.md)
