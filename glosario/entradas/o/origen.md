# Origen

[↑ Glosario](../../README.md) · [← Organización](./organizacion.md) · [Orquestación →](./orquestacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Tupla de esquema, host y puerto que delimita qué datos puede leer una página.

Definición de trabajo de [SE-236 — Seguridad del navegador y políticas de contenido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md).

## Por qué importa

En [SE-236 — Seguridad del navegador y políticas de contenido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md), el tema «Origen y aislamiento» importa porque la política de mismo origen es la base de todo lo demás; entenderla evita falsas expectativas.

## Cómo funciona

Según [SE-236 — Seguridad del navegador y políticas de contenido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md):

Un origen es la tupla (esquema, host, puerto). Por defecto, una página de un origen no puede leer los datos de otro (política de mismo origen): puede enviar peticiones, incrustar recursos y mostrar un marco, pero no leer el resultado. Todo lo demás se construye sobre esa regla: CORS la relaja de forma explícita, las cookies tienen su propio criterio (sitio, no origen) y la política de seguridad de contenido restringe qué puede cargar la propia página. Un origen es una frontera de confianza: todo el código que corre en él, incluido el de bibliotecas de terceros, puede leer lo que la página lee.

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

- Por defecto, una página de un origen no puede leer los datos de otro (política de mismo origen): puede enviar peticiones, incrustar recursos y mostrar un marco, pero no leer el resultado. ([SE-236](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Esquema](../e/esquema.md), [Página](../p/pagina.md), [Puerto](../p/puerto.md), [Codificación de salida por contexto](../c/codificacion-de-salida-por-contexto.md), [Comprobación previa de CORS](../c/comprobacion-previa-de-cors.md), [Política de seguridad de contenido](../p/politica-de-seguridad-de-contenido.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-236 — Seguridad del navegador y políticas de contenido](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

**También se usa en** (148 clases más lo mencionan; las que más):

[SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), [SE-044](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md), [SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md), [SE-227](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-227-taller-endurecer-una-automatizacion-fragil/README.md), [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md), [SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md), [SE-367](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md), [SE-371](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-371-taller-reparar-un-pipeline-defectuoso/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MDN: política de mismo origen](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy) — qué aísla el navegador por origen; autoridad: MDN.
- [OWASP: Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) — codificación por contexto; autoridad: OWASP.
- [CSP Level 3 (W3C)](https://www.w3.org/TR/CSP3/) — directivas, nonces y hashes; autoridad: W3C.
- [Fetch Standard: protocolo CORS (WHATWG)](https://fetch.spec.whatwg.org/#http-cors-protocol) — peticiones simples y comprobación previa; autoridad: WHATWG.
- [web.dev: SameSite cookies explained](https://web.dev/articles/samesite-cookies-explained) — valores de SameSite y envío entre sitios; autoridad: Google web.dev.

---

[↑ Glosario](../../README.md) · [← Organización](./organizacion.md) · [Orquestación →](./orquestacion.md)
