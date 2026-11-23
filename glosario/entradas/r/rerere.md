# Rerere

[↑ Glosario](../../README.md) · [← Requisitos universales y negativos](./requisitos-universales-y-negativos.md) · [Reserva →](./reserva.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Mecanismo que guarda resoluciones de conflictos y las reaplica cuando el mismo conflicto reaparece.

Definición de trabajo de [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md).

## Por qué importa

La clase donde se define, [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md), existe con este propósito: la clase existe para que integrar el trabajo de varias personas sea una decisión con consecuencias conocidas y no un ritual: elegir entre fusionar, rebasar o aplastar sabiendo qué historia queda, y resolver un conflicto sabiendo qué se decidió y qué se perdió.

## Cómo funciona

Según [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md):

`git rerere` guarda cómo se resolvió un conflicto y, si vuelve a aparecer el mismo, lo resuelve igual. Es útil cuando una rama larga se rebasa varias veces o cuando se prueba una fusión y se descarta. Reduce el trabajo pero también la atención: una resolución reutilizada se aplica sin que nadie la lea, así que hay que revisarla y volver a ejecutar las pruebas.

Según [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md):

Compara el caso normal con una rama de dos semanas que se rebasa sobre `main` tres veces: cada rebase repite los mismos conflictos y `rerere` ahorra la decisión, pero la rama larga es el problema de fondo (`SE-197`). La práctica es apropiada cuando se elige estrategia por la rama y se documenta; es peligrosa cuando se aplica una sola a todo, porque se pierde la información que la rama sí necesitaba.

## Ejemplo

Ejemplo de [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md) (sección «Ejemplo profesional»):

Compara el caso normal con una rama de dos semanas que se rebasa sobre `main` tres veces: cada rebase repite los mismos conflictos y `rerere` ahorra la decisión, pero la rama larga es el problema de fondo (`SE-197`). La práctica es apropiada cuando se elige estrategia por la rama y se documenta; es peligrosa cuando se aplica una sola a todo, porque se pierde la información que la rama sí necesitaba.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un conflicto reaparece una y otra vez** — causa: la rama vive mucho tiempo y se repite el mismo rebase. Corrección: acortar la rama o activar `rerere` y revisar las resoluciones. ([SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** se repitió exactamente la misma fusión; si la base o alguno de los lados cambió ligeramente, `rerere` no reconoce el conflicto y vuelve a pedir una decisión, y una resolución reaplicada puede ser obsoleta aunque no haya marcas. ([SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-194](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conflicto](../c/conflicto.md), [Guarda](../g/guarda.md), [Mecanismo](../m/mecanismo.md), [Resolución](./resolucion.md), [Conflicto de texto](../c/conflicto-de-texto.md), [Fusión de tres vías](../f/fusion-de-tres-vias.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-203](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [git-rerere](https://git-scm.com/docs/git-rerere) — reutilización de resoluciones; autoridad: documentación de Git.
- [git-merge](https://git-scm.com/docs/git-merge) — fusión, avance rápido y squash; autoridad: documentación de Git.
- [git-rebase](https://git-scm.com/docs/git-rebase) — reaplicación de commits y modo interactivo; autoridad: documentación de Git.
- [Pro Git: Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) — peligros de rebasar commits publicados; autoridad: Pro Git.
- [git-merge-file](https://git-scm.com/docs/git-merge-file) — fusión de tres versiones de un archivo; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [← Requisitos universales y negativos](./requisitos-universales-y-negativos.md) · [Reserva →](./reserva.md)
