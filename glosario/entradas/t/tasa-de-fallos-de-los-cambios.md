# Tasa de fallos de los cambios

[↑ Glosario](../../README.md) · [← Tasa de consumo](./tasa-de-consumo.md) · [Tasa interna de retorno →](./tasa-interna-de-retorno.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Fracción de los despliegues que requieren una intervención inmediata tras ejecutarse.

Definición de trabajo de [SE-490 — Métricas DORA y mejora sin gaming](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md).

## Por qué importa

La clase donde se define, [SE-490 — Métricas DORA y mejora sin gaming](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md), existe con este propósito: la clase existe para que midas la entrega de software sin engañarte ni dejar que otros se engañen.

## Cómo funciona

Según [SE-490 — Métricas DORA y mejora sin gaming](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md):

La guía de DORA agrupa las métricas en dos dimensiones. El **rendimiento** (throughput) describe la velocidad con que los cambios llegan a producción: el **plazo de los cambios** (tiempo desde que un cambio se confirma en el control de versiones hasta que se despliega en producción), la **frecuencia de despliegue** y el **tiempo de recuperación de un despliegue fallido**. La **inestabilidad** describe la calidad de esas entregas: la **tasa de fallos de los cambios** (fracción de despliegues que requieren una intervención inmediata, normalmente un retroceso o una corrección urgente) y la **tasa de retrabajo** (fracción de despliegues no planificados que ocurren a consecuencia de un incidente). Las dos dimensiones se miran juntas porque la velocidad sin estabilidad es acumular deuda y la estabilidad sin velocidad es no entregar.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-490 — Métricas DORA y mejora sin gaming](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md):

El equipo de la API de entregas escribe sus definiciones antes de construir ningún panel. El plazo empieza en la fusión a la troncal y termina cuando el despliegue a producción es sano (no cuando se lanza); una segunda serie mide desde el primer commit para ver cuánto se pierde antes de integrar. La frecuencia cuenta solo despliegues de cambios de comportamiento a producción, por servicio. Un fallo es cualquier despliegue seguido de un retroceso, una corrección urgente o una incidencia de gravedad alta en las dos horas siguientes.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-490 — Métricas DORA y mejora sin gaming](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md)) son:

- **Dos equipos reportan plazos muy distintos** — causa: definiciones diferentes. Corrección: escribir y versionar las definiciones; comparar solo con la misma.
- **La frecuencia sube y la entrega no mejora** — causa: la métrica es objetivo y se cuentan despliegues vacíos. Corrección: contar solo cambios de comportamiento; añadir contrapeso.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **inestabilidad** describe la calidad de esas entregas: la **tasa de fallos de los cambios** (fracción de despliegues que requieren una intervención inmediata, normalmente un retroceso o una corrección urgente) y la **tasa de retrabajo** (fracción de despliegues no planificados que ocurren a consecuencia de un incidente). ([SE-490](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Frecuencia de despliegue](../f/frecuencia-de-despliegue.md), [Medida de contrapeso](../m/medida-de-contrapeso.md), [Plazo de los cambios](../p/plazo-de-los-cambios.md), [Tiempo de recuperación](./tiempo-de-recuperacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-490 — Métricas DORA y mejora sin gaming](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [DORA: guía de métricas](https://dora.dev/guides/dora-metrics/) — definición de las métricas de rendimiento e inestabilidad de la entrega; autoridad: DORA, Google Cloud, consultada el 15 de noviembre de 2026.
- [Forsgren et al., «The SPACE of Developer Productivity»](https://doi.org/10.1145/3454122.3454124) — productividad multidimensional (ACM Queue, 2021); autoridad: artículo con DOI verificado en Crossref.
- [Wilson, «Probable inference, the law of succession, and statistical inference»](https://doi.org/10.1080/01621459.1927.10502953) — intervalo para proporciones (Journal of the American Statistical Association, 1927); autoridad: artículo con DOI verificado en Crossref.

---

[↑ Glosario](../../README.md) · [← Tasa de consumo](./tasa-de-consumo.md) · [Tasa interna de retorno →](./tasa-interna-de-retorno.md)
