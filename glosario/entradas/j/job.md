# Job

[↑ Glosario](../../README.md) · [← JIT](./jit.md) · [Job stories →](./job-stories.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Unidad de trabajo de una canalización que se ejecuta en un entorno aislado y puede depender de otros jobs.

Definición de trabajo de [SE-482 — Pipelines, jobs, matrices y cachés](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md).

## Por qué importa

En [SE-482 — Pipelines, jobs, matrices y cachés](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md), el tema «Canalización como grafo» importa porque sin el grafo no se sabe qué acelerar: acortar un job fuera del camino crítico no cambia la duración.

## Cómo funciona

Según [SE-482 — Pipelines, jobs, matrices y cachés](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md):

Un **job** es una unidad de trabajo que se ejecuta en un ejecutor aislado, con su propio sistema de archivos, de modo que nada de lo que un job deja en disco está disponible para otro salvo que se transmita de forma explícita. Un **paso** es una instrucción dentro de un job y comparte con sus hermanos el mismo entorno. Las dependencias entre jobs (`needs` en la sintaxis de GitHub Actions) forman un **grafo dirigido sin ciclos**: un job empieza cuando han terminado todos los que necesita. Esa estructura es la que determina qué puede ejecutarse a la vez y qué debe esperar.

Según [SE-482 — Pipelines, jobs, matrices y cachés](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md):

El equipo de la API de entregas dibuja su canalización con las duraciones reales de los últimos treinta días. El camino crítico pasa por compilar y por las pruebas e2e: los 22 minutos no bajarán comprando ejecutores. Deciden dividir e2e en tres grupos que corren a la vez (con lo que el camino se acorta a unos 14 minutos, a costa de tres arranques más) y mover la documentación a una etapa posterior que no bloquea. Para la matriz, la compatibilidad declarada es Linux, Windows y macOS, Python 3.10 a 3.13 y tres bases de datos; el producto completo son 36 jobs, y optan por doce combinaciones que cubren todas las parejas más la configuración de producción completa en cada ejecución nocturna.

## Ejemplo

Ejemplo de [SE-482 — Pipelines, jobs, matrices y cachés](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md) (sección «Ejemplo profesional»):

El equipo de la API de entregas dibuja su canalización con las duraciones reales de los últimos treinta días. El camino crítico pasa por compilar y por las pruebas e2e: los 22 minutos no bajarán comprando ejecutores. Deciden dividir e2e en tres grupos que corren a la vez (con lo que el camino se acorta a unos 14 minutos, a costa de tres arranques más) y mover la documentación a una etapa posterior que no bloquea.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Muchos jobs pequeños y la duración sube** — causa: el arranque domina la duración de cada job. Corrección: fundir jobs que comparten preparación. ([SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md))
- **Un artefacto distinto del probado llega a producción** — causa: se reconstruyó en otro job. Corrección: pasar el artefacto por resumen, no reconstruirlo. ([SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un **job** es una unidad de trabajo que se ejecuta en un ejecutor aislado, con su propio sistema de archivos, de modo que nada de lo que un job deja en disco está disponible para otro salvo que se transmita de forma explícita. ([SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md))
- Dividir ayuda mientras el camino crítico se acorta más de lo que el arranque suma; dividir un job que ya está fuera del camino crítico solo aumenta el costo. ([SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Entorno aislado](../e/entorno-aislado.md), [Entorno](../e/entorno.md), [Trabajo](../t/trabajo.md), [Camino crítico](../c/camino-critico.md), [Clave de caché](../c/clave-de-cache.md), [Cobertura de parejas](../c/cobertura-de-parejas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-482 — Pipelines, jobs, matrices y cachés](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GitHub Actions: sintaxis de flujos de trabajo](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) — jobs, dependencias y matrices; autoridad: documentación de GitHub.
- [GitHub Actions: variaciones de un job](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations) — matrices de combinaciones; autoridad: documentación de GitHub.
- [GitHub Actions: dependencias en caché](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching) — claves, respaldos y restricciones de la caché; autoridad: documentación de GitHub.
- [NIST SP 800-142: Practical Combinatorial Testing](https://csrc.nist.gov/pubs/sp/800/142/final) — pruebas combinatorias y cobertura de parejas; autoridad: NIST.
- [Graham, «Bounds on Multiprocessing Timing Anomalies»](https://doi.org/10.1137/0117039) — anomalías de planificación con precedencias (SIAM Journal on Applied Mathematics, 1969); autoridad: artículo con DOI verificado en Crossref.

---

[↑ Glosario](../../README.md) · [← JIT](./jit.md) · [Job stories →](./job-stories.md)
