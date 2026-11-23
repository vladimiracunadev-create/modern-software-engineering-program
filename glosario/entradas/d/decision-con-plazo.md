# Decisión con plazo

[↑ Glosario](../../README.md) · [← Decisión colectiva](./decision-colectiva.md) · [Decisión con rangos →](./decision-con-rangos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Decisión que debe tomarse en un tiempo acotado, sin depender de recursos remotos.

Definición de trabajo de [SE-273 — Edge, gateways y procesamiento local](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md).

## Por qué importa

En [SE-273 — Edge, gateways y procesamiento local](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md), el tema «Decisiones con plazo» importa porque una decisión con plazo corto no puede depender de la red.

## Cómo funciona

Según [SE-273 — Edge, gateways y procesamiento local](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md), en la sección «Decisiones con plazo»:

Si la ventilación debe arrancar en menos de 100 ms tras superar un umbral, la decisión no puede depender de una ida y vuelta a la nube, cuya latencia tiene cola larga y a veces no hay. La decisión se toma en el dispositivo y se informa a la nube después. La nube puede ajustar umbrales y reglas con calma, y el dispositivo debe tener valores seguros por defecto cuando no recibe nada. Es el mismo principio de `SE-268` (el plazo decide dónde vive el cómputo) llevado a la red.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-273 — Edge, gateways y procesamiento local](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md):

El equipo de la plataforma asigna cada decisión a un nivel. La alarma de ventilación se decide en el nodo con un umbral guardado en memoria y un valor seguro por defecto; el nodo informa del evento cuando hay red.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-273 — Edge, gateways y procesamiento local](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md)) son:

- **Una alarma no actúa cuando se corta la red** — causa: decisión en la nube. Corrección: decidir en el dispositivo con valores por defecto seguros.
- **La factura de datos es alta con datos casi constantes** — causa: envío de cada muestra. Corrección: banda muerta o promedios con evento.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **una decisión con plazo que depende de la nube**. ([SE-273](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Recurso](../r/recurso.md), [Banda muerta](../b/banda-muerta.md), [Borde de la red](../b/borde-de-la-red.md), [Carga útil](../c/carga-util.md), [Pasarela](../p/pasarela.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-273 — Edge, gateways y procesamiento local](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Bormann, Ersue y Keränen, RFC 7228: Terminology for Constrained-Node Networks](https://www.rfc-editor.org/rfc/rfc7228) — restricciones de nodos y redes; autoridad: IETF.
- [Hartke, RFC 8576: IoT Security: State of the Art and Challenges](https://www.rfc-editor.org/rfc/rfc8576) — desafíos de seguridad del IoT; autoridad: IETF.
- [Lee y Seshia, «Introduction to Embedded Systems»](https://ptolemy.berkeley.edu/books/leeseshia/) — latencia y plazos en sistemas ciberfísicos; autoridad: autores del libro (UC Berkeley).
- [Python: `struct`](https://docs.python.org/3/library/struct.html) — empaquetado binario; autoridad: documentación de Python.
- [Python: `zlib`](https://docs.python.org/3/library/zlib.html) — compresión usada en la comparación; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Decisión colectiva](./decision-colectiva.md) · [Decisión con rangos →](./decision-con-rangos.md)
