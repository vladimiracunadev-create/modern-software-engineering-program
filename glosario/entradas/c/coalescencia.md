# Coalescencia

[↑ Glosario](../../README.md) · [← Cloud Engineer](./cloud-engineer.md) · [Cobertura →](./cobertura.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Fusión de accesos contiguos de un grupo en pocas transacciones de memoria.

Definición de trabajo de [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md).

## Por qué importa

En [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md), el tema «Coalescencia» importa porque accesos contiguos de un grupo se sirven con pocas transacciones.

## Cómo funciona

Según [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md):

Hay tres niveles que importa distinguir: los registros de cada hilo (rápidos, pocos), una memoria compartida por bloque (rápida, pequeña, gestionada por el programador) y la memoria global (grande, con latencia de cientos de ciclos). El ancho de banda de la memoria global es muy alto, pero solo se alcanza cuando los hilos de un grupo piden direcciones contiguas, porque el hardware fusiona esas peticiones en pocas transacciones (coalescencia). El proxy en CPU reproduce la idea con la caché: sumar 1 048 576 elementos de un arreglo de 16 777 216 valores de 32 bits (64 MiB) tardó unos 4,7 ms leyendo posiciones contiguas, unos 9,3 ms con un salto de 16 posiciones y unos 27,6 ms en orden aleatorio: casi seis veces el contiguo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El ancho de banda de la memoria global es muy alto, pero solo se alcanza cuando los hilos de un grupo piden direcciones contiguas, porque el hardware fusiona esas peticiones en pocas transacciones (coalescencia). ([SE-280](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), [SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md), [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-279](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Fusión](../f/fusion.md), [Transacción](../t/transaccion.md), [Bloque y rejilla](../b/bloque-y-rejilla.md), [Divergencia](../d/divergencia.md), [Intensidad aritmética](../i/intensidad-aritmetica.md), [Proxy](../p/proxy.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-280 — GPU y aceleradores: modelo de ejecución](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Cloud Engineer](./cloud-engineer.md) · [Cobertura →](./cobertura.md)
