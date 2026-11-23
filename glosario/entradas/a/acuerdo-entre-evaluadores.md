# Acuerdo entre evaluadores

[↑ Glosario](../../README.md) · [← Actualización y rollback](./actualizacion-y-rollback.md) · [Acuse →](./acuse.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Dos personas no puntúan igual aunque usen la misma escala. El porcentaje de coincidencias exactas es engañoso porque parte del acuerdo es azar. El **kappa ponderado** corrige el azar y, al ser ponderado, penaliza menos una diferencia de un punto que una de cuatro. Landis y Koch propusieron bandas de lectura, que son convenciones útiles y no leyes. Lo decisivo para el taller es otra medida: **cuánto cambia la conclusión** (el podio) cuando se cambia de evaluador, porque un kappa alto puede convivir con un orden distinto.

Explicación de la sección «Acuerdo entre evaluadores» de [SE-299 — Taller: comparar riesgos entre dominios](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md).

## Por qué importa

En [SE-299 — Taller: comparar riesgos entre dominios](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md), el tema «Acuerdo entre evaluadores» importa porque mide cuánto del orden depende de quién puntúa.

En [SE-180 — Proyecto: prototipo accesible evaluado con usuarios](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md), el tema «Acuerdo entre evaluadores» importa porque mide si dos personas distinguen lo mismo.

## Cómo funciona

Según [SE-299 — Taller: comparar riesgos entre dominios](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md), en la sección «Acuerdo entre evaluadores»:

Dos personas no puntúan igual aunque usen la misma escala. El porcentaje de coincidencias exactas es engañoso porque parte del acuerdo es azar. El **kappa ponderado** corrige el azar y, al ser ponderado, penaliza menos una diferencia de un punto que una de cuatro. Landis y Koch propusieron bandas de lectura, que son convenciones útiles y no leyes. Lo decisivo para el taller es otra medida: **cuánto cambia la conclusión** (el podio) cuando se cambia de evaluador, porque un kappa alto puede convivir con un orden distinto. La respuesta práctica es calibrar con ejemplos ancla, puntuar a ciegas y reconciliar las diferencias grandes.

Según [SE-180 — Proyecto: prototipo accesible evaluado con usuarios](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md), en la sección «Acuerdo entre evaluadores»:

El porcentaje de acuerdo infla el resultado cuando casi todo cumple: dos evaluadores que siempre dicen «cumple» coinciden casi siempre sin distinguir nada. Kappa corrige por el acuerdo esperado por azar. Con una tasa de error del 8 % en cada evaluador, el acuerdo medio es del 85 % en cualquier prevalencia, pero kappa baja de 0,70 a 0,21 al subir la prevalencia de «cumple» del 50 % al 97 %. Informar ambos y la prevalencia es la forma honesta.

## Ejemplo

Ejemplo de [SE-299 — Taller: comparar riesgos entre dominios](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md) (sección «Caso conductor»):

La plataforma educativa ficticia es el caso conductor de la [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md). Este taller deja el undécimo artefacto: una matriz de diez dominios con su estabilidad, su acuerdo entre evaluadores y su cobertura de controles. `SE-300` pide aplicar el método a un dominio elegido, con un diseño profundo y su propia evidencia. Cambia después una sola decisión, el peso de un criterio, y observa qué parte del orden se mueve.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-299 — Taller: comparar riesgos entre dominios](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md)) son:

- **Los dos evaluadores discrepan en muchas celdas** — causa: escala sin ejemplos ancla. Corrección: calibrar con casos ancla y puntuar a ciegas.
- **Se publica un orden como si fuera un hecho** — causa: no se mide la sensibilidad a los pesos. Corrección: muestrear pesos y declarar la estabilidad.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-299 — Taller: comparar riesgos entre dominios](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md)) son: Las definiciones son operativas para el taller. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos salvo el orden de listado de empates. Las puntuaciones, los riesgos y los controles son un juicio ilustrativo del autor, no una medición de ningún dominio, evaluador ni organización. El proyecto final aplica este método a un dominio elegido.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-169](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md), [SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cobertura de controles](../c/cobertura-de-controles.md), [Control](../c/control.md), [Declaración de conformidad](../d/declaracion-de-conformidad.md), [Ejemplo ancla](../e/ejemplo-ancla.md), [Kappa de Cohen](../k/kappa-de-cohen.md), [Kappa ponderado](../k/kappa-ponderado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-180 — Proyecto: prototipo accesible evaluado con usuarios](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.
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

[↑ Glosario](../../README.md) · [← Actualización y rollback](./actualizacion-y-rollback.md) · [Acuse →](./acuse.md)
