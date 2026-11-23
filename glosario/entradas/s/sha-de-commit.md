# SHA de commit

[↑ Glosario](../../README.md) · [← Severidad](./severidad.md) · [Shell →](./shell.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md)

## Definición

Identificador inmutable de un estado del repositorio; fijar una acción a él evita que la referencia cambie.

Definición de trabajo de [SE-478 — Riesgos de CI y dependencias comprometidas](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md).

## Por qué importa

La clase donde se define, [SE-478 — Riesgos de CI y dependencias comprometidas](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md), existe con este propósito: la clase existe para que veas el sistema de integración continua (CI) como lo que es para un atacante: un lugar donde se ejecuta código con credenciales.

## Cómo funciona

Según [SE-478 — Riesgos de CI y dependencias comprometidas](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md):

Las **acciones** reutilizables de terceros son código que corre dentro de tu flujo con acceso a su entorno. Referenciarlas por una etiqueta de versión (`@v4`) es confiar en que nadie mueva esa etiqueta, y las etiquetas de un repositorio las controla quien tiene permiso de escritura en él; el incidente de la acción `tj-actions/changed-files` es el ejemplo: las etiquetas v1 a v45.0.7 fueron modificadas para apuntar a un commit malicioso. Fijar la acción a un **SHA de commit completo** hace inmutable la referencia; el control no impide que el SHA sea malicioso desde el principio ni que una acción fijada descargue código mutable en su ejecución.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-478 — Riesgos de CI y dependencias comprometidas](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md):

El flujo de publicación de la API de entregas se reescribe con cuatro reglas. Todas las acciones se fijan a un SHA y un trabajo semanal propone las actualizaciones como solicitudes revisables. El permiso por defecto es vacío y cada trabajo declara el suyo: las pruebas leen el contenido, la publicación escribe solo la etiqueta del release.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-478 — Riesgos de CI y dependencias comprometidas](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md)) son:

- **Una acción cambia de comportamiento sin cambios en el repositorio** — causa: referencia por etiqueta. Corrección: fijar a un SHA y revisar las actualizaciones.
- **Un título de solicitud ejecuta órdenes** — causa: interpolación del contexto en `run`. Corrección: pasar el dato como variable de entorno.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Fijar la acción a un **SHA de commit completo** hace inmutable la referencia; el control no impide que el SHA sea malicioso desde el principio ni que una acción fijada descargue código mutable en su ejecución. ([SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-477](../../../classes/part-39-build-release-y-cadena-de-suministro/se-477-instaladores-paquetes-y-actualizaciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Referencia](../r/referencia.md), [Acción de terceros](../a/accion-de-terceros.md), [CI](../c/ci.md), [Inyección de scripts](../i/inyeccion-de-scripts.md), [Mínimo privilegio](../m/minimo-privilegio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-478 — Riesgos de CI y dependencias comprometidas](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md) — [Parte 39](../../../classes/part-39-build-release-y-cadena-de-suministro/README.md), Build, release y cadena de suministro.

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

[↑ Glosario](../../README.md) · [← Severidad](./severidad.md) · [Shell →](./shell.md)
