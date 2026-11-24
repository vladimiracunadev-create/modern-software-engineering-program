# Conflicto

[↑ Glosario](../../README.md) · [← Confirmación](./confirmacion.md) · [Conflicto de intereses →](./conflicto-de-intereses.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

**Conflicto** designa, en el programa, una situación de incompatibilidad que se resuelve decidiendo, no ignorando. El sentido base es de [SE-059](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md): objetivos o restricciones incompatibles. Se concreta en otros contextos:

- **En control de versiones** ([SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md)): dos cambios afectan líneas contiguas respecto de una base común.
- **En réplicas** ([SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md)): dos réplicas modificaron el mismo dato sin ver el cambio de la otra, y existen varios estados finales razonables.

## Por qué importa

Un conflicto es información: dice que dos decisiones no caben juntas. Ocultarlo en favor de un resultado limpio produce un modelo falso ([SE-059](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md)). Y resolverlo mal, o creer que no existe porque no hay marcas, entrega un programa roto. La pregunta que cambia: ¿qué estado es el correcto?

## Cómo funciona

- **Texto** ([SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md)): Git marca ambas versiones; el estilo `diff3` añade la base. Resolver es decidir el estado correcto: uno de los lados, una combinación o algo nuevo.
- **Fusión sin marcas** ([SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md), [SE-197](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md)): dos cambios pueden fusionarse sin conflicto textual y romper el programa, porque la compatibilidad semántica no es textual.
- **Réplicas** ([SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md)): al sincronizar datos editados sin conexión, el sistema necesita una política (la última escritura gana, fusión por campos, resolución por el usuario) y debe elegirla de forma explícita.
- **Restricciones** ([SE-059](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md)): se resuelve comprobando si existe alguna implementación válida; si no existe, hay una contradicción real que hay que devolver a quien decide.

## Ejemplo

Dos ramas cambian la misma función: una renombra un parámetro y otra añade una llamada con el nombre antiguo. Git puede fusionarlas sin marcas, pero el programa falla; solo una prueba lo detecta. Ilustración de marcas con `diff3`:

```text
<<<<<<< HEAD
tope = 5
||||||| base
tope = 3
=======
tope = 10
>>>>>>> rama
```

## Errores y confusiones comunes

- **El conflicto reaparece.** Causa: rama de larga vida con el mismo rebase repetido; corrección: acortarla o activar `rerere` y revisar las resoluciones ([SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md)).
- **Se oculta una observación contradictoria.** Causa: se prefiere un resultado limpio; corrección: hacer fallar el modelo con el conflicto ([SE-059](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md)).
- **Tratar un conflicto de recursos como contradicción.** Causa: confusión de conceptos; corrección: comprobar si existe alguna implementación válida ([SE-059](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md)).

## Límites y cuándo no aplica

La ausencia de conflicto no prueba corrección ([SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md)). Los conflictos textuales no existen en datos binarios o generados de la misma forma, y en réplicas no hay una única solución «correcta» sin una regla de negocio. La palabra no significa lo mismo en las tres clases: fija siempre de cuál hablas.

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

**Aparece en los casos de estudio:** [Post Office Horizon](../../../casos/fallo/post-office-horizon.md).

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
