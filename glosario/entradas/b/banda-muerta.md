# Banda muerta

[↑ Glosario](../../README.md) · [← Banda](./banda.md) · [Bandeja de salida →](./bandeja-de-salida.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Umbral de variación por debajo del cual no se envía una nueva lectura.

Definición de trabajo de [SE-273 — Edge, gateways y procesamiento local](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md).

## Por qué importa

La clase donde se define, [SE-273 — Edge, gateways y procesamiento local](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md), existe con este propósito: la clase existe para que decidas qué se procesa en el dispositivo, qué en una pasarela local y qué en la nube por lo que se pierde y se gana en cada sitio: bytes enviados, eventos que dejan de verse, plazos que se cumplen y coste de cada formato de datos.

## Cómo funciona

Según [SE-273 — Edge, gateways y procesamiento local](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md):

Enviar cada muestra conserva todo y cuesta lo máximo. Enviar el promedio por minuto reduce unos 60 veces los bytes y suaviza los picos. Enviar el máximo por minuto conserva los picos y pierde la forma de la señal. La banda muerta (enviar solo si cambia más de un umbral) ahorra más en señales estables y envía en cuanto hay un cambio. Cada estrategia fija qué se puede reconstruir y qué eventos se ven. La elección depende de la decisión que se toma con los datos, no de los bytes.

Según [SE-273 — Edge, gateways y procesamiento local](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md):

El equipo de la plataforma asigna cada decisión a un nivel. La alarma de ventilación se decide en el nodo con un umbral guardado en memoria y un valor seguro por defecto; el nodo informa del evento cuando hay red. La pasarela del piso agrupa los 20 nodos, aplica la banda muerta de 0,5 °C a la temperatura y el promedio por minuto al CO₂ más un evento si hay un pico, almacena hasta tres horas por si cae la nube y envía en lotes de 60 muestras en binario comprimido. La nube guarda el histórico y ajusta umbrales, que la pasarela distribuye a los nodos con firma (`SE-272`). La pasarela tiene su propia identidad, su plan de actualización y una alarma si deja de recibir datos de un nodo.

## Ejemplo

Ejemplo de [SE-273 — Edge, gateways y procesamiento local](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md) (sección «Ejemplo mínimo»):

El ahorro es de 60 veces (691 200 frente a 11 520 bytes por día). Registra versión, comando y salida; calcula el ahorro con banda muerta si hay 125 envíos de 10 bytes al día en lugar de 86 400 de 8.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La factura de datos es alta con datos casi constantes** — causa: envío de cada muestra. Corrección: banda muerta o promedios con evento. ([SE-273](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La banda muerta (enviar solo si cambia más de un umbral) ahorra más en señales estables y envía en cuanto hay un cambio. ([SE-273](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Borde de la red](./borde-de-la-red.md), [Carga útil](../c/carga-util.md), [Decisión con plazo](../d/decision-con-plazo.md), [Pasarela](../p/pasarela.md).
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

[↑ Glosario](../../README.md) · [← Banda](./banda.md) · [Bandeja de salida →](./bandeja-de-salida.md)
