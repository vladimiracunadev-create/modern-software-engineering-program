# Compilación JIT

[↑ Glosario](../../README.md) · [← Competencia](./competencia.md) · [Compilación y front-end →](./compilacion-y-front-end.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Traducción del bytecode a instrucciones nativas al cargar el programa.

Definición de trabajo de [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md).

## Por qué importa

La clase donde se define, [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md), existe con este propósito: la clase existe para que entiendas eBPF como lo que es en la práctica: un mecanismo para cargar programas pequeños en el núcleo de Linux sin recompilarlo ni reiniciarlo, con un verificador que decide antes de ejecutar si el programa es seguro.

## Cómo funciona

Según [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md):

Un programa eBPF es una secuencia de instrucciones de 8 bytes (con una excepción de 16 para cargar constantes de 64 bits) para una máquina de registros: diez registros de 64 bits, `r0` para el valor de retorno, `r1` a `r5` para los argumentos, `r10` como puntero de solo lectura a una pila de 512 bytes. Se carga con la llamada de sistema `bpf` y la orden `BPF_PROG_LOAD`, que recibe el tipo de programa, las instrucciones, la licencia y un búfer donde el núcleo escribe el registro del verificador. Si el verificador acepta, el núcleo compila el programa a instrucciones nativas (compilación JIT, habilitada en el núcleo del laboratorio) y devuelve un descriptor de archivo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md)) son: Se cargaron nueve programas de tipo filtro de socket en un núcleo de WSL2 y se ejecutaron con el servicio de pruebas; no se enganchó ningún programa a tráfico real ni se probó ninguna versión distinta de núcleo. El siguiente paso, `SE-280`, pasa a otra clase de runtime: los aceleradores, donde un mismo programa se ejecuta en miles de hilos y la memoria, no el cómputo, suele decidir el rendimiento.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Bytecode](../b/bytecode.md), [Instrucción](../i/instruccion.md), [Traducción](../t/traduccion.md), [BPF_PROG_TEST_RUN](../b/bpf-prog-test-run.md), [EBPF](../e/ebpf.md), [Mapa](../m/mapa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Competencia](./competencia.md) · [Compilación y front-end →](./compilacion-y-front-end.md)
