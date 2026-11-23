# Invalidación

[↑ Glosario](../../README.md) · [← Introspección](./introspeccion.md) · [Invariante →](./invariante.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Eliminación o actualización de una entrada de la caché cuando cambia el dato de origen.

Definición de trabajo de [SE-356 — Cachés y consistencia entre capas](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md).

## Por qué importa

En [SE-356 — Cachés y consistencia entre capas](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md), el tema «Invalidación» importa porque borrar la clave elimina el valor viejo solo si la orden llega siempre.

## Cómo funciona

Según [SE-356 — Cachés y consistencia entre capas](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md), en la sección «Invalidación»:

Invalidar al escribir mantiene la caché fresca sin renunciar a los aciertos, y por eso se prefiere donde el costo de un valor viejo es alto. Es difícil por tres razones: la escritura puede cambiar datos que alimentan muchas claves (un cambio en un curso afecta a las listas de todos sus estudiantes), la orden de invalidación puede perderse o llegar tarde en un sistema distribuido, y la propia invalidación compite con las lecturas que rellenan. Por eso se combina con un TTL de respaldo: la invalidación da frescura en el caso normal y el TTL acota el daño cuando falla.

## Ejemplo

Ejemplo de [SE-356 — Cachés y consistencia entre capas](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma asigna una política por dato. El resumen del estudiante usa cache-aside con invalidación al escribir, TTL de respaldo de 60 s con variación de ±20 % y recarga única; cada entrada guarda la versión de la fila de origen para que un relleno tardío no pise una versión nueva. El catálogo de cursos, que cambia unas pocas veces al día, usa un TTL de 6 horas sin invalidación, con una acción administrativa que lo vacía. El saldo de cupos no se cachea: el costo de un valor viejo es una reserva de más.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un valor sigue viejo tras una invalidación** — causa: relleno tardío de un lector lento. Corrección: guardar con versión y no pisar una mayor. ([SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md))
- **La tasa de aciertos es alta y los usuarios se quejan** — causa: TTL largo sin invalidación. Corrección: acotar el TTL por tolerancia e invalidar donde importe. ([SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La figura no dice qué política usar, sino que cada una compra frescura con aciertos o con una promesa sobre la invalidación. ([SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Origen](../o/origen.md), [Cache-aside](../c/cache-aside.md), [Estampida](../e/estampida.md), [Recarga única](../r/recarga-unica.md), [Vigencia de la caché](../v/vigencia-de-la-cache.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-356 — Cachés y consistencia entre capas](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (10 clases más lo mencionan; las que más):

[SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md), [SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md), [SE-514](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md), [SE-051](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md), [SE-115](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md), [SE-231](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md), [SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md), [SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md).

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

[↑ Glosario](../../README.md) · [← Introspección](./introspeccion.md) · [Invariante →](./invariante.md)
