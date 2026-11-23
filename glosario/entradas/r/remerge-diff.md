# --remerge-diff

[↑ Glosario](../../README.md) · [← --ours y --theirs](../o/ours-y-theirs.md) · [429 →](../0-9/429.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Vista que muestra lo que una resolución cambió respecto de la fusión automática.

Definición de trabajo de [SE-203 — Taller: rescatar una integración conflictiva](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md).

## Por qué importa

En [SE-203 — Taller: rescatar una integración conflictiva](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md), el tema «Detectar qué se decidió» importa porque `--remerge-diff` y las pruebas muestran qué se perdió.

## Cómo funciona

Según [SE-203 — Taller: rescatar una integración conflictiva](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md):

Una fusión resuelta es un commit con dos padres cuyo árbol no coincide con ninguno. `git show --remerge-diff` rehace la fusión automática y muestra lo que cambió la resolución sobre ella: las líneas que la persona escribió o descartó. Es la herramienta para revisar una resolución, junto con las pruebas del resultado. Si las pruebas no cubren la intención perdida, nada la detecta.

Según [SE-203 — Taller: rescatar una integración conflictiva](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md):

En la plataforma, una fusión conflictiva se hace en una rama temporal, con `merge.conflictStyle=zdiff3`, y se resuelve leyendo las tres versiones. Antes de abrir el PR, la persona adjunta la salida de `git show --remerge-diff` y ejecuta las pruebas sobre el resultado; el PR añade una prueba para la intención que habría perdido «ours». El procedimiento de rescate del equipo pregunta primero «¿ya se publicó?» y asigna el camino: rehacer o corregir hacia delante, nunca reescribir una rama protegida.

## Ejemplo

Ejemplo de [SE-203 — Taller: rescatar una integración conflictiva](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md) (sección «Ejemplo profesional»):

En la plataforma, una fusión conflictiva se hace en una rama temporal, con `merge.conflictStyle=zdiff3`, y se resuelve leyendo las tres versiones. Antes de abrir el PR, la persona adjunta la salida de `git show --remerge-diff` y ejecuta las pruebas sobre el resultado; el PR añade una prueba para la intención que habría perdido «ours». El procedimiento de rescate del equipo pregunta primero «¿ya se publicó?» y asigna el camino: rehacer o corregir hacia delante, nunca reescribir una rama protegida.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una rama «integrada» no tiene sus cambios** — causa: se resolvió con un lado o se revirtió la fusión. Corrección: comprobar con `--remerge-diff` y rehacer o corregir hacia delante. ([SE-203](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-203 — Taller: rescatar una integración conflictiva](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con repositorios temporales y datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. El escenario tiene un único conflicto entre dos ramas, la resolución manual correcta se escribió conociendo las intenciones y no se midió ningún equipo, tiempo ni error humano. La siguiente clase reúne todo en un proyecto: una contribución que otra persona puede revisar, probar, atribuir y fusionar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md), [SE-202](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Fusión](../f/fusion.md), [Resolución](./resolucion.md), [Vista](../v/vista.md), [Corrección hacia delante](../c/correccion-hacia-delante.md), [Fusión de tres ramas](../f/fusion-de-tres-ramas.md), [Merge --abort](../m/merge-abort.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-203 — Taller: rescatar una integración conflictiva](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [git-show](https://git-scm.com/docs/git-show) — `--remerge-diff`; autoridad: documentación de Git.
- [How to revert a faulty merge](https://git-scm.com/docs/howto/revert-a-faulty-merge) — efectos de revertir una fusión; autoridad: documentación de Git.
- [git-merge](https://git-scm.com/docs/git-merge) — `--abort`, estilos de marcas y estrategias; autoridad: documentación de Git.
- [git-reflog](https://git-scm.com/docs/git-reflog) — recuperación de estados previos; autoridad: documentación de Git.
- [git-revert](https://git-scm.com/docs/git-revert) — revertir commits y fusiones con `-m`; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [← --ours y --theirs](../o/ours-y-theirs.md) · [429 →](../0-9/429.md)
