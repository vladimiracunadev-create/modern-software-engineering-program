# Service worker

[↑ Glosario](../../README.md) · [← Serverless](./serverless.md) · [Servicio →](./servicio.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Script que el navegador ejecuta aparte de la página y que intercepta las peticiones de un alcance para responder desde caché, red o lógica propia.

Definición de trabajo de [SE-237 — PWA, caché, offline y sincronización](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md).

## Por qué importa

En [SE-237 — PWA, caché, offline y sincronización](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md), el tema «Qué es una aplicación web progresiva» importa porque un manifiesto, HTTPS y un service worker hacen la aplicación instalable y capaz de funcionar sin red.

## Cómo funciona

Según [SE-237 — PWA, caché, offline y sincronización](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md):

Una aplicación web progresiva es una aplicación web servida por HTTPS con un **manifiesto** (nombre, iconos, URL de inicio, alcance, modo de visualización) y un **service worker** que intercepta las peticiones. El manifiesto permite instalarla; el service worker permite responder sin red. «Progresiva» significa que debe funcionar en cualquier navegador y mejorar donde haya soporte: sin el service worker, sigue siendo una página normal. No sustituye a una aplicación nativa en todo; es una opción para llegar con un coste de distribución bajo.

Según [SE-237 — PWA, caché, offline y sincronización](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md):

La aplicación de entregas precarga el esqueleto (HTML, CSS, JavaScript y los iconos) con una revisión por huella y lo sirve con caché primero; los datos de la lista de entregas usan revalidar en segundo plano y las calificaciones, red primero con un tiempo de espera corto. El script del service worker se sirve con `no-cache`, la versión nueva avisa a la persona («hay una versión nueva») y se conserva una generación anterior. El envío de una entrega sin conexión va a una cola local con una clave de idempotencia por operación; al recibirla, el servidor marca la hora de recepción, que es la que cuenta para el plazo. Las ediciones del perfil llevan la versión del dato y un conflicto se muestra a la persona.

## Ejemplo

Ejemplo de [SE-237 — PWA, caché, offline y sincronización](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md) (sección «Ejemplo profesional»):

La aplicación de entregas precarga el esqueleto (HTML, CSS, JavaScript y los iconos) con una revisión por huella y lo sirve con caché primero; los datos de la lista de entregas usan revalidar en segundo plano y las calificaciones, red primero con un tiempo de espera corto. El script del service worker se sirve con `no-cache`, la versión nueva avisa a la persona («hay una versión nueva») y se conserva una generación anterior. El envío de una entrega sin conexión va a una cola local con una clave de idempotencia por operación; al recibirla, el servidor marca la hora de recepción, que es la que cuenta para el plazo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Nadie ve la versión nueva de la aplicación** — causa: script del service worker servido con caché larga o activación bloqueada por pestañas. Corrección: servirlo con `no-cache` y avisar de la versión nueva. ([SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El manifiesto permite instalarla; el service worker permite responder sin red. ([SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-236](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcance](../a/alcance.md), [Página](../p/pagina.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Estrategia de caché](../e/estrategia-de-cache.md), [Huella de contenido](../h/huella-de-contenido.md), [Última escritura gana](../u/ultima-escritura-gana.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-237 — PWA, caché, offline y sincronización](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-240](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md), [SE-236](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md), [SE-234](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md), [SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md), [SE-238](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md), [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Service Workers (W3C)](https://www.w3.org/TR/service-workers/) — registro, ciclo de vida e interceptación; autoridad: W3C.
- [MDN: usar service workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers) — instalación, espera y activación; autoridad: MDN.
- [Web Application Manifest (W3C)](https://www.w3.org/TR/appmanifest/) — campos del manifiesto; autoridad: W3C.
- [web.dev: The Offline Cookbook](https://web.dev/articles/offline-cookbook) — estrategias de caché; autoridad: Google web.dev.
- [RFC 8246: HTTP Immutable Responses](https://www.rfc-editor.org/rfc/rfc8246) — recursos con huella que no cambian; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Serverless](./serverless.md) · [Servicio →](./servicio.md)
