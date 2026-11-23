# Commit atómico

[↑ Glosario](../../README.md) · [← Command](./command.md) · [Commit colgante →](./commit-colgante.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Commit que hace una cosa, deja el repositorio en un estado comprobable y puede revertirse sin arrastrar otra.

Definición de trabajo de [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md).

## Por qué importa

En [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md), el tema «Commits atómicos» importa porque un commit que mezcla cambios obliga a leer todo para entender uno.

## Cómo funciona

Según [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md), en la sección «Commits atómicos»:

Un commit atómico hace una cosa, deja el repositorio en un estado que compila y pasa las pruebas y se puede describir en una frase. La atomicidad no es una cuestión de líneas: un renombre de cuarenta archivos puede ser atómico y una corrección de tres líneas que además cambia un formato no lo es. El criterio práctico es el uso: debe poder revertirse sin arrastrar otra cosa, revisarse sin leer lo ajeno y localizarse con una bisección.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md):

En la plataforma, cada cambio a `penal.py` va en un commit con una frase de resumen, un cuerpo que explica la regla de negocio afectada y un pie con el issue. Una prueba corta (`pytest -q tests/test_penal.py`) se ejecuta con `git bisect run` cuando una nota sale mal. El equipo exige que cada commit de una rama compile, de modo que la bisección no deba omitir puntos.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md)) son:

- **La bisección no señala un solo commit** — causa: hay un commit que no compila junto al defecto. Corrección: reordenar la rama para que cada paso compile y repetir.
- **Hay que leer cientos de líneas tras la bisección** — causa: el commit culpable mezcla varias intenciones. Corrección: dividir los commits con `git add -p` antes de publicarlos.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con repositorios temporales en Windows y Ubuntu (WSL2) con resultados idénticos. La prueba de bisección fue determinista, el remoto no tenía protección, las historias son de 64 cambios de dos líneas y no se midió a ninguna persona leyendo ni un repositorio real. La siguiente clase pregunta qué pasa cuando varias personas hacen commits a la vez en ramas distintas y cómo se integran.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Bisección](../b/biseccion.md), [Commit colgante](./commit-colgante.md), [Recuperación](../r/recuperacion.md), [Reescribir historia](../r/reescribir-historia.md), [Reflog](../r/reflog.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-204](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md), [SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md), [SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md), [SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Commits atómicos».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [git-bisect](https://git-scm.com/docs/git-bisect) — búsqueda binaria y `bisect run`; autoridad: documentación de Git.
- [git-reflog](https://git-scm.com/docs/git-reflog) — registro de movimientos de referencias; autoridad: documentación de Git.
- [git-revert](https://git-scm.com/docs/git-revert) — deshacer con un commit nuevo; autoridad: documentación de Git.
- [git-reset](https://git-scm.com/docs/git-reset) — mover una rama y sus efectos en el índice y el árbol de trabajo; autoridad: documentación de Git.
- [git-fsck](https://git-scm.com/docs/git-fsck) — objetos colgantes y `--lost-found`; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [← Command](./command.md) · [Commit colgante →](./commit-colgante.md)
