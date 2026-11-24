# Triaje por riesgo

[↑ Glosario](../../README.md) · [← Triaje](./triaje.md) · [Triangulación →](./triangulacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

El **triaje por riesgo** es el orden de lectura de un cambio según el riesgo esperado de cada parte, y no según su orden de aparición ([SE-196](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md)). Es una técnica de revisión de código: la revisora decide por dónde empezar y cuánta atención dar a cada archivo en función de cuánto cuesta equivocarse en él.

## Por qué importa

Los archivos de un cambio no tienen el mismo riesgo: una migración de datos, la autenticación o la configuración son más caras de equivocar que la documentación. Una revisora que lee en el orden del diff gasta su atención en lo que viene primero y puede agotarla antes de llegar a lo crítico. Cambia el reparto de la atención donde es más probable un defecto de alto costo.

## Cómo funciona

El triaje ordena la lectura por **riesgo esperado**: qué tocó cada archivo, cuánto cambió y cuánto cuesta equivocarse. Es una heurística con supuestos (qué tipos de archivo son riesgosos) que deben **declararse y revisarse con los defectos reales que se escapen**. La plantilla del pull request ayuda: pide qué cambia, por qué, cómo se probó y qué archivos merecen más atención.

[SE-196](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md) demuestra el efecto con una prueba: con un presupuesto de lectura del 30 % en el orden de aparición, la revisora no alcanza la migración; con triaje por riesgo, la lee primero. La razón es que la atención es un recurso finito y el orden decide en qué se gasta.

El triaje se combina con automatización: un flujo de integración continua ejecuta formato, pruebas, análisis estático y búsqueda de secretos **antes** de asignar revisora, de modo que lo mecánico no ocupa atención humana. El archivo de propietarios (CODEOWNERS, [SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md)) añade como revisor obligatorio al equipo dueño de las migraciones cuando un PR toca `migraciones/`. La revisora abre primero los archivos de riesgo alto, lee la descripción y, tras las correcciones, usa `range-diff` para ver solo lo que cambió.

## Ejemplo

Un PR toca cinco archivos: un cambio de texto en la documentación, una prueba, una migración que altera una columna de notas, la configuración del plazo y un comentario. Con triaje, el orden de lectura es migración, configuración, prueba, texto y comentario. Si el presupuesto de atención se acaba, lo que queda sin leer es lo de menor riesgo. (Ilustración construida con el criterio de [SE-196](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md).)

## Errores y confusiones comunes

- **Comentarios de estilo mientras se escapan defectos**: la lectura sigue el orden del diff; corrección: ordenar por riesgo y automatizar el estilo.
- **Releer todo tras cada corrección**: la rama se reescribió sin mostrar lo cambiado; corrección: `range-diff` o commits de corrección.
- **Clasificar el riesgo por tamaño**: un cambio de una línea en autenticación puede ser más riesgoso que cien líneas de documentación.
- **No actualizar los supuestos** tras defectos que se escapan.

## Límites y cuándo no aplica

El triaje depende de que los supuestos de riesgo sean razonables; si una categoría considerada inocua esconde defectos, la lectura se desvía. En cambios pequeños, el orden da igual. No sustituye la lectura completa cuando el cambio es crítico: ordena la atención, no la reduce por debajo de lo necesario.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Riesgo](../r/riesgo.md), [Comprobación automática](../c/comprobacion-automatica.md), [Pila de PR](../p/pila-de-pr.md), [Pull request](../p/pull-request.md), [Range-diff](../r/range-diff.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-196 — Pull requests y revisión basada en riesgo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Sadowski et al., «Modern code review: a case study at Google» (ICSE-SEIP, 2018)](https://doi.org/10.1145/3183519.3183525) — práctica de revisión en una organización grande; autoridad: ACM/IEEE ICSE-SEIP.
- [Bacchelli y Bird, «Expectations, outcomes, and challenges of modern code review» (ICSE, 2013)](https://doi.org/10.1109/ICSE.2013.6606617) — expectativas y dificultades de la revisión; autoridad: IEEE ICSE.
- [Google Engineering Practices: code review](https://google.github.io/eng-practices/review/) — guía de revisión y tamaño de cambios; autoridad: Google.
- [git-range-diff](https://git-scm.com/docs/git-range-diff) — comparación entre series de commits; autoridad: documentación de Git.
- [git-rebase](https://git-scm.com/docs/git-rebase) — `--update-refs`, `--onto` y `--autosquash`; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [← Triaje](./triaje.md) · [Triangulación →](./triangulacion.md)
