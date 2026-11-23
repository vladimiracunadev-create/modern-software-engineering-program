# Acoplamiento temporal

[↑ Glosario](../../README.md) · [← Acoplamiento](./acoplamiento.md) · [Acotar →](./acotar.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Dependencia de que dos componentes estén disponibles al mismo tiempo para completar una operación.

Definición de trabajo de [SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md).

## Por qué importa

La clase donde se define, [SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md), existe con este propósito: la clase existe para que elijas entre esperar la respuesta de otro componente y dejarle un mensaje con criterios medibles, en lugar de por costumbre o por moda: cuánto baja la disponibilidad cuando una petición cruza varias dependencias, cuánta carga añaden los reintentos apilados y cuánto tarda en recuperarse una cola después de una caída.

## Cómo funciona

Según [SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md):

Dos componentes están **acoplados en el tiempo** cuando uno solo puede avanzar si el otro está vivo en ese instante; en el espacio cuando uno necesita conocer la dirección del otro; y en el formato cuando ambos comparten el mismo esquema de datos. Una llamada síncrona los suma los tres. Una cola elimina el acoplamiento temporal (el receptor puede estar caído cuando el emisor escribe) y el de ubicación (el emisor conoce una cola, no un servidor), pero conserva el de formato: el mensaje sigue teniendo un esquema que ambos deben entender (`SE-380`). Reducir un acoplamiento no los reduce todos, y por eso «desacoplar» sin decir de cuál es una afirmación vacía.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md):

El equipo de la plataforma revisa cuatro interacciones y las clasifica con la pregunta «¿qué necesita saber el estudiante ahora?». **Recibir la entrega:** síncrona, con almacenamiento duradero y una clave de idempotencia generada por el cliente, porque el estudiante debe saber que su archivo llegó. **Calificación automática:** asíncrona, por una cola con límite de edad de 24 horas y un estado «en proceso» visible. **Aviso por correo:** asíncrona y con reintentos acotados; si falla, la entrega no cambia.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md)) son:

- **Los estudiantes ven errores aunque el calificador funciona** — causa: la entrega depende de un servicio secundario en la ruta síncrona. Corrección: sacar la dependencia de la ruta crítica o degradar su respuesta.
- **El servicio enfermo no se recupera** — causa: reintentos en varias capas multiplican la carga. Corrección: reintentar en una capa, con retroceso, aleatoriedad y presupuesto.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una cola elimina el acoplamiento temporal (el receptor puede estar caído cuando el emisor escribe) y el de ubicación (el emisor conoce una cola, no un servidor), pero conserva el de formato: el mensaje sigue teniendo un esquema que ambos deben entender (`SE-380`). ([SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Dependencia](../d/dependencia.md), [Operación](../o/operacion.md), [Amplificación de reintentos](./amplificacion-de-reintentos.md), [Backlog](../b/backlog.md), [Disponibilidad en cadena](../d/disponibilidad-en-cadena.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md), [SE-518](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Hohpe y Woolf, «Enterprise Integration Patterns»](https://www.enterpriseintegrationpatterns.com/) — catálogo de patrones de mensajería frente a invocación remota; autoridad: autores del libro.
- [RFC 9110: semántica de HTTP](https://www.rfc-editor.org/rfc/rfc9110) — métodos seguros e idempotentes y reintentos automáticos; autoridad: IETF.
- [AWS Builders' Library: timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — amplificación de reintentos y retroceso con aleatoriedad; autoridad: Amazon Web Services.
- [Google SRE: addressing cascading failures](https://sre.google/sre-book/addressing-cascading-failures/) — reintentos y fallos en cascada; autoridad: Google.
- [Helland, «Life beyond distributed transactions»](https://www.cidrdb.org/cidr2007/papers/cidr07p15.pdf) — diseño con mensajes entre entidades sin transacción compartida; autoridad: artículo del autor (CIDR 2007).

---

[↑ Glosario](../../README.md) · [← Acoplamiento](./acoplamiento.md) · [Acotar →](./acotar.md)
