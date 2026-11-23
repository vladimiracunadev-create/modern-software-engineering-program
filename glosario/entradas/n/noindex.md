# Noindex

[↑ Glosario](../../README.md) · [← Nodo completo](./nodo-completo.md) · [Nombre accesible →](./nombre-accesible.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Directiva que pide no incluir una página en el índice; solo se obedece si el rastreador puede leerla.

Definición de trabajo de [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md).

## Por qué importa

En [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md), el tema «robots.txt y noindex» importa porque uno limita la lectura y el otro la inclusión; combinarlos mal anula al segundo.

## Cómo funciona

Según [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md):

Un buscador descubre URLs (por enlaces y mapas del sitio), las **rastrea** (pide la página), las **indexa** (decide si la guarda y con qué contenido) y las **muestra** (la ordena entre los resultados de una consulta). Cada etapa tiene sus controles: `robots.txt` actúa sobre rastrear; `noindex` y las canónicas, sobre indexar; el título y la descripción, sobre cómo se muestra. Que una página no se rastree no significa que no pueda aparecer: si otras páginas la enlazan, el buscador puede listar la URL sin su contenido.

Según [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md):

La plataforma publica un `robots.txt` que bloquea solo patrones que nunca interesan (`/buscar?`, `/api/`) con los `Allow` más específicos primero y lo comprueba con dos analizadores. Las páginas privadas se protegen con autenticación y devuelven `noindex` en la cabecera, sin estar bloqueadas, para que el rastreador pueda leer esa directiva. La lista de cursos tiene un orden fijo de parámetros, una canónica a la lista base en cada combinación de filtros y enlaces de filtro con `rel="nofollow"`. El mapa del sitio lista solo las URLs canónicas, y un auditor revisa en la integración continua que cada página tenga título, descripción, canónica absoluta y JSON-LD válido.

## Ejemplo

Ejemplo de [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md) (sección «Ejemplo profesional»):

La plataforma publica un `robots.txt` que bloquea solo patrones que nunca interesan (`/buscar?`, `/api/`) con los `Allow` más específicos primero y lo comprueba con dos analizadores. Las páginas privadas se protegen con autenticación y devuelven `noindex` en la cabecera, sin estar bloqueadas, para que el rastreador pueda leer esa directiva. La lista de cursos tiene un orden fijo de parámetros, una canónica a la lista base en cada combinación de filtros y enlaces de filtro con `rel="nofollow"`. El mapa del sitio lista solo las URLs canónicas, y un auditor revisa en la integración continua que cada página tenga título, descripción, canónica absoluta y JSON-LD válido.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una URL bloqueada aparece sin contenido** — causa: `Disallow` en vez de `noindex` o autenticación. Corrección: dejar rastreable con `noindex` o proteger con autenticación. ([SE-238](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md))
- **El rastreador se pierde en filtros** — causa: navegación facetada sin contención. Corrección: orden fijo de parámetros, canónica a la lista base y `noindex` en combinaciones. ([SE-238](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md))
- **Todo el sitio desaparece tras un despliegue** — causa: plantilla con `noindex` heredada de preproducción. Corrección: auditar metadatos en la integración continua. ([SE-238](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- `noindex` (en una etiqueta `meta` o una cabecera) pide no incluir la página en el índice, pero para que se obedezca el rastreador tiene que **leer** la página: si se bloquea en `robots.txt`, no ve el `noindex`. ([SE-238](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Índice](../i/indice.md), [Página](../p/pagina.md), [Indexar](../i/indexar.md), [Navegación facetada](./navegacion-facetada.md), [Rastrear](../r/rastrear.md), [URL canónica](../u/url-canonica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 9309: Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309) — sintaxis y regla de coincidencia más larga; autoridad: IETF.
- [Google Search Central: introducción a robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro) — qué hace y qué no hace `robots.txt`; autoridad: Google Search Central.
- [Google Search Central: gestionar la navegación facetada](https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation) — contener URLs generadas por filtros; autoridad: Google Search Central.
- [Google Search Central: consolidar URLs duplicadas](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) — canónicas como señal; autoridad: Google Search Central.
- [Sitemaps XML (sitemaps.org)](https://www.sitemaps.org/protocol.html) — formato del mapa del sitio; autoridad: sitemaps.org.

---

[↑ Glosario](../../README.md) · [← Nodo completo](./nodo-completo.md) · [Nombre accesible →](./nombre-accesible.md)
