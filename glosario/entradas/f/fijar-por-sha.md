# Fijar por SHA

[↑ Glosario](../../README.md) · [← Fijación de sesión](./fijacion-de-sesion.md) · [Filtro →](./filtro.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Referenciar una acción por el identificador completo de un contenido en lugar de una etiqueta que puede moverse.

Definición de trabajo de [SE-491 — Taller: endurecer un pipeline vulnerable](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md).

## Por qué importa

La clase donde se define, [SE-491 — Taller: endurecer un pipeline vulnerable](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md), existe con este propósito: el taller existe para que practiques lo que las clases anteriores explicaron por separado: tomar una canalización que funciona y es insegura, encontrar cada defecto con un verificador, corregirlo con el cambio más pequeño posible y demostrar con una prueba que el cambio hizo lo que decía.

## Cómo funciona

Según [SE-491 — Taller: endurecer un pipeline vulnerable](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md):

Una acción de terceros es código que se ejecuta dentro de tu flujo. Se referencia por una **etiqueta** (`@v4`), que es un puntero que su autor puede mover, o por un **SHA completo**, que identifica un contenido. Fijar por SHA hace que un cambio posterior en el repositorio de la acción no llegue a tu canalización sin que lo decidas. El **token** del flujo tiene permisos configurables; con `write-all` cada trabajo recibe escritura sobre todos los ámbitos, incluidos los que no necesita. Reducir los permisos al mínimo por trabajo (`contents: read` para quien solo lee) limita lo que puede hacer una acción comprometida. Es la misma lógica del mínimo privilegio que se aplicó al rol de la nube en `SE-484`.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-491 — Taller: endurecer un pipeline vulnerable](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md):

El equipo de la API de entregas aplica el taller a su canalización real. Primero ejecuta el verificador sobre todos los flujos de trabajo y obtiene hallazgos en tres de once. Para cada hallazgo abre un cambio pequeño con su prueba: la acción fijada por SHA (con un comentario que indica la versión legible), los permisos declarados por trabajo, el evento cambiado a `pull_request` y el título pasado como variable. El script descargado se sustituye por uno versionado en el repositorio que verifica la huella de lo que descarga.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una acción cambia de comportamiento sin aviso** — causa: referencia por etiqueta. Corrección: fijar por SHA y actualizar con un cambio revisado. ([SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Fijar por SHA hace que un cambio posterior en el repositorio de la acción no llegue a tu canalización sin que lo decidas. ([SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md), [SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md), [SE-490](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Etiqueta](../e/etiqueta.md), [Evento privilegiado](../e/evento-privilegiado.md), [Hallazgo](../h/hallazgo.md), [Inyección por expansión](../i/inyeccion-por-expansion.md), [Mínimo privilegio](../m/minimo-privilegio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-491 — Taller: endurecer un pipeline vulnerable](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GitHub Actions: uso seguro](https://docs.github.com/en/actions/reference/security/secure-use) — fijar acciones, variables intermedias y permisos; autoridad: documentación de GitHub.
- [GitHub Security Lab: preventing pwn requests](https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/) — riesgo de `pull_request_target` con código del cambio; autoridad: GitHub Security Lab.
- [GitHub Actions: eventos que activan flujos](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows) — contexto de ejecución de cada evento; autoridad: documentación de GitHub.
- [OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/) — catálogo de riesgos de canalizaciones; autoridad: OWASP.
- [OpenSSF Scorecard](https://github.com/ossf/scorecard) — auditoría automática de prácticas de seguridad de repositorios; autoridad: OpenSSF.

---

[↑ Glosario](../../README.md) · [← Fijación de sesión](./fijacion-de-sesion.md) · [Filtro →](./filtro.md)
