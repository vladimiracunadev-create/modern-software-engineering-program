# Estampida

[↑ Glosario](../../README.md) · [← Estados e invariantes](./estados-e-invariantes.md) · [Estándar de codificación segura →](./estandar-de-codificacion-segura.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

La **estampida** (*cache stampede*) es el pico de consultas a la base que ocurre cuando muchas entradas de la caché faltan o expiran a la vez ([SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md)). Una caché existe para proteger a la base; la estampida es el momento en que esa protección desaparece de golpe y toda la carga cae sobre ella.

## Por qué importa

El sistema funciona bien con la caché caliente y se cae justo cuando más depende de ella: tras un despliegue, un reinicio o la expiración de una clave popular. La decisión que cambia es que la caché no se diseña solo para el caso normal: se diseña también para el instante en que está vacía, porque la base quizá no tenga capacidad para atender sola ese tráfico.

## Cómo funciona

[SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md) describe el mecanismo en dos escalas. A escala de una clave: cuando una clave popular expira, muchas peticiones simultáneas encuentran la caché vacía y todas van a la base a calcular lo mismo; el trabajo se repite tantas veces como peticiones llegaron en esa ventana. A escala del sistema: si mil claves se crearon al mismo tiempo (un despliegue, un arranque en frío), expiran juntas y el pico es mil veces peor. Una caché fría tras un reinicio es el mismo problema a escala de todo el sistema.

La causa es la sincronización: todas las entradas comparten el mismo instante de creación y el mismo TTL, así que expiran juntas. Los remedios que da la clase se combinan:

1. **Variar el TTL** con un componente aleatorio, para repartir las expiraciones en el tiempo.
2. **Recarga única**: solo una petición recalcula; las demás esperan o sirven el valor viejo.
3. **Precalentar o renovar** antes de que expire, y de forma escalonada tras un despliegue.

La clase añade el cuidado con las versiones: un lector lento puede rellenar la caché con un valor viejo después de una invalidación; se corrige guardando con versión y sin pisar una mayor.

## Ejemplo

Tras un despliegue, la caché de calificaciones queda vacía y el tráfico de una hora pico va directo a la base, que se satura. Con TTL aleatorio, recarga única y precalentamiento escalonado, solo una petición por clave llega a la base y las expiraciones dejan de coincidir. Escenario de las simulaciones de [SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md).

## Errores y confusiones comunes

- **La base se satura tras un despliegue**: caché fría y expiraciones simultáneas; se corrige variando el TTL, precalentando escalonadamente y con recarga única.
- **Un valor sigue viejo tras una invalidación**: relleno tardío de un lector lento; se corrige guardando con versión.
- **TTL idéntico para todo**: sincroniza las expiraciones.
- **Creer que más caché lo resuelve**: el problema es el instante de vacío, no la capacidad.

## Límites y cuándo no aplica

[SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md) aclara que no usó una caché real ni red de entrega: el reloj es discreto, la popularidad Zipf, el 5 % de escrituras, la recarga de 2 s y los TTL son supuestos del autor, y no se midió la espera de los clientes ni la latencia. La estampida solo importa donde la base no soporta el tráfico sin caché; si la base tiene holgura de sobra, el efecto es menor. La recarga única sirve valores viejos durante la recarga, lo que exige que el negocio acepte esa obsolescencia.

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
