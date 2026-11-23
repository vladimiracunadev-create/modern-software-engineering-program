# Disponibilidad en cadena

[↑ Glosario](../../README.md) · [← Disponibilidad compuesta](./disponibilidad-compuesta.md) · [Disposición →](./disposicion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Probabilidad de que una operación termine bien cuando necesita que varias dependencias respondan; con fallos independientes es el producto de las de cada una.

Definición de trabajo de [SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md).

## Por qué importa

En [SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md), el tema «Disponibilidad en cadena» importa porque cada dependencia síncrona multiplica una probabilidad de fallo.

## Cómo funciona

Según [SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md), en la sección «Disponibilidad en cadena»:

Si una petición necesita que k dependencias respondan y cada una falla con probabilidad p de forma independiente, la probabilidad de éxito es (1−p)^k. Con p = 1 % y cinco dependencias el éxito baja a 95,1 %: una cadena de eslabones muy fiables es menos fiable que cada eslabón. La independencia es una hipótesis optimista; fallos correlacionados (un mismo despliegue, una misma red) empeoran el resultado. Lo útil del modelo es la dirección: cada dependencia síncrona añadida a la ruta crítica tiene un precio de disponibilidad, aunque el código sea correcto. Por eso conviene preguntar cuáles de esas dependencias son necesarias para responder **ahora**.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md):

El equipo de la plataforma revisa cuatro interacciones y las clasifica con la pregunta «¿qué necesita saber el estudiante ahora?». **Recibir la entrega:** síncrona, con almacenamiento duradero y una clave de idempotencia generada por el cliente, porque el estudiante debe saber que su archivo llegó. **Calificación automática:** asíncrona, por una cola con límite de edad de 24 horas y un estado «en proceso» visible. **Aviso por correo:** asíncrona y con reintentos acotados; si falla, la entrega no cambia.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md)) son:

- **Los estudiantes ven errores aunque el calificador funciona** — causa: la entrega depende de un servicio secundario en la ruta síncrona. Corrección: sacar la dependencia de la ruta crítica o degradar su respuesta.
- **El servicio enfermo no se recupera** — causa: reintentos en varias capas multiplican la carga. Corrección: reintentar en una capa, con retroceso, aleatoriedad y presupuesto.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó red, servidor, corredor de mensajes ni medición de latencia: las tasas de fallo, la llegada constante, la caída de 600 s y el presupuesto de reintentos son construcciones del autor, y los resultados no se extrapolan a otros sistemas ni a cargas de producción.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dependencia](./dependencia.md), [Operación](../o/operacion.md), [Producto](../p/producto.md), [Acoplamiento temporal](../a/acoplamiento-temporal.md), [Amplificación de reintentos](../a/amplificacion-de-reintentos.md), [Backlog](../b/backlog.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

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

[↑ Glosario](../../README.md) · [← Disponibilidad compuesta](./disponibilidad-compuesta.md) · [Disposición →](./disposicion.md)
