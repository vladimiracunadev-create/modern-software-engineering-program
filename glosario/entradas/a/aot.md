# AOT

[↑ Glosario](../../README.md) · [← Anytime](./anytime.md) · [Apelación →](./apelacion.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Traducción antes de ejecutar.

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

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md)) son:

- **lenguaje clasificado por una palabra** — causa: etapas combinadas ocultas. Corrección: dibuja traducción real de implementación.
- **bytecode = máquina** — causa: niveles confundidos. Corrección: nombra VM y versión.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md)) son: No implementa compilador ni inspecciona código nativo. `SE-021` estudia runtime y memoria automática.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Traducción](../t/traduccion.md), [AST](./ast.md), [Bytecode](../b/bytecode.md), [Enlace](../e/enlace.md), [IR](../i/ir.md), [JIT](../j/jit.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Anytime](./anytime.md) · [Apelación →](./apelacion.md)
