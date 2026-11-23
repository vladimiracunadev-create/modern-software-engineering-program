# WIT

[↑ Glosario](../../README.md) · [← WIP](./wip.md) · [Workflow →](./workflow.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Lenguaje de descripción de interfaces del modelo de componentes.

Definición de trabajo de [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md).

## Por qué importa

La clase donde se define, [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md), existe con este propósito: la clase existe para que puedas decidir con números cuándo tiene sentido ejecutar módulos de WebAssembly en un servicio o en el borde, y qué decisiones de diseño evitan que esa promesa se rompa: separar la compilación del arranque, crear una instancia por petición (o saber por qué no), no dejar que el estado de una petición llegue a la siguiente y declarar las capacidades del módulo como un contrato que se revisa antes de desplegar.

## Cómo funciona

Según [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md):

Un módulo de Wasm solo conoce enteros y flotantes y una memoria; pasar una cadena o un registro exige un acuerdo manual sobre dónde está en memoria, cuánto mide y quién la libera. Cada pareja de lenguajes lo resuelve a su manera y cada acuerdo es un lugar donde aparecen errores de memoria. El modelo de componentes define: interfaces escritas en WIT con tipos ricos (cadenas, listas, registros, variantes, opciones, resultados), *mundos* que declaran lo que un componente importa y exporta, una ABI canónica que fija cómo esos tipos se convierten en memoria lineal, y la composición de componentes (el que exporta una interfaz se enlaza con el que la importa).

Según [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md):

No. WASI define interfaces de sistema; el modelo de componentes define cómo se describen y componen interfaces. De hecho, las versiones recientes de WASI se expresan con WIT.

## Ejemplo

Ejemplo de [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md) (sección «Preguntas frecuentes»):

No. WASI define interfaces de sistema; el modelo de componentes define cómo se describen y componen interfaces. De hecho, las versiones recientes de WASI se expresan con WIT.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md)) son: Se midió un módulo trivial con `wasmtime` desde Python; no se midió una plataforma de borde, ningún módulo de tamaño real ni el modelo de componentes. El siguiente paso, `SE-279`, cambia de runtime: eBPF permite ejecutar programas pequeños dentro del núcleo de Linux, con un verificador que decide si se pueden cargar, y se ejecuta de verdad en esta parte.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Interfaz](../i/interfaz.md), [Modelo](../m/modelo.md), [Almacén](../a/almacen.md), [Borde](../b/borde.md), [Enlace](../e/enlace.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← WIP](./wip.md) · [Workflow →](./workflow.md)
