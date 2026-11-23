# Enlace roto

[↑ Glosario](../../README.md) · [← Enlace profundo](./enlace-profundo.md) · [Enlace simbólico →](./enlace-simbolico.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Referencia a un archivo o a una ancla que no existe en el conjunto publicado.

Definición de trabajo de [SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md).

## Por qué importa

En [SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md), el tema «Enlaces y anclas» importa porque un enlace roto es el defecto más frecuente y el más barato de detectar.

## Cómo funciona

Según [SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md):

Un enlace roto es la forma más frecuente de documentación que miente. Hay dos clases: el enlace a un archivo que se movió o renombró, y el enlace a un encabezado cuyo título cambió. La primera se detecta comprobando que la ruta exista; la segunda exige conocer cómo se genera la ancla de un encabezado, y ese algoritmo no está en la especificación de Markdown: cada renderizador convierte los títulos en identificadores con sus propias reglas (minúsculas, eliminación de signos, guiones por espacios, sufijos para duplicados). Un comprobador que use una regla distinta de la del sitio publicado dará falsas alarmas o dejará pasar enlaces rotos.

## Ejemplo

Ejemplo de [SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula la ancla de dos encabezados y detecta un enlace roto. Antes de ejecutarlo, predice qué enlace queda marcado.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md)) son:

- **El linter emite cientos de avisos y nadie los lee** — causa: no respeta los bloques de código. Corrección: usar un analizador de Markdown o ignorar las vallas de forma explícita.
- **Un cambio de título rompe enlaces internos sin aviso** — causa: no se comprueban las anclas. Corrección: añadir la comprobación con la regla de ancla del sitio.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md)) son: Las definiciones son operativas para el portal; no reemplazan las de las fuentes enlazadas abajo. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ninguna canalización real ni el tiempo de revisión: el corpus de 60 archivos, la regla de ancla y el linter de tres reglas son construcciones del autor, y la construcción reproducible controla solo tres fuentes de variación.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-211](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ancla](../a/ancla.md), [Conjunto](../c/conjunto.md), [Referencia](../r/referencia.md), [Construcción reproducible](../c/construccion-reproducible.md), [Documentación como código](../d/documentacion-como-codigo.md), [Huella](../h/huella.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md), [SE-264](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md), [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), [SE-424](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Write the Docs: Docs as Code](https://www.writethedocs.org/guide/docs-as-code/) — práctica y herramientas; autoridad: Write the Docs.
- [CommonMark: especificación](https://spec.commonmark.org/) — sintaxis de Markdown; autoridad: proyecto CommonMark.
- [GitHub Flavored Markdown: especificación](https://github.github.com/gfm/) — extensiones de Markdown de GitHub; autoridad: GitHub.
- [markdownlint: reglas](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md) — catálogo de reglas de estilo de Markdown; autoridad: proyecto markdownlint.
- [Reproducible Builds: documentación](https://reproducible-builds.org/docs/) — causas de variación y prácticas; autoridad: proyecto Reproducible Builds.

---

[↑ Glosario](../../README.md) · [← Enlace profundo](./enlace-profundo.md) · [Enlace simbólico →](./enlace-simbolico.md)
