# Documentación como código

[↑ Glosario](../../README.md) · [← Doce factores](./doce-factores.md) · [Documentación ejecutable →](./documentacion-ejecutable.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Práctica de escribir y mantener la documentación con control de versiones, revisión y comprobaciones automáticas.

Definición de trabajo de [SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md).

## Por qué importa

La clase donde se define, [SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md), existe con este propósito: la clase existe para que trates la documentación con las mismas prácticas que el código (control de versiones, revisión, comprobaciones automáticas, publicación reproducible) y para que sepas qué ganas, qué cuesta y qué sigue necesitando a una persona.

## Cómo funciona

[SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el portal; no reemplazan las de las fuentes enlazadas abajo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md):

La documentación de la plataforma de entregas se construye en cada pull request: un comprobador de enlaces y anclas con la regla del sitio, un linter de Markdown consciente de los bloques de código, los comprobadores de las clases anteriores (opciones del README, grafo de ADR, diagrama frente a importaciones, ejemplos de la API, linter de runbooks) y una construcción reproducible cuya huella se publica junto a la página. La revisión humana mira exactitud, tarea de la audiencia y tipo de página, con una lista corta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md)) son:

- **El linter emite cientos de avisos y nadie los lee** — causa: no respeta los bloques de código. Corrección: usar un analizador de Markdown o ignorar las vallas de forma explícita.
- **Un cambio de título rompe enlaces internos sin aviso** — causa: no se comprueban las anclas. Corrección: añadir la comprobación con la regla de ancla del sitio.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md)) son: Las definiciones son operativas para el portal; no reemplazan las de las fuentes enlazadas abajo. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ninguna canalización real ni el tiempo de revisión: el corpus de 60 archivos, la regla de ancla y el linter de tres reglas son construcciones del autor, y la construcción reproducible controla solo tres fuentes de variación.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-211](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Comprobación automática](../c/comprobacion-automatica.md), [Control](../c/control.md), [Práctica](../p/practica.md), [Revisión](../r/revision.md), [Ancla](../a/ancla.md), [Construcción reproducible](../c/construccion-reproducible.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md).

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

[↑ Glosario](../../README.md) · [← Doce factores](./doce-factores.md) · [Documentación ejecutable →](./documentacion-ejecutable.md)
