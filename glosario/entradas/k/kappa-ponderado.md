# Kappa ponderado

[↑ Glosario](../../README.md) · [← Kappa de Cohen](./kappa-de-cohen.md) · [Kernel →](./kernel.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Medida de acuerdo entre evaluadores corregida por azar que penaliza más las diferencias grandes.

Definición de trabajo de [SE-299 — Taller: comparar riesgos entre dominios](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md).

## Por qué importa

La clase donde se define, [SE-299 — Taller: comparar riesgos entre dominios](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md), existe con este propósito: el taller entrena a comparar los riesgos de dominios distintos sin fingir una precisión que no existe: construir una matriz con criterios explícitos, comprobar cuánto cambia el orden cuando cambian los pesos, medir cuánto discrepan dos personas que puntúan lo mismo y ver qué cubre una lista corta de controles comunes y qué queda sin cubrir en cada dominio.

## Cómo funciona

Según [SE-299 — Taller: comparar riesgos entre dominios](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md):

Dos personas no puntúan igual aunque usen la misma escala. El porcentaje de coincidencias exactas es engañoso porque parte del acuerdo es azar. El **kappa ponderado** corrige el azar y, al ser ponderado, penaliza menos una diferencia de un punto que una de cuatro. Landis y Koch propusieron bandas de lectura, que son convenciones útiles y no leyes. Lo decisivo para el taller es otra medida: **cuánto cambia la conclusión** (el podio) cuando se cambia de evaluador, porque un kappa alto puede convivir con un orden distinto. La respuesta práctica es calibrar con ejemplos ancla, puntuar a ciegas y reconciliar las diferencias grandes.

Según [SE-299 — Taller: comparar riesgos entre dominios](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md):

El equipo de la plataforma redacta la matriz con una escala de cinco niveles y un ejemplo ancla por criterio (por ejemplo, para *irreversibilidad*: 1 = se deshace con un clic; 3 = se deshace con una operación manual; 5 = no se puede deshacer). Dos personas puntúan por separado y sin ver la otra tabla; las diferencias de dos o más puntos se discuten y se registran con su motivo. Se calcula el kappa ponderado y la estabilidad del ranking con 5 000 sorteos de pesos, y el informe publica tres líneas: el primer lugar (con su estabilidad), las parejas empatadas y la lista de comparaciones que no se hacen. La recomendación de controles no es «los seis para todos» sino los dos comunes más uno propio por dominio.

## Ejemplo

Ejemplo de [SE-299 — Taller: comparar riesgos entre dominios](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma redacta la matriz con una escala de cinco niveles y un ejemplo ancla por criterio (por ejemplo, para *irreversibilidad*: 1 = se deshace con un clic; 3 = se deshace con una operación manual; 5 = no se puede deshacer). Dos personas puntúan por separado y sin ver la otra tabla; las diferencias de dos o más puntos se discuten y se registran con su motivo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-299 — Taller: comparar riesgos entre dominios](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md)) son:

- **Los dos evaluadores discrepan en muchas celdas** — causa: escala sin ejemplos ancla. Corrección: calibrar con casos ancla y puntuar a ciegas.
- **Se publica un orden como si fuera un hecho** — causa: no se mide la sensibilidad a los pesos. Corrección: muestrear pesos y declarar la estabilidad.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-299 — Taller: comparar riesgos entre dominios](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md)) son: Las definiciones son operativas para el taller. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos salvo el orden de listado de empates. Las puntuaciones, los riesgos y los controles son un juicio ilustrativo del autor, no una medición de ningún dominio, evaluador ni organización. El proyecto final aplica este método a un dominio elegido.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-298](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Acuerdo entre evaluadores](../a/acuerdo-entre-evaluadores.md), [Evaluador](../e/evaluador.md), [Medida](../m/medida.md), [Cobertura de controles](../c/cobertura-de-controles.md), [Control](../c/control.md), [Ejemplo ancla](../e/ejemplo-ancla.md).
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

[↑ Glosario](../../README.md) · [← Kappa de Cohen](./kappa-de-cohen.md) · [Kernel →](./kernel.md)
