# Última escritura gana

[↑ Glosario](../../README.md) · [← ULP](./ulp.md) · [Último momento responsable →](./ultimo-momento-responsable.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Política de conflicto que conserva la edición con la marca de tiempo mayor y descarta las demás.

Definición de trabajo de [SE-237 — PWA, caché, offline y sincronización](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md).

## Por qué importa

La clase donde se define, [SE-237 — PWA, caché, offline y sincronización](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md), existe con este propósito: la clase existe para que diseñes una aplicación web que siga siendo útil sin conexión sabiendo qué promete cada estrategia de caché, cómo se actualiza el código que vive en el dispositivo y qué ocurre con lo que la persona hizo mientras no había red, de modo que «funciona offline» sea una propiedad con casos, límites y reglas de reconciliación, y no un efecto secundario de una biblioteca.

## Cómo funciona

Según [SE-237 — PWA, caché, offline y sincronización](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md):

Las acciones hechas sin conexión se guardan en una cola local y se envían al volver la red. Si la confirmación se pierde, el cliente reintenta, y si el servidor no reconoce la repetición, la operación se aplica dos veces. La solución es una **clave de idempotencia** generada en el cliente por operación. Para las ediciones concurrentes hay dos familias de políticas: **la última escritura gana** (simple, descarta una edición) y **comprobar una versión** (el servidor rechaza una edición basada en una versión vieja y obliga a combinar). La hora del dispositivo no es una fuente fiable para ordenarlas: los relojes difieren, como mostró Lamport al definir el orden de eventos sin relojes comunes.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-237 — PWA, caché, offline y sincronización](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md):

La aplicación de entregas precarga el esqueleto (HTML, CSS, JavaScript y los iconos) con una revisión por huella y lo sirve con caché primero; los datos de la lista de entregas usan revalidar en segundo plano y las calificaciones, red primero con un tiempo de espera corto. El script del service worker se sirve con `no-cache`, la versión nueva avisa a la persona («hay una versión nueva») y se conserva una generación anterior.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se pierde una edición hecha en otro dispositivo** — causa: última escritura gana con relojes desviados. Corrección: comprobar versión y resolver el conflicto. ([SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **la última escritura gana descarta una edición en los 300 casos**, y en el **13,3 %** gana la más antigua según el reloj real; con **comprobación de versión** no se descarta ninguna en silencio, a costa de obligar a resolver el conflicto. ([SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-236](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conflicto](../c/conflicto.md), [Edición](../e/edicion.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Estrategia de caché](../e/estrategia-de-cache.md), [Huella de contenido](../h/huella-de-contenido.md), [Service worker](../s/service-worker.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-237 — PWA, caché, offline y sincronización](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-418](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Service Workers (W3C)](https://www.w3.org/TR/service-workers/) — registro, ciclo de vida e interceptación; autoridad: W3C.
- [Web Application Manifest (W3C)](https://www.w3.org/TR/appmanifest/) — campos del manifiesto; autoridad: W3C.
- [web.dev: The Offline Cookbook](https://web.dev/articles/offline-cookbook) — estrategias de caché; autoridad: Google web.dev.
- [MDN: usar service workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers) — instalación, espera y activación; autoridad: MDN.
- [RFC 8246: HTTP Immutable Responses](https://www.rfc-editor.org/rfc/rfc8246) — recursos con huella que no cambian; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← ULP](./ulp.md) · [Último momento responsable →](./ultimo-momento-responsable.md)
