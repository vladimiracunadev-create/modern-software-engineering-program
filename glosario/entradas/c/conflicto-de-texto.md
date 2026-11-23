# Conflicto de texto

[↑ Glosario](../../README.md) · [← Conflicto de intereses](./conflicto-de-intereses.md) · [Conflicto semántico →](./conflicto-semantico.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Región donde dos cambios afectan líneas contiguas respecto de la base y Git no puede decidir.

Definición de trabajo de [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md).

## Por qué importa

La clase donde se define, [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md), existe con este propósito: la clase existe para que integrar el trabajo de varias personas sea una decisión con consecuencias conocidas y no un ritual: elegir entre fusionar, rebasar o aplastar sabiendo qué historia queda, y resolver un conflicto sabiendo qué se decidió y qué se perdió.

## Cómo funciona

Según [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md):

Un conflicto de texto aparece cuando dos cambios afectan líneas contiguas respecto de la base. Git marca ambas versiones; el estilo `diff3` añade la base. Resolver es decidir cuál es el estado correcto, que puede ser uno de los lados, una combinación o algo nuevo. Un conflicto que no aparece no significa que la combinación sea correcta: dos cambios pueden fusionarse sin marcas y romper el programa (`SE-197` lo mide).

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md):

En la plataforma, las ramas de funcionalidad viven pocos días y se integran con squash porque cada una es un cambio de intención única; las ramas de varias personas se integran con fusión para conservar quién hizo qué; las correcciones urgentes se rebasan sobre `main` antes de la revisión. La regla está escrita en `CONTRIBUTING.md`, con una excepción: una rama con commits atómicos y comprobables que alguien podría querer bisecar se integra sin squash.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md)) son:

- **Aparecen commits duplicados tras un rebase** — causa: se rebasó una rama que otra persona ya tenía. Corrección: rebasar solo ramas propias no publicadas o acordadas.
- **Un conflicto reaparece una y otra vez** — causa: la rama vive mucho tiempo y se repite el mismo rebase. Corrección: acortar la rama o activar `rerere` y revisar las resoluciones.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con repositorios temporales y datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún repositorio real, las ediciones al azar son uniformes, el conflicto se midió solo sobre texto y no se midió a ningún equipo. La siguiente clase pregunta cómo se revisan los cambios que llegan por estas integraciones.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-194](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Base](../b/base.md), [Región](../r/region.md), [Conflicto](./conflicto.md), [Fusión de tres vías](../f/fusion-de-tres-vias.md), [Rebase](../r/rebase.md), [Rerere](../r/rerere.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-197](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md), [SE-584](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md).

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

[↑ Glosario](../../README.md) · [← Conflicto de intereses](./conflicto-de-intereses.md) · [Conflicto semántico →](./conflicto-semantico.md)
