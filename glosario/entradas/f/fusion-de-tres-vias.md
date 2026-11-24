# Fusión de tres vías

[↑ Glosario](../../README.md) · [← Fusión de tres ramas](./fusion-de-tres-ramas.md) · [Fusión errónea →](./fusion-erronea.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

La **fusión de tres vías** (*three-way merge*) es la combinación de dos puntas de rama respecto de su ancestro común, que crea un commit con dos padres. Es el sentido de [SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md) (ramas, integración, rebase y conflictos). Se llama «de tres vías» porque intervienen tres versiones: la base y las dos puntas.

## Por qué importa

Cambia qué queda registrado en la historia. Según [SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md), combina dos cambios respecto de una base común y conserva la forma de la bifurcación: se ve que hubo dos líneas de trabajo, quién hizo qué y cuándo. Frente a alternativas como el squash o el rebase, es la integración que no reescribe nada.

## Cómo funciona

Git compara cada punta con el ancestro común. Lo que cambió solo en un lado se toma tal cual; lo que cambió en ambos lados en lugares distintos se combina automáticamente. Si ambos cambiaron el mismo lugar, Git no decide: deja marcas de conflicto para que una persona resuelva. El resultado es un commit de fusión con dos padres, que fija en la historia el momento de la integración.

La elección de estrategia es una decisión de equipo. En la plataforma de entregas de [SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md), las ramas de funcionalidad viven pocos días y se integran con *squash* porque cada una es un cambio de intención única. Las ramas de varias personas se integran con fusión para conservar quién hizo qué. Las correcciones urgentes se rebasan sobre `main` antes de la revisión. La regla está escrita en `CONTRIBUTING.md`, con una excepción: una rama con commits atómicos y comprobables que alguien podría querer bisecar se integra sin squash. Dos defectos típicos se asocian: commits duplicados tras un rebase de una rama que otra persona ya tenía, y un conflicto que reaparece cuando la rama vive mucho tiempo.

## Ejemplo

Dos personas parten de la misma base. Una cambia la función de cálculo; otra, el texto de ayuda de otro archivo. La fusión de tres vías toma ambos cambios sin conflicto y crea un commit con dos padres. Si ambas hubieran tocado la misma línea, Git dejaría marcas y la resolución sería manual.

## Errores y confusiones comunes

- **Commits duplicados tras un rebase.** Se rebasó una rama que otra persona ya tenía; rebasar solo ramas propias no publicadas o acordadas.
- **El mismo conflicto reaparece.** La rama vive demasiado; acortarla o activar `rerere` y revisar las resoluciones.
- **Creer que sin conflicto la fusión es correcta.** Dos cambios que no chocan textualmente pueden romper el comportamiento juntos.
- **Confundir fusión con rebase.** El rebase reescribe; la fusión añade un commit.

## Límites y cuándo no aplica

Genera un historial más ancho y difícil de leer cuando hay muchas ramas largas. Detecta conflictos textuales, no semánticos: una prueba tras la fusión sigue siendo necesaria. Los experimentos de [SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md) usan repositorios temporales con datos sintéticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-194](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Combinación](../c/combinacion.md), [Conflicto](../c/conflicto.md), [Conflicto de texto](../c/conflicto-de-texto.md), [Rebase](../r/rebase.md), [Rerere](../r/rerere.md), [Squash](../s/squash.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [git-merge](https://git-scm.com/docs/git-merge) — fusión, avance rápido y squash; autoridad: documentación de Git.
- [git-rebase](https://git-scm.com/docs/git-rebase) — reaplicación de commits y modo interactivo; autoridad: documentación de Git.
- [Pro Git: Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) — peligros de rebasar commits publicados; autoridad: Pro Git.
- [git-merge-file](https://git-scm.com/docs/git-merge-file) — fusión de tres versiones de un archivo; autoridad: documentación de Git.
- [git-rerere](https://git-scm.com/docs/git-rerere) — reutilización de resoluciones; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [← Fusión de tres ramas](./fusion-de-tres-ramas.md) · [Fusión errónea →](./fusion-erronea.md)
