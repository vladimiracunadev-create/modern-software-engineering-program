# Rebase

[↑ Glosario](../../README.md) · [← Rebanada](./rebanada.md) · [Rebuild y prueba cruzada →](./rebuild-y-prueba-cruzada.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

El **rebase** es la reaplicación de commits sobre otra base, que crea commits nuevos con otros identificadores ([SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md)). Toma los commits de una rama y los reaplica uno por uno sobre otro punto de partida; el resultado es una historia lineal.

## Por qué importa

Cambia cómo se ve y cómo se comparte la historia. Un rebase limpia la bifurcación (la rama parece haberse escrito sobre la última versión de `main`), pero reescribe los commits. Elegirlo bien evita historias confusas; usarlo donde no corresponde provoca commits duplicados y conflictos repetidos.

## Cómo funciona

Git toma cada commit de la rama, calcula su cambio respecto de su padre y lo aplica sobre la nueva base. Cada commit reaplicado es un **objeto nuevo con otro identificador**, aunque diga lo mismo, porque el identificador depende del contenido, del padre y de los metadatos. Los commits originales siguen existiendo hasta que dejan de ser alcanzables ([SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md)): el registro de movimientos (reflog) permite recuperarlos.

Esa reescritura explica la regla central de [SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md): **rebasar solo ramas propias no publicadas, o ramas acordadas**. Si otra persona ya tiene los commits originales, tras el rebase tendrá commits «duplicados» con otro nombre, y al integrar aparecerán dos versiones del mismo trabajo. Un segundo problema es la repetición: una rama que vive semanas y se rebasa varias veces repite los mismos conflictos; `rerere` (reutilizar resoluciones registradas) ahorra la decisión, pero la rama larga es el problema de fondo ([SE-197](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md)).

La clase insiste en elegir la estrategia por la rama y documentarla (squash para ramas cortas de intención única, fusión cuando importa quién hizo qué, rebase para correcciones urgentes antes de la revisión), en lugar de aplicar una sola a todo, porque se pierde la información que alguna rama sí necesitaba.

## Ejemplo

Una rama `arreglo-plazo` con tres commits sale de `main` en el commit A; mientras tanto `main` avanza a D. Un `git rebase main` reaplica los tres commits sobre D, creando tres commits nuevos (B', C', E'). Si el compañero ya había descargado los originales, ahora ve B, C y E junto a B', C' y E' tras un merge. Con el comando `git pull --rebase` sobre una rama propia no publicada, el mismo proceso es seguro. (Ilustración del mecanismo de Git.)

## Errores y confusiones comunes

- **Commits duplicados tras un rebase**: se rebasó una rama que otra persona ya tenía; corrección: rebasar solo ramas propias no publicadas o acordadas.
- **Un conflicto que reaparece**: la rama vive mucho y se repite el rebase; corrección: acortar la rama o activar `rerere` y revisar las resoluciones.
- **Rebasar `main` o ramas compartidas.**
- **Confundirlo con fusión**: la fusión conserva la forma de la bifurcación y no reescribe commits.

## Límites y cuándo no aplica

Reescribir historia ya publicada obliga a empujes forzados y a coordinar con el equipo. El rebase pierde la información de cuándo se integró cada línea de trabajo. En una rama con commits atómicos que alguien podría querer bisecar, conviene conservarlos (integrar sin squash). Para ramas de vida corta con intención única, el squash suele ser más simple que el rebase.

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
