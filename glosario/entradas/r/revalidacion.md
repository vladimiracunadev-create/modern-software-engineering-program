# Revalidación

[↑ Glosario](../../README.md) · [← Reuse y verificación](./reuse-y-verificacion.md) · [Reverse proxy →](./reverse-proxy.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Comprobación con el origen de si una respuesta obsoleta sigue siendo válida.

Definición de trabajo de [SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md).

## Por qué importa

La clase donde se define, [SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md), existe con este propósito: la clase existe para que decidas qué se guarda en caché y por cuánto tiempo, midas qué compras en aciertos y qué pagas en lecturas obsoletas, evites que una clave caliente que expira haga caer el origen y elijas un limitador de tasa sabiendo qué deja pasar en el borde de su ventana.

## Cómo funciona

Según [SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md):

La plataforma cachea el enunciado de la tarea durante una hora con validador, el estado de una entrega en la caché privada durante 10 s con revalidación y no cachea las notas. La clave del resumen del curso se renueva con una única carga en vuelo y servirá el valor obsoleto hasta 5 s mientras se renueva. Cada identidad tiene una cubeta de 10 solicitudes por segundo con capacidad 20; el exceso recibe 429 con `Retry-After`. Compara con el original en tres casos: cierre de plazo, expiración de una clave caliente y un script mal configurado.

## Ejemplo

Ejemplo de [SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md) (sección «Ejemplo profesional»):

La plataforma cachea el enunciado de la tarea durante una hora con validador, el estado de una entrega en la caché privada durante 10 s con revalidación y no cachea las notas. La clave del resumen del curso se renueva con una única carga en vuelo y servirá el valor obsoleto hasta 5 s mientras se renueva. Cada identidad tiene una cubeta de 10 solicitudes por segundo con capacidad 20; el exceso recibe 429 con `Retry-After`. Compara con el original en tres casos: cierre de plazo, expiración de una clave caliente y un script mal configurado.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Los docentes ven notas viejas** — causa: TTL largo en datos que cambian. Corrección: TTL corto o invalidación al cambiar; revalidación condicional. ([SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2): dos deterministas e idénticos y uno con hilos reales cuyo recuento cambia. No se midió ningún tráfico real ni cliente: la popularidad, los cambios y las ráfagas son construcciones del autor. La siguiente clase pregunta cómo se sabe que el servicio está vivo, listo y cómo se apaga sin perder trabajo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), [SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Origen](../o/origen.md), [429](../0-9/429.md), [Clave de caché](../c/clave-de-cache.md), [Cubeta de fichas](../c/cubeta-de-fichas.md), [Degradación elegante](../d/degradacion-elegante.md), [Lectura obsoleta](../l/lectura-obsoleta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-042](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md), [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), [SE-231](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md), [SE-240](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [HTTP Caching (RFC 9111)](https://www.rfc-editor.org/rfc/rfc9111) — frescura, almacenes de caché y revalidación; autoridad: IETF.
- [Google SRE Book: Handling Overload](https://sre.google/sre-book/handling-overload/) — limitación de tasa y degradación; autoridad: Google.
- [Dean y Barroso, «The tail at scale» (CACM, 2013)](https://doi.org/10.1145/2408776.2408794) — latencia de cola en servicios compuestos; autoridad: Communications of the ACM.
- [Python: collections](https://docs.python.org/3/library/collections.html) — `OrderedDict` usado como LRU; autoridad: Python Software Foundation.
- [Python: threading](https://docs.python.org/3/library/threading.html) — hilos y eventos del experimento; autoridad: Python Software Foundation.

---

[↑ Glosario](../../README.md) · [← Reuse y verificación](./reuse-y-verificacion.md) · [Reverse proxy →](./reverse-proxy.md)
