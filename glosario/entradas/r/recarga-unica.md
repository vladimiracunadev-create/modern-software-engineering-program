# Recarga única

[↑ Glosario](../../README.md) · [← Recall o TPR](./recall-o-tpr.md) · [Receptor idempotente →](./receptor-idempotente.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Técnica en la que solo una petición recalcula un valor y las demás esperan su resultado.

Definición de trabajo de [SE-356 — Cachés y consistencia entre capas](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md): Mecanismo por el que, ante varios fallos de la misma clave, solo uno carga y los demás esperan.

## Por qué importa

La clase donde se define, [SE-356 — Cachés y consistencia entre capas](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md), existe con este propósito: la clase existe para que decidas qué se guarda en una caché, cuánto tiempo y quién la invalida, midiendo cuántas lecturas viejas permite cada política, y para que reconozcas los dos fallos típicos de una caché que funciona: la estampida tras una expiración y la carrera entre una lectura y una escritura.

## Cómo funciona

Según [SE-356 — Cachés y consistencia entre capas](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md):

Cuando una clave popular expira, muchas peticiones simultáneas encuentran la caché vacía y todas van a la base a calcular lo mismo. Si mil claves se crearon al mismo tiempo (un despliegue, un arranque en frío), expiran juntas y el pico es mil veces peor. Hay tres remedios que se combinan: **variar el TTL** con un componente aleatorio para repartir las expiraciones, **recarga única** (solo una petición recalcula y las demás esperan o sirven el valor viejo), y **precalentar** o renovar antes de que expire. Una caché fría tras un reinicio es el mismo problema a escala de todo el sistema.

Según [SE-356 — Cachés y consistencia entre capas](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md):

El equipo de la plataforma asigna una política por dato. El resumen del estudiante usa cache-aside con invalidación al escribir, TTL de respaldo de 60 s con variación de ±20 % y recarga única; cada entrada guarda la versión de la fila de origen para que un relleno tardío no pise una versión nueva. El catálogo de cursos, que cambia unas pocas veces al día, usa un TTL de 6 horas sin invalidación, con una acción administrativa que lo vacía. El saldo de cupos no se cachea: el costo de un valor viejo es una reserva de más. Al desplegar, un script precalienta las 1 000 claves más pedidas escalonadamente para evitar una estampida fría.

## Ejemplo

Ejemplo de [SE-356 — Cachés y consistencia entre capas](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma asigna una política por dato. El resumen del estudiante usa cache-aside con invalidación al escribir, TTL de respaldo de 60 s con variación de ±20 % y recarga única; cada entrada guarda la versión de la fila de origen para que un relleno tardío no pise una versión nueva. El catálogo de cursos, que cambia unas pocas veces al día, usa un TTL de 6 horas sin invalidación, con una acción administrativa que lo vacía. El saldo de cupos no se cachea: el costo de un valor viejo es una reserva de más.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La base se satura tras un despliegue** — causa: caché fría y expiraciones simultáneas. Corrección: variar el TTL, precalentar escalonadamente y recarga única. ([SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **variar el TTL** con un componente aleatorio para repartir las expiraciones, **recarga única** (solo una petición recalcula y las demás esperan o sirven el valor viejo), y **precalentar** o renovar antes de que expire. ([SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), [SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Mecanismo](../m/mecanismo.md), [Resultado](./resultado.md), [Valor](../v/valor.md), [429](../0-9/429.md), [Cache-aside](../c/cache-aside.md), [Clave de caché](../c/clave-de-cache.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-356 — Cachés y consistencia entre capas](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «single-flight».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Azure Architecture Center: Cache-Aside](https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside) — patrón y sus riesgos; autoridad: documentación de Microsoft.
- [AWS Builders' Library: caching challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/) — retos de consistencia y de carga; autoridad: Amazon Web Services.
- [MDN: Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control) — directivas de la caché HTTP; autoridad: MDN Web Docs.
- [Python: functools.lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache) — caché en memoria con LRU; autoridad: documentación de Python.
- [Python: itertools.permutations](https://docs.python.org/3/library/itertools.html#itertools.permutations) — enumeración de órdenes usada en el experimento; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Recall o TPR](./recall-o-tpr.md) · [Receptor idempotente →](./receptor-idempotente.md)
