# Cobertura de parejas

[↑ Glosario](../../README.md) · [← Cobertura de documentación](./cobertura-de-documentacion.md) · [Cobertura de pares →](./cobertura-de-pares.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Conjunto de combinaciones en el que cada pareja de niveles de dos factores aparece al menos una vez.

Definición de trabajo de [SE-482 — Pipelines, jobs, matrices y cachés](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md).

## Por qué importa

La clase donde se define, [SE-482 — Pipelines, jobs, matrices y cachés](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md), existe con este propósito: la clase existe para que diseñes una canalización como un grafo de trabajos con dependencias, tiempos y costos, y no como una lista de pasos copiada de una plantilla.

## Cómo funciona

Según [SE-482 — Pipelines, jobs, matrices y cachés](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md):

Una **matriz** genera un job por cada combinación de valores de varios factores (sistema operativo, versión del lenguaje, base de datos). El número de combinaciones es el producto de los niveles: tres sistemas, cuatro versiones y tres bases dan 36 jobs. Cada factor adicional multiplica el costo. La pregunta correcta no es «¿qué combinaciones existen?» sino «¿qué defectos esperamos y de cuántos factores dependen?». La evidencia empírica recogida por el NIST indica que la mayoría de los defectos dependen de uno o dos factores, lo que justifica probar **todas las parejas** de niveles en lugar de todas las combinaciones. Una cobertura de parejas puede lograrse con muy pocas ejecuciones (la tabla de abajo la obtiene con 12 de 36).

Según [SE-482 — Pipelines, jobs, matrices y cachés](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md):

Traslada el análisis a otra canalización (por ejemplo, la de una aplicación móvil con compilaciones para dos sistemas): cambia los jobs, sus duraciones y los factores de la matriz, y conserva el procedimiento de calcular el camino crítico, elegir cobertura de parejas y definir la clave por la entrada. La transferencia está lograda cuando puedes decir qué eslabón del camino acelerar primero y qué combinación quedaría sin probar, no cuando el grafo se parece al de la plataforma.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-482 — Pipelines, jobs, matrices y cachés](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md):

El equipo de la API de entregas dibuja su canalización con las duraciones reales de los últimos treinta días. El camino crítico pasa por compilar y por las pruebas e2e: los 22 minutos no bajarán comprando ejecutores. Deciden dividir e2e en tres grupos que corren a la vez (con lo que el camino se acorta a unos 14 minutos, a costa de tres arranques más) y mover la documentación a una etapa posterior que no bloquea.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La matriz triplica el costo cada trimestre** — causa: se añaden factores sin retirar ninguno. Corrección: cobertura de parejas y exclusiones con motivo. ([SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Traslada el análisis a otra canalización (por ejemplo, la de una aplicación móvil con compilaciones para dos sistemas): cambia los jobs, sus duraciones y los factores de la matriz, y conserva el procedimiento de calcular el camino crítico, elegir cobertura de parejas y definir la clave por la entrada. ([SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Al menos una vez](../a/al-menos-una-vez.md), [Combinación](./combinacion.md), [Conjunto](./conjunto.md), [Camino crítico](./camino-critico.md), [Clave de caché](./clave-de-cache.md), [Job](../j/job.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-482 — Pipelines, jobs, matrices y cachés](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-142: Practical Combinatorial Testing](https://csrc.nist.gov/pubs/sp/800/142/final) — pruebas combinatorias y cobertura de parejas; autoridad: NIST.
- [GitHub Actions: sintaxis de flujos de trabajo](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) — jobs, dependencias y matrices; autoridad: documentación de GitHub.
- [GitHub Actions: dependencias en caché](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching) — claves, respaldos y restricciones de la caché; autoridad: documentación de GitHub.
- [GitHub Actions: variaciones de un job](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations) — matrices de combinaciones; autoridad: documentación de GitHub.
- [Graham, «Bounds on Multiprocessing Timing Anomalies»](https://doi.org/10.1137/0117039) — anomalías de planificación con precedencias (SIAM Journal on Applied Mathematics, 1969); autoridad: artículo con DOI verificado en Crossref.

---

[↑ Glosario](../../README.md) · [← Cobertura de documentación](./cobertura-de-documentacion.md) · [Cobertura de pares →](./cobertura-de-pares.md)
