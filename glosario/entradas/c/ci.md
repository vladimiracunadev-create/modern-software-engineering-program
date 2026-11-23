# CI

[↑ Glosario](../../README.md) · [← Churn](./churn.md) · [Ciclo →](./ciclo.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Sistema que construye y prueba el código de forma automática ante cada cambio.

Definición de trabajo de [SE-478 — Riesgos de CI y dependencias comprometidas](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md).

## Por qué importa

En [SE-478 — Riesgos de CI y dependencias comprometidas](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md), el tema «El CI como objetivo» importa porque concentra permisos y secretos.

## Cómo funciona

Según [SE-478 — Riesgos de CI y dependencias comprometidas](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md):

Un flujo de CI es un programa que ejecuta órdenes en una máquina efímera con un conjunto de credenciales: un **token** del repositorio con permisos de lectura o escritura, **secretos** inyectados como variables (claves de despliegue, tokens de publicación), acceso a una **caché** compartida y, en el paso de publicación, la clave que firma. Esa concentración lo convierte en un objetivo más rentable que el código de la aplicación: un solo compromiso permite alterar el repositorio, publicar un release con la firma legítima o robar credenciales que sirven para otros sistemas. Y la mayoría de los pasos ejecutan código escrito por otras personas (las acciones, las herramientas, las dependencias instaladas), de modo que el CI también es una cadena de suministro dentro de la cadena de suministro.

Según [SE-478 — Riesgos de CI y dependencias comprometidas](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md):

Traslada el análisis a otra plataforma de CI (GitLab, Jenkins, un sistema propio): cambia la sintaxis de permisos y de secretos y conserva el procedimiento de listar activos y entradas no confiables, fijar las dependencias del CI, minimizar el alcance, evaluar el escáner con mutaciones y preparar la respuesta. La transferencia está lograda cuando puedes decir cuál es en la nueva plataforma el equivalente a `pull_request_target` y qué runner conserva estado.

## Ejemplo

Ejemplo de [SE-478 — Riesgos de CI y dependencias comprometidas](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md) (sección «Caso conductor»):

La API de entregas es el caso conductor de la [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md). Esta clase deja el décimo artefacto: un modelo de amenazas del CI con permisos mínimos, dependencias fijadas, un escáner evaluado y un plan de respuesta. `SE-479` pondrá a prueba la cadena completa en un taller: verificar la procedencia de un release. Cambia después un solo dato, el permiso por defecto del token, y observa cuánto crece el alcance de un paso comprometido.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-478 — Riesgos de CI y dependencias comprometidas](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md)) son:

- **Una acción cambia de comportamiento sin cambios en el repositorio** — causa: referencia por etiqueta. Corrección: fijar a un SHA y revisar las actualizaciones.
- **Un título de solicitud ejecuta órdenes** — causa: interpolación del contexto en `run`. Corrección: pasar el dato como variable de entorno.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Y la mayoría de los pasos ejecutan código escrito por otras personas (las acciones, las herramientas, las dependencias instaladas), de modo que el CI también es una cadena de suministro dentro de la cadena de suministro. ([SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md))
- Traslada el análisis a otra plataforma de CI (GitLab, Jenkins, un sistema propio): cambia la sintaxis de permisos y de secretos y conserva el procedimiento de listar activos y entradas no confiables, fijar las dependencias del CI, minimizar el alcance, evaluar el escáner con mutaciones y preparar la respuesta. ([SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-477](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Acción de terceros](../a/accion-de-terceros.md), [Inyección de scripts](../i/inyeccion-de-scripts.md), [Mínimo privilegio](../m/minimo-privilegio.md), [SHA de commit](../s/sha-de-commit.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-478 — Riesgos de CI y dependencias comprometidas](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «integración continua».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/) — catálogo de riesgos; autoridad: OWASP.
- [GitHub Docs: Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions) — endurecimiento de flujos; autoridad: documentación oficial de GitHub.
- [GitHub Docs: Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) — riesgos de disparadores y de interpolación; autoridad: documentación oficial de GitHub.
- [NVD: CVE-2025-30066](https://nvd.nist.gov/vuln/detail/CVE-2025-30066) — acción comprometida mediante etiquetas movidas; autoridad: NIST National Vulnerability Database.
- [NVD: CVE-2024-3094](https://nvd.nist.gov/vuln/detail/CVE-2024-3094) — código malicioso en los tarballs de xz; autoridad: NIST National Vulnerability Database.

---

[↑ Glosario](../../README.md) · [← Churn](./churn.md) · [Ciclo →](./ciclo.md)
