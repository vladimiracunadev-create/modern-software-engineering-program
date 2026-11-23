# Rastrear

[↑ Glosario](../../README.md) · [← Rareza heredada](./rareza-heredada.md) · [Raw data →](./raw-data.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Pedir una página para leer su contenido y sus enlaces.

Definición de trabajo de [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md).

## Por qué importa

En [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md), el tema «Rastrear, indexar y mostrar» importa porque tres etapas, tres mecanismos; confundirlos deja páginas visibles que se quería ocultar o invisibles que se quería mostrar.

## Cómo funciona

Según [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md):

Un buscador descubre URLs (por enlaces y mapas del sitio), las **rastrea** (pide la página), las **indexa** (decide si la guarda y con qué contenido) y las **muestra** (la ordena entre los resultados de una consulta). Cada etapa tiene sus controles: `robots.txt` actúa sobre rastrear; `noindex` y las canónicas, sobre indexar; el título y la descripción, sobre cómo se muestra. Que una página no se rastree no significa que no pueda aparecer: si otras páginas la enlazan, el buscador puede listar la URL sin su contenido.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md):

La plataforma publica un `robots.txt` que bloquea solo patrones que nunca interesan (`/buscar?`, `/api/`) con los `Allow` más específicos primero y lo comprueba con dos analizadores. Las páginas privadas se protegen con autenticación y devuelven `noindex` en la cabecera, sin estar bloqueadas, para que el rastreador pueda leer esa directiva. La lista de cursos tiene un orden fijo de parámetros, una canónica a la lista base en cada combinación de filtros y enlaces de filtro con `rel="nofollow"`.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md)) son:

- **Una URL bloqueada aparece sin contenido** — causa: `Disallow` en vez de `noindex` o autenticación. Corrección: dejar rastreable con `noindex` o proteger con autenticación.
- **El rastreador se pierde en filtros** — causa: navegación facetada sin contención. Corrección: orden fijo de parámetros, canónica a la lista base y `noindex` en combinaciones.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md)) son: Las definiciones son operativas para esta clase y deben contrastarse con la documentación enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se rastreó ningún sitio ni se consultó ningún buscador: las 14 rutas, los seis filtros y las 120 páginas son construcciones del autor y el auditor comprueba forma, no verdad. La siguiente clase reúne lo aprendido en un taller para construir un flujo web resiliente de punta a punta.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Página](../p/pagina.md), [Indexar](../i/indexar.md), [Navegación facetada](../n/navegacion-facetada.md), [Noindex](../n/noindex.md), [URL canónica](../u/url-canonica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-117](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-117-licencias-procedencia-y-reutilizacion/README.md), [SE-024](../../../classes/part-01-computadores-y-representacion-de-informacion/se-024-proyecto-informe-reproducible-de-comportamiento-y-recursos/README.md), [SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md), [SE-194](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md), [SE-215](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md), [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md), [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md).

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

[↑ Glosario](../../README.md) · [← Rareza heredada](./rareza-heredada.md) · [Raw data →](./raw-data.md)
