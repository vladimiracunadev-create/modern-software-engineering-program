# Criterio de parada

[↑ Glosario](../../README.md) · [← Criterio de éxito](./criterio-de-exito.md) · [Criterio de retroceso →](./criterio-de-retroceso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Condición que termina el bucle.

Definición de trabajo de [SE-581 — Loops de agentes y criterios de parada](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md).

## Por qué importa

En [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md), el tema «Criterios de parada» importa porque sin una regla previa, nadie detiene un despliegue a tiempo.

## Cómo funciona

Según [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md), en la sección «Criterios de parada»:

Un criterio de parada se fija antes de empezar: «detener si tres dispositivos informan fallo en la etapa», «detener si el porcentaje de arranques fallidos supera el 1 %». Sin él, la decisión se toma bajo presión, con información parcial. Un criterio útil tiene umbral, ventana y responsable, igual que un disparador de replanificación (`SE-192`), y se acompaña de la capacidad de revertir a los dispositivos ya actualizados, que es lo que convierte una parada en una recuperación.

## Ejemplo

Ejemplo de [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma define el plan para sus 200 nodos. El firmware tiene dos ranuras de 256 KiB con un indicador de un byte atómico y un cargador que arranca la nueva en modo de prueba y vuelve a la anterior si no confirma en 60 s. La actualización es diferencial por bloques de 256 B con búsqueda en cualquier posición, con un tamaño típico de unos pocos kilobytes.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Nadie detiene un despliegue defectuoso** — causa: sin criterio de parada previo. Corrección: fijar umbral, ventana y responsable antes de empezar. ([SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md)) son: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se actualizó ningún dispositivo ni se usó un cargador de arranque: los pasos de la actualización, las imágenes sintéticas, el 0,9 de informe y los fallos independientes son construcciones del autor. La siguiente clase pregunta cómo el nodo sabe que la actualización que recibe es legítima.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-270](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](./condicion.md), [Actualización diferencial](../a/actualizacion-diferencial.md), [Actualización inalámbrica](../a/actualizacion-inalambrica.md), [Cambio de plan](./cambio-de-plan.md), [Despliegue por etapas](../d/despliegue-por-etapas.md), [Escalada](../e/escalada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-271 — Actualizaciones OTA y recuperación](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.
- [SE-581 — Loops de agentes y criterios de parada](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (12 clases más lo mencionan; las que más):

[SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md), [SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md), [SE-259](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md), [SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md), [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md), [SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md), [SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md), [SE-229](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Criterios de parada».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Moran et al., RFC 9019: A Firmware Update Architecture for Internet of Things](https://www.rfc-editor.org/rfc/rfc9019) — arquitectura de actualización de firmware; autoridad: IETF.
- [Moran et al., RFC 9124: A Manifest Information Model for Firmware Updates in IoT Devices](https://www.rfc-editor.org/rfc/rfc9124) — modelo de información del manifiesto; autoridad: IETF.
- [The Update Framework (TUF)](https://theupdateframework.io/) — distribución segura de actualizaciones; autoridad: proyecto TUF (CNCF).
- [Uptane](https://uptane.org/) — marco de actualización segura de software para vehículos; autoridad: proyecto Uptane.
- [Tridgell y Mackerras, «The rsync algorithm»](https://rsync.samba.org/tech_report/) — diferencia de archivos con sumas de comprobación móviles; autoridad: proyecto rsync.

---

[↑ Glosario](../../README.md) · [← Criterio de éxito](./criterio-de-exito.md) · [Criterio de retroceso →](./criterio-de-retroceso.md)
