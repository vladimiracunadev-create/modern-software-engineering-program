# Carga útil

[↑ Glosario](../../README.md) · [← Carga por lotes](./carga-por-lotes.md) · [Cargas adversarias →](./cargas-adversarias.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Datos de aplicación transportados por un mensaje, sin las cabeceras del protocolo.

Definición de trabajo de [SE-273 — Edge, gateways y procesamiento local](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md).

## Por qué importa

La clase donde se define, [SE-273 — Edge, gateways y procesamiento local](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md), existe con este propósito: la clase existe para que decidas qué se procesa en el dispositivo, qué en una pasarela local y qué en la nube por lo que se pierde y se gana en cada sitio: bytes enviados, eventos que dejan de verse, plazos que se cumplen y coste de cada formato de datos.

## Cómo funciona

[SE-273 — Edge, gateways y procesamiento local](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-273 — Edge, gateways y procesamiento local](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md):

El equipo de la plataforma asigna cada decisión a un nivel. La alarma de ventilación se decide en el nodo con un umbral guardado en memoria y un valor seguro por defecto; el nodo informa del evento cuando hay red.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-273 — Edge, gateways y procesamiento local](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md)) son:

- **Una alarma no actúa cuando se corta la red** — causa: decisión en la nube. Corrección: decidir en el dispositivo con valores por defecto seguros.
- **La factura de datos es alta con datos casi constantes** — causa: envío de cada muestra. Corrección: banda muerta o promedios con evento.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-273 — Edge, gateways y procesamiento local](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md)) son: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ninguna pasarela, red ni nube: la señal de temperatura, las latencias, las caídas del 5 % y las lecturas con ruido son construcciones del autor. La siguiente clase pregunta qué ocurre con la seguridad, la safety y una vida útil de años.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Banda muerta](../b/banda-muerta.md), [Borde de la red](../b/borde-de-la-red.md), [Decisión con plazo](../d/decision-con-plazo.md), [Pasarela](../p/pasarela.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-273 — Edge, gateways y procesamiento local](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-086](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-086-pilas-colas-deques-y-prioridades/README.md), [SE-046](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md), [SE-087](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-087-tablas-hash-mapas-y-conjuntos/README.md), [SE-038](../../../classes/part-03-redes-internet-y-protocolos/se-038-ethernet-wi-fi-direccionamiento-y-redes-locales/README.md), [SE-236](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md), [SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md).

**Aparece en los casos de estudio:** [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «payload».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Bormann, Ersue y Keränen, RFC 7228: Terminology for Constrained-Node Networks](https://www.rfc-editor.org/rfc/rfc7228) — restricciones de nodos y redes; autoridad: IETF.
- [Hartke, RFC 8576: IoT Security: State of the Art and Challenges](https://www.rfc-editor.org/rfc/rfc8576) — desafíos de seguridad del IoT; autoridad: IETF.
- [Lee y Seshia, «Introduction to Embedded Systems»](https://ptolemy.berkeley.edu/books/leeseshia/) — latencia y plazos en sistemas ciberfísicos; autoridad: autores del libro (UC Berkeley).
- [Python: `struct`](https://docs.python.org/3/library/struct.html) — empaquetado binario; autoridad: documentación de Python.
- [Python: `zlib`](https://docs.python.org/3/library/zlib.html) — compresión usada en la comparación; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Carga por lotes](./carga-por-lotes.md) · [Cargas adversarias →](./cargas-adversarias.md)
