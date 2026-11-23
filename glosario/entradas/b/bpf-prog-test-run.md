# BPF_PROG_TEST_RUN

[↑ Glosario](../../README.md) · [← Borde de la red](./borde-de-la-red.md) · [Breakpoint y condición →](./breakpoint-y-condicion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Orden que ejecuta un programa sobre datos de prueba sin enganchar tráfico real.

Definición de trabajo de [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md).

## Por qué importa

La clase donde se define, [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md), existe con este propósito: la clase existe para que entiendas eBPF como lo que es en la práctica: un mecanismo para cargar programas pequeños en el núcleo de Linux sin recompilarlo ni reiniciarlo, con un verificador que decide antes de ejecutar si el programa es seguro.

## Cómo funciona

Según [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md):

Un programa eBPF es una secuencia de instrucciones de 8 bytes (con una excepción de 16 para cargar constantes de 64 bits) para una máquina de registros: diez registros de 64 bits, `r0` para el valor de retorno, `r1` a `r5` para los argumentos, `r10` como puntero de solo lectura a una pila de 512 bytes. Se carga con la llamada de sistema `bpf` y la orden `BPF_PROG_LOAD`, que recibe el tipo de programa, las instrucciones, la licencia y un búfer donde el núcleo escribe el registro del verificador. Si el verificador acepta, el núcleo compila el programa a instrucciones nativas (compilación JIT, habilitada en el núcleo del laboratorio) y devuelve un descriptor de archivo.

## Ejemplo

Ejemplo de [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md) (sección «Ejemplo mínimo»):

Las dos instrucciones ocupan 16 bytes. El verificador procesó 2 instrucciones y el núcleo, al ejecutarlo con `BPF_PROG_TEST_RUN`, devolvió 42.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El laboratorio usa el tipo «filtro de socket» y la orden `BPF_PROG_TEST_RUN`, que ejecuta el programa sobre un paquete de prueba sin enganchar nada a tráfico real: es la forma más segura de probar una carga y la razón por la que el experimento no toca la red. ([SE-279](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Sobre](../s/sobre.md), [Compilación JIT](../c/compilacion-jit.md), [EBPF](../e/ebpf.md), [Mapa](../m/mapa.md), [Presupuesto de complejidad](../p/presupuesto-de-complejidad.md), [Tipo de programa](../t/tipo-de-programa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Borde de la red](./borde-de-la-red.md) · [Breakpoint y condición →](./breakpoint-y-condicion.md)
