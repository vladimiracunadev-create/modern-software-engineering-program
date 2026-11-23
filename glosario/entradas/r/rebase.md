# Rebase

[↑ Glosario](../../README.md) · [← Rebanada](./rebanada.md) · [Rebuild y prueba cruzada →](./rebuild-y-prueba-cruzada.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Reaplicación de commits sobre otra base que crea commits nuevos con otros identificadores.

Definición de trabajo de [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md).

## Por qué importa

En [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md), el tema «Rebase» importa porque reaplica commits sobre otra base y los reescribe: cambia identificadores.

## Cómo funciona

Según [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md), en la sección «Rebase»:

Un rebase toma los commits de una rama y los reaplica uno por uno sobre otra base. Cada commit reaplicado es un objeto nuevo, con otro identificador, aunque diga lo mismo. La historia resultante es lineal. El costo es que cualquier persona que tenga los commits originales tiene ahora commits «duplicados» con otro nombre; por eso la regla es rebasar solo ramas propias no publicadas, o ramas acordadas.

## Ejemplo

Ejemplo de [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md) (sección «Ejemplo profesional»):

Compara el caso normal con una rama de dos semanas que se rebasa sobre `main` tres veces: cada rebase repite los mismos conflictos y `rerere` ahorra la decisión, pero la rama larga es el problema de fondo (`SE-197`). La práctica es apropiada cuando se elige estrategia por la rama y se documenta; es peligrosa cuando se aplica una sola a todo, porque se pierde la información que la rama sí necesitaba.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Aparecen commits duplicados tras un rebase** — causa: se rebasó una rama que otra persona ya tenía. Corrección: rebasar solo ramas propias no publicadas o acordadas. ([SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md))
- **Un conflicto reaparece una y otra vez** — causa: la rama vive mucho tiempo y se repite el mismo rebase. Corrección: acortar la rama o activar `rerere` y revisar las resoluciones. ([SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un rebase toma los commits de una rama y los reaplica uno por uno sobre otra base. ([SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-194](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Base](../b/base.md), [Sobre](../s/sobre.md), [Conflicto](../c/conflicto.md), [Conflicto de texto](../c/conflicto-de-texto.md), [Fusión de tres vías](../f/fusion-de-tres-vias.md), [Rerere](./rerere.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-196](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md), [SE-194](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [git-rebase](https://git-scm.com/docs/git-rebase) — reaplicación de commits y modo interactivo; autoridad: documentación de Git.
- [GitHub: acerca de rebase](https://docs.github.com/en/get-started/using-git/about-git-rebase) — explicación de rebase por el alojamiento; autoridad: GitHub Docs.
- [git-merge](https://git-scm.com/docs/git-merge) — fusión, avance rápido y squash; autoridad: documentación de Git.
- [Pro Git: Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) — peligros de rebasar commits publicados; autoridad: Pro Git.
- [git-merge-file](https://git-scm.com/docs/git-merge-file) — fusión de tres versiones de un archivo; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [← Rebanada](./rebanada.md) · [Rebuild y prueba cruzada →](./rebuild-y-prueba-cruzada.md)
