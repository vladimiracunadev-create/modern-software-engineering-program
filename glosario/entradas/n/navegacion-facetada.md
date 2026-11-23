# Navegación facetada

[↑ Glosario](../../README.md) · [← NAT](./nat.md) · [Necesidades →](./necesidades.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Conjunto de filtros combinables que produce muchas URLs de listas que se solapan.

Definición de trabajo de [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md).

## Por qué importa

La clase donde se define, [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md), existe con este propósito: la clase existe para que trates la descubribilidad como una propiedad técnica de la web con tres etapas distintas (rastrear, indexar, mostrar), con herramientas que controlan cosas distintas (robots.txt, `noindex`, canónicas, mapas del sitio, datos estructurados) y con límites que conviene declarar, de modo que «hacer SEO» no signifique añadir etiquetas sin saber qué problema resuelve cada una.

## Cómo funciona

Según [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md):

Una navegación facetada (filtros combinables) produce una explosión de URLs que muestran subconjuntos de lo mismo; un buscador puede gastar su presupuesto de rastreo en ellas sin llegar a lo importante. Se contiene combinando medidas: enlaces de filtro que no se siguen, `canonical` hacia la lista base, `noindex` en las combinaciones sin valor propio, `robots.txt` para patrones que nunca interesan y un orden fijo de parámetros. La canónica es una **señal**, no una orden: el buscador puede ignorarla si la considera incoherente.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md):

La plataforma publica un `robots.txt` que bloquea solo patrones que nunca interesan (`/buscar?`, `/api/`) con los `Allow` más específicos primero y lo comprueba con dos analizadores. Las páginas privadas se protegen con autenticación y devuelven `noindex` en la cabecera, sin estar bloqueadas, para que el rastreador pueda leer esa directiva. La lista de cursos tiene un orden fijo de parámetros, una canónica a la lista base en cada combinación de filtros y enlaces de filtro con `rel="nofollow"`.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El rastreador se pierde en filtros** — causa: navegación facetada sin contención. Corrección: orden fijo de parámetros, canónica a la lista base y `noindex` en combinaciones. ([SE-238](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una navegación facetada (filtros combinables) produce una explosión de URLs que muestran subconjuntos de lo mismo; un buscador puede gastar su presupuesto de rastreo en ellas sin llegar a lo importante. ([SE-238](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Filtro](../f/filtro.md), [Indexar](../i/indexar.md), [Noindex](./noindex.md), [Rastrear](../r/rastrear.md), [URL canónica](../u/url-canonica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google Search Central: gestionar la navegación facetada](https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation) — contener URLs generadas por filtros; autoridad: Google Search Central.
- [RFC 9309: Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309) — sintaxis y regla de coincidencia más larga; autoridad: IETF.
- [Google Search Central: introducción a robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro) — qué hace y qué no hace `robots.txt`; autoridad: Google Search Central.
- [Google Search Central: consolidar URLs duplicadas](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) — canónicas como señal; autoridad: Google Search Central.
- [Sitemaps XML (sitemaps.org)](https://www.sitemaps.org/protocol.html) — formato del mapa del sitio; autoridad: sitemaps.org.

---

[↑ Glosario](../../README.md) · [← NAT](./nat.md) · [Necesidades →](./necesidades.md)
