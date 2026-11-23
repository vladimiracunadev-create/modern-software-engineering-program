# Comando

[↑ Glosario](../../README.md) · [← Comandante del incidente](./comandante-del-incidente.md) · [Comando compuesto →](./comando-compuesto.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Mensaje que expresa una intención dirigida a un destinatario esperado y que puede ser rechazada.

Definición de trabajo de [SE-374 — Mensajes, eventos, comandos y documentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md).

## Por qué importa

En [SE-374 — Mensajes, eventos, comandos y documentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md), el tema «Comando» importa porque dirige una intención a un destinatario y puede ser rechazada.

## Cómo funciona

Según [SE-374 — Mensajes, eventos, comandos y documentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md), en la sección «Comando»:

Un **comando** expresa una intención dirigida: «califica esta entrega». Tiene un destinatario esperado, se nombra en imperativo y puede ser rechazado (la entrega no existe, el plazo venció). Por eso el emisor suele necesitar saber si se aceptó, y un comando sin manejador es un error que debería ser visible. La confusión habitual es difundirlo a todos los oyentes: entonces cada uno lo ejecuta y la acción ocurre varias veces. Un comando es adecuado cuando el emisor sabe qué quiere que ocurra y quién debe hacerlo.

## Ejemplo

Ejemplo de [SE-374 — Mensajes, eventos, comandos y documentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md) (sección «Ejemplo mínimo»):

El fragmento muestra un bus con un manejador y otro mensaje enviado sin manejador. Antes de ejecutarlo, predice qué ocurre con el comando y con el evento cuando no hay manejador.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una acción se ejecuta varias veces** — causa: un comando se difundió a varios oyentes. Corrección: un destinatario por comando y rechazo si no hay uno. ([SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Por eso el emisor suele necesitar saber si se aceptó, y un comando sin manejador es un error que debería ser visible. ([SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md))
- Un comando espera uno y falla si no está; un evento acepta cero o muchos. ([SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Intención](../i/intencion.md), [Documento](../d/documento.md), [Evento](../e/evento.md), [Sobre](../s/sobre.md), [Transferencia de estado en el evento](../t/transferencia-de-estado-en-el-evento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-374 — Mensajes, eventos, comandos y documentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (484 clases más lo mencionan; las que más):

[SE-579](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md), [SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md), [SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md), [SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md), [SE-029](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md), [SE-108](../../../classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md), [SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md), [SE-073](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [Therac-25](../../../casos/fallo/therac-25.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [EIP: Command Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CommandMessage.html) — mensaje que invoca una acción en otra aplicación; autoridad: autores del libro.
- [EIP: Event Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventMessage.html) — mensaje que notifica un hecho; autoridad: autores del libro.
- [EIP: Document Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DocumentMessage.html) — mensaje que transfiere datos; autoridad: autores del libro.
- [Fowler, «What do you mean by Event-Driven?»](https://martinfowler.com/articles/201701-event-driven.html) — cuatro significados de dirigido por eventos; autoridad: autor del texto.
- [CloudEvents: especificación](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md) — atributos comunes de un evento; autoridad: proyecto CloudEvents de la CNCF.

---

[↑ Glosario](../../README.md) · [← Comandante del incidente](./comandante-del-incidente.md) · [Comando compuesto →](./comando-compuesto.md)
