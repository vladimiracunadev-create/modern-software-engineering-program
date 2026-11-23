# Módulo serializado

[↑ Glosario](../../README.md) · [← Módulo](./modulo.md) · [Módulo, paquete e importación →](./modulo-paquete-e-importacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Módulo ya compilado a código nativo guardado para cargarlo sin recompilar.

Definición de trabajo de [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md).

## Por qué importa

La clase donde se define, [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md), existe con este propósito: la clase existe para que puedas decidir con números cuándo tiene sentido ejecutar módulos de WebAssembly en un servicio o en el borde, y qué decisiones de diseño evitan que esa promesa se rompa: separar la compilación del arranque, crear una instancia por petición (o saber por qué no), no dejar que el estado de una petición llegue a la siguiente y declarar las capacidades del módulo como un contrato que se revisa antes de desplegar.

## Cómo funciona

Según [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md):

En `wasmtime`, `Engine` es la configuración y el compilador, `Module` es el binario ya compilado a código nativo, `Store` es el estado de una ejecución (memoria, combustible, límites) e `Instance` es el módulo con su memoria enlazada. Los valores medidos (medianas de varias repeticiones) fueron: crear un `Engine`, unos 0,05 ms; compilar el módulo desde el binario, unos 3,5 ms; deserializar el módulo ya compilado (14 728 bytes serializados para un binario de 236 bytes), unos 0,17 ms; y crear un `Store`, instanciar y hacer una llamada, unos 0,47 ms. Dos lecturas. Primera: compilar es unas 7 veces más caro que instanciar y unas 20 veces más caro que deserializar, así que compilar en cada petición convierte una ventaja en un problema; se compila una vez por versión del módulo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Segunda: el módulo serializado es unas 60 veces mayor que el binario original, porque contiene código nativo; el ahorro de tiempo se paga con espacio y con una dependencia más fuerte del runtime y de la arquitectura. ([SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Módulo](./modulo.md).
- **Ver también:** [Almacén](../a/almacen.md), [Borde](../b/borde.md), [Enlace](../e/enlace.md), [Instancia por petición](../i/instancia-por-peticion.md), [Motor](./motor.md), [WIT](../w/wit.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Módulo](./modulo.md) · [Módulo, paquete e importación →](./modulo-paquete-e-importacion.md)
