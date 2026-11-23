# Clave de flota

[↑ Glosario](../../README.md) · [← Clave de caché](./clave-de-cache.md) · [Clave de idempotencia →](./clave-de-idempotencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Secreto compartido por todos los dispositivos de una flota; su extracción compromete a todos.

Definición de trabajo de [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md).

## Por qué importa

En [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md), el tema «Esquemas de claves» importa porque clave de flota, claves por dispositivo y derivación tienen alcances distintos.

## Cómo funciona

Según [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md):

Con una **clave de flota**, quien extrae la clave de un dispositivo puede firmar como cualquiera de los 10 000. Con **claves por dispositivo** almacenadas en el servidor, la extracción compromete un dispositivo, a costa de custodiar una base de claves. Con **derivación**, cada clave se calcula como HMAC o HKDF de un secreto maestro y del identificador del dispositivo; el servidor no necesita almacenar las claves, y la extracción de una compromete un dispositivo, siempre que el secreto maestro nunca esté en un dispositivo. Si el maestro se filtra, el alcance es toda la flota.

Según [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md):

Debe poder revocarse y reemplazarse; por eso la identidad única por dispositivo es una condición: una clave de flota no se puede revocar sin tocar a todos.

## Ejemplo

Ejemplo de [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md) (sección «Preguntas frecuentes»):

Debe poder revocarse y reemplazarse; por eso la identidad única por dispositivo es una condición: una clave de flota no se puede revocar sin tocar a todos.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md)) son:

- **Un dispositivo comprometido permite suplantar a toda la flota** — causa: clave compartida. Corrección: claves únicas por dispositivo o derivadas de un secreto maestro externo.
- **Mensajes legítimos rechazados** — causa: ventana de tiempo estrecha frente al desfase. Corrección: ensanchar la ventana, sincronizar el reloj o usar un contador persistente.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Debe poder revocarse y reemplazarse; por eso la identidad única por dispositivo es una condición: una clave de flota no se puede revocar sin tocar a todos. ([SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dispositivo](../d/dispositivo.md), [Extracción](../e/extraccion.md), [Secreto](../s/secreto.md), [Derivación de claves](../d/derivacion-de-claves.md), [Entropía](../e/entropia.md), [Reproducción](../r/reproduccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Krawczyk, Bellare y Canetti, RFC 2104: HMAC](https://www.rfc-editor.org/rfc/rfc2104) — autenticación de mensajes con hash y clave; autoridad: IETF.
- [Krawczyk y Eronen, RFC 5869: HKDF](https://www.rfc-editor.org/rfc/rfc5869) — derivación de claves; autoridad: IETF.
- [NIST SP 800-57 Parte 1 rev. 5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final) — gestión de claves; autoridad: NIST.
- [Heninger et al., «Mining your Ps and Qs» (USENIX Security, 2012)](https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/heninger) — claves débiles por entropía insuficiente; autoridad: USENIX Security.
- [ETSI EN 303 645](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/) — requisitos básicos de ciberseguridad para IoT de consumo; autoridad: ETSI.

---

[↑ Glosario](../../README.md) · [← Clave de caché](./clave-de-cache.md) · [Clave de idempotencia →](./clave-de-idempotencia.md)
