# Medida de contrapeso

[↑ Glosario](../../README.md) · [← Medida](./medida.md) · [Medida de control de riesgo →](./medida-de-control-de-riesgo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Medida que empeoraría si otra se mejorara con un atajo.

Definición de trabajo de [SE-490 — Métricas DORA y mejora sin gaming](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md).

## Por qué importa

La clase donde se define, [SE-490 — Métricas DORA y mejora sin gaming](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md), existe con este propósito: la clase existe para que midas la entrega de software sin engañarte ni dejar que otros se engañen.

## Cómo funciona

Según [SE-490 — Métricas DORA y mejora sin gaming](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md):

Las métricas valen cuando abren una conversación: «el plazo desde el primer commit es de 32 horas y desde la fusión de 4,6; ¿qué pasa en las 27 horas anteriores?». Esa pregunta lleva a ramas largas, revisiones lentas o trabajo en curso acumulado, y se contesta con un experimento (limitar el trabajo en curso, acortar las ramas) cuyo efecto se mide con la misma definición. Un uso sano tiene cuatro rasgos: las métricas son del **equipo** y no de individuos; se muestran con su incertidumbre; se acompañan de una medida de contrapeso y de una lectura cualitativa (una encuesta breve, una conversación); y el equipo puede **proponer cambiar la métrica** si deja de reflejar su trabajo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-490 — Métricas DORA y mejora sin gaming](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md):

El equipo de la API de entregas escribe sus definiciones antes de construir ningún panel. El plazo empieza en la fusión a la troncal y termina cuando el despliegue a producción es sano (no cuando se lanza); una segunda serie mide desde el primer commit para ver cuánto se pierde antes de integrar. La frecuencia cuenta solo despliegues de cambios de comportamiento a producción, por servicio. Un fallo es cualquier despliegue seguido de un retroceso, una corrección urgente o una incidencia de gravedad alta en las dos horas siguientes.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-490 — Métricas DORA y mejora sin gaming](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md)) son:

- **Dos equipos reportan plazos muy distintos** — causa: definiciones diferentes. Corrección: escribir y versionar las definiciones; comparar solo con la misma.
- **La frecuencia sube y la entrega no mejora** — causa: la métrica es objetivo y se cuentan despliegues vacíos. Corrección: contar solo cambios de comportamiento; añadir contrapeso.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un uso sano tiene cuatro rasgos: las métricas son del **equipo** y no de individuos; se muestran con su incertidumbre; se acompañan de una medida de contrapeso y de una lectura cualitativa (una encuesta breve, una conversación); y el equipo puede **proponer cambiar la métrica** si deja de reflejar su trabajo. ([SE-490](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Medida](./medida.md), [Frecuencia de despliegue](../f/frecuencia-de-despliegue.md), [Plazo de los cambios](../p/plazo-de-los-cambios.md), [Tasa de fallos de los cambios](../t/tasa-de-fallos-de-los-cambios.md), [Tiempo de recuperación](../t/tiempo-de-recuperacion.md).
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

[↑ Glosario](../../README.md) · [← Medida](./medida.md) · [Medida de control de riesgo →](./medida-de-control-de-riesgo.md)
