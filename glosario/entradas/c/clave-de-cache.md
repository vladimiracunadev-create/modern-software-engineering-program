# Clave de caché

[↑ Glosario](../../README.md) · [← Clave caliente](./clave-caliente.md) · [Clave de flota →](./clave-de-flota.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Identificador que decide cuándo una entrada guardada se considera la misma entrada.

Definición de trabajo de [SE-482 — Pipelines, jobs, matrices y cachés](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md): Valor que identifica una respuesta guardada e incluye todo lo que la hace variar.

## Por qué importa

La clase donde se define, [SE-482 — Pipelines, jobs, matrices y cachés](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md), existe con este propósito: la clase existe para que diseñes una canalización como un grafo de trabajos con dependencias, tiempos y costos, y no como una lista de pasos copiada de una plantilla.

## Cómo funciona

Según [SE-482 — Pipelines, jobs, matrices y cachés](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md):

**Cómo leer la figura.** Cada grupo es una clave de caché, con su instalación media entre paréntesis; las barras son el porcentaje de aciertos (verde), de restauraciones parciales (dorada) y de entorno obsoleto (roja). Mira primero la barra roja de la clave fija: es la más larga y la que acompaña al mejor tiempo. **Dónde deja de valer:** el modelo supone que un entorno obsoleto es siempre un error, cuando a veces pasa las pruebas sin que nadie lo note; esa invisibilidad es el peligro. Los tiempos de 180, 45 y 8 segundos son supuestos y la proporción de cambios del archivo bloqueado depende del proyecto.

Según [SE-482 — Pipelines, jobs, matrices y cachés](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** la rama pasa y la troncal falla con un error de versión de una biblioteca. **Hipótesis rivales:** (a) la prueba es inestable; (b) hay una diferencia de sistema entre ejecutores; (c) el entorno restaurado de la caché no coincide con el archivo bloqueado. **Prueba:** imprime el resumen del archivo bloqueado y el de la clave de caché en cada ejecución; si no coinciden y la clave es la misma, la causa es la caché. **Conclusión:** la clave fija trataba entradas distintas como una sola; una caché solo es segura si la clave refleja la entrada.

## Ejemplo

Ejemplo de [SE-482 — Pipelines, jobs, matrices y cachés](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md) (sección «Caso conductor»):

La canalización de la API de entregas es el caso conductor de la [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md). Esta clase deja el segundo artefacto: el grafo de jobs con su camino crítico, la matriz y la clave de caché. `SE-483` decidirá qué comprobaciones bloquean la integración y en qué orden, y `SE-484` dará a esos jobs credenciales de corta vida. Cambia después un solo dato, el arranque por job, y observa si sigue valiendo la pena dividir un job.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-482 — Pipelines, jobs, matrices y cachés](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md)) son:

- **La canalización no baja de un mínimo al añadir ejecutores** — causa: el camino crítico ya está alcanzado. Corrección: calcular el camino crítico y acortar su eslabón más largo.
- **Muchos jobs pequeños y la duración sube** — causa: el arranque domina la duración de cada job. Corrección: fundir jobs que comparten preparación.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Cómo leer la figura.** Cada grupo es una clave de caché, con su instalación media entre paréntesis; las barras son el porcentaje de aciertos (verde), de restauraciones parciales (dorada) y de entorno obsoleto (roja). ([SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), [SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Valor](../v/valor.md), [429](../0-9/429.md), [Camino crítico](./camino-critico.md), [Cobertura de parejas](./cobertura-de-parejas.md), [Cubeta de fichas](./cubeta-de-fichas.md), [Degradación elegante](../d/degradacion-elegante.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-482 — Pipelines, jobs, matrices y cachés](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-410](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md), [SE-042](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md), [SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GitHub Actions: sintaxis de flujos de trabajo](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) — jobs, dependencias y matrices; autoridad: documentación de GitHub.
- [GitHub Actions: dependencias en caché](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching) — claves, respaldos y restricciones de la caché; autoridad: documentación de GitHub.
- [GitHub Actions: variaciones de un job](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations) — matrices de combinaciones; autoridad: documentación de GitHub.
- [NIST SP 800-142: Practical Combinatorial Testing](https://csrc.nist.gov/pubs/sp/800/142/final) — pruebas combinatorias y cobertura de parejas; autoridad: NIST.
- [Graham, «Bounds on Multiprocessing Timing Anomalies»](https://doi.org/10.1137/0117039) — anomalías de planificación con precedencias (SIAM Journal on Applied Mathematics, 1969); autoridad: artículo con DOI verificado en Crossref.

---

[↑ Glosario](../../README.md) · [← Clave caliente](./clave-caliente.md) · [Clave de flota →](./clave-de-flota.md)
