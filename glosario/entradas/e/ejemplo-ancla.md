# Ejemplo ancla

[↑ Glosario](../../README.md) · [← Ejecución gestionada](./ejecucion-gestionada.md) · [Ejemplo como especificación →](./ejemplo-como-especificacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Caso concreto que fija el significado de un nivel de una escala de puntuación.

Definición de trabajo de [SE-299 — Taller: comparar riesgos entre dominios](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md).

## Por qué importa

La clase donde se define, [SE-299 — Taller: comparar riesgos entre dominios](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md), existe con este propósito: el taller entrena a comparar los riesgos de dominios distintos sin fingir una precisión que no existe: construir una matriz con criterios explícitos, comprobar cuánto cambia el orden cuando cambian los pesos, medir cuánto discrepan dos personas que puntúan lo mismo y ver qué cubre una lista corta de controles comunes y qué queda sin cubrir en cada dominio.

## Cómo funciona

Según [SE-299 — Taller: comparar riesgos entre dominios](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md):

Comparar exige criterios que se puedan puntuar con el mismo significado en todos los dominios. Los seis del taller son: *daño del error* (cuánto cuesta equivocarse), *irreversibilidad* (si se puede deshacer), *regulación* (cuánto la ley condiciona el diseño), *dificultad de verificar* (cuánto cuesta saber si el resultado es correcto), *datos sensibles* y *dependencia de terceros*. Cada criterio necesita una **escala con ejemplos ancla** (qué es un 1, un 3 y un 5, con un caso concreto), porque «3» no significa lo mismo para dos personas. NIST recomienda además documentar los supuestos y la incertidumbre de cada valoración; una puntuación sin justificación no se puede revisar.

Según [SE-299 — Taller: comparar riesgos entre dominios](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md):

El equipo de la plataforma redacta la matriz con una escala de cinco niveles y un ejemplo ancla por criterio (por ejemplo, para *irreversibilidad*: 1 = se deshace con un clic; 3 = se deshace con una operación manual; 5 = no se puede deshacer). Dos personas puntúan por separado y sin ver la otra tabla; las diferencias de dos o más puntos se discuten y se registran con su motivo. Se calcula el kappa ponderado y la estabilidad del ranking con 5 000 sorteos de pesos, y el informe publica tres líneas: el primer lugar (con su estabilidad), las parejas empatadas y la lista de comparaciones que no se hacen. La recomendación de controles no es «los seis para todos» sino los dos comunes más uno propio por dominio.

## Ejemplo

Ejemplo de [SE-299 — Taller: comparar riesgos entre dominios](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma redacta la matriz con una escala de cinco niveles y un ejemplo ancla por criterio (por ejemplo, para *irreversibilidad*: 1 = se deshace con un clic; 3 = se deshace con una operación manual; 5 = no se puede deshacer). Dos personas puntúan por separado y sin ver la otra tabla; las diferencias de dos o más puntos se discuten y se registran con su motivo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Los dos evaluadores discrepan en muchas celdas** — causa: escala sin ejemplos ancla. Corrección: calibrar con casos ancla y puntuar a ciegas. ([SE-299](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cada criterio necesita una **escala con ejemplos ancla** (qué es un 1, un 3 y un 5, con un caso concreto), porque «3» no significa lo mismo para dos personas. ([SE-299](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-298](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cobertura de controles](../c/cobertura-de-controles.md), [Control](../c/control.md), [Kappa ponderado](../k/kappa-ponderado.md), [Sensibilidad global](../s/sensibilidad-global.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-299 — Taller: comparar riesgos entre dominios](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-30 Rev. 1, «Guide for Conducting Risk Assessments»](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-30r1.pdf) — evaluación de riesgos con documentación de supuestos e incertidumbre; autoridad: NIST.
- [Landis y Koch, «The Measurement of Observer Agreement for Categorical Data» (Biometrics, 1977)](https://doi.org/10.2307/2529310) — kappa y su interpretación; autoridad: Biometrics.
- [Saltelli et al., «Global Sensitivity Analysis: The Primer» (2008)](https://doi.org/10.1002/9780470725184) — análisis de sensibilidad global; autoridad: Wiley.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — áreas de conocimiento de ingeniería de software; autoridad: IEEE Computer Society.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla para las simulaciones; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Ejecución gestionada](./ejecucion-gestionada.md) · [Ejemplo como especificación →](./ejemplo-como-especificacion.md)
