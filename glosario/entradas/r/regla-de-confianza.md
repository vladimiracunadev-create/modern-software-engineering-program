# Regla de confianza

[↑ Glosario](../../README.md) · [← Regla](./regla.md) · [Regla de decisión →](./regla-de-decision.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Condición que el receptor aplica a las notificaciones del token para decidir si entrega una credencial.

Definición de trabajo de [SE-484 — Credenciales efímeras y OIDC](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md).

## Por qué importa

La clase donde se define, [SE-484 — Credenciales efímeras y OIDC](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md), existe con este propósito: la clase existe para que sustituyas la credencial que alguien copió en un secreto del repositorio por una identidad que la canalización demuestra en cada ejecución y que el proveedor cambia por una credencial de minutos.

## Cómo funciona

Según [SE-484 — Credenciales efímeras y OIDC](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md):

El esquema general, que GitHub Actions implementa sobre OpenID Connect, tiene cuatro pasos. El job, si tiene permiso para ello, pide al emisor de la plataforma de integración continua un **token de identidad**: un documento firmado que dice quién es (repositorio, rama, entorno, flujo de trabajo), quién lo emitió (`iss`), a quién va dirigido (`aud`), hasta cuándo vale (`exp`) y desde cuándo (`nbf`). El job presenta ese token al proveedor de la nube. El proveedor lo valida (firma con las claves públicas del emisor, vigencia, emisor y audiencia esperados) y comprueba la **regla de confianza** configurada en su lado: «acepto tokens cuyo sujeto sea exactamente este repositorio y esta rama». Si coincide, devuelve una credencial temporal con los permisos del rol asociado.

Según [SE-484 — Credenciales efímeras y OIDC](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md):

El equipo de la API de entregas retira la clave de la nube del repositorio. El job de despliegue pide el permiso de identidad y ningún otro job lo tiene. En la nube crean un rol que solo puede publicar en un registro y actualizar un servicio, y una regla de confianza con emisor de la plataforma, audiencia propia del receptor, sujeto exacto del repositorio y del entorno de producción —que exige una aprobación humana— y vida máxima del token de quince minutos. Escriben diez pruebas con tokens manipulados (sujeto de otro repositorio, de una bifurcación, de una rama sin proteger, audiencia ajena, expirado) y exigen que todas sean rechazadas.

## Ejemplo

Ejemplo de [SE-484 — Credenciales efímeras y OIDC](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md) (sección «Ejemplo profesional»):

El equipo de la API de entregas retira la clave de la nube del repositorio. El job de despliegue pide el permiso de identidad y ningún otro job lo tiene. En la nube crean un rol que solo puede publicar en un registro y actualizar un servicio, y una regla de confianza con emisor de la plataforma, audiencia propia del receptor, sujeto exacto del repositorio y del entorno de producción —que exige una aprobación humana— y vida máxima del token de quince minutos. Escriben diez pruebas con tokens manipulados (sujeto de otro repositorio, de una bifurcación, de una rama sin proteger, audiencia ajena, expirado) y exigen que todas sean rechazadas.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-484 — Credenciales efímeras y OIDC](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md)) son:

- **Un repositorio ajeno obtiene credenciales** — causa: sujeto con prefijo o comodín. Corrección: sujeto exacto y pruebas con tokens manipulados.
- **Un token para otro receptor funciona** — causa: no se comprueba la audiencia. Corrección: exigir la audiencia propia.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-484 — Credenciales efímeras y OIDC](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md)) son: Las definiciones son operativas para la canalización de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Token](../t/token.md), [Audiencia](../a/audiencia.md), [Credencial efímera](../c/credencial-efimera.md), [Identidad federada](../i/identidad-federada.md), [Sujeto](../s/sujeto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-484 — Credenciales efímeras y OIDC](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GitHub: OpenID Connect en Actions](https://docs.github.com/en/actions/concepts/security/openid-connect) — identidad federada para flujos de trabajo y formato del sujeto; autoridad: documentación de GitHub, consultada el 15 de noviembre de 2026.
- [RFC 7519: JSON Web Token](https://www.rfc-editor.org/rfc/rfc7519) — notificaciones registradas y vigencia; autoridad: IETF.
- [RFC 8725: buenas prácticas para JWT](https://www.rfc-editor.org/rfc/rfc8725) — validación del algoritmo, emisor y audiencia; autoridad: IETF.
- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html) — token de identidad y su validación; autoridad: OpenID Foundation.
- [GitHub Actions: uso seguro](https://docs.github.com/en/actions/reference/security/secure-use) — sustituir secretos de larga vida y limitar permisos; autoridad: documentación de GitHub.

---

[↑ Glosario](../../README.md) · [← Regla](./regla.md) · [Regla de decisión →](./regla-de-decision.md)
