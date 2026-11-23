# Ancla

[↑ Glosario](../../README.md) · [← Anchura](./anchura.md) · [Ancla de confianza →](./ancla-de-confianza.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Identificador de un encabezado dentro de una página, generado por el renderizador a partir de su título.

Definición de trabajo de [SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md).

## Por qué importa

En [SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md), el tema «Enlaces y anclas» importa porque un enlace roto es el defecto más frecuente y el más barato de detectar.

## Cómo funciona

Según [SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md):

Un enlace roto es la forma más frecuente de documentación que miente. Hay dos clases: el enlace a un archivo que se movió o renombró, y el enlace a un encabezado cuyo título cambió. La primera se detecta comprobando que la ruta exista; la segunda exige conocer cómo se genera la ancla de un encabezado, y ese algoritmo no está en la especificación de Markdown: cada renderizador convierte los títulos en identificadores con sus propias reglas (minúsculas, eliminación de signos, guiones por espacios, sufijos para duplicados). Un comprobador que use una regla distinta de la del sitio publicado dará falsas alarmas o dejará pasar enlaces rotos.

Según [SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md):

La documentación de la plataforma de entregas se construye en cada pull request: un comprobador de enlaces y anclas con la regla del sitio, un linter de Markdown consciente de los bloques de código, los comprobadores de las clases anteriores (opciones del README, grafo de ADR, diagrama frente a importaciones, ejemplos de la API, linter de runbooks) y una construcción reproducible cuya huella se publica junto a la página. La revisión humana mira exactitud, tarea de la audiencia y tipo de página, con una lista corta. Cuando alguien renombra la página de penalización, el comprobador lista los 12 enlaces que apuntan a ella y el pull request no se fusiona hasta corregirlos.

## Ejemplo

Ejemplo de [SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula la ancla de dos encabezados y detecta un enlace roto. Antes de ejecutarlo, predice qué enlace queda marcado.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un cambio de título rompe enlaces internos sin aviso** — causa: no se comprueban las anclas. Corrección: añadir la comprobación con la regla de ancla del sitio. ([SE-212](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La primera se detecta comprobando que la ruta exista; la segunda exige conocer cómo se genera la ancla de un encabezado, y ese algoritmo no está en la especificación de Markdown: cada renderizador convierte los títulos en identificadores con sus propias reglas (minúsculas, eliminación de signos, guiones por espacios, sufijos para duplicados). ([SE-212](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-211](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Página](../p/pagina.md), [Construcción reproducible](../c/construccion-reproducible.md), [Documentación como código](../d/documentacion-como-codigo.md), [Enlace roto](../e/enlace-roto.md), [Huella](../h/huella.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (16 clases más lo mencionan; las que más):

[SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md), [SE-564](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md), [SE-299](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md), [SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md), [SE-043](../../../classes/part-03-redes-internet-y-protocolos/se-043-tls-certificados-y-confianza-en-transito/README.md), [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), [SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md), [SE-531](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-531-comunicacion-facilitacion-y-conflicto/README.md).

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

[↑ Glosario](../../README.md) · [← Anchura](./anchura.md) · [Ancla de confianza →](./ancla-de-confianza.md)
