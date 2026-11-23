# URL canónica

[↑ Glosario](../../README.md) · [← Unit of Work](./unit-of-work.md) · [Utilidad graduada →](./utilidad-graduada.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

URL preferida de un conjunto de duplicados, declarada con `rel="canonical"` o con una redirección.

Definición de trabajo de [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-234 — Navegación, routing y URLs durables](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md): Forma elegida de una URL entre varias que nombran el mismo recurso, a la que se redirige o se refiere.

## Por qué importa

La clase donde se define, [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md), existe con este propósito: la clase existe para que trates la descubribilidad como una propiedad técnica de la web con tres etapas distintas (rastrear, indexar, mostrar), con herramientas que controlan cosas distintas (robots.txt, `noindex`, canónicas, mapas del sitio, datos estructurados) y con límites que conviene declarar, de modo que «hacer SEO» no signifique añadir etiquetas sin saber qué problema resuelve cada una.

## Cómo funciona

Según [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md):

Un rastreador moderno puede ejecutar JavaScript, pero con límites y con retraso; el contenido que existe en el primer HTML se procesa antes y con menos riesgo. Los enlaces deben ser elementos `a` con `href` reales, no `div` con un manejador; la navegación por JavaScript sin URL no es descubrible. La decisión de renderizado de `SE-231` y las URLs de `SE-234` son aquí SEO: una página con contenido en el HTML inicial y una URL canónica estable es más fácil de descubrir, de compartir y de mantener.

Según [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md):

La plataforma publica un `robots.txt` que bloquea solo patrones que nunca interesan (`/buscar?`, `/api/`) con los `Allow` más específicos primero y lo comprueba con dos analizadores. Las páginas privadas se protegen con autenticación y devuelven `noindex` en la cabecera, sin estar bloqueadas, para que el rastreador pueda leer esa directiva. La lista de cursos tiene un orden fijo de parámetros, una canónica a la lista base en cada combinación de filtros y enlaces de filtro con `rel="nofollow"`. El mapa del sitio lista solo las URLs canónicas, y un auditor revisa en la integración continua que cada página tenga título, descripción, canónica absoluta y JSON-LD válido.

## Ejemplo

Ejemplo de [SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md) (sección «Ejemplo profesional»):

La plataforma publica un `robots.txt` que bloquea solo patrones que nunca interesan (`/buscar?`, `/api/`) con los `Allow` más específicos primero y lo comprueba con dos analizadores. Las páginas privadas se protegen con autenticación y devuelven `noindex` en la cabecera, sin estar bloqueadas, para que el rastreador pueda leer esa directiva. La lista de cursos tiene un orden fijo de parámetros, una canónica a la lista base en cada combinación de filtros y enlaces de filtro con `rel="nofollow"`. El mapa del sitio lista solo las URLs canónicas, y un auditor revisa en la integración continua que cada página tenga título, descripción, canónica absoluta y JSON-LD válido.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md)) son:

- **Una URL bloqueada aparece sin contenido** — causa: `Disallow` en vez de `noindex` o autenticación. Corrección: dejar rastreable con `noindex` o proteger con autenticación.
- **El rastreador se pierde en filtros** — causa: navegación facetada sin contención. Corrección: orden fijo de parámetros, canónica a la lista base y `noindex` en combinaciones.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-238 — SEO, metadatos y descubribilidad](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md)) son: Las definiciones son operativas para esta clase y deben contrastarse con la documentación enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se rastreó ningún sitio ni se consultó ningún buscador: las 14 rutas, los seis filtros y las 120 páginas son construcciones del autor y el auditor comprueba forma, no verdad. La siguiente clase reúne lo aprendido en un taller para construir un flujo web resiliente de punta a punta.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-233](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Recurso](../r/recurso.md), [Redirección](../r/redireccion.md), [Enlace profundo](../e/enlace-profundo.md), [Indexar](../i/indexar.md), [Navegación facetada](../n/navegacion-facetada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-234 — Navegación, routing y URLs durables](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.
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

[↑ Glosario](../../README.md) · [← Unit of Work](./unit-of-work.md) · [Utilidad graduada →](./utilidad-graduada.md)
