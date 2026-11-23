# Conflicto

[↑ Glosario](../../README.md) · [← Confirmación](./confirmacion.md) · [Conflicto de intereses →](./conflicto-de-intereses.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Objetivos o restricciones incompatibles.

Definición de trabajo de [SE-059 — Taller: descomponer un problema ambiguo](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-260 — Offline-first y resolución de conflictos](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md): Situación en que dos réplicas modificaron el mismo dato sin ver el cambio de la otra y existen varios estados finales razonables.

## Por qué importa

En [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md), el tema «Conflictos» importa porque son la señal de que se necesita una decisión; no un error.

## Cómo funciona

Según [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md), en la sección «Conflictos»:

Un conflicto de texto aparece cuando dos cambios afectan líneas contiguas respecto de la base. Git marca ambas versiones; el estilo `diff3` añade la base. Resolver es decidir cuál es el estado correcto, que puede ser uno de los lados, una combinación o algo nuevo. Un conflicto que no aparece no significa que la combinación sea correcta: dos cambios pueden fusionarse sin marcas y romper el programa (`SE-197` lo mide).

## Ejemplo

Ejemplo de [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md) (sección «Ejemplo profesional»):

Compara el caso normal con una rama de dos semanas que se rebasa sobre `main` tres veces: cada rebase repite los mismos conflictos y `rerere` ahorra la decisión, pero la rama larga es el problema de fondo (`SE-197`). La práctica es apropiada cuando se elige estrategia por la rama y se documenta; es peligrosa cuando se aplica una sola a todo, porque se pierde la información que la rama sí necesitaba.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un conflicto reaparece una y otra vez** — causa: la rama vive mucho tiempo y se repite el mismo rebase. Corrección: acortar la rama o activar `rerere` y revisar las resoluciones. ([SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md))
- **Se oculta una observación contradictoria** — causa: se prefiere un resultado limpio. Corrección: hacer fallar el modelo con el conflicto. ([SE-059](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md))
- **Se trata un conflicto de recursos como contradicción** — causa: confusión de conceptos. Corrección: comprobar si existe alguna implementación válida. ([SE-059](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un conflicto que no aparece no significa que la combinación sea correcta: dos cambios pueden fusionarse sin marcas y romper el programa (`SE-197` lo mide). ([SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md))
- Traslada el análisis a otro escenario de combinación de cambios concurrentes (por ejemplo, ediciones simultáneas de un documento o de un archivo de configuración compartido): decide qué sería una base común, qué es un conflicto y cuándo una combinación sin conflicto puede ser incorrecta. ([SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Estado](../e/estado.md), [Réplica](../r/replica.md), [Restricciones](../r/restricciones.md), [Actor](../a/actor.md), [Ambigüedad](../a/ambiguedad.md), [Conflicto de texto](./conflicto-de-texto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-059 — Taller: descomponer un problema ambiguo](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-195 — Ramas, integración, rebase y conflictos](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.
- [SE-260 — Offline-first y resolución de conflictos](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

**También se usa en** (72 clases más lo mencionan; las que más):

[SE-197](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md), [SE-584](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md), [SE-203](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md), [SE-213](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md), [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), [SE-572](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md), [SE-077](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md), [SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Conflictos».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [git-merge-file](https://git-scm.com/docs/git-merge-file) — herramienta usada para medir conflictos.
- [git-merge](https://git-scm.com/docs/git-merge) — fusión, avance rápido y squash; autoridad: documentación de Git.
- [git-rebase](https://git-scm.com/docs/git-rebase) — reaplicación de commits y modo interactivo; autoridad: documentación de Git.
- [Pro Git: Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) — peligros de rebasar commits publicados; autoridad: Pro Git.
- [git-rerere](https://git-scm.com/docs/git-rerere) — reutilización de resoluciones; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [← Confirmación](./confirmacion.md) · [Conflicto de intereses →](./conflicto-de-intereses.md)
