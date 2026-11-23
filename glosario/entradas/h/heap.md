# Heap

[↑ Glosario](../../README.md) · [← Health check](./health-check.md) · [Heap y prioridad parcial →](./heap-y-prioridad-parcial.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Heap almacena objetos de vida dinámica.

Tomado del glosario de [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md).

## Por qué importa

En [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md), el tema «Pila/heap» importa porque separan llamadas y objetos de vida variable

## Cómo funciona

Según [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md):

Cada llamada crea estado lógico: parámetros, locales, retorno y operandos. Objetos cuya vida no coincide con una llamada se asignan en un heap administrado. Optimización puede evitar o mover asignaciones, por lo que este modelo orienta razonamiento pero no prueba ubicación física de cada valor.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md):

Un servicio guarda respuestas en una caché sin límite. Los objetos son alcanzables; no es fallo del GC. Se define tamaño, expiración, métrica y comportamiento al saturarse.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md)) son:

- **toda memoria creciente = fuga GC** — causa: causas no separadas. Corrección: inspecciona alcanzabilidad, caché y memoria nativa.
- **`del` = liberación física** — causa: niveles confundidos. Corrección: habla de referencias y política del runtime.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Objetos cuya vida no coincide con una llamada se asignan en un heap administrado. ([SE-021](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-020](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Objeto](../o/objeto.md), [Finalización](../f/finalizacion.md), [Máquina virtual](../m/maquina-virtual.md), [Objeto alcanzable](../o/objeto-alcanzable.md), [Raíz](../r/raiz.md), [Runtime](../r/runtime.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-086](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-086-pilas-colas-deques-y-prioridades/README.md), [SE-090](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Health check](./health-check.md) · [Heap y prioridad parcial →](./heap-y-prioridad-parcial.md)
