# Presupuesto de complejidad

[↑ Glosario](../../README.md) · [← Presupuesto](./presupuesto.md) · [Presupuesto de consultas →](./presupuesto-de-consultas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Límite de instrucciones que el verificador explora.

Definición de trabajo de [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md).

## Por qué importa

En [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md), el tema «Presupuesto de complejidad» importa porque un bucle «correcto» puede rechazarse por exceso de caminos.

## Cómo funciona

[SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Caso medido en la sección «Un presupuesto de complejidad, no un detector de bucles» de [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md):

El programa `r0 = 0; r0 += 1; saltar a la instrucción anterior` es un bucle sin salida. El núcleo no respondió «bucle infinito»: respondió `BPF program is too large. Processed 1000001 insn` con un límite de 1 000 000. El verificador exploró el bucle iteración tras iteración hasta agotar su presupuesto. Dos consecuencias para el diseño.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md)) son: Se cargaron nueve programas de tipo filtro de socket en un núcleo de WSL2 y se ejecutaron con el servicio de pruebas; no se enganchó ningún programa a tráfico real ni se probó ninguna versión distinta de núcleo. El siguiente paso, `SE-280`, pasa a otra clase de runtime: los aceleradores, donde un mismo programa se ejecuta en miles de hilos y la memoria, no el cómputo, suele decidir el rendimiento.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Instrucción](../i/instruccion.md), [Límite](../l/limite.md), [Verificador](../v/verificador.md), [BPF_PROG_TEST_RUN](../b/bpf-prog-test-run.md), [Compilación JIT](../c/compilacion-jit.md), [EBPF](../e/ebpf.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-279 — eBPF: observabilidad, red y seguridad en el kernel](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Presupuesto](./presupuesto.md) · [Presupuesto de consultas →](./presupuesto-de-consultas.md)
