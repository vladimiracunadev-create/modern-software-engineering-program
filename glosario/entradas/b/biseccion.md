# Bisección

[↑ Glosario](../../README.md) · [← Bind mount](./bind-mount.md) · [Bit →](./bit.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

La **bisección** es una búsqueda binaria en el historial entre un commit bueno y uno malo para localizar el cambio que introdujo un defecto ([SE-194](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md)). [SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md) la generaliza: búsqueda binaria del primer cambio defectuoso dividiendo repetidamente un conjunto de cambios, algo que se aplica también a lotes de cambios integrados en una canalización. En Git la implementa `git bisect`.

## Por qué importa

Convierte un historial en una búsqueda de coste logarítmico, siempre que cada punto sea comprobable. Sin bisección, encontrar cuándo se rompió algo exige leer commits uno a uno; con ella, mil commits se resuelven en unas diez pruebas. Cambia cómo se escriben los commits: si la historia se va a bisecar, cada commit debe poder probarse.

## Cómo funciona

Dado un commit bueno y uno malo, se prueba el del medio y se descarta la mitad según el resultado; se repite. Con N commits necesita unas log₂ N ejecuciones: 64 commits en 6 pasos y mil en 10 ([SE-194](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md)). `git bisect run` automatiza el proceso con un programa que devuelve éxito o fallo, de modo que la búsqueda se hace sin intervención.

La técnica requiere dos condiciones. Primero, un **criterio de prueba determinista**: una comprobación corta (por ejemplo, un test concreto) que distinga bueno de malo. Segundo, que **cada punto sea comprobable**: un commit que no compila no es ni bueno ni malo y se omite (código 125 en `bisect run`). Si el defecto está junto a commits omitidos, Git solo puede señalar un conjunto de candidatos. De ahí la regla de la plataforma: cada commit de una rama debe compilar, para que la bisección no deba omitir puntos.

Un segundo requisito es que el commit culpable sea legible. Si mezcla varias intenciones, aunque la bisección lo señale hay que leer cientos de líneas; por eso los commits atómicos y `git add -p` para dividirlos antes de publicar. En [SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md) el mismo principio se aplica a lotes: si una canalización integra varios cambios juntos y falla, se bisecan los lotes para aislar el culpable.

## Ejemplo

En la plataforma, una nota sale mal tras una semana de cambios en `penal.py`. Se marca el commit de hace una semana como bueno y la punta como mala, y se ejecuta `git bisect run pytest -q tests/test_penal.py`. Tras unas seis ejecuciones sobre 64 commits, Git señala el commit que cambió el redondeo. Como ese commit hacía una sola cosa y traía una frase de resumen y el issue, se entiende de inmediato. (Ejemplo derivado de [SE-194](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md).)

## Errores y confusiones comunes

- **La bisección no señala un solo commit**: hay un commit que no compila junto al defecto; corrección: reordenar la rama para que cada paso compile y repetir.
- **Hay que leer cientos de líneas tras bisecar**: el commit culpable mezcla intenciones; corrección: dividir con `git add -p`.
- **Usarla con un defecto intermitente**: la prueba no es determinista y la búsqueda se desvía.
- **Marcar mal el commit «bueno».**

## Límites y cuándo no aplica

No sirve si no hay una prueba automatizable ni un punto bueno conocido, ni con historiales donde el defecto se introduce y corrige varias veces. Para defectos que dependen de la combinación de dos cambios, señala uno de ellos y puede engañar. La transferencia está lograda cuando se sabe qué dependía de poder probar cada punto, no solo de recordar los comandos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Cola de integración](../c/cola-de-integracion.md), [Commit atómico](../c/commit-atomico.md), [Commit colgante](../c/commit-colgante.md), [Conflicto semántico](../c/conflicto-semantico.md), [Integración continua](../i/integracion-continua.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-194 — Commits atómicos, historial y recuperación](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.
- [SE-481 — Integración continua y feedback temprano](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-105](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md), [SE-058](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-058-resolucion-sistematica-y-registro-de-hipotesis/README.md), [SE-107](../../../classes/part-08-entornos-herramientas-y-depuracion/se-107-taller-diagnosticar-un-fallo-desconocido/README.md), [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md), [SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md), [SE-307](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md).

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

[↑ Glosario](../../README.md) · [← Bind mount](./bind-mount.md) · [Bit →](./bit.md)
