# AST

[↑ Glosario](../../README.md) · [← ASIL](./asil.md) · [ATDD →](./atdd.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Árbol de estructura sintáctica relevante.

Definición de trabajo de [SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md).

## Por qué importa

La clase donde se define, [SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md), existe con este propósito: la clase existe para seguir fuente, AST, bytecode, IR y ejecución para localizar la etapa que introduce un fallo.

## Cómo funciona

Según [SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md):

Lexer y parser reconocen unidades y gramática; el AST descarta detalles de superficie y conserva estructura. Análisis semántico resuelve nombres, tipos o reglas según lenguaje. Un error de sintaxis ocurre antes de ejecutar la rama, aunque algunos entornos difieran en cuándo procesan el archivo.

## Ejemplo

Ejemplo de [SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md) (sección «Ejemplo mínimo»):

`python -m ast` y `python -m dis` ofrecen vistas diferentes del mismo fuente. Cambiar versión puede cambiar bytecode sin cambiar el resultado del lenguaje.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md)) son:

- **lenguaje clasificado por una palabra** — causa: etapas combinadas ocultas. Corrección: dibuja traducción real de implementación.
- **bytecode = máquina** — causa: niveles confundidos. Corrección: nombra VM y versión.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Los *tokens* separan unidades; el *árbol sintáctico* (AST) muestra cómo se agrupan, de modo que `price * 3` se evalúa antes de sumar `tax`; el *bytecode* es lo que ejecuta la máquina virtual; y solo en la *ejecución* se buscan `price` y `tax` por su nombre y se descubre si existen. ([SE-020](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Árbol](./arbol.md), [Estructura](../e/estructura.md), [AOT](./aot.md), [Bytecode](../b/bytecode.md), [Enlace](../e/enlace.md), [IR](../i/ir.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← ASIL](./asil.md) · [ATDD →](./atdd.md)
