# Despliegue por etapas

[↑ Glosario](../../README.md) · [← Despliegue escalonado](./despliegue-escalonado.md) · [Despliegue progresivo →](./despliegue-progresivo.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Un **despliegue por etapas** (*staged rollout*) es la publicación de una versión a fracciones crecientes de la flota con una regla para detenerla. [SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md) (actualizaciones OTA y recuperación) lo enseña para flotas de dispositivos. La diferencia con un despliegue «de golpe» es doble: la exposición crece de a poco y cada paso tiene una condición explícita para avanzar o frenar.

## Por qué importa

Publicar a toda la flota a la vez expone a todos a un defecto. En dispositivos físicos recuperar uno es caro, y a veces imposible sin visita. [SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md) lo resume: limitar la exposición de una versión nueva acota el daño si falla.

## Cómo funciona

Las etapas típicas son 1 %, 10 % y 100 %. Funcionan solo con dos condiciones:

1. **Cada etapa es lo bastante grande para ver el defecto.**
2. **El sistema recoge informes de fallo** y alguien (o una regla) los lee antes de avanzar.

[SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md) da la cuenta: si un defecto afecta a una fracción *f* de los dispositivos, una etapa de *n* dispositivos espera *n·f* fallos. Si *n·f* es menor que el umbral de informes, el defecto no se ve y el despliegue avanza, justo lo que no debía. Una etapa de 100 dispositivos con un defecto que afecta al 1 % espera un fallo, que puede pasar inadvertido o ser atribuido al ruido.

## Ejemplo

Cálculo ilustrativo propio, con la fórmula de la clase: una flota de 10 000 dispositivos, etapa del 1 % (100 dispositivos), defecto con *f* = 2 %. Se esperan 2 fallos; si la regla de parada exige 5 informes, el despliegue pasa a 10 % y el defecto aparece con 20 fallos (1 000 × 2 %). La etapa inicial protegió poco, y el ajuste razonable es subir la primera etapa o bajar el umbral.

## Errores y confusiones comunes

- **Etapas demasiado pequeñas para detectar el defecto** (`n·f` bajo el umbral).
- **Avanzar por tiempo en vez de por señal:** el calendario no sustituye a los informes.
- **Un corte durante la actualización deja el dispositivo mudo,** problema de otra capa que la clase resuelve con dos ranuras y cambio de indicador al final; el despliegue por etapas no lo previene.
- **Confundirlo con la actualización diferencial,** que trata de los bytes enviados, no de a quién.

## Límites y cuándo no aplica

No detecta defectos que solo aparecen tras mucho tiempo o en un subconjunto no representado por la etapa (otro hardware, otra región). Requiere una forma de detener y de revertir. Las simulaciones de [SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md) usaron fallos independientes y valores del autor, no una flota real.

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
