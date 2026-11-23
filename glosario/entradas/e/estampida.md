# Estampida

[↑ Glosario](../../README.md) · [← Estados e invariantes](./estados-e-invariantes.md) · [Estándar de codificación segura →](./estandar-de-codificacion-segura.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Pico de consultas a la base cuando muchas entradas faltan o expiran a la vez.

Definición de trabajo de [SE-356 — Cachés y consistencia entre capas](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md).

## Por qué importa

En [SE-356 — Cachés y consistencia entre capas](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md), el tema «Estampida» importa porque muchas expiraciones o fallos simultáneos recaen en la base.

## Cómo funciona

Según [SE-356 — Cachés y consistencia entre capas](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md), en la sección «Estampida»:

Cuando una clave popular expira, muchas peticiones simultáneas encuentran la caché vacía y todas van a la base a calcular lo mismo. Si mil claves se crearon al mismo tiempo (un despliegue, un arranque en frío), expiran juntas y el pico es mil veces peor. Hay tres remedios que se combinan: **variar el TTL** con un componente aleatorio para repartir las expiraciones, **recarga única** (solo una petición recalcula y las demás esperan o sirven el valor viejo), y **precalentar** o renovar antes de que expire. Una caché fría tras un reinicio es el mismo problema a escala de todo el sistema.

## Ejemplo

Ejemplo de [SE-356 — Cachés y consistencia entre capas](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma asigna una política por dato. El resumen del estudiante usa cache-aside con invalidación al escribir, TTL de respaldo de 60 s con variación de ±20 % y recarga única; cada entrada guarda la versión de la fila de origen para que un relleno tardío no pise una versión nueva. El catálogo de cursos, que cambia unas pocas veces al día, usa un TTL de 6 horas sin invalidación, con una acción administrativa que lo vacía. El saldo de cupos no se cachea: el costo de un valor viejo es una reserva de más.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-356 — Cachés y consistencia entre capas](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md)) son:

- **Un valor sigue viejo tras una invalidación** — causa: relleno tardío de un lector lento. Corrección: guardar con versión y no pisar una mayor.
- **La base se satura tras un despliegue** — causa: caché fría y expiraciones simultáneas. Corrección: variar el TTL, precalentar escalonadamente y recarga única.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-356 — Cachés y consistencia entre capas](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con semilla fija en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ninguna caché real ni red de entrega; el reloj es discreto, la popularidad Zipf, el 5 % de escrituras, la recarga de 2 s y los TTL son supuestos del autor, y no se midió la espera de los clientes ni la latencia.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Base](../b/base.md), [Cache-aside](../c/cache-aside.md), [Invalidación](../i/invalidacion.md), [Recarga única](../r/recarga-unica.md), [Vigencia de la caché](../v/vigencia-de-la-cache.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-356 — Cachés y consistencia entre capas](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Azure Architecture Center: Cache-Aside](https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside) — patrón y sus riesgos; autoridad: documentación de Microsoft.
- [AWS Builders' Library: caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/) — retos de consistencia y de carga; autoridad: Amazon Web Services.
- [MDN: Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control) — directivas de la caché HTTP; autoridad: MDN Web Docs.
- [Python: functools.lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache) — caché en memoria con LRU; autoridad: documentación de Python.
- [Python: itertools.permutations](https://docs.python.org/3/library/itertools.html#itertools.permutations) — enumeración de órdenes usada en el experimento; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Estados e invariantes](./estados-e-invariantes.md) · [Estándar de codificación segura →](./estandar-de-codificacion-segura.md)
