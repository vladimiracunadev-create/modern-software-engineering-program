# Intensidad aritmética

[↑ Glosario](../../README.md) · [← Intención perdida](./intencion-perdida.md) · [Interbloqueo →](./interbloqueo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Operaciones realizadas por byte movido desde memoria.

Definición de trabajo de [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md).

## Por qué importa

En [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md), el tema «Intensidad aritmética» importa porque predice si manda la memoria o el cómputo.

## Cómo funciona

Según [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md):

El modelo *roofline* acota el rendimiento de un programa por el menor entre el pico de cómputo del hardware y el producto del ancho de banda de memoria por la intensidad aritmética (operaciones por byte movido). Dos operaciones que se midieron en la CPU del laboratorio muestran los extremos. `v·1,5 + w` sobre 8 000 000 de valores: dos operaciones por cada 12 bytes movidos (leer dos valores de 4 bytes y escribir uno), unos 0,4 GFLOP/s y unos 2 GB/s efectivos; la operación está limitada por memoria y el cómputo está casi ocioso.

Según [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md):

Elige un cálculo de tu sistema que consideres pesado. Descompón su tiempo en lectura de datos, cálculo y escritura; mide la intensidad aritmética; vectoriza en CPU y mide de nuevo. Escribe la condición bajo la cual un acelerador valdría la pena (volumen mínimo, trabajo por transferencia, utilización) y cómo la medirías.

## Ejemplo

Caso medido en la sección «Intensidad aritmética: quién limita» de [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md):

El modelo *roofline* acota el rendimiento de un programa por el menor entre el pico de cómputo del hardware y el producto del ancho de banda de memoria por la intensidad aritmética (operaciones por byte movido). Dos operaciones que se midieron en la CPU del laboratorio muestran los extremos. `v·1,5 + w` sobre 8 000 000 de valores: dos operaciones por cada 12 bytes movidos (leer dos valores de 4 bytes y escribir uno), unos 0,4 GFLOP/s y unos 2 GB/s efectivos; la operación está limitada por memoria y el cómputo está casi ocioso.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md)) son: No se ejecutó ningún núcleo en una GPU; las medidas son de CPU y NumPy y la divergencia es un modelo con semilla 48. El siguiente paso, `SE-281`, lleva el modelo al terreno económico: qué rendimiento y qué costo por petición se obtienen según el tamaño del lote, la precisión y la utilización, con parámetros del autor para los precios.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), [SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md), [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-279](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Byte](../b/byte.md), [Operación](../o/operacion.md), [Bloque y rejilla](../b/bloque-y-rejilla.md), [Coalescencia](../c/coalescencia.md), [Divergencia](../d/divergencia.md), [Proxy](../p/proxy.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Intención perdida](./intencion-perdida.md) · [Interbloqueo →](./interbloqueo.md)
