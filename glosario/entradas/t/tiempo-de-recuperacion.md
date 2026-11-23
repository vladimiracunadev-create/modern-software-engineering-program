# Tiempo de recuperación

[↑ Glosario](../../README.md) · [← Tiempo de pared y cpu](./tiempo-de-pared-y-cpu.md) · [Tiempo de respuesta →](./tiempo-de-respuesta.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Tiempo que tarda en restaurarse el servicio tras un despliegue fallido.

Definición de trabajo de [SE-490 — Métricas DORA y mejora sin gaming](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md).

## Por qué importa

La clase donde se define, [SE-490 — Métricas DORA y mejora sin gaming](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md), existe con este propósito: la clase existe para que midas la entrega de software sin engañarte ni dejar que otros se engañen.

## Cómo funciona

Según [SE-490 — Métricas DORA y mejora sin gaming](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md):

La guía de DORA agrupa las métricas en dos dimensiones. El **rendimiento** (throughput) describe la velocidad con que los cambios llegan a producción: el **plazo de los cambios** (tiempo desde que un cambio se confirma en el control de versiones hasta que se despliega en producción), la **frecuencia de despliegue** y el **tiempo de recuperación de un despliegue fallido**. La **inestabilidad** describe la calidad de esas entregas: la **tasa de fallos de los cambios** (fracción de despliegues que requieren una intervención inmediata, normalmente un retroceso o una corrección urgente) y la **tasa de retrabajo** (fracción de despliegues no planificados que ocurren a consecuencia de un incidente). Las dos dimensiones se miran juntas porque la velocidad sin estabilidad es acumular deuda y la estabilidad sin velocidad es no entregar.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-490 — Métricas DORA y mejora sin gaming](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md):

El equipo de la API de entregas escribe sus definiciones antes de construir ningún panel. El plazo empieza en la fusión a la troncal y termina cuando el despliegue a producción es sano (no cuando se lanza); una segunda serie mide desde el primer commit para ver cuánto se pierde antes de integrar. La frecuencia cuenta solo despliegues de cambios de comportamiento a producción, por servicio. Un fallo es cualquier despliegue seguido de un retroceso, una corrección urgente o una incidencia de gravedad alta en las dos horas siguientes.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-490 — Métricas DORA y mejora sin gaming](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md)) son:

- **Dos equipos reportan plazos muy distintos** — causa: definiciones diferentes. Corrección: escribir y versionar las definiciones; comparar solo con la misma.
- **La frecuencia sube y la entrega no mejora** — causa: la métrica es objetivo y se cuentan despliegues vacíos. Corrección: contar solo cambios de comportamiento; añadir contrapeso.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-490 — Métricas DORA y mejora sin gaming](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md)) son: Las definiciones son operativas para la canalización de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos.

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
