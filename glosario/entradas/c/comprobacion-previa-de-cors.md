# Comprobación previa de CORS

[↑ Glosario](../../README.md) · [← Comprobación inestable](./comprobacion-inestable.md) · [Compromiso →](./compromiso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Petición `OPTIONS` que el navegador envía para saber si el servidor permite una petición no simple.

Definición de trabajo de [SE-236 — Seguridad del navegador y políticas de contenido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md).

## Por qué importa

La clase donde se define, [SE-236 — Seguridad del navegador y políticas de contenido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md), existe con este propósito: la clase existe para que entiendas qué defiende el navegador por sí mismo (el aislamiento por origen), qué dejas abierto al incluir datos ajenos en una página y qué políticas puedes declarar para reducir el daño (codificación por contexto, política de seguridad de contenido, atributos de cookie, comprobación de origen), de modo que «hemos añadido seguridad» sea una afirmación con casos probados y límites declarados.

## Cómo funciona

[SE-236 — Seguridad del navegador y políticas de contenido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para esta clase y deben contrastarse con las especificaciones enlazadas al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-236 — Seguridad del navegador y políticas de contenido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md):

La plataforma escribe cada dato ajeno con la codificación de su contexto, mediante una función por contexto y sin concatenar HTML a mano. Los enlaces de «ver trabajo» pasan por una lista de esquemas permitidos. La respuesta lleva una política `default-src 'none'; script-src 'self'; style-src 'self'; connect-src 'self'; base-uri 'none'; frame-ancestors 'none'; form-action 'self'` probada primero en modo de solo informe. La cookie de sesión es `Secure; HttpOnly;

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-236 — Seguridad del navegador y políticas de contenido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md)) son:

- **Un nombre ejecuta código en un atributo** — causa: atributo sin comillas con escape genérico. Corrección: poner comillas y usar la codificación del contexto.
- **Un enlace ejecuta `javascript:` al pulsarlo** — causa: dirección aceptada sin validar el esquema. Corrección: permitir solo `http`, `https` y `mailto` y codificar.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-236 — Seguridad del navegador y políticas de contenido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md)) son: Las definiciones son operativas para esta clase y deben contrastarse con las especificaciones enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. Las 16 cargas útiles y las cinco políticas son una muestra del autor, el analizador no ejecuta código y las tablas de SameSite y CORS reflejan la regla, no un navegador: no se atacó ningún sistema. La siguiente clase pregunta cómo hacer que la aplicación siga funcionando sin conexión y qué se debe sincronizar después.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Option](../o/option.md), [Codificación de salida por contexto](./codificacion-de-salida-por-contexto.md), [Origen](../o/origen.md), [Política de seguridad de contenido](../p/politica-de-seguridad-de-contenido.md), [SameSite](../s/samesite.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-236 — Seguridad del navegador y políticas de contenido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «preflight».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OWASP: Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) — codificación por contexto; autoridad: OWASP.
- [CSP Level 3 (W3C)](https://www.w3.org/TR/CSP3/) — directivas, nonces y hashes; autoridad: W3C.
- [Fetch Standard: protocolo CORS (WHATWG)](https://fetch.spec.whatwg.org/#http-cors-protocol) — peticiones simples y comprobación previa; autoridad: WHATWG.
- [MDN: política de mismo origen](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy) — qué aísla el navegador por origen; autoridad: MDN.
- [web.dev: SameSite cookies explained](https://web.dev/articles/samesite-cookies-explained) — valores de SameSite y envío entre sitios; autoridad: Google web.dev.

---

[↑ Glosario](../../README.md) · [← Comprobación inestable](./comprobacion-inestable.md) · [Compromiso →](./compromiso.md)
