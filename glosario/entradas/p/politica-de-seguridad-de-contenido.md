# Política de seguridad de contenido

[↑ Glosario](../../README.md) · [← Política de reentrenamiento](./politica-de-reentrenamiento.md) · [Política de solape →](./politica-de-solape.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Cabecera que declara de dónde puede cargar recursos una página y si puede ejecutar código en línea.

Definición de trabajo de [SE-236 — Seguridad del navegador y políticas de contenido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md).

## Por qué importa

En [SE-236 — Seguridad del navegador y políticas de contenido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md), el tema «Política de seguridad de contenido» importa porque una política estricta limita qué código se ejecuta incluso cuando hay una inyección.

## Cómo funciona

Según [SE-236 — Seguridad del navegador y políticas de contenido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md), en la sección «Política de seguridad de contenido»:

La política de seguridad de contenido (CSP) es una cabecera que declara de dónde puede cargar la página scripts, estilos, imágenes y conexiones y si puede ejecutar código en línea. Una política con `script-src 'self'` y sin `'unsafe-inline'` bloquea el código en línea que inyectaría un ataque; con un `nonce` por respuesta se permite el código propio en línea. Una política con `*`, `'unsafe-inline'` o `'unsafe-eval'` casi no restringe. Es una **segunda barrera**: no reemplaza la codificación, y una política demasiado estricta puede romper la página, por lo que se introduce en modo de solo informe antes de aplicarla.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-236 — Seguridad del navegador y políticas de contenido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md):

La plataforma escribe cada dato ajeno con la codificación de su contexto, mediante una función por contexto y sin concatenar HTML a mano. Los enlaces de «ver trabajo» pasan por una lista de esquemas permitidos. La respuesta lleva una política `default-src 'none'; script-src 'self'; style-src 'self'; connect-src 'self'; base-uri 'none'; frame-ancestors 'none'; form-action 'self'` probada primero en modo de solo informe. La cookie de sesión es `Secure; HttpOnly;

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La CSP no bloquea nada** — causa: política con `*`, `unsafe-inline` o `unsafe-eval`. Corrección: restringir orígenes, usar nonces y probar en solo informe. ([SE-236](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- CORS la relaja de forma explícita, las cookies tienen su propio criterio (sitio, no origen) y la política de seguridad de contenido restringe qué puede cargar la propia página. ([SE-236](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Página](./pagina.md), [Recurso](../r/recurso.md), [Codificación de salida por contexto](../c/codificacion-de-salida-por-contexto.md), [Comprobación previa de CORS](../c/comprobacion-previa-de-cors.md), [Origen](../o/origen.md), [SameSite](../s/samesite.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-236 — Seguridad del navegador y políticas de contenido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «CSP».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [CSP Level 3 (W3C)](https://www.w3.org/TR/CSP3/) — directivas, nonces y hashes; autoridad: W3C.
- [OWASP: Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) — codificación por contexto; autoridad: OWASP.
- [Fetch Standard: protocolo CORS (WHATWG)](https://fetch.spec.whatwg.org/#http-cors-protocol) — peticiones simples y comprobación previa; autoridad: WHATWG.
- [MDN: política de mismo origen](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy) — qué aísla el navegador por origen; autoridad: MDN.
- [web.dev: SameSite cookies explained](https://web.dev/articles/samesite-cookies-explained) — valores de SameSite y envío entre sitios; autoridad: Google web.dev.

---

[↑ Glosario](../../README.md) · [← Política de reentrenamiento](./politica-de-reentrenamiento.md) · [Política de solape →](./politica-de-solape.md)
