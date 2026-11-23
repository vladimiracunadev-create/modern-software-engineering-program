# Pila de PR

[↑ Glosario](../../README.md) · [← Pie de commit](./pie-de-commit.md) · [Pila y disciplina lifo →](./pila-y-disciplina-lifo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Serie de pull requests encadenados donde cada uno parte de la rama del anterior.

Definición de trabajo de [SE-196 — Pull requests y revisión basada en riesgo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md).

## Por qué importa

La clase donde se define, [SE-196 — Pull requests y revisión basada en riesgo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md), existe con este propósito: la clase existe para que una revisión de cambios sea una decisión sobre dónde poner la atención limitada de una persona y no un trámite ni una lectura lineal de un diff.

## Cómo funciona

Según [SE-196 — Pull requests y revisión basada en riesgo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md):

La capacidad de atención de una persona es finita y un cambio grande se revisa por encima. Dividir no es solo partir un diff: cada parte debe tener sentido por sí misma, compilar y poder revertirse sola. Un PR de refactor mecánico (un renombre masivo) puede ser grande y revisable si se separa del cambio de lógica; uno de lógica no. Una pila de PR encadenados reduce lo que se lee pero tiene un costo: corregir el primero obliga a reapilar los demás.

## Ejemplo

Caso medido en la sección «Una pila de PR y la corrección del primero» de [SE-196 — Pull requests y revisión basada en riesgo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md):

Cuatro PR apilados cambian cada uno una línea distinta de un archivo de 60 líneas. El autor corrige el primero y reapila con `git rebase --update-refs --onto`. Con la corrección en **una zona lejana**, el reapilado no tuvo conflictos y actualizó las 3 ramas dependientes. Con la corrección **junto a la línea que edita el segundo PR**, Git se detuvo con conflicto y no actualizó ninguna de las 3.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-196 — Pull requests y revisión basada en riesgo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md)) son:

- **Comentarios de estilo y defectos que se escapan** — causa: la lectura sigue el orden del diff. Corrección: ordenar por riesgo y automatizar el estilo.
- **Hay que releer todo tras cada corrección** — causa: la rama se reescribió sin mostrar lo cambiado. Corrección: usar `range-diff` o commits de corrección.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-196 — Pull requests y revisión basada en riesgo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con repositorios temporales y datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. Las densidades de defectos y el presupuesto de lectura son supuestos del autor, el criterio por riesgo se evaluó con los mismos tipos que usó el generador y no se midió a ningún revisor ni un proyecto real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Pull request](./pull-request.md), [Encadenado](../e/encadenado.md), [Comprobación automática](../c/comprobacion-automatica.md), [Range-diff](../r/range-diff.md), [Triaje por riesgo](../t/triaje-por-riesgo.md).
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

[↑ Glosario](../../README.md) · [← Pie de commit](./pie-de-commit.md) · [Pila y disciplina lifo →](./pila-y-disciplina-lifo.md)
