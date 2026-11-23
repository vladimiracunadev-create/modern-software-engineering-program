# Bytecode

[↑ Glosario](../../README.md) · [← Byte](./byte.md) · [Bytes escaneados →](./bytes-escaneados.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Instrucciones de una máquina virtual.

Definición de trabajo de [SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md).

## Por qué importa

En [SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md), el tema «IR/bytecode» importa porque conserva operaciones en formato intermedio

## Cómo funciona

Según [SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md):

**Cómo leer la figura.** La misma línea de código atraviesa cuatro representaciones, y cada una permite una pregunta que la anterior no responde. Los *tokens* separan unidades; el *árbol sintáctico* (AST) muestra cómo se agrupan, de modo que `price * 3` se evalúa antes de sumar `tax`; el *bytecode* es lo que ejecuta la máquina virtual; y solo en la *ejecución* se buscan `price` y `tax` por su nombre y se descubre si existen. En CPython 3.12 puedes ver cada etapa con `tokenize`, `ast.dump`, `dis` y `exec`. **Dónde deja de valer:** otras implementaciones siguen etapas distintas o las fusionan, y el bytecode cambia entre versiones menores (el listado de la figura corresponde a 3.12). El esquema es un modelo para razonar, no una descripción del interior de todos los compiladores.

Según [SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md):

Las dos cosas, en etapas distintas: CPython compila el fuente a bytecode y luego lo interpreta con una máquina virtual. «Interpretado» describe una *estrategia de ejecución* de una implementación, no una propiedad del lenguaje; existen implementaciones de Python con otras estrategias, incluyendo compilación anticipada y JIT.

## Ejemplo

Ejemplo de [SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md) (sección «Ejemplo mínimo»):

`python -m ast` y `python -m dis` ofrecen vistas diferentes del mismo fuente. Cambiar versión puede cambiar bytecode sin cambiar el resultado del lenguaje.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **bytecode = máquina** — causa: niveles confundidos. Corrección: nombra VM y versión. ([SE-020](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Los *tokens* separan unidades; el *árbol sintáctico* (AST) muestra cómo se agrupan, de modo que `price * 3` se evalúa antes de sumar `tax`; el *bytecode* es lo que ejecuta la máquina virtual; y solo en la *ejecución* se buscan `price` y `tax` por su nombre y se descubre si existen. ([SE-020](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Instrucción](../i/instruccion.md).
- **Ver también:** [Máquina virtual](../m/maquina-virtual.md), [AOT](../a/aot.md), [AST](../a/ast.md), [Enlace](../e/enlace.md), [IR](../i/ir.md), [JIT](../j/jit.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-020 — Compilación, interpretación, bytecode y JIT](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (18 clases más lo mencionan; las que más):

[SE-023](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md), [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md), [SE-021](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md), [SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md), [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md), [SE-279](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Byte](./byte.md) · [Bytes escaneados →](./bytes-escaneados.md)
