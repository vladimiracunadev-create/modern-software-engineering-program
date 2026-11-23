# Identidad federada

[↑ Glosario](../../README.md) · [← Identidad de una versión](./identidad-de-una-version.md) · [Identificabilidad →](./identificabilidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md)

## Definición

Identidad que un sistema demuestra con un token firmado que otro sistema acepta según una regla de confianza.

Definición de trabajo de [SE-484 — Credenciales efímeras y OIDC](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md).

## Por qué importa

En [SE-484 — Credenciales efímeras y OIDC](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md), el tema «Identidad federada (OIDC)» importa porque sustituye un secreto copiado por una identidad demostrable en cada ejecución.

## Cómo funciona

Según [SE-484 — Credenciales efímeras y OIDC](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md):

Una **credencial estática** es un secreto que vale hasta que alguien lo revoca: una clave de acceso, un token personal, una contraseña de servicio. Su problema no es que se filtre —cualquier secreto puede filtrarse— sino lo que dura la exposición cuando ocurre: desde el instante de la fuga hasta que se descubre y se revoca. Una **credencial efímera** expira sola en minutos u horas. La diferencia es de orden de magnitud en la ventana de riesgo. Además la estática exige gobernanza: quién la creó, quién la puede leer, cuándo se rotó, qué permisos tiene. Eliminar la credencial elimina esa gobernanza, que casi nunca se hace bien. La regla es: si el proveedor permite una identidad federada, un secreto de larga vida es una deuda que se paga con intereses.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-484 — Credenciales efímeras y OIDC](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md):

El equipo de la API de entregas retira la clave de la nube del repositorio. El job de despliegue pide el permiso de identidad y ningún otro job lo tiene. En la nube crean un rol que solo puede publicar en un registro y actualizar un servicio, y una regla de confianza con emisor de la plataforma, audiencia propia del receptor, sujeto exacto del repositorio y del entorno de producción —que exige una aprobación humana— y vida máxima del token de quince minutos.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-484 — Credenciales efímeras y OIDC](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md)) son:

- **Un repositorio ajeno obtiene credenciales** — causa: sujeto con prefijo o comodín. Corrección: sujeto exacto y pruebas con tokens manipulados.
- **Un token para otro receptor funciona** — causa: no se comprueba la audiencia. Corrección: exigir la audiencia propia.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-484 — Credenciales efímeras y OIDC](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md)) son: Las definiciones son operativas para la canalización de la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Regla de confianza](../r/regla-de-confianza.md), [Confianza](../c/confianza.md), [Regla](../r/regla.md), [Token](../t/token.md), [Audiencia](../a/audiencia.md), [Credencial efímera](../c/credencial-efimera.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-484 — Credenciales efímeras y OIDC](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-484-credenciales-efimeras-y-oidc/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-485](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-485-entrega-y-despliegue-continuos/README.md), [SE-483](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-483-tests-seguridad-y-politicas-como-gates/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «OIDC».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GitHub: OpenID Connect en Actions](https://docs.github.com/en/actions/concepts/security/openid-connect) — identidad federada para flujos de trabajo y formato del sujeto; autoridad: documentación de GitHub, consultada el 15 de noviembre de 2026.
- [RFC 7519: JSON Web Token](https://www.rfc-editor.org/rfc/rfc7519) — notificaciones registradas y vigencia; autoridad: IETF.
- [RFC 8725: buenas prácticas para JWT](https://www.rfc-editor.org/rfc/rfc8725) — validación del algoritmo, emisor y audiencia; autoridad: IETF.
- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html) — token de identidad y su validación; autoridad: OpenID Foundation.
- [GitHub Actions: uso seguro](https://docs.github.com/en/actions/reference/security/secure-use) — sustituir secretos de larga vida y limitar permisos; autoridad: documentación de GitHub.

---

[↑ Glosario](../../README.md) · [← Identidad de una versión](./identidad-de-una-version.md) · [Identificabilidad →](./identificabilidad.md)
