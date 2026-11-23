# Despliegue por etapas

[↑ Glosario](../../README.md) · [← Despliegue escalonado](./despliegue-escalonado.md) · [Despliegue progresivo →](./despliegue-progresivo.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Publicación de una versión a fracciones crecientes de la flota con una regla para detenerla.

Definición de trabajo de [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md).

## Por qué importa

En [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md), el tema «Despliegue por etapas» importa porque limitar la exposición de una versión nueva acota el daño si falla.

## Cómo funciona

Según [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md), en la sección «Despliegue por etapas»:

Publicar a toda la flota a la vez expone a todos a un defecto. Un despliegue por etapas (1 %, 10 %, 100 %) limita el daño, siempre que cada etapa sea lo bastante grande para ver el defecto y el sistema recoja informes de fallo. Si un defecto afecta a una fracción f de los dispositivos, una etapa de n dispositivos espera n·f fallos; con n·f menor que el umbral de informes, el defecto no se ve y el despliegue avanza.

## Ejemplo

Caso medido en la sección «Despliegue por etapas» de [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md):

Publicar a toda la flota a la vez expone a todos a un defecto. Un despliegue por etapas (1 %, 10 %, 100 %) limita el daño, siempre que cada etapa sea lo bastante grande para ver el defecto y el sistema recoja informes de fallo. Si un defecto afecta a una fracción f de los dispositivos, una etapa de n dispositivos espera n·f fallos; con n·f menor que el umbral de informes, el defecto no se ve y el despliegue avanza.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md)) son:

- **Un corte durante la actualización deja el dispositivo mudo** — causa: sobrescritura de la imagen activa. Corrección: dos ranuras y cambio de indicador al final.
- **Un indicador inválido tras un corte** — causa: indicador de varios bytes sin validación. Corrección: hacerlo atómico o validarlo con una suma.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md)) son: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se actualizó ningún dispositivo ni se usó un cargador de arranque: los pasos de la actualización, las imágenes sintéticas, el 0,9 de informe y los fallos independientes son construcciones del autor. La siguiente clase pregunta cómo el nodo sabe que la actualización que recibe es legítima.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-270](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Regla](../r/regla.md), [Versión](../v/version.md), [Actualización diferencial](../a/actualizacion-diferencial.md), [Actualización inalámbrica](../a/actualizacion-inalambrica.md), [Criterio de parada](../c/criterio-de-parada.md), [Ranura](../r/ranura.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md), [SE-142](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md), [SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md), [SE-608](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md).

**Aparece en los casos de estudio:** [CrowdStrike](../../../casos/fallo/crowdstrike.md).

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

[↑ Glosario](../../README.md) · [← Despliegue escalonado](./despliegue-escalonado.md) · [Despliegue progresivo →](./despliegue-progresivo.md)
