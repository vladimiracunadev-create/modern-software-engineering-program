# Comando

[↑ Glosario](../../README.md) · [← Comandante del incidente](./comandante-del-incidente.md) · [Comando compuesto →](./comando-compuesto.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Un **comando** es un mensaje que expresa una intención dirigida a un destinatario esperado y que puede ser rechazada ([SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md)). Se nombra en imperativo («califica esta entrega») y se contrapone al evento, que describe un hecho ya ocurrido.

## Por qué importa

Distinguir comando de evento decide quién conoce a quién y qué ocurre si nadie responde. Con un comando, el emisor sabe qué quiere que pase y quién debe hacerlo; por eso necesita saber si se aceptó. Confundirlo con un evento lleva a difundir una orden a todos los oyentes y a que la acción ocurra varias veces, o a no notar que nadie la ejecutó.

## Cómo funciona

Tres rasgos lo definen en [SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md):

1. **Destinatario esperado**: está dirigido a quien debe ejecutarlo. Un comando sin manejador es un error que debe ser visible, no un mensaje que se pierde en silencio.
2. **Imperativo**: nombra lo que se quiere que ocurra, no lo que ocurrió.
3. **Puede ser rechazado**: el receptor valida y puede negarse (la entrega no existe, el plazo venció). Por eso el emisor suele necesitar el resultado.

La diferencia con el evento es de cardinalidad y de acoplamiento: un comando espera **uno** y falla si no está; un evento acepta **cero o muchos**. En un evento, quien lo emite no sabe quién lo escucha; en un comando, el emisor depende de que alguien lo atienda, de modo que el acoplamiento es más fuerte y deliberado. La falla clásica es difundir el comando a todos los oyentes: cada uno lo ejecuta y la acción ocurre varias veces.

## Ejemplo

`CalificarEntrega(entrega_id=17, nota=8)` va a un manejador concreto. Este puede rechazarlo si la entrega no existe o si el plazo venció, y responde aceptado o rechazado. En cambio `EntregaCalificada` es un evento: se publica después de que ocurrió y lo pueden leer cero, uno o varios servicios (aviso por correo, estadísticas) sin que el emisor lo sepa. Ejemplo ilustrativo siguiendo la distinción de [SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md).

## Errores y confusiones comunes

- **Una acción se ejecuta varias veces**: un comando se difundió a varios oyentes; se corrige con un destinatario por comando y rechazo si no hay uno ([SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md)).
- **Nombrarlo en pasado**: un comando en pasado se lee como evento y oculta quién debe actuar.
- **Ignorar el rechazo**: asumir que fue aceptado sin confirmar.
- **Enviar un evento esperando que alguien lo ejecute**: el evento no garantiza ningún destinatario.

## Límites y cuándo no aplica

El comando es adecuado cuando el emisor sabe qué quiere y quién debe hacerlo. Si el emisor solo anuncia un hecho y le da igual quién reaccione, es un evento. Un comando asíncrono no elimina la necesidad de manejar reintentos y duplicados: sigue sujeto a la semántica de entrega y requiere un manejador idempotente si puede repetirse. Y exigir respuesta acopla en tiempo al emisor con el receptor; conviene valorarlo frente a un enfoque basado en eventos.

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
