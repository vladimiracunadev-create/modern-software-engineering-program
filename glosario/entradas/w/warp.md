# Warp

[↑ Glosario](../../README.md) · [← Warm-up, caché y aislamiento](./warm-up-cache-y-aislamiento.md) · [WASI →](./wasi.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Grupo de 32 hilos que avanzan juntos en el hardware descrito por la guía de CUDA.

Definición de trabajo de [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md).

## Por qué importa

La clase donde se define, [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md), existe con este propósito: la clase existe para que puedas razonar sobre un acelerador sin haberlo tocado y sin creer que «la GPU es una CPU más rápida».

## Cómo funciona

Según [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md):

La guía de CUDA organiza los hilos en una jerarquía: los hilos se agrupan en *bloques*, los bloques en una *rejilla*. Dentro de un bloque los hilos pueden cooperar y compartir una memoria rápida; entre bloques no hay cooperación directa durante la ejecución. Físicamente, el hardware ejecuta los hilos de un bloque en grupos de 32 llamados *warps*, que avanzan en bloque: una sola instrucción se emite para los 32. El tamaño exacto y los detalles dependen de la arquitectura; el principio, no: la unidad de ejecución no es el hilo sino el grupo, y todo lo que haga que los hilos de un grupo se comporten distinto (ramas, accesos dispersos) cuesta.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md)) son: No se ejecutó ningún núcleo en una GPU; las medidas son de CPU y NumPy y la divergencia es un modelo con semilla 48. El siguiente paso, `SE-281`, lleva el modelo al terreno económico: qué rendimiento y qué costo por petición se obtienen según el tamaño del lote, la precisión y la utilización, con parámetros del autor para los precios.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), [SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md), [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-279](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Hilo](../h/hilo.md), [Bloque y rejilla](../b/bloque-y-rejilla.md), [Coalescencia](../c/coalescencia.md), [Divergencia](../d/divergencia.md), [Intensidad aritmética](../i/intensidad-aritmetica.md), [Proxy](../p/proxy.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Warm-up, caché y aislamiento](./warm-up-cache-y-aislamiento.md) · [WASI →](./wasi.md)
