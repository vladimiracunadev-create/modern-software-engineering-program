# Instancia por petición

[↑ Glosario](../../README.md) · [← Instancia](./instancia.md) · [Instantánea →](./instantanea.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Política que crea y destruye una instancia en cada llamada.

Definición de trabajo de [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md).

## Por qué importa

En [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md), el tema «Instancia por petición» importa porque es la frontera de aislamiento entre peticiones.

## Cómo funciona

[SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Caso medido en la sección «Una instancia por petición es la frontera» de [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md):

La política más segura es una instancia nueva por petición: la memoria parte limpia y lo que la petición escriba desaparece con ella. En el experimento, un módulo con un contador en memoria devolvió `[1, 2, 3, 4, 5]` en cinco peticiones con una instancia reutilizada, y `[1, 1, 1, 1, 1]` con una instancia nueva por petición. En un servicio real eso no es una curiosidad: es la diferencia entre que el aviso de un estudiante dependa de otro o no.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md)) son: Se midió un módulo trivial con `wasmtime` desde Python; no se midió una plataforma de borde, ningún módulo de tamaño real ni el modelo de componentes. El siguiente paso, `SE-279`, cambia de runtime: eBPF permite ejecutar programas pequeños dentro del núcleo de Linux, con un verificador que decide si se pueden cargar, y se ejecuta de verdad en esta parte.

## Relación con otros conceptos

- **Prerrequisito:** [Instancia](./instancia.md).
- **Ver también:** [Almacén](../a/almacen.md), [Borde](../b/borde.md), [Enlace](../e/enlace.md), [Módulo serializado](../m/modulo-serializado.md), [Motor](../m/motor.md), [WIT](../w/wit.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md), [SE-288](../../../classes/part-23-runtimes-y-plataformas-modernas/se-288-proyecto-plataforma-de-ejecucion-aislada-con-evidencia/README.md), [SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Instancia](./instancia.md) · [Instantánea →](./instantanea.md)
