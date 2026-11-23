# Similitud de Jaccard

[↑ Glosario](../../README.md) · [← Silo, puente, pool](./silo-puente-pool.md) · [SIMT →](./simt.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Cociente entre las palabras comunes de dos textos y las palabras totales de ambos.

Definición de trabajo de [SE-213 — Búsqueda, glosarios y arquitectura de conocimiento](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md).

## Por qué importa

La clase donde se define, [SE-213 — Búsqueda, glosarios y arquitectura de conocimiento](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md), existe con este propósito: la clase existe para que trates la recuperabilidad como una propiedad de la documentación que se diseña y se mide: que lo escrito se encuentre con las palabras de quien busca, que los términos signifiquen lo mismo en todas partes y que ninguna página quede fuera del camino de nadie.

## Cómo funciona

Según [SE-213 — Búsqueda, glosarios y arquitectura de conocimiento](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md):

Se simulan 20 términos con definiciones de 14 palabras. Para cada término se generan 12 paráfrasis (se reordenan las palabras y se cambian 3 por sinónimos) y 12 definiciones en conflicto (se cambia 1 palabra clave por un número distinto), 240 pares de cada clase. Se calcula la similitud de Jaccard (palabras comunes sobre palabras totales) respecto a la definición original.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-213 — Búsqueda, glosarios y arquitectura de conocimiento](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md):

El portal de la plataforma de entregas mantiene un glosario de 30 términos con etiqueta preferida, alternativas y una definición única que las demás páginas enlazan. El buscador indexa título, cuerpo y alternativas del glosario. El registro de consultas sin resultado se revisa cada mes: «descuento por tarde» pasó a ser una alternativa de «penalización por retraso». Un recorrido en anchura en cada construcción comprueba que no hay huérfanas y que ninguna página está a más de tres clics.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-213 — Búsqueda, glosarios y arquitectura de conocimiento](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md)) son:

- **Quien busca con otras palabras no encuentra nada** — causa: el buscador es léxico y no hay alternativas. Corrección: añadir etiquetas alternativas al glosario y a los metadatos.
- **Un término tiene tres definiciones distintas** — causa: se copió y se editó sin fuente única. Corrección: centralizar la definición y enlazarla desde las demás.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-213 — Búsqueda, glosarios y arquitectura de conocimiento](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md)) son: Las definiciones son operativas para el portal; no reemplazan las de SKOS ni las de la bibliografía enlazada abajo. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió a ningún lector ni se evaluó un buscador de producción: el vocabulario de 40 conceptos con tres sinónimos exactos, las definiciones de 14 palabras sorteadas y el sitio aleatorio de 120 páginas son construcciones del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-212](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Etiqueta alternativa](../e/etiqueta-alternativa.md), [Página huérfana](../p/pagina-huerfana.md), [Recuperabilidad](../r/recuperabilidad.md), [Vocabulario controlado](../v/vocabulario-controlado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-213 — Búsqueda, glosarios y arquitectura de conocimiento](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md).

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

[↑ Glosario](../../README.md) · [← Silo, puente, pool](./silo-puente-pool.md) · [SIMT →](./simt.md)
