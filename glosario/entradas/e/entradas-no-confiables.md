# Entradas no confiables

[↑ Glosario](../../README.md) · [← Entradas de frontera](./entradas-de-frontera.md) · [Entrega al menos una vez →](./entrega-al-menos-una-vez.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Una entrada del contexto puede convertirse en código.

Es uno de los temas de [SE-478 — Riesgos de CI y dependencias comprometidas](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md), donde se enseña como «Entradas no confiables».

## Por qué importa

En [SE-478 — Riesgos de CI y dependencias comprometidas](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md), el tema «Entradas no confiables» importa porque una entrada del contexto puede convertirse en código.

En [SE-491 — Taller: endurecer un pipeline vulnerable](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md), el tema «Entradas no confiables» importa porque el texto de una solicitud de integración es una entrada del atacante.

## Cómo funciona

Según [SE-478 — Riesgos de CI y dependencias comprometidas](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md):

Traslada el análisis a otra plataforma de CI (GitLab, Jenkins, un sistema propio): cambia la sintaxis de permisos y de secretos y conserva el procedimiento de listar activos y entradas no confiables, fijar las dependencias del CI, minimizar el alcance, evaluar el escáner con mutaciones y preparar la respuesta. La transferencia está lograda cuando puedes decir cuál es en la nueva plataforma el equivalente a `pull_request_target` y qué runner conserva estado.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-478 — Riesgos de CI y dependencias comprometidas](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md):

El flujo de publicación de la API de entregas se reescribe con cuatro reglas. Todas las acciones se fijan a un SHA y un trabajo semanal propone las actualizaciones como solicitudes revisables. El permiso por defecto es vacío y cada trabajo declara el suyo: las pruebas leen el contenido, la publicación escribe solo la etiqueta del release.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-478 — Riesgos de CI y dependencias comprometidas](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md)) son:

- **Una acción cambia de comportamiento sin cambios en el repositorio** — causa: referencia por etiqueta. Corrección: fijar a un SHA y revisar las actualizaciones.
- **Un título de solicitud ejecuta órdenes** — causa: interpolación del contexto en `run`. Corrección: pasar el dato como variable de entorno.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Traslada el análisis a otra plataforma de CI (GitLab, Jenkins, un sistema propio): cambia la sintaxis de permisos y de secretos y conserva el procedimiento de listar activos y entradas no confiables, fijar las dependencias del CI, minimizar el alcance, evaluar el escáner con mutaciones y preparar la respuesta. ([SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-477](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Acción de terceros](../a/accion-de-terceros.md), [CI](../c/ci.md), [Evento privilegiado](./evento-privilegiado.md), [Fijar por SHA](../f/fijar-por-sha.md), [Hallazgo](../h/hallazgo.md), [Inyección de scripts](../i/inyeccion-de-scripts.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-478 — Riesgos de CI y dependencias comprometidas](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.
- [SE-491 — Taller: endurecer un pipeline vulnerable](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (17 clases más lo mencionan; las que más):

[SE-011](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md), [SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md), [SE-061](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md), [SE-062](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md), [SE-063](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md), [SE-064](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md), [SE-065](../../../classes/part-05-fundamentos-de-programacion/se-065-errores-excepciones-y-resultados-explicitos/README.md), [SE-066](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GitHub Docs: Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions) — endurecimiento de flujos; autoridad: documentación oficial de GitHub.
- [GitHub Docs: Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) — riesgos de disparadores y de interpolación; autoridad: documentación oficial de GitHub.
- [OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/) — catálogo de riesgos; autoridad: OWASP.
- [NVD: CVE-2025-30066](https://nvd.nist.gov/vuln/detail/CVE-2025-30066) — acción comprometida mediante etiquetas movidas; autoridad: NIST National Vulnerability Database.
- [NVD: CVE-2024-3094](https://nvd.nist.gov/vuln/detail/CVE-2024-3094) — código malicioso en los tarballs de xz; autoridad: NIST National Vulnerability Database.

---

[↑ Glosario](../../README.md) · [← Entradas de frontera](./entradas-de-frontera.md) · [Entrega al menos una vez →](./entrega-al-menos-una-vez.md)
