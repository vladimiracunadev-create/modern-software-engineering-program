# SameSite

[↑ Glosario](../../README.md) · [← Salto](./salto.md) · [SAN →](./san.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Atributo de cookie que limita su envío en peticiones iniciadas desde otro sitio.

Definición de trabajo de [SE-236 — Seguridad del navegador y políticas de contenido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md).

## Por qué importa

En [SE-236 — Seguridad del navegador y políticas de contenido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md), el tema «Cookies y falsificación entre sitios» importa porque SameSite decide cuándo viaja la cookie; sin ella, otro sitio puede hacer peticiones con tu sesión.

## Cómo funciona

Según [SE-236 — Seguridad del navegador y políticas de contenido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md):

La falsificación de petición entre sitios (CSRF) abusa de que el navegador adjunta las cookies a una petición aunque la inicie otro sitio. El atributo `SameSite` limita ese envío: con `Strict`, la cookie no viaja nunca en una petición iniciada desde otro sitio; con `Lax`, solo en una navegación de nivel superior con método seguro (un GET desde un enlace); con `None` (y `Secure`), siempre. Los navegadores han ido adoptando `Lax` como valor por defecto, pero no conviene suponerlo: se declara. SameSite no sustituye a una comprobación de origen o un token en las operaciones que cambian estado.

Según [SE-236 — Seguridad del navegador y políticas de contenido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md):

La plataforma escribe cada dato ajeno con la codificación de su contexto, mediante una función por contexto y sin concatenar HTML a mano. Los enlaces de «ver trabajo» pasan por una lista de esquemas permitidos. La respuesta lleva una política `default-src 'none'; script-src 'self'; style-src 'self'; connect-src 'self'; base-uri 'none'; frame-ancestors 'none'; form-action 'self'` probada primero en modo de solo informe. La cookie de sesión es `Secure; HttpOnly; SameSite=Lax`, las operaciones que cambian estado comprueban el origen y un token, y la API devuelve cabeceras CORS solo para los orígenes de la lista.

## Ejemplo

Ejemplo de [SE-236 — Seguridad del navegador y políticas de contenido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md) (sección «Ejemplo profesional»):

La plataforma escribe cada dato ajeno con la codificación de su contexto, mediante una función por contexto y sin concatenar HTML a mano. Los enlaces de «ver trabajo» pasan por una lista de esquemas permitidos. La respuesta lleva una política `default-src 'none'; script-src 'self'; style-src 'self'; connect-src 'self'; base-uri 'none'; frame-ancestors 'none'; form-action 'self'` probada primero en modo de solo informe. La cookie de sesión es `Secure; HttpOnly; SameSite=Lax`, las operaciones que cambian estado comprueban el origen y un token, y la API devuelve cabeceras CORS solo para los orígenes de la lista.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Otro sitio hace acciones con la sesión de una persona** — causa: cookie con `SameSite=None` y sin comprobación de origen. Corrección: usar `Lax` o `Strict` y verificar origen o token en las operaciones que cambian estado. ([SE-236](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El atributo `SameSite` limita ese envío: con `Strict`, la cookie no viaja nunca en una petición iniciada desde otro sitio; con `Lax`, solo en una navegación de nivel superior con método seguro (un GET desde un enlace); con `None` (y `Secure`), siempre. ([SE-236](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Atributo](../a/atributo.md), [Codificación de salida por contexto](../c/codificacion-de-salida-por-contexto.md), [Comprobación previa de CORS](../c/comprobacion-previa-de-cors.md), [Origen](../o/origen.md), [Política de seguridad de contenido](../p/politica-de-seguridad-de-contenido.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-236 — Seguridad del navegador y políticas de contenido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-467](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-467-taller-explotar-y-reparar-un-control-aparente/README.md), [SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [web.dev: SameSite cookies explained](https://web.dev/articles/samesite-cookies-explained) — valores de SameSite y envío entre sitios; autoridad: Google web.dev.
- [OWASP: Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) — codificación por contexto; autoridad: OWASP.
- [CSP Level 3 (W3C)](https://www.w3.org/TR/CSP3/) — directivas, nonces y hashes; autoridad: W3C.
- [Fetch Standard: protocolo CORS (WHATWG)](https://fetch.spec.whatwg.org/#http-cors-protocol) — peticiones simples y comprobación previa; autoridad: WHATWG.
- [MDN: política de mismo origen](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy) — qué aísla el navegador por origen; autoridad: MDN.

---

[↑ Glosario](../../README.md) · [← Salto](./salto.md) · [SAN →](./san.md)
