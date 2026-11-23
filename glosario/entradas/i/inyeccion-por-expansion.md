# Inyección por expansión

[↑ Glosario](../../README.md) · [← Inyección indirecta de instrucciones](./inyeccion-indirecta-de-instrucciones.md) · [IR →](./ir.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Ejecución de texto de un tercero como código porque se sustituyó en un script antes de que el intérprete lo leyera.

Definición de trabajo de [SE-491 — Taller: endurecer un pipeline vulnerable](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md).

## Por qué importa

La clase donde se define, [SE-491 — Taller: endurecer un pipeline vulnerable](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md), existe con este propósito: el taller existe para que practiques lo que las clases anteriores explicaron por separado: tomar una canalización que funciona y es insegura, encontrar cada defecto con un verificador, corregirlo con el cambio más pequeño posible y demostrar con una prueba que el cambio hizo lo que decía.

## Cómo funciona

[SE-491 — Taller: endurecer un pipeline vulnerable](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el taller de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-491 — Taller: endurecer un pipeline vulnerable](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md):

El equipo de la API de entregas aplica el taller a su canalización real. Primero ejecuta el verificador sobre todos los flujos de trabajo y obtiene hallazgos en tres de once. Para cada hallazgo abre un cambio pequeño con su prueba: la acción fijada por SHA (con un comentario que indica la versión legible), los permisos declarados por trabajo, el evento cambiado a `pull_request` y el título pasado como variable. El script descargado se sustituye por uno versionado en el repositorio que verifica la huella de lo que descarga.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-491 — Taller: endurecer un pipeline vulnerable](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md)) son:

- **Un título o rama ejecuta código en el flujo** — causa: expresión insertada en un script. Corrección: variable de entorno intermedia.
- **Una solicitud externa accede a secretos** — causa: evento privilegiado más código del cambio. Corrección: `pull_request` o dos flujos separados.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-491 — Taller: endurecer un pipeline vulnerable](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md)) son: Las definiciones son operativas para el taller de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md), [SE-484](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md), [SE-490](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento privilegiado](../e/evento-privilegiado.md), [Fijar por SHA](../f/fijar-por-sha.md), [Hallazgo](../h/hallazgo.md), [Mínimo privilegio](../m/minimo-privilegio.md).
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

[↑ Glosario](../../README.md) · [← Inyección indirecta de instrucciones](./inyeccion-indirecta-de-instrucciones.md) · [IR →](./ir.md)
