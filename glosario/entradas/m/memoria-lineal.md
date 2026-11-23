# Memoria lineal

[↑ Glosario](../../README.md) · [← Memoria de largo plazo](./memoria-de-largo-plazo.md) · [Memoria persistente →](./memoria-persistente.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Arreglo de bytes de la instancia, en páginas de 64 KiB.

Definición de trabajo de [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md).

## Por qué importa

En [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), el tema «Memoria lineal» importa porque un acceso fuera de rango es una trampa, no una corrupción de memoria ajena.

## Cómo funciona

Según [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md):

Un módulo recibe una memoria lineal: un arreglo de bytes que crece en páginas de 64 KiB y que solo se direcciona con enteros relativos a su inicio. No existe la instrucción «leer la dirección absoluta X del proceso». En el experimento, el módulo declara una página (65 536 bytes) y se le pide leer en la dirección 70 000: el runtime responde con una trampa (`out of bounds memory access`), el llamador recibe una excepción y, lo importante, el almacén sigue utilizable: llamar después a `add(40, 2)` devuelve 42. La trampa mata la llamada, no el servicio. Esa propiedad es la que permite ejecutar muchas reglas ajenas en el mismo proceso del anfitrión sin que una corrompa el estado de otra.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un módulo recibe una memoria lineal: un arreglo de bytes que crece en páginas de 64 KiB y que solo se direcciona con enteros relativos a su inicio. ([SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), [SE-021](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md), [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md), [SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Byte](../b/byte.md), [Instancia](../i/instancia.md), [Página](../p/pagina.md), [Capacidad](../c/capacidad.md), [Combustible](../c/combustible.md), [Importación](../i/importacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md), [SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Memoria de largo plazo](./memoria-de-largo-plazo.md) · [Memoria persistente →](./memoria-persistente.md)
