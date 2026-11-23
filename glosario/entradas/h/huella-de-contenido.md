# Huella de contenido

[↑ Glosario](../../README.md) · [← Huella de código](./huella-de-codigo.md) · [Huella de la carga →](./huella-de-la-carga.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Identificador derivado del contenido de un recurso que cambia solo cuando el contenido cambia.

Definición de trabajo de [SE-237 — PWA, caché, offline y sincronización](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md).

## Por qué importa

La clase donde se define, [SE-237 — PWA, caché, offline y sincronización](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md), existe con este propósito: la clase existe para que diseñes una aplicación web que siga siendo útil sin conexión sabiendo qué promete cada estrategia de caché, cómo se actualiza el código que vive en el dispositivo y qué ocurre con lo que la persona hizo mientras no había red, de modo que «funciona offline» sea una propiedad con casos, límites y reglas de reconciliación, y no un efecto secundario de una biblioteca.

## Cómo funciona

[SE-237 — PWA, caché, offline y sincronización](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para esta clase y deben contrastarse con las especificaciones enlazadas al final.

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
- **Ver también:** [Recurso](../r/recurso.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Estrategia de caché](../e/estrategia-de-cache.md), [Service worker](../s/service-worker.md), [Última escritura gana](../u/ultima-escritura-gana.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-237 — PWA, caché, offline y sincronización](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: `hashlib`](https://docs.python.org/3/library/hashlib.html) — huellas de contenido.
- [Service Workers (W3C)](https://www.w3.org/TR/service-workers/) — registro, ciclo de vida e interceptación; autoridad: W3C.
- [Web Application Manifest (W3C)](https://www.w3.org/TR/appmanifest/) — campos del manifiesto; autoridad: W3C.
- [web.dev: The Offline Cookbook](https://web.dev/articles/offline-cookbook) — estrategias de caché; autoridad: Google web.dev.
- [MDN: usar service workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers) — instalación, espera y activación; autoridad: MDN.

---

[↑ Glosario](../../README.md) · [← Huella de código](./huella-de-codigo.md) · [Huella de la carga →](./huella-de-la-carga.md)
