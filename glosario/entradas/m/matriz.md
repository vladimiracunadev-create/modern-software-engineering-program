# Matriz

[↑ Glosario](../../README.md) · [← Máscara](./mascara.md) · [Matriz de autorización →](./matriz-de-autorizacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

En integración continua, una **matriz** genera un job por cada combinación de valores de varios factores, como sistema operativo, versión del lenguaje y base de datos ([SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md)).

## Por qué importa

El número de combinaciones es el producto de los niveles: tres sistemas, cuatro versiones y tres bases dan 36 jobs. Cada factor adicional multiplica el costo. La pregunta correcta no es «¿qué combinaciones existen?» sino «¿qué defectos esperamos y de cuántos factores dependen?».

## Cómo funciona

[SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md) apoya la decisión en evidencia empírica del NIST: la mayoría de los defectos de configuración dependen de pocos factores a la vez, por lo que la **cobertura de parejas** (cada par de valores aparece al menos una vez) reduce muchísimo el número de jobs sin perder casi detección. Se combinan exclusiones con motivo.

## Ejemplo

El equipo de la API de entregas declara su compatibilidad y reemplaza la matriz completa por una de cobertura de parejas, calculando antes el camino crítico de la canalización.

## Errores y confusiones comunes

**La matriz triplica el costo cada trimestre.** Se añaden factores sin retirar ninguno; cobertura de parejas y exclusiones con motivo.

## Límites y cuándo no aplica

En el experimento, los defectos son un nivel por factor elegido al azar, algo mucho más regular que los reales; una interacción que depende de una combinación inusual (una versión con una base en un sistema concretos) la ve solo la matriz completa.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Combinación](../c/combinacion.md), [Generación](../g/generacion.md), [Valor](../v/valor.md), [Camino crítico](../c/camino-critico.md), [Clave de caché](../c/clave-de-cache.md), [Cobertura de parejas](../c/cobertura-de-parejas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-482 — Pipelines, jobs, matrices y cachés](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (123 clases más lo mencionan; las que más):

[SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md), [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md), [SE-534](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md), [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md), [SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md), [SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md).

**Aparece en los casos de estudio:** [Instagram](../../../casos/exito/instagram.md).

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

[↑ Glosario](../../README.md) · [← Máscara](./mascara.md) · [Matriz de autorización →](./matriz-de-autorizacion.md)
