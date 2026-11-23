# Sobre

[↑ Glosario](../../README.md) · [← SLO](./slo.md) · [Sobreasignación →](./sobreasignacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Conjunto de atributos comunes a todo mensaje que permiten manejarlo sin interpretar su contenido.

Definición de trabajo de [SE-374 — Mensajes, eventos, comandos y documentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md).

## Por qué importa

En [SE-374 — Mensajes, eventos, comandos y documentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md), el tema «Sobre del mensaje» importa porque permite deduplicar, ordenar y seguir sin leer el cuerpo.

## Cómo funciona

Según [SE-374 — Mensajes, eventos, comandos y documentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md):

El **sobre** son los atributos comunes a cualquier mensaje: un identificador único, el tipo, el origen, la hora de emisión, un número de secuencia por origen o por entidad, un identificador de correlación y la versión del esquema. Existen para que la infraestructura y los consumidores puedan **deduplicar** (identificador), **enrutar** (tipo), **ordenar** (secuencia), **seguir** una operación entre servicios (correlación) y **interpretar** (versión) sin entender el contenido. CloudEvents estandariza una parte de este sobre para eventos. Cuando falta un campo, los consumidores lo sustituyen con heurísticas (hash del cuerpo, hora del reloj, ventanas de tiempo) que funcionan en demostraciones y fallan bajo concurrencia.

Según [SE-374 — Mensajes, eventos, comandos y documentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md):

El equipo de la plataforma escribe el catálogo de mensajes antes de implementarlos. `CalificarEntrega` es un **comando** con un único destinatario, el calificador, que puede rechazarlo (entrega inexistente, plazo vencido). `EntregaRecibida` es un **evento** con sobre completo (identificador, tipo, origen, hora, secuencia por entrega, correlación) y un contenido mínimo: identificador de la entrega, de estudiante y de curso. `CalificacionPublicada` es un **documento** con la nota y su versión, porque el aviso y la analítica quieren el estado **del instante**. Dejan fuera del evento los archivos y el texto de la entrega (se consultan por referencia) y cualquier dato de contacto, que el servicio de avisos obtiene con el identificador del estudiante. Cada mensaje declara su versión de esquema y la regla de cambio compatible.

## Ejemplo

Ejemplo de [SE-374 — Mensajes, eventos, comandos y documentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma escribe el catálogo de mensajes antes de implementarlos. `CalificarEntrega` es un **comando** con un único destinatario, el calificador, que puede rechazarlo (entrega inexistente, plazo vencido). `EntregaRecibida` es un **evento** con sobre completo (identificador, tipo, origen, hora, secuencia por entrega, correlación) y un contenido mínimo: identificador de la entrega, de estudiante y de curso. `CalificacionPublicada` es un **documento** con la nota y su versión, porque el aviso y la analítica quieren el estado **del instante**.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Los duplicados no se detectan o se descartan mensajes válidos** — causa: el sobre no tiene identificador único. Corrección: identificador único en el sobre desde el primer mensaje. ([SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La figura no prueba que haya que usar CloudEvents: prueba que hay que decidir un sobre. ([SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Atributo](../a/atributo.md), [Conjunto](../c/conjunto.md), [Comando](../c/comando.md), [Documento](../d/documento.md), [Evento](../e/evento.md), [Transferencia de estado en el evento](../t/transferencia-de-estado-en-el-evento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-374 — Mensajes, eventos, comandos y documentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (574 clases más lo mencionan; las que más):

[SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md), [SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md), [SE-348](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md), [SE-452](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md), [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md), [SE-543](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md), [SE-229](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md), [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

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

[↑ Glosario](../../README.md) · [← SLO](./slo.md) · [Sobreasignación →](./sobreasignacion.md)
