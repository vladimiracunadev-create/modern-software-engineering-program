# Etiqueta alternativa

[↑ Glosario](../../README.md) · [← Etiqueta](./etiqueta.md) · [ETL →](./etl.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Sinónimo, forma coloquial o abreviatura de un concepto que lleva a la misma página que la etiqueta preferida.

Definición de trabajo de [SE-213 — Búsqueda, glosarios y arquitectura de conocimiento](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md).

## Por qué importa

La clase donde se define, [SE-213 — Búsqueda, glosarios y arquitectura de conocimiento](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md), existe con este propósito: la clase existe para que trates la recuperabilidad como una propiedad de la documentación que se diseña y se mide: que lo escrito se encuentre con las palabras de quien busca, que los términos signifiquen lo mismo en todas partes y que ninguna página quede fuera del camino de nadie.

## Cómo funciona

Según [SE-213 — Búsqueda, glosarios y arquitectura de conocimiento](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md):

Un glosario con vocabulario controlado asigna a cada concepto una etiqueta preferida y varias alternativas (sinónimos, formas coloquiales, abreviaturas). El modelo SKOS lo formaliza: un concepto tiene una etiqueta preferida y puede tener etiquetas alternativas. En un portal, las alternativas se añaden a los metadatos de la página o se expanden al consultar. El glosario también cumple otra función: fija una definición por término, de modo que «prórroga» signifique lo mismo en el manual del estudiante y en la guía del docente. Mantenerlo exige un responsable y una revisión, como cualquier otra pieza del portal.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-213 — Búsqueda, glosarios y arquitectura de conocimiento](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md):

El portal de la plataforma de entregas mantiene un glosario de 30 términos con etiqueta preferida, alternativas y una definición única que las demás páginas enlazan. El buscador indexa título, cuerpo y alternativas del glosario. El registro de consultas sin resultado se revisa cada mes: «descuento por tarde» pasó a ser una alternativa de «penalización por retraso». Un recorrido en anchura en cada construcción comprueba que no hay huérfanas y que ninguna página está a más de tres clics.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Quien busca con otras palabras no encuentra nada** — causa: el buscador es léxico y no hay alternativas. Corrección: añadir etiquetas alternativas al glosario y a los metadatos. ([SE-213](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-213 — Búsqueda, glosarios y arquitectura de conocimiento](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md)) son: Las definiciones son operativas para el portal; no reemplazan las de SKOS ni las de la bibliografía enlazada abajo. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió a ningún lector ni se evaluó un buscador de producción: el vocabulario de 40 conceptos con tres sinónimos exactos, las definiciones de 14 palabras sorteadas y el sitio aleatorio de 120 páginas son construcciones del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-212](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Etiqueta](./etiqueta.md), [Página](../p/pagina.md), [Página huérfana](../p/pagina-huerfana.md), [Recuperabilidad](../r/recuperabilidad.md), [Similitud de Jaccard](../s/similitud-de-jaccard.md), [Vocabulario controlado](../v/vocabulario-controlado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-213 — Búsqueda, glosarios y arquitectura de conocimiento](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-170](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Robertson y Zaragoza, «The Probabilistic Relevance Framework: BM25 and Beyond» (2009)](https://doi.org/10.1561/1500000019) — función de ordenación BM25; autoridad: Foundations and Trends in Information Retrieval.
- [W3C, SKOS Reference](https://www.w3.org/TR/skos-reference/) — etiquetas preferidas y alternativas de un concepto; autoridad: W3C.
- [Pirolli y Card, «Information Foraging» (Psychological Review, 1999)](https://doi.org/10.1037/0033-295X.106.4.643) — rastros de información y navegación; autoridad: Psychological Review.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — criterios de accesibilidad, incluido ofrecer más de una forma de localizar una página; autoridad: W3C.
- [Diátaxis](https://diataxis.fr/) — organización de la documentación alrededor de necesidades; autoridad: proyecto Diátaxis.

---

[↑ Glosario](../../README.md) · [← Etiqueta](./etiqueta.md) · [ETL →](./etl.md)
