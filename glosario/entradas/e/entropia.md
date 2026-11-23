# Entropía

[↑ Glosario](../../README.md) · [← Entrevista estructurada](./entrevista-estructurada.md) · [Entropía de Shannon →](./entropia-de-shannon.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Medida de la imprevisibilidad de una fuente de datos; determina la seguridad de una clave generada a partir de ella.

Definición de trabajo de [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md).

## Por qué importa

En [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md), el tema «Aleatoriedad» importa porque una clave es tan fuerte como la entropía de su origen.

## Cómo funciona

Según [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md):

Una clave generada con una semilla de pocos valores posibles tiene la seguridad de esa cantidad de valores, no la de su longitud. Un dispositivo recién arrancado tiene poca entropía: no hay teclado, ni disco, ni red variable. Si usa el segundo de arranque como semilla, el espacio de búsqueda es el de segundos posibles. Heninger y colaboradores encontraron que muchos dispositivos de red generaban claves repetidas o factorizables por esa razón. La solución es una fuente de entropía de hardware (un generador verdadero de números aleatorios) o claves inyectadas en fábrica, y mezclar la entropía antes de generar.

Según [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md):

Porque es predecible: un atacante que sabe cuándo se instaló la flota puede enumerar los segundos posibles. Se necesita una fuente de entropía real.

## Ejemplo

Ejemplo de [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md) (sección «Preguntas frecuentes»):

Porque es predecible: un atacante que sabe cuándo se instaló la flota puede enumerar los segundos posibles. Se necesita una fuente de entropía real.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Varias unidades tienen la misma clave** — causa: semilla predecible al generar claves. Corrección: fuente de entropía de hardware o claves inyectadas en fábrica. ([SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un dispositivo recién arrancado tiene poca entropía: no hay teclado, ni disco, ni red variable. ([SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Medida](../m/medida.md), [Seguridad](../s/seguridad.md), [Clave de flota](../c/clave-de-flota.md), [Derivación de claves](../d/derivacion-de-claves.md), [Reproducción](../r/reproduccion.md), [Revocación](../r/revocacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-272 — Identidad de dispositivo y gestión de claves](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md), [SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), [SE-462](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-462-secretos-configuracion-y-separacion-de-ambientes/README.md), [SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md), [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md), [SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md), [SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Heninger et al., «Mining your Ps and Qs» (USENIX Security, 2012)](https://www.usenix.org/conference/usenixsecurity12/technical-sessions/presentation/heninger) — claves débiles por entropía insuficiente; autoridad: USENIX Security.
- [Krawczyk, Bellare y Canetti, RFC 2104: HMAC](https://www.rfc-editor.org/rfc/rfc2104) — autenticación de mensajes con hash y clave; autoridad: IETF.
- [Krawczyk y Eronen, RFC 5869: HKDF](https://www.rfc-editor.org/rfc/rfc5869) — derivación de claves; autoridad: IETF.
- [NIST SP 800-57 Parte 1 rev. 5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final) — gestión de claves; autoridad: NIST.
- [ETSI EN 303 645](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/) — requisitos básicos de ciberseguridad para IoT de consumo; autoridad: ETSI.

---

[↑ Glosario](../../README.md) · [← Entrevista estructurada](./entrevista-estructurada.md) · [Entropía de Shannon →](./entropia-de-shannon.md)
