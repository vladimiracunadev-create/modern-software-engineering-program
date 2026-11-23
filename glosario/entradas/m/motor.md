# Motor

[↑ Glosario](../../README.md) · [← MoSCoW](./moscow.md) · [MRR →](./mrr.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Configuración y compilador compartidos por los módulos de un anfitrión.

Definición de trabajo de [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md).

## Por qué importa

La clase donde se define, [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md), existe con este propósito: la clase existe para que puedas decidir con números cuándo tiene sentido ejecutar módulos de WebAssembly en un servicio o en el borde, y qué decisiones de diseño evitan que esa promesa se rompa: separar la compilación del arranque, crear una instancia por petición (o saber por qué no), no dejar que el estado de una petición llegue a la siguiente y declarar las capacidades del módulo como un contrato que se revisa antes de desplegar.

## Cómo funciona

Según [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md):

En `wasmtime`, `Engine` es la configuración y el compilador, `Module` es el binario ya compilado a código nativo, `Store` es el estado de una ejecución (memoria, combustible, límites) e `Instance` es el módulo con su memoria enlazada. Los valores medidos (medianas de varias repeticiones) fueron: crear un `Engine`, unos 0,05 ms; compilar el módulo desde el binario, unos 3,5 ms; deserializar el módulo ya compilado (14 728 bytes serializados para un binario de 236 bytes), unos 0,17 ms; y crear un `Store`, instanciar y hacer una llamada, unos 0,47 ms. Dos lecturas. Primera: compilar es unas 7 veces más caro que instanciar y unas 20 veces más caro que deserializar, así que compilar en cada petición convierte una ventaja en un problema; se compila una vez por versión del módulo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En `wasmtime`, `Engine` es la configuración y el compilador, `Module` es el binario ya compilado a código nativo, `Store` es el estado de una ejecución (memoria, combustible, límites) e `Instance` es el módulo con su memoria enlazada. ([SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Módulo](./modulo.md).
- **Ver también:** [Anfitrión](../a/anfitrion.md), [Almacén](../a/almacen.md), [Borde](../b/borde.md), [Enlace](../e/enlace.md), [Instancia por petición](../i/instancia-por-peticion.md), [Módulo serializado](./modulo-serializado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (105 clases más lo mencionan; las que más):

[SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md), [SE-077](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md), [SE-078](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md), [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md), [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md), [SE-350](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md), [SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md), [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md), [Slack](../../../casos/exito/slack.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Engine».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← MoSCoW](./moscow.md) · [MRR →](./mrr.md)
