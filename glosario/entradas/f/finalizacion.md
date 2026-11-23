# Finalización

[↑ Glosario](../../README.md) · [← Filtro con estado](./filtro-con-estado.md) · [FinOps Engineer →](./finops-engineer.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Acción asociada al fin de vida, no garantía de liberación inmediata.

Definición de trabajo de [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md).

## Por qué importa

La clase donde se define, [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md), existe con este propósito: la clase existe para razonar sobre carga, memoria y recolección separando especificación de estrategia del runtime.

## Cómo funciona

Según [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md):

La memoria automática gestiona *objetos*, no *recursos*: un archivo, un socket o una transacción de base de datos viven fuera del heap. Que el objeto Python que los representa quede inalcanzable no garantiza que el recurso se cierre en el momento oportuno. Los *finalizadores* (`__del__`) se ejecutan cuando el objeto se libera, algo que en CPython suele ser inmediato para objetos sin ciclos pero que no está garantizado por el lenguaje, y que no ocurre de forma determinista en otras implementaciones. La JVM lo reconoció: la finalización está *deprecada para su eliminación* desde JDK 18 (JEP 421) por su imprevisibilidad.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md):

Un servicio guarda respuestas en una caché sin límite. Los objetos son alcanzables; no es fallo del GC. Se define tamaño, expiración, métrica y comportamiento al saturarse.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md)) son:

- **toda memoria creciente = fuga GC** — causa: causas no separadas. Corrección: inspecciona alcanzabilidad, caché y memoria nativa.
- **`del` = liberación física** — causa: niveles confundidos. Corrección: habla de referencias y política del runtime.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md)) son: No perfila memoria nativa ni compara recolectores productivos. `SE-022` diseña mediciones de rendimiento y energía.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-020](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Garantía](../g/garantia.md), [Máquina virtual](../m/maquina-virtual.md), [Objeto alcanzable](../o/objeto-alcanzable.md), [Raíz](../r/raiz.md), [Runtime](../r/runtime.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-021 — Runtimes, máquinas virtuales y recolección de basura](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (10 clases más lo mencionan; las que más):

[SE-007](../../../classes/part-00-ingenieria-de-software-como-profesion/se-007-calidad-interna-externa-y-calidad-en-uso/README.md), [SE-009](../../../classes/part-00-ingenieria-de-software-como-profesion/se-009-sostenibilidad-inclusion-y-responsabilidad-social/README.md), [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md), [SE-078](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md), [SE-079](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md), [SE-080](../../../classes/part-06-paradigmas-de-programacion/se-080-programacion-reactiva-y-flujos/README.md), [SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Filtro con estado](./filtro-con-estado.md) · [FinOps Engineer →](./finops-engineer.md)
