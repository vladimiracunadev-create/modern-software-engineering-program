# Amplificación de reintentos

[↑ Glosario](../../README.md) · [← Ampliar, migrar y contraer](./ampliar-migrar-y-contraer.md) · [Amplificación por reintentos →](./amplificacion-por-reintentos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Multiplicación de la carga sobre un servicio cuando varias capas reintentan sin coordinarse.

Definición de trabajo de [SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md).

## Por qué importa

La clase donde se define, [SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md), existe con este propósito: la clase existe para que elijas entre esperar la respuesta de otro componente y dejarle un mensaje con criterios medibles, en lugar de por costumbre o por moda: cuánto baja la disponibilidad cuando una petición cruza varias dependencias, cuánta carga añaden los reintentos apilados y cuánto tarda en recuperarse una cola después de una caída.

## Cómo funciona

[SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md):

El equipo de la plataforma revisa cuatro interacciones y las clasifica con la pregunta «¿qué necesita saber el estudiante ahora?». **Recibir la entrega:** síncrona, con almacenamiento duradero y una clave de idempotencia generada por el cliente, porque el estudiante debe saber que su archivo llegó. **Calificación automática:** asíncrona, por una cola con límite de edad de 24 horas y un estado «en proceso» visible. **Aviso por correo:** asíncrona y con reintentos acotados; si falla, la entrega no cambia.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md)) son:

- **Los estudiantes ven errores aunque el calificador funciona** — causa: la entrega depende de un servicio secundario en la ruta síncrona. Corrección: sacar la dependencia de la ruta crítica o degradar su respuesta.
- **El servicio enfermo no se recupera** — causa: reintentos en varias capas multiplican la carga. Corrección: reintentar en una capa, con retroceso, aleatoriedad y presupuesto.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó red, servidor, corredor de mensajes ni medición de latencia: las tasas de fallo, la llegada constante, la caída de 600 s y el presupuesto de reintentos son construcciones del autor, y los resultados no se extrapolan a otros sistemas ni a cargas de producción.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capa](../c/capa.md), [Servicio](../s/servicio.md), [Sobre](../s/sobre.md), [Acoplamiento temporal](./acoplamiento-temporal.md), [Backlog](../b/backlog.md), [Disponibilidad en cadena](../d/disponibilidad-en-cadena.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md), [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [AWS Builders' Library: timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — amplificación de reintentos y retroceso con aleatoriedad; autoridad: Amazon Web Services.
- [Hohpe y Woolf, «Enterprise Integration Patterns»](https://www.enterpriseintegrationpatterns.com/) — catálogo de patrones de mensajería frente a invocación remota; autoridad: autores del libro.
- [RFC 9110: semántica de HTTP](https://www.rfc-editor.org/rfc/rfc9110) — métodos seguros e idempotentes y reintentos automáticos; autoridad: IETF.
- [Google SRE: addressing cascading failures](https://sre.google/sre-book/addressing-cascading-failures/) — reintentos y fallos en cascada; autoridad: Google.
- [Helland, «Life beyond distributed transactions»](https://www.cidrdb.org/cidr2007/papers/cidr07p15.pdf) — diseño con mensajes entre entidades sin transacción compartida; autoridad: artículo del autor (CIDR 2007).

---

[↑ Glosario](../../README.md) · [← Ampliar, migrar y contraer](./ampliar-migrar-y-contraer.md) · [Amplificación por reintentos →](./amplificacion-por-reintentos.md)
