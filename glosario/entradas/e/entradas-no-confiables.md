# Entradas no confiables

[↑ Glosario](../../README.md) · [← Entradas de frontera](./entradas-de-frontera.md) · [Entrega al menos una vez →](./entrega-al-menos-una-vez.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

En una canalización de integración continua, una **entrada no confiable** es un dato del contexto del evento que puede convertirse en código si el flujo lo interpreta mal ([SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md)): el título de una solicitud, el nombre de una rama, el cuerpo de un comentario.

## Por qué importa

Quien controla esos datos puede ser una persona externa. Si el flujo los interpola dentro de una orden, ejecutan lo que esa persona escribió, con los permisos del flujo.

## Cómo funciona

[SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md) trata el análisis de seguridad de una canalización como un procedimiento: listar los **activos** (secretos, permisos) y las **entradas no confiables**, fijar las dependencias del CI, minimizar el alcance, evaluar el escáner con mutaciones y preparar la respuesta. Dos errores típicos: interpolar el contexto directamente en un paso `run`, y referenciar acciones por etiqueta movible.

## Ejemplo

Un flujo hace `echo "${{ github.event.pull_request.title }}"` dentro de un `run`; un título con comillas y órdenes se ejecuta. La corrección es pasar el dato como variable de entorno y usarlo como variable, no como texto de la orden.

## Errores y confusiones comunes

- **Un título de solicitud ejecuta órdenes.** Interpolación del contexto en `run`; pasar el dato como variable de entorno.
- **Una acción cambia de comportamiento sin cambios en el repositorio.** Referencia por etiqueta; fijar a un SHA y revisar las actualizaciones.

## Límites y cuándo no aplica

La sintaxis es de una plataforma concreta; en GitLab o Jenkins cambian permisos y secretos, pero se conserva el procedimiento. [SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md) pide poder decir cuál es en la nueva plataforma el equivalente a `pull_request_target` y qué runner conserva estado.

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
