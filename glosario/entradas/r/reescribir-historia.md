# Reescribir historia

[↑ Glosario](../../README.md) · [← Reentrada](./reentrada.md) · [Reescritura por estructura →](./reescritura-por-estructura.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Crear commits nuevos y mover una referencia, de modo que los identificadores cambian para todos los descendientes.

Definición de trabajo de [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md).

## Por qué importa

En [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md), el tema «Revertir o reescribir» importa porque reescribir historia compartida impone trabajo a quien la tiene; revertir converge sin coordinación.

## Cómo funciona

[SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md):

En la plataforma, cada cambio a `penal.py` va en un commit con una frase de resumen, un cuerpo que explica la regla de negocio afectada y un pie con el issue. Una prueba corta (`pytest -q tests/test_penal.py`) se ejecuta con `git bisect run` cuando una nota sale mal. El equipo exige que cada commit de una rama compile, de modo que la bisección no deba omitir puntos.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md)) son:

- **La bisección no señala un solo commit** — causa: hay un commit que no compila junto al defecto. Corrección: reordenar la rama para que cada paso compile y repetir.
- **Hay que leer cientos de líneas tras la bisección** — causa: el commit culpable mezcla varias intenciones. Corrección: dividir los commits con `git add -p` antes de publicarlos.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con repositorios temporales en Windows y Ubuntu (WSL2) con resultados idénticos. La prueba de bisección fue determinista, el remoto no tenía protección, las historias son de 64 cambios de dos líneas y no se midió a ninguna persona leyendo ni un repositorio real. La siguiente clase pregunta qué pasa cuando varias personas hacen commits a la vez en ramas distintas y cómo se integran.

## Relación con otros conceptos

- **Prerrequisito:** [Referencia](./referencia.md).
- **Ver también:** [Bisección](../b/biseccion.md), [Commit atómico](../c/commit-atomico.md), [Commit colgante](../c/commit-colgante.md), [Recuperación](./recuperacion.md), [Reflog](./reflog.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md), [SE-202](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md), [SE-203](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [git-bisect](https://git-scm.com/docs/git-bisect) — búsqueda binaria y `bisect run`; autoridad: documentación de Git.
- [git-reflog](https://git-scm.com/docs/git-reflog) — registro de movimientos de referencias; autoridad: documentación de Git.
- [git-revert](https://git-scm.com/docs/git-revert) — deshacer con un commit nuevo; autoridad: documentación de Git.
- [git-reset](https://git-scm.com/docs/git-reset) — mover una rama y sus efectos en el índice y el árbol de trabajo; autoridad: documentación de Git.
- [git-fsck](https://git-scm.com/docs/git-fsck) — objetos colgantes y `--lost-found`; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [← Reentrada](./reentrada.md) · [Reescritura por estructura →](./reescritura-por-estructura.md)
