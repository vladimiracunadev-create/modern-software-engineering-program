# Evento

[↑ Glosario](../../README.md) · [← Evasión](./evasion.md) · [Evento ancho →](./evento-ancho.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Mensaje que afirma un hecho ya ocurrido, inmutable y sin destinatario conocido.

Definición de trabajo de [SE-374 — Mensajes, eventos, comandos y documentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-033 — Logs del sistema y diagnóstico de fallos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md): Observación estructurada con significado estable.
- En [SE-057 — Modelado de estado, transiciones y eventos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md): Hecho que puede activar una transición.
- En [SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md): Mensaje que comunica que algo ocurrió y que el emisor no espera que se responda de inmediato.

## Por qué importa

En [SE-374 — Mensajes, eventos, comandos y documentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md), el tema «Evento» importa porque afirma un hecho pasado sin saber quién escuchará.

## Cómo funciona

Según [SE-374 — Mensajes, eventos, comandos y documentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md), en la sección «Evento»:

Un **evento** afirma que algo ocurrió: «la entrega 4721 fue recibida». Se nombra en pasado, es inmutable (no se puede «desrecibir»: se emite otro evento) y no conoce a sus oyentes. Eso permite agregar un consumidor nuevo sin tocar al emisor, que es su gran ventaja, y también significa que, si no hay ningún oyente, nadie se entera. El evento no ordena nada: lo que el receptor haga con él es decisión suya. Confundirlo con un comando disfrazado («EntregaRecibida» que en realidad dispara el calificador y nadie más debe reaccionar) acopla al emisor con la lógica de otro y esconde una dependencia.

## Ejemplo

Ejemplo de [SE-374 — Mensajes, eventos, comandos y documentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md) (sección «Ejemplo mínimo»):

El fragmento muestra un bus con un manejador y otro mensaje enviado sin manejador. Antes de ejecutarlo, predice qué ocurre con el comando y con el evento cuando no hay manejador.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Nadie reacciona a un evento y no hay error** — causa: ningún oyente registrado y el bus descarta en silencio. Corrección: alarma por eventos sin consumidor donde importe. ([SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md))
- **Los consumidores llaman todos de vuelta** — causa: el evento solo lleva un identificador. Corrección: incluir el contenido mínimo que casi todos necesitan. ([SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md))
- **Los consumidores operan con datos viejos** — causa: el evento lleva el estado y la entidad cambió. Corrección: incluir una versión y comparar con la vigente donde importe. ([SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Se nombra en pasado, es inmutable (no se puede «desrecibir»: se emite otro evento) y no conoce a sus oyentes. ([SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md))
- Un comando espera uno y falla si no está; un evento acepta cero o muchos. ([SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Espera](./espera.md).
- **Ver también:** [Hecho](../h/hecho.md), [Observación](../o/observacion.md), [Transición](../t/transicion.md), [Correlación](../c/correlacion.md), [Dominio](../d/dominio.md), [Estado](./estado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-033 — Logs del sistema y diagnóstico de fallos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-057 — Modelado de estado, transiciones y eventos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-374 — Mensajes, eventos, comandos y documentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (212 clases más lo mencionan; las que más):

[SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md), [SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md), [SE-362](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md), [SE-230](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md), [SE-079](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md), [SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md), [SE-290](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md), [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «What do you mean by Event-Driven?»](https://martinfowler.com/articles/201701-event-driven.html) — cuatro significados de dirigido por eventos; autoridad: autor del texto.
- [CloudEvents: especificación](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md) — atributos comunes de un evento; autoridad: proyecto CloudEvents de la CNCF.
- [systemd — journalctl](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html) — define ciclo de vida, supervisión o consulta de eventos en systemd.
- [CloudEvents](https://cloudevents.io/) — envoltura estándar de eventos con identificador, tipo y origen; autoridad: CNCF.
- [EIP: Command Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CommandMessage.html) — mensaje que invoca una acción en otra aplicación; autoridad: autores del libro.

---

[↑ Glosario](../../README.md) · [← Evasión](./evasion.md) · [Evento ancho →](./evento-ancho.md)
