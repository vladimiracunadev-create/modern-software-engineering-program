# Derivación de claves

[↑ Glosario](../../README.md) · [← Deriva semántica](./deriva-semantica.md) · [Desacuerdo de hechos, de intereses y de valores →](./desacuerdo-de-hechos-de-intereses-y-de-valores.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Cálculo de una clave a partir de un secreto maestro y un identificador mediante una función como HKDF o HMAC.

Definición de trabajo de [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md).

## Por qué importa

La clase donde se define, [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md), existe con este propósito: la clase existe para que decidas cómo un dispositivo prueba quién es y cómo un servidor decide a quién cree, midiendo cuánto daño causa extraer una clave de un dispositivo, qué ventana de tiempo tolera un mensaje firmado y qué seguridad queda cuando la clave se genera con una semilla predecible.

## Cómo funciona

[SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md):

El equipo de la plataforma cambia la política de identidad del nodo. Cada nodo recibe en fábrica una clave única derivada con HKDF de un secreto maestro que vive en un módulo de seguridad del fabricante y nunca en los nodos; el servidor deriva la misma clave al recibir un mensaje. Los mensajes llevan un contador persistente (guardado con la política de `SE-267` en un sector aparte) y la marca de tiempo solo como señal auxiliar, con una ventana de ±120 s.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md)) son:

- **Un dispositivo comprometido permite suplantar a toda la flota** — causa: clave compartida. Corrección: claves únicas por dispositivo o derivadas de un secreto maestro externo.
- **Mensajes legítimos rechazados** — causa: ventana de tiempo estrecha frente al desfase. Corrección: ensanchar la ventana, sincronizar el reloj o usar un contador persistente.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md)) son: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se atacó ningún chip ni se auditó un dispositivo: la flota, la extracción, el desfase gaussiano y la semilla por segundo de arranque son construcciones del autor, y el generador de Python no es criptográfico. La siguiente clase mueve parte del procesamiento al borde de la red.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Función](../f/funcion.md), [HMAC](../h/hmac.md), [Secreto](../s/secreto.md), [Clave de flota](../c/clave-de-flota.md), [Entropía](../e/entropia.md), [Reproducción](../r/reproduccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Krawczyk y Eronen, RFC 5869: HKDF](https://www.rfc-editor.org/rfc/rfc5869) — derivación de claves; autoridad: IETF.
- [Krawczyk, Bellare y Canetti, RFC 2104: HMAC](https://www.rfc-editor.org/rfc/rfc2104) — autenticación de mensajes con hash y clave; autoridad: IETF.
- [NIST SP 800-57 Parte 1 rev. 5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final) — gestión de claves; autoridad: NIST.
- [Heninger et al., «Mining your Ps and Qs» (USENIX Security, 2012)](https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/heninger) — claves débiles por entropía insuficiente; autoridad: USENIX Security.
- [ETSI EN 303 645](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/) — requisitos básicos de ciberseguridad para IoT de consumo; autoridad: ETSI.

---

[↑ Glosario](../../README.md) · [← Deriva semántica](./deriva-semantica.md) · [Desacuerdo de hechos, de intereses y de valores →](./desacuerdo-de-hechos-de-intereses-y-de-valores.md)
