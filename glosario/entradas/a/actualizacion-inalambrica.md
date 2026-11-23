# Actualización inalámbrica

[↑ Glosario](../../README.md) · [← Actualización diferencial](./actualizacion-diferencial.md) · [Actualización perdida →](./actualizacion-perdida.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Actualización del firmware de un dispositivo a través de una red, sin acceso físico.

Definición de trabajo de [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md).

## Por qué importa

La clase donde se define, [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md), existe con este propósito: la clase existe para que diseñes una actualización de firmware que sobreviva a un corte de energía en cualquier paso, que transmita lo mínimo y que se despliegue por etapas con una regla para detenerse, de modo que una versión defectuosa no deje inservible a una flota entera.

## Cómo funciona

[SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md):

El equipo de la plataforma define el plan para sus 200 nodos. El firmware tiene dos ranuras de 256 KiB con un indicador de un byte atómico y un cargador que arranca la nueva en modo de prueba y vuelve a la anterior si no confirma en 60 s. La actualización es diferencial por bloques de 256 B con búsqueda en cualquier posición, con un tamaño típico de unos pocos kilobytes.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md)) son:

- **Un corte durante la actualización deja el dispositivo mudo** — causa: sobrescritura de la imagen activa. Corrección: dos ranuras y cambio de indicador al final.
- **Un indicador inválido tras un corte** — causa: indicador de varios bytes sin validación. Corrección: hacerlo atómico o validarlo con una suma.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md)) son: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se actualizó ningún dispositivo ni se usó un cargador de arranque: los pasos de la actualización, las imágenes sintéticas, el 0,9 de informe y los fallos independientes son construcciones del autor. La siguiente clase pregunta cómo el nodo sabe que la actualización que recibe es legítima.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-270](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dispositivo](../d/dispositivo.md), [Firmware](../f/firmware.md), [Actualización diferencial](./actualizacion-diferencial.md), [Criterio de parada](../c/criterio-de-parada.md), [Despliegue por etapas](../d/despliegue-por-etapas.md), [Ranura](../r/ranura.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «OTA».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Moran et al., RFC 9019: A Firmware Update Architecture for Internet of Things](https://www.rfc-editor.org/rfc/rfc9019) — arquitectura de actualización de firmware; autoridad: IETF.
- [Moran et al., RFC 9124: A Manifest Information Model for Firmware Updates in IoT Devices](https://www.rfc-editor.org/rfc/rfc9124) — modelo de información del manifiesto; autoridad: IETF.
- [The Update Framework (TUF)](https://theupdateframework.io/) — distribución segura de actualizaciones; autoridad: proyecto TUF (CNCF).
- [Uptane](https://uptane.org/) — marco de actualización segura de software para vehículos; autoridad: proyecto Uptane.
- [Tridgell y Mackerras, «The rsync algorithm»](https://rsync.samba.org/tech_report/) — diferencia de archivos con sumas de comprobación móviles; autoridad: proyecto rsync.

---

[↑ Glosario](../../README.md) · [← Actualización diferencial](./actualizacion-diferencial.md) · [Actualización perdida →](./actualizacion-perdida.md)
