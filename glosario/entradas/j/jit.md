# JIT

[↑ Glosario](../../README.md) · [← Iterable](../i/iterable.md) · [Job →](./job.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Traducción durante ejecución.

Definición de trabajo de [SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md).

## Por qué importa

En [SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md), el tema «AOT/JIT» importa porque elige cuándo generar código

## Cómo funciona

Según [SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md):

Un intérprete ejecuta una representación mediante otro programa. AOT genera artefactos antes de ejecutar. Un JIT compila durante ejecución, usando información observada. Una VM puede interpretar al inicio y compilar rutas calientes después. La elección considera arranque, pico, portabilidad, memoria, depuración y distribución.

Según [SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md):

Una función JIT tarda al inicio y mejora después de calentamiento. Un benchmark que mide una sola llamada favorece AOT; otro que descarta arranque favorece estado estable. Se reportan ambos según uso.

## Ejemplo

Ejemplo de [SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md) (sección «Ejemplo profesional»):

Una función JIT tarda al inicio y mejora después de calentamiento. Un benchmark que mide una sola llamada favorece AOT; otro que descarta arranque favorece estado estable. Se reportan ambos según uso.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **benchmark ignora calentamiento** — causa: JIT/arranque omitido. Corrección: mide fases por separado. ([SE-020](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Lo que distingue a un JIT no es ser «más rápido», sino pagar un costo de arranque y de memoria para obtener un rendimiento sostenido mayor *si* el programa vive lo suficiente y su perfil es representativo. ([SE-020](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Traducción](../t/traduccion.md), [AOT](../a/aot.md), [AST](../a/ast.md), [Bytecode](../b/bytecode.md), [Enlace](../e/enlace.md), [IR](../i/ir.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Iterable](../i/iterable.md) · [Job →](./job.md)
