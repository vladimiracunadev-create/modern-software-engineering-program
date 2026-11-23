# Squash

[↑ Glosario](../../README.md) · [← Specification by Example](./specification-by-example.md) · [Srcset →](./srcset.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Integración que reduce los cambios de una rama a un solo commit nuevo.

Definición de trabajo de [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md).

## Por qué importa

En [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md), el tema «Squash» importa porque reduce una rama a un commit y descarta su historia interna.

## Cómo funciona

Según [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md), en la sección «Squash»:

Un squash junta todos los cambios de una rama en un solo commit nuevo en la rama de destino; los commits originales no entran en esa historia. Da una historia lineal con una entrada por cambio y pierde los pasos intermedios, que son útiles para una bisección fina. Conviene cuando los pasos intermedios son ruido y no cuando cada uno es atómico y comprobable.

## Ejemplo

Ejemplo de [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md) (sección «Ejemplo profesional»):

En la plataforma, las ramas de funcionalidad viven pocos días y se integran con squash porque cada una es un cambio de intención única; las ramas de varias personas se integran con fusión para conservar quién hizo qué; las correcciones urgentes se rebasan sobre `main` antes de la revisión. La regla está escrita en `CONTRIBUTING.md`, con una excepción: una rama con commits atómicos y comprobables que alguien podría querer bisecar se integra sin squash.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se pierde la historia de una rama** — causa: squash de una rama de commits atómicos. Corrección: elegir estrategia por rama y documentar la excepción. ([SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un squash junta todos los cambios de una rama en un solo commit nuevo en la rama de destino; los commits originales no entran en esa historia. ([SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-194](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conflicto](../c/conflicto.md), [Conflicto de texto](../c/conflicto-de-texto.md), [Fusión de tres vías](../f/fusion-de-tres-vias.md), [Rebase](../r/rebase.md), [Rerere](../r/rerere.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md).

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

[↑ Glosario](../../README.md) · [← Specification by Example](./specification-by-example.md) · [Srcset →](./srcset.md)
