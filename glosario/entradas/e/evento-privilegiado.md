# Evento privilegiado

[↑ Glosario](../../README.md) · [← Evento de uso](./evento-de-uso.md) · [Evento tardío →](./evento-tardio.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Evento de activación cuyo flujo se ejecuta con secretos y permisos de escritura aunque lo origine un tercero.

Definición de trabajo de [SE-491 — Taller: endurecer un pipeline vulnerable](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md).

## Por qué importa

En [SE-491 — Taller: endurecer un pipeline vulnerable](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md), el tema «Eventos privilegiados» importa porque `pull_request_target` ejecuta con secretos; mezclarlo con el código del cambio es la combinación peligrosa.

## Cómo funciona

Según [SE-491 — Taller: endurecer un pipeline vulnerable](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md), en la sección «Eventos privilegiados»:

El evento `pull_request` ejecuta el flujo de trabajo del cambio con permisos reducidos y sin secretos cuando viene de una bifurcación. El evento `pull_request_target` ejecuta el flujo de la **rama base**, con acceso a secretos y permisos de escritura, pensado para tareas como etiquetar o comentar. El peligro aparece al combinarlo con una descarga del código del cambio (`ref` apuntando al SHA de la cabeza de la solicitud): se ejecuta código no revisado con privilegios completos. El patrón se conoce como «solicitud pwn». La defensa es no descargar ni ejecutar código del cambio en un evento privilegiado, o dividir el trabajo en dos flujos: uno sin privilegios que construye y prueba, y otro privilegiado que solo consume el resultado como datos.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-491 — Taller: endurecer un pipeline vulnerable](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md):

El equipo de la API de entregas aplica el taller a su canalización real. Primero ejecuta el verificador sobre todos los flujos de trabajo y obtiene hallazgos en tres de once. Para cada hallazgo abre un cambio pequeño con su prueba: la acción fijada por SHA (con un comentario que indica la versión legible), los permisos declarados por trabajo, el evento cambiado a `pull_request` y el título pasado como variable. El script descargado se sustituye por uno versionado en el repositorio que verifica la huella de lo que descarga.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una solicitud externa accede a secretos** — causa: evento privilegiado más código del cambio. Corrección: `pull_request` o dos flujos separados. ([SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La defensa es no descargar ni ejecutar código del cambio en un evento privilegiado, o dividir el trabajo en dos flujos: uno sin privilegios que construye y prueba, y otro privilegiado que solo consume el resultado como datos. ([SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md), [SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md), [SE-490](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Activación](../a/activacion.md), [Evento](./evento.md), [Flujo](../f/flujo.md), [Permiso](../p/permiso.md), [Fijar por SHA](../f/fijar-por-sha.md), [Hallazgo](../h/hallazgo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-491 — Taller: endurecer un pipeline vulnerable](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Eventos privilegiados».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GitHub Actions: uso seguro](https://docs.github.com/en/actions/reference/security/secure-use) — fijar acciones, variables intermedias y permisos; autoridad: documentación de GitHub.
- [GitHub Security Lab: preventing pwn requests](https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/) — riesgo de `pull_request_target` con código del cambio; autoridad: GitHub Security Lab.
- [GitHub Actions: eventos que activan flujos](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows) — contexto de ejecución de cada evento; autoridad: documentación de GitHub.
- [OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/) — catálogo de riesgos de canalizaciones; autoridad: OWASP.
- [OpenSSF Scorecard](https://github.com/ossf/scorecard) — auditoría automática de prácticas de seguridad de repositorios; autoridad: OpenSSF.

---

[↑ Glosario](../../README.md) · [← Evento de uso](./evento-de-uso.md) · [Evento tardío →](./evento-tardio.md)
