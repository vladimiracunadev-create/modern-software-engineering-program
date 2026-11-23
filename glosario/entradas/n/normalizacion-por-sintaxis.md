# Normalización por sintaxis

[↑ Glosario](../../README.md) · [← Normalización](./normalizacion.md) · [Normalización Unicode →](./normalizacion-unicode.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Transformación que no cambia el significado de una URL (minúsculas del host, codificación porcentual, segmentos de punto).

Definición de trabajo de [SE-234 — Navegación, routing y URLs durables](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md).

## Por qué importa

La clase donde se define, [SE-234 — Navegación, routing y URLs durables](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md), existe con este propósito: la clase existe para que trates la URL como una interfaz pública y duradera: lo que otras personas, otros sistemas y tú mismo guardan, comparten y enlazan.

## Cómo funciona

Según [SE-234 — Navegación, routing y URLs durables](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md):

La RFC 3986 define una normalización por sintaxis que no cambia el significado: el esquema y el host se escriben en minúsculas, el puerto por defecto se omite, los segmentos `.` y `..` se resuelven y la codificación porcentual se uniformiza (mayúsculas hexadecimales y decodificar caracteres no reservados). Más allá de la sintaxis hay decisiones: si la barra final importa, si el orden de los parámetros importa, si `index.html` equivale a la carpeta, si los parámetros de seguimiento cuentan. Esas son decisiones de política y de servidor, no de sintaxis: la ruta puede distinguir mayúsculas.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-234 — Navegación, routing y URLs durables](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md):

La plataforma publica una tabla de URLs: `/entregas/:id` identifica una entrega, `/entregas?estado=tarde&curso=3&pagina=2` describe una vista de la lista, y los parámetros de la vista se leen con un esquema de tipos que ignora lo desconocido. Las rutas se declaran ordenadas por especificidad y una prueba comprueba que cada URL de una lista de ejemplos se resuelve a la vista esperada en cualquier orden de declaración.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-234 — Navegación, routing y URLs durables](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md)) son:

- **Los filtros se pierden al compartir el enlace** — causa: el estado vive solo en memoria. Corrección: llevar a la consulta lo que repite la vista.
- **La misma página cuenta como dos en las métricas** — causa: variantes de la URL sin normalizar (barra final, mayúsculas, utm). Corrección: elegir una forma canónica y redirigir a ella.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La RFC 3986 define una normalización por sintaxis que no cambia el significado: el esquema y el host se escriben en minúsculas, el puerto por defecto se omite, los segmentos `.` y `..` se resuelven y la codificación porcentual se uniformiza (mayúsculas hexadecimales y decodificar caracteres no reservados). ([SE-234](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-233](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Codificación](../c/codificacion.md), [Segmento](../s/segmento.md), [Enlace profundo](../e/enlace-profundo.md), [Redirección permanente](../r/redireccion-permanente.md), [Ruta ambigua](../r/ruta-ambigua.md), [URL canónica](../u/url-canonica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-234 — Navegación, routing y URLs durables](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 3986: URI, sintaxis genérica](https://www.rfc-editor.org/rfc/rfc3986) — sintaxis y normalización de URIs; autoridad: IETF.
- [URL Standard (WHATWG)](https://url.spec.whatwg.org/) — análisis y serialización de URLs en los navegadores; autoridad: WHATWG.
- [HTML Standard: la interfaz de historial (WHATWG)](https://html.spec.whatwg.org/multipage/nav-history-apis.html#the-history-interface) — `pushState` y `popstate`; autoridad: WHATWG.
- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — códigos de redirección y longitud mínima soportada de URIs; autoridad: IETF.
- [W3C: Cool URIs don't change](https://www.w3.org/Provider/Style/URI) — por qué una URL debe perdurar; autoridad: W3C.

---

[↑ Glosario](../../README.md) · [← Normalización](./normalizacion.md) · [Normalización Unicode →](./normalizacion-unicode.md)
