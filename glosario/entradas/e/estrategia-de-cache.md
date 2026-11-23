# Estrategia de caché

[↑ Glosario](../../README.md) · [← Estrategia](./estrategia.md) · [Estrategia de pruebas →](./estrategia-de-pruebas.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Regla que decide, para cada petición, si se responde desde la caché, desde la red o desde ambas.

Definición de trabajo de [SE-237 — PWA, caché, offline y sincronización](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md).

## Por qué importa

En [SE-237 — PWA, caché, offline y sincronización](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md), el tema «Estrategias de caché» importa porque cada estrategia cambia obsolescencia por velocidad y por disponibilidad.

## Cómo funciona

Según [SE-237 — PWA, caché, offline y sincronización](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md), en la sección «Estrategias de caché»:

**Solo red** es lo más fresco y no funciona sin conexión. **Caché primero** responde al instante y puede servir contenido viejo indefinidamente. **Red primero con respaldo en caché** da frescura cuando hay red y degrada con elegancia, a costa de esperar el tiempo de espera cuando la red es mala. **Revalidar en segundo plano** (`stale-while-revalidate`) responde desde la caché y renueva para la próxima vez: rápido y casi fresco, con la limitación de mostrar una versión vieja una vez. No hay una estrategia correcta: se elige por tipo de recurso (el esqueleto de la aplicación admite caché primero; los datos de una calificación, no).

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-237 — PWA, caché, offline y sincronización](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md):

La aplicación de entregas precarga el esqueleto (HTML, CSS, JavaScript y los iconos) con una revisión por huella y lo sirve con caché primero; los datos de la lista de entregas usan revalidar en segundo plano y las calificaciones, red primero con un tiempo de espera corto. El script del service worker se sirve con `no-cache`, la versión nueva avisa a la persona («hay una versión nueva») y se conserva una generación anterior.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-237 — PWA, caché, offline y sincronización](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md)) son:

- **Nadie ve la versión nueva de la aplicación** — causa: script del service worker servido con caché larga o activación bloqueada por pestañas. Corrección: servirlo con `no-cache` y avisar de la versión nueva.
- **Cada versión descarga toda la aplicación** — causa: caché con otro nombre en cada versión. Corrección: revisar por huella y descargar solo lo que cambió.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-237 — PWA, caché, offline y sincronización](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md)) son: Las definiciones son operativas para esta clase y deben contrastarse con las especificaciones enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se ejecutó ningún service worker ni un navegador: la traza, las latencias, las pérdidas de confirmación y los desvíos de reloj son supuestos del autor y las pestañas con versiones mixtas no se midieron. La siguiente clase pregunta cómo hacer que las páginas se encuentren y se entiendan fuera de la aplicación.

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
