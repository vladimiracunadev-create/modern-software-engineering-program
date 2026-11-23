# Indexar

[↑ Glosario](../../README.md) · [← Independencia de fuentes](./independencia-de-fuentes.md) · [Indicador →](./indicador.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Decidir qué guardar de una página rastreada para poder devolverla en búsquedas.

Definición de trabajo de [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md).

## Por qué importa

En [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md), el tema «Rastrear, indexar y mostrar» importa porque tres etapas, tres mecanismos; confundirlos deja páginas visibles que se quería ocultar o invisibles que se quería mostrar.

## Cómo funciona

Según [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md):

Un buscador descubre URLs (por enlaces y mapas del sitio), las **rastrea** (pide la página), las **indexa** (decide si la guarda y con qué contenido) y las **muestra** (la ordena entre los resultados de una consulta). Cada etapa tiene sus controles: `robots.txt` actúa sobre rastrear; `noindex` y las canónicas, sobre indexar; el título y la descripción, sobre cómo se muestra. Que una página no se rastree no significa que no pueda aparecer: si otras páginas la enlazan, el buscador puede listar la URL sin su contenido.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md):

La plataforma publica un `robots.txt` que bloquea solo patrones que nunca interesan (`/buscar?`, `/api/`) con los `Allow` más específicos primero y lo comprueba con dos analizadores. Las páginas privadas se protegen con autenticación y devuelven `noindex` en la cabecera, sin estar bloqueadas, para que el rastreador pueda leer esa directiva. La lista de cursos tiene un orden fijo de parámetros, una canónica a la lista base en cada combinación de filtros y enlaces de filtro con `rel="nofollow"`.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md)) son:

- **Una URL bloqueada aparece sin contenido** — causa: `Disallow` en vez de `noindex` o autenticación. Corrección: dejar rastreable con `noindex` o proteger con autenticación.
- **El rastreador se pierde en filtros** — causa: navegación facetada sin contención. Corrección: orden fijo de parámetros, canónica a la lista base y `noindex` en combinaciones.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Si solo se permite indexar **como mucho una faceta** (y el resto lleva `canonical` a la lista base), quedan **600** URLs. ([SE-238](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Página](../p/pagina.md), [Navegación facetada](../n/navegacion-facetada.md), [Noindex](../n/noindex.md), [Rastrear](../r/rastrear.md), [URL canónica](../u/url-canonica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-066](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md), [SE-594](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md), [SE-097](../../../classes/part-08-entornos-herramientas-y-depuracion/se-097-editores-ide-y-servidores-de-lenguaje/README.md), [SE-213](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md), [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md), [SE-297](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md), [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md), [SE-350](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md).

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

[↑ Glosario](../../README.md) · [← Independencia de fuentes](./independencia-de-fuentes.md) · [Indicador →](./indicador.md)
