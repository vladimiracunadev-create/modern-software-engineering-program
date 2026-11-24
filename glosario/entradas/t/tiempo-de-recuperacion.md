# Tiempo de recuperación

[↑ Glosario](../../README.md) · [← Tiempo de pared y cpu](./tiempo-de-pared-y-cpu.md) · [Tiempo de respuesta →](./tiempo-de-respuesta.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

En las métricas de entrega, el **tiempo de recuperación** es el tiempo que tarda en restaurarse el servicio tras un despliegue fallido ([SE-490](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md)). No se debe confundir con el MTTR de la ingeniería de fiabilidad en general ni con los objetivos de recuperación de desastres (RTO), de otra clase.

## Por qué importa

Es una de las métricas de DORA y mide cuánto dura el daño cuando un cambio falla; junto con la tasa de fallos de los cambios, describe la estabilidad de las entregas.

## Cómo funciona

La guía de DORA agrupa las métricas en dos dimensiones. El **rendimiento** describe la velocidad con que los cambios llegan a producción: plazo de los cambios (desde la confirmación hasta producción), frecuencia de despliegue y tiempo de recuperación. La **inestabilidad** describe la calidad: la tasa de fallos de los cambios y la tasa de retrabajo. [SE-490](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md) insiste en que cada definición se escriba y versione, porque dos equipos con definiciones distintas reportan números no comparables.

## Ejemplo

Un despliegue falla a las 10:00 y se revierte a las 10:20: el tiempo de recuperación es de 20 minutos. Un equipo con retroceso automático lo reduce; uno que debe corregir hacia adelante tarda más.

## Errores y confusiones comunes

- **Dos equipos reportan plazos muy distintos.** Definiciones diferentes; escribirlas, versionarlas y comparar solo con la misma.
- **La frecuencia sube y la entrega no mejora.** La métrica es objetivo y se cuentan despliegues vacíos; contar solo cambios de comportamiento y añadir contrapeso.

## Límites y cuándo no aplica

Una métrica de equipo no es un objetivo individual: cuando se vuelve meta, se manipula. Solo es comparable dentro de la misma definición.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Servicio](../s/servicio.md), [Frecuencia de despliegue](../f/frecuencia-de-despliegue.md), [Medida de contrapeso](../m/medida-de-contrapeso.md), [Plazo de los cambios](../p/plazo-de-los-cambios.md), [Tasa de fallos de los cambios](./tasa-de-fallos-de-los-cambios.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-490 — Métricas DORA y mejora sin gaming](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (13 clases más lo mencionan; las que más):

[SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md), [SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md), [SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md), [SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md), [SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md), [SE-189](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md), [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), [SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md).

**Aparece en los casos de estudio:** [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [DORA: guía de métricas](https://dora.dev/guides/dora-metrics/) — definición de las métricas de rendimiento e inestabilidad de la entrega; autoridad: DORA, Google Cloud, consultada el 15 de noviembre de 2026.
- [Forsgren et al., «The SPACE of Developer Productivity»](https://doi.org/10.1145/3454122.3454124) — productividad multidimensional (ACM Queue, 2021); autoridad: artículo con DOI verificado en Crossref.
- [Wilson, «Probable inference, the law of succession, and statistical inference»](https://doi.org/10.1080/01621459.1927.10502953) — intervalo para proporciones (Journal of the American Statistical Association, 1927); autoridad: artículo con DOI verificado en Crossref.

---

[↑ Glosario](../../README.md) · [← Tiempo de pared y cpu](./tiempo-de-pared-y-cpu.md) · [Tiempo de respuesta →](./tiempo-de-respuesta.md)
