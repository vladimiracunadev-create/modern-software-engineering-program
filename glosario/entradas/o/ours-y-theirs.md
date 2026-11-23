# --ours y --theirs

[↑ Glosario](../../README.md) · [--remerge-diff →](../r/remerge-diff.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Resolución de un conflicto tomando el lado de la rama actual o el de la rama que se fusiona.

Definición de trabajo de [SE-203 — Taller: rescatar una integración conflictiva](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md).

## Por qué importa

La clase donde se define, [SE-203 — Taller: rescatar una integración conflictiva](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md), existe con este propósito: el taller existe para practicar bajo presión lo que las clases anteriores explican por separado: una integración con conflictos que se resolvió mal, una rama que otras personas ya tienen y una decisión que hay que tomar con poco tiempo sobre cómo recuperar la intención perdida sin empeorar la historia.

## Cómo funciona

Según [SE-203 — Taller: rescatar una integración conflictiva](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md):

**Cómo leer la figura.** Cada barra es una estrategia aplicada a los mismos seis órdenes; la cifra cuenta cuántos terminan con las cuatro pruebas verdes. **Dónde deja de valer:** el escenario tiene un solo conflicto entre dos ramas, que hace que «ours» y «theirs» sean complementarios; con más conflictos o en archivos distintos ninguna estrategia automática acierta de forma estable, y la resolución manual aquí se escribió conociendo las tres intenciones.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-203 — Taller: rescatar una integración conflictiva](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md):

En la plataforma, una fusión conflictiva se hace en una rama temporal, con `merge.conflictStyle=zdiff3`, y se resuelve leyendo las tres versiones. Antes de abrir el PR, la persona adjunta la salida de `git show --remerge-diff` y ejecuta las pruebas sobre el resultado; el PR añade una prueba para la intención que habría perdido «ours». El procedimiento de rescate del equipo pregunta primero «¿ya se publicó?» y asigna el camino: rehacer o corregir hacia delante, nunca reescribir una rama protegida.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-203 — Taller: rescatar una integración conflictiva](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md)) son:

- **Una rama «integrada» no tiene sus cambios** — causa: se resolvió con un lado o se revirtió la fusión. Corrección: comprobar con `--remerge-diff` y rehacer o corregir hacia delante.
- **Volver a fusionar no hace nada** — causa: la rama es ancestro tras la fusión o su revert. Corrección: revertir el revert o rehacer la fusión desde el primer padre.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** el escenario tiene un solo conflicto entre dos ramas, que hace que «ours» y «theirs» sean complementarios; con más conflictos o en archivos distintos ninguna estrategia automática acierta de forma estable, y la resolución manual aquí se escribió conociendo las tres intenciones. ([SE-203](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Conflicto](../c/conflicto.md).
- **Ver también:** [Resolución](../r/resolucion.md), [Corrección hacia delante](../c/correccion-hacia-delante.md), [Fusión de tres ramas](../f/fusion-de-tres-ramas.md), [Merge --abort](../m/merge-abort.md), [--remerge-diff](../r/remerge-diff.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-203 — Taller: rescatar una integración conflictiva](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [How to revert a faulty merge](https://git-scm.com/docs/howto/revert-a-faulty-merge) — efectos de revertir una fusión; autoridad: documentación de Git.
- [git-merge](https://git-scm.com/docs/git-merge) — `--abort`, estilos de marcas y estrategias; autoridad: documentación de Git.
- [git-show](https://git-scm.com/docs/git-show) — `--remerge-diff`; autoridad: documentación de Git.
- [git-reflog](https://git-scm.com/docs/git-reflog) — recuperación de estados previos; autoridad: documentación de Git.
- [git-revert](https://git-scm.com/docs/git-revert) — revertir commits y fusiones con `-m`; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [--remerge-diff →](../r/remerge-diff.md)
