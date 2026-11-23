# Keyset

[↑ Glosario](../../README.md) · [← Kernel](./kernel.md) · [KS →](./ks.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Paginación cuyo punto de continuación es el valor de la clave de orden del último elemento visto.

Definición de trabajo de [SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md).

## Por qué importa

La clase donde se define, [SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), existe con este propósito: la clase existe para que modeles la plataforma como recursos con identidad y operaciones de semántica conocida, y para que sepas qué garantiza cada método HTTP (seguro, idempotente, cacheable) y qué se rompe cuando un diseño usa un método con otro sentido.

## Cómo funciona

Según [SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md):

**Cómo leer la figura.** Cada grupo es una estrategia de paginación; la barra dorada son las filas devueltas y la coral las que se devuelven repetidas, mientras llegan 7 entregas nuevas antes de cada página. El offset devuelve 161 filas repetidas porque los datos nuevos desplazan las páginas; el keyset no repite ninguna y devuelve solo 7 filas más que las 1 000 originales, las nuevas. Las dos ven las 1 000 originales, que es lo que la tabla anterior conserva. **Dónde deja de valer:** solo se simularon inserciones. Con borrados, el desplazamiento omite filas en vez de repetirlas, y no se midió. Además la paginación por clave exige un índice sobre la clave de orden; sin él, la consulta recorre toda la tabla (`SE-243`).

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md):

La plataforma define cinco recursos: la colección `/entregas`, la entrega, la nota, la apelación y el estado de un trabajo. Cada operación del panel se asigna a un método: listar y leer con GET (cacheable con revalidación), crear con POST y respuesta 201, editar con PUT y `If-Match` obligatorio, anular con DELETE y apelar con POST sobre `/entregas/{id}/apelaciones`. La colección pagina por clave (fecha y identificador).

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md)) son:

- **Entregas que desaparecen al abrir una página** — causa: una operación destructiva usa GET. Corrección: mover a DELETE y probar con un rastreador.
- **Un docente pierde su cambio sin error** — causa: PUT ciego sobre un recurso editable por varias personas. Corrección: ETag, If-Match y 412 con releer.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El offset devuelve 161 filas repetidas porque los datos nuevos desplazan las páginas; el keyset no repite ninguna y devuelve solo 7 filas más que las 1 000 originales, las nuevas. ([SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Valor](../v/valor.md), [Actualización perdida](../a/actualizacion-perdida.md), [Colección](../c/coleccion.md), [ETag](../e/etag.md), [Método idempotente](../m/metodo-idempotente.md), [Método seguro](../m/metodo-seguro.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110) — métodos seguros e idempotentes, `ETag`, 412 y 428; autoridad: IETF.
- [HTTP Caching (RFC 9111)](https://www.rfc-editor.org/rfc/rfc9111) — reutilización y revalidación de respuestas cacheadas; autoridad: IETF.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — transacciones y consultas del experimento de paginación; autoridad: Python Software Foundation.
- [SQLite: The Query Planner](https://www.sqlite.org/queryplanner.html) — cómo un índice sirve a una consulta por rango; autoridad: SQLite.
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) — descripción de recursos y métodos de una API; autoridad: OpenAPI Initiative.

---

[↑ Glosario](../../README.md) · [← Kernel](./kernel.md) · [KS →](./ks.md)
