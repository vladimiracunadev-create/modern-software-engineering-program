# Recuperabilidad

[↑ Glosario](../../README.md) · [← Recreación y comprobación](./recreacion-y-comprobacion.md) · [Recuperación →](./recuperacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Propiedad de una página de poder ser encontrada por alguien que la necesita con las palabras que usa y los caminos que sigue.

Definición de trabajo de [SE-213 — Búsqueda, glosarios y arquitectura de conocimiento](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md).

## Por qué importa

En [SE-213 — Búsqueda, glosarios y arquitectura de conocimiento](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md), el tema «Medir la recuperabilidad» importa porque sin consultas reales no se sabe qué falla; con ellas se corrige donde duele.

## Cómo funciona

Según [SE-213 — Búsqueda, glosarios y arquitectura de conocimiento](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md):

La recuperabilidad se mide con consultas: las reales, tomadas del registro del buscador, y un conjunto de consultas de prueba por tarea. Para cada consulta se registra si una página relevante aparece entre las primeras posiciones, y se vigila la tasa de consultas sin resultado. Esa lista es el insumo del glosario y de los títulos. La medición tiene sus límites: depende de que alguien haya decidido qué página es relevante, y una consulta con resultado no prueba que el lector haya entendido la página.

## Ejemplo

Ejemplo de [SE-213 — Búsqueda, glosarios y arquitectura de conocimiento](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md) (sección «Caso conductor»):

El portal de la plataforma de entregas se vuelve encontrable: glosario de 30 términos, buscador medido y un recorrido que impide páginas huérfanas. Esta clase deja el glosario con alternativas, la medición de recuperabilidad y el comprobador de alcance, que `SE-214` convierte en metadatos para máquinas y `SE-216` incorpora a la auditoría del portal.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-213 — Búsqueda, glosarios y arquitectura de conocimiento](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md)) son:

- **Quien busca con otras palabras no encuentra nada** — causa: el buscador es léxico y no hay alternativas. Corrección: añadir etiquetas alternativas al glosario y a los metadatos.
- **Un término tiene tres definiciones distintas** — causa: se copió y se editó sin fuente única. Corrección: centralizar la definición y enlazarla desde las demás.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-213 — Búsqueda, glosarios y arquitectura de conocimiento](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md)) son: Las definiciones son operativas para el portal; no reemplazan las de SKOS ni las de la bibliografía enlazada abajo. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió a ningún lector ni se evaluó un buscador de producción: el vocabulario de 40 conceptos con tres sinónimos exactos, las definiciones de 14 palabras sorteadas y el sitio aleatorio de 120 páginas son construcciones del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-212](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Página](../p/pagina.md), [Propiedad](../p/propiedad.md), [Etiqueta alternativa](../e/etiqueta-alternativa.md), [Página huérfana](../p/pagina-huerfana.md), [Similitud de Jaccard](../s/similitud-de-jaccard.md), [Vocabulario controlado](../v/vocabulario-controlado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-213 — Búsqueda, glosarios y arquitectura de conocimiento](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

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

[↑ Glosario](../../README.md) · [← Recreación y comprobación](./recreacion-y-comprobacion.md) · [Recuperación →](./recuperacion.md)
