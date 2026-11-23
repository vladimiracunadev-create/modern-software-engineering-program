# ETag

[↑ Glosario](../../README.md) · [← Estructuras persistentes](./estructuras-persistentes.md) · [Etiqueta →](./etiqueta.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Validador opaco de una representación.

Definición de trabajo de [SE-042 — HTTP, semántica, caché y negociación](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md): Validador opaco que identifica la versión de una representación y permite solicitudes condicionales.

## Por qué importa

La clase donde se define, [SE-042 — HTTP, semántica, caché y negociación](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md), existe con este propósito: la clase existe para razonar sobre HTTP por semántica de método, representación, validación, caché y negociación.

## Cómo funciona

Según [SE-042 — HTTP, semántica, caché y negociación](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md):

Una caché reutiliza respuestas si las reglas lo permiten. `Cache-Control` gobierna frescura; ETag y `If-None-Match` permiten validar sin transferir todo. `no-cache` exige revalidación; no equivale a prohibir almacenamiento. Datos personalizados requieren especial cuidado en cachés compartidas.

Según [SE-042 — HTTP, semántica, caché y negociación](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md):

La petición observable de extremo a extremo expone `GET /health` sin datos sensibles y `POST /diagnoses` con una clave idempotente. Las respuestas de catálogo usan ETag; las del usuario son privadas. Una traza registra método, target, estado, `Age`, `Cache-Control`, `Vary` y tiempo, evitando cuerpos con secretos.

## Ejemplo

Ejemplo de [SE-042 — HTTP, semántica, caché y negociación](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md) (sección «Ejemplo profesional»):

La petición observable de extremo a extremo expone `GET /health` sin datos sensibles y `POST /diagnoses` con una clave idempotente. Las respuestas de catálogo usan ETag; las del usuario son privadas. Una traza registra método, target, estado, `Age`, `Cache-Control`, `Vary` y tiempo, evitando cuerpos con secretos.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un docente pierde su cambio sin error** — causa: PUT ciego sobre un recurso editable por varias personas. Corrección: ETag, If-Match y 412 con releer. ([SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md))
- **La caché sirve datos viejos tras editar** — causa: respuesta cacheable sin validador ni invalidación. Corrección: ETag y revalidación; evitar TTL largos en recursos editables. ([SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- ETag y `If-None-Match` permiten validar sin transferir todo. ([SE-042](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-041](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Representación](../r/representacion.md), [Versión](../v/version.md), [Actualización perdida](../a/actualizacion-perdida.md), [Alcance](../a/alcance.md), [Colección](../c/coleccion.md), [Diagnóstico](../d/diagnostico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-042 — HTTP, semántica, caché y negociación](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.
- [SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110) — métodos seguros e idempotentes, `ETag`, 412 y 428; autoridad: IETF.
- [RFC 9111 — HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — transacciones y consultas del experimento de paginación; autoridad: Python Software Foundation.
- [SQLite: The Query Planner](https://www.sqlite.org/queryplanner.html) — cómo un índice sirve a una consulta por rango; autoridad: SQLite.
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) — descripción de recursos y métodos de una API; autoridad: OpenAPI Initiative.

---

[↑ Glosario](../../README.md) · [← Estructuras persistentes](./estructuras-persistentes.md) · [Etiqueta →](./etiqueta.md)
