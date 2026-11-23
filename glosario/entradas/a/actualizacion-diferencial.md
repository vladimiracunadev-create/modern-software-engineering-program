# Actualización diferencial

[↑ Glosario](../../README.md) · [← Actualización condicional atómica](./actualizacion-condicional-atomica.md) · [Actualización inalámbrica →](./actualizacion-inalambrica.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Envío de las diferencias entre dos versiones del firmware en lugar de la imagen completa.

Definición de trabajo de [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md).

## Por qué importa

En [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md), el tema «Actualización diferencial» importa porque enviar solo lo que cambió ahorra ancho de banda y energía, salvo que el cambio desplace todo.

## Cómo funciona

Según [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md), en la sección «Actualización diferencial»:

Enviar la diferencia entre versiones ahorra bytes y energía de radio, que suele costar más que el cálculo. Comparar bloques por posición es simple y falla cuando una inserción desplaza el resto: todos los bloques posteriores «cambian». Buscar bloques en cualquier posición (con sumas de comprobación que se actualizan al desplazar una ventana, como en rsync) los reconoce aunque se hayan movido. El coste es más cálculo en el dispositivo o en el servidor y un formato de diferencias que el cargador debe aplicar con seguridad, también ante cortes.

## Ejemplo

Ejemplo de [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md) (sección «Ejemplo profesional»):

Compara con el prototipo: un corte durante la actualización deja el nodo con la versión anterior, la actualización diferencial no envía la mitad de la imagen por insertar una línea y un defecto raro se detecta por telemetría y no por la queja de una sala. Un plan es adecuado cuando cada paso tolera un corte; es frágil cuando funciona solo si nada falla.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La actualización diferencial envía la mitad de la imagen** — causa: comparación por posición con una inserción. Corrección: buscar bloques en cualquier posición. ([SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md)) son: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se actualizó ningún dispositivo ni se usó un cargador de arranque: los pasos de la actualización, las imágenes sintéticas, el 0,9 de informe y los fallos independientes son construcciones del autor. La siguiente clase pregunta cómo el nodo sabe que la actualización que recibe es legítima.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-270](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Firmware](../f/firmware.md), [Imagen](../i/imagen.md), [Versión](../v/version.md), [Actualización inalámbrica](./actualizacion-inalambrica.md), [Criterio de parada](../c/criterio-de-parada.md), [Despliegue por etapas](../d/despliegue-por-etapas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Moran et al., RFC 9019: A Firmware Update Architecture for Internet of Things](https://www.rfc-editor.org/rfc/rfc9019) — arquitectura de actualización de firmware; autoridad: IETF.
- [Moran et al., RFC 9124: A Manifest Information Model for Firmware Updates in IoT Devices](https://www.rfc-editor.org/rfc/rfc9124) — modelo de información del manifiesto; autoridad: IETF.
- [The Update Framework (TUF)](https://theupdateframework.io/) — distribución segura de actualizaciones; autoridad: proyecto TUF (CNCF).
- [Uptane](https://uptane.org/) — marco de actualización segura de software para vehículos; autoridad: proyecto Uptane.
- [Tridgell y Mackerras, «The rsync algorithm»](https://rsync.samba.org/tech_report/) — diferencia de archivos con sumas de comprobación móviles; autoridad: proyecto rsync.

---

[↑ Glosario](../../README.md) · [← Actualización condicional atómica](./actualizacion-condicional-atomica.md) · [Actualización inalámbrica →](./actualizacion-inalambrica.md)
