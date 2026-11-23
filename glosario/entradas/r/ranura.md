# Ranura

[↑ Glosario](../../README.md) · [← Rango con confianza](./rango-con-confianza.md) · [Rareza heredada →](./rareza-heredada.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Región de memoria que contiene una imagen de firmware completa; con dos, una está activa y la otra recibe la actualización.

Definición de trabajo de [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md).

## Por qué importa

En [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md), el tema «Ranuras y reversión» importa porque dos ranuras convierten cualquier corte en «antigua o nueva».

## Cómo funciona

Según [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md):

Con dos ranuras, la nueva imagen se escribe en la inactiva y la activa no se toca hasta que la nueva está completa y validada. El cambio de ranura es un único indicador, cuya escritura debe ser atómica o validable: si ocupa dos bytes y se corta entre ambos, el cargador de arranque encuentra un valor inválido. El cargador arranca la nueva en modo de prueba y, si no confirma en un plazo (con un temporizador de vigilancia, `SE-274`), vuelve a la anterior. El coste es el doble de memoria para firmware.

Según [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md):

El equipo de la plataforma define el plan para sus 200 nodos. El firmware tiene dos ranuras de 256 KiB con un indicador de un byte atómico y un cargador que arranca la nueva en modo de prueba y vuelve a la anterior si no confirma en 60 s. La actualización es diferencial por bloques de 256 B con búsqueda en cualquier posición, con un tamaño típico de unos pocos kilobytes.

## Ejemplo

Ejemplo de [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma define el plan para sus 200 nodos. El firmware tiene dos ranuras de 256 KiB con un indicador de un byte atómico y un cargador que arranca la nueva en modo de prueba y vuelve a la anterior si no confirma en 60 s. La actualización es diferencial por bloques de 256 B con búsqueda en cualquier posición, con un tamaño típico de unos pocos kilobytes.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un corte durante la actualización deja el dispositivo mudo** — causa: sobrescritura de la imagen activa. Corrección: dos ranuras y cambio de indicador al final. ([SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Con dos ranuras, la nueva imagen se escribe en la inactiva y la activa no se toca hasta que la nueva está completa y validada. ([SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md))
- No si la memoria no alcanza o el firmware es pequeño: se puede usar una ranura con una pequeña copia de recuperación. ([SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-270](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Firmware](../f/firmware.md), [Imagen](../i/imagen.md), [Región](./region.md), [Actualización diferencial](../a/actualizacion-diferencial.md), [Actualización inalámbrica](../a/actualizacion-inalambrica.md), [Criterio de parada](../c/criterio-de-parada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md), [SE-087](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-087-tablas-hash-mapas-y-conjuntos/README.md), [SE-085](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md), [SE-183](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md), [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md).

**Aparece en los casos de estudio:** [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

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

[↑ Glosario](../../README.md) · [← Rango con confianza](./rango-con-confianza.md) · [Rareza heredada →](./rareza-heredada.md)
