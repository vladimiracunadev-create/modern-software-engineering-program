# Representación

[↑ Glosario](../../README.md) · [← Reposo](./reposo.md) · [Reproducción →](./reproduccion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md)

## Definición

Estado transferible de un recurso en un formato.

Definición de trabajo de [SE-042 — HTTP, semántica, caché y negociación](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md): Forma concreta (formato y campos) en que un recurso se entrega a un cliente.

## Por qué importa

La clase donde se define, [SE-042 — HTTP, semántica, caché y negociación](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md), existe con este propósito: la clase existe para razonar sobre HTTP por semántica de método, representación, validación, caché y negociación.

## Cómo funciona

Según [SE-042 — HTTP, semántica, caché y negociación](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md):

La URI identifica el objetivo; la respuesta lleva una representación de su estado, no el recurso mismo. Dos formatos pueden representar el mismo recurso. Cambiar de JSON a HTML no debería cambiar la identidad, pero sí metadatos y negociación.

Según [SE-042 — HTTP, semántica, caché y negociación](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md):

Significa que el servidor procesó la petición y devolvió una representación con éxito. Si el cuerpo contiene un error de negocio, o si la operación se encola, la semántica real está en el contrato de la API. Un buen diseño usa el estado para el resultado del protocolo y el cuerpo para el detalle.

## Ejemplo

Ejemplo de [SE-042 — HTTP, semántica, caché y negociación](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md) (sección «Preguntas frecuentes»):

Significa que el servidor procesó la petición y devolvió una representación con éxito. Si el cuerpo contiene un error de negocio, o si la operación se encola, la semántica real está en el contrato de la API. Un buen diseño usa el estado para el resultado del protocolo y el cuerpo para el detalle.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-042 — HTTP, semántica, caché y negociación](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md)) son:

- **Descargar completo un recurso que no cambió** — causa: no se usa validación condicional. Corrección: enviar `If-None-Match` o `If-Modified-Since` y manejar `304`.
- **Mezclar respuestas comprimidas y no comprimidas en una caché** — causa: falta `Vary: Accept-Encoding`. Corrección: declarar `Vary` en las respuestas que varían.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La URI identifica el objetivo; la respuesta lleva una representación de su estado, no el recurso mismo. ([SE-042](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-041](../../../classes/part-03-redes-internet-y-protocolos/se-041-dns-nombres-resolucion-y-fallos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Recurso](./recurso.md), [Actualización perdida](../a/actualizacion-perdida.md), [Alcance](../a/alcance.md), [Colección](../c/coleccion.md), [Diagnóstico](../d/diagnostico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-042 — HTTP, semántica, caché y negociación](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.
- [SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

**También se usa en** (108 clases más lo mencionan; las que más):

[SE-441](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md), [SE-016](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md), [SE-020](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md), [SE-014](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md), [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md), [SE-085](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md), [SE-294](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md), [SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [RFC 9111 — HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111) — define la semántica normativa del protocolo nombrado en el título y sus límites interoperables.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — transacciones y consultas del experimento de paginación; autoridad: Python Software Foundation.
- [SQLite: The Query Planner](https://www.sqlite.org/queryplanner.html) — cómo un índice sirve a una consulta por rango; autoridad: SQLite.
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) — descripción de recursos y métodos de una API; autoridad: OpenAPI Initiative.

---

[↑ Glosario](../../README.md) · [← Reposo](./reposo.md) · [Reproducción →](./reproduccion.md)
