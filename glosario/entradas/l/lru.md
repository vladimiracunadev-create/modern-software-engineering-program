# LRU

[↑ Glosario](../../README.md) · [← LPT](./lpt.md) · [LSB →](./lsb.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Política que expulsa la entrada usada hace más tiempo.

Definición de trabajo de [SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md).

## Por qué importa

La clase donde se define, [SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md), existe con este propósito: la clase existe para que decidas qué se guarda en caché y por cuánto tiempo, midas qué compras en aciertos y qué pagas en lecturas obsoletas, evites que una clave caliente que expira haga caer el origen y elijas un limitador de tasa sabiendo qué deja pasar en el borde de su ventana.

## Cómo funciona

Según [SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md):

La caché tiene espacio finito y expulsa entradas (por ejemplo, la usada hace más tiempo: LRU). Si la popularidad de las claves está muy concentrada (pocas entregas muy consultadas), unas pocas entradas dan muchos aciertos; si es plana, hace falta mucho espacio. En la simulación con 5 000 claves y popularidad Zipf, 50 entradas dan 34 % de aciertos con cualquier TTL, 500 dan entre 58 y 65 % y 2 500 llegan a 88 % con TTL largo. Aumentar el TTL con poca capacidad no compra aciertos.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md):

La plataforma cachea el enunciado de la tarea durante una hora con validador, el estado de una entrega en la caché privada durante 10 s con revalidación y no cachea las notas. La clave del resumen del curso se renueva con una única carga en vuelo y servirá el valor obsoleto hasta 5 s mientras se renueva. Cada identidad tiene una cubeta de 10 solicitudes por segundo con capacidad 20; el exceso recibe 429 con `Retry-After`.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md)) son:

- **Los docentes ven notas viejas** — causa: TTL largo en datos que cambian. Corrección: TTL corto o invalidación al cambiar; revalidación condicional.
- **La caché no mejora la carga** — causa: capacidad menor que la popularidad concentrada. Corrección: medir aciertos y dimensionar la capacidad.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2): dos deterministas e idénticos y uno con hilos reales cuyo recuento cambia. No se midió ningún tráfico real ni cliente: la popularidad, los cambios y las ráfagas son construcciones del autor. La siguiente clase pregunta cómo se sabe que el servicio está vivo, listo y cómo se apaga sin perder trabajo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), [SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [429](../0-9/429.md), [Clave de caché](../c/clave-de-cache.md), [Cubeta de fichas](../c/cubeta-de-fichas.md), [Degradación elegante](../d/degradacion-elegante.md), [Lectura obsoleta](./lectura-obsoleta.md), [Ráfaga](../r/rafaga.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-249 — Caching, rate limiting y protección](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: collections](https://docs.python.org/3/library/collections.html) — `OrderedDict` usado como LRU; autoridad: Python Software Foundation.
- [HTTP Caching (RFC 9111)](https://www.rfc-editor.org/rfc/rfc9111) — frescura, almacenes de caché y revalidación; autoridad: IETF.
- [Google SRE Book: Handling Overload](https://sre.google/sre-book/handling-overload/) — limitación de tasa y degradación; autoridad: Google.
- [Dean y Barroso, «The tail at scale» (CACM, 2013)](https://doi.org/10.1145/2408776.2408794) — latencia de cola en servicios compuestos; autoridad: Communications of the ACM.
- [Python: threading](https://docs.python.org/3/library/threading.html) — hilos y eventos del experimento; autoridad: Python Software Foundation.

---

[↑ Glosario](../../README.md) · [← LPT](./lpt.md) · [LSB →](./lsb.md)
