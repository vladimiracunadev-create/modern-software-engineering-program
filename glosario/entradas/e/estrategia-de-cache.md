# Estrategia de caché

[↑ Glosario](../../README.md) · [← Estrategia](./estrategia.md) · [Estrategia de pruebas →](./estrategia-de-pruebas.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Una **estrategia de caché** es la regla que decide, para cada petición, si se responde desde la caché, desde la red o desde ambas. Es el sentido de [SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md) (PWA, caché, offline y sincronización), donde se aplica a un *service worker*. No hay una estrategia correcta: cada una intercambia obsolescencia por velocidad y disponibilidad.

## Por qué importa

La estrategia decide qué ve la persona cuando la red es lenta o está caída, y cuán viejo puede ser lo que ve. Elegir mal significa mostrar una calificación desactualizada o dejar una aplicación en blanco sin conexión.

## Cómo funciona

[SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md) describe cuatro estrategias:

- **Solo red:** lo más fresco; no funciona sin conexión.
- **Caché primero:** responde al instante y puede servir contenido viejo indefinidamente.
- **Red primero con respaldo en caché:** frescura cuando hay red y degradación elegante cuando no; a costa de esperar el tiempo de espera cuando la red es mala.
- **Revalidar en segundo plano** (*stale-while-revalidate*): responde desde la caché y renueva para la próxima vez; rápido y casi fresco, con la limitación de mostrar una versión vieja una vez.

La elección es **por tipo de recurso**: el esqueleto de la aplicación (HTML, CSS, JavaScript, iconos) admite caché primero; los datos de una calificación, no.

## Ejemplo

La aplicación de entregas de [SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md) precarga el esqueleto con una revisión por huella y lo sirve con caché primero; la lista de entregas usa revalidar en segundo plano; las calificaciones, red primero con tiempo de espera corto. El script del service worker se sirve con `no-cache`, la versión nueva avisa a la persona («hay una versión nueva») y se conserva una generación anterior.

## Errores y confusiones comunes

- **Aplicar una sola estrategia a todo.**
- **Caché primero para datos que cambian:** se sirve contenido viejo indefinidamente.
- **Cachear el propio script del service worker,** que impide actualizar.
- **Confundir estrategia con política de expiración:** la estrategia decide el orden de consulta; la expiración decide cuándo un dato deja de valer.

## Límites y cuándo no aplica

No resuelve la invalidación: saber cuándo un dato cacheado dejó de ser válido es un problema aparte. No aplica a recursos no cacheables (respuestas personalizadas sensibles). Y la estrategia vale en el navegador y el contexto de la clase; otras cachés (de servidor, de CDN) tienen sus propias reglas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-236](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Regla](../r/regla.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Huella de contenido](../h/huella-de-contenido.md), [Service worker](../s/service-worker.md), [Última escritura gana](../u/ultima-escritura-gana.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-237 — PWA, caché, offline y sincronización](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-240](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md), [SE-064](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Estrategias de caché».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [web.dev: The Offline Cookbook](https://web.dev/articles/offline-cookbook) — estrategias de caché; autoridad: Google web.dev.
- [Service Workers (W3C)](https://www.w3.org/TR/service-workers/) — registro, ciclo de vida e interceptación; autoridad: W3C.
- [Web Application Manifest (W3C)](https://www.w3.org/TR/appmanifest/) — campos del manifiesto; autoridad: W3C.
- [MDN: usar service workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers) — instalación, espera y activación; autoridad: MDN.
- [RFC 8246: HTTP Immutable Responses](https://www.rfc-editor.org/rfc/rfc8246) — recursos con huella que no cambian; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Estrategia](./estrategia.md) · [Estrategia de pruebas →](./estrategia-de-pruebas.md)
