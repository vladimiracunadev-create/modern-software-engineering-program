# Borde

[↑ Glosario](../../README.md) · [← Bootstrap](./bootstrap.md) · [Borde de la red →](./borde-de-la-red.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Ubicación de cómputo cercana al usuario con recursos acotados por inquilino.

Definición de trabajo de [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md).

## Por qué importa

La clase donde se define, [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md), existe con este propósito: la clase existe para que puedas decidir con números cuándo tiene sentido ejecutar módulos de WebAssembly en un servicio o en el borde, y qué decisiones de diseño evitan que esa promesa se rompa: separar la compilación del arranque, crear una instancia por petición (o saber por qué no), no dejar que el estado de una petición llegue a la siguiente y declarar las capacidades del módulo como un contrato que se revisa antes de desplegar.

## Cómo funciona

Según [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md):

Arrancar un intérprete de Python vacío como proceso tardó unos 100 a 160 ms en la misma máquina, entre unas 210 y unas 340 veces el costo de instanciar el módulo de la clase (según la ejecución). La comparación es orientativa y no de funciones equivalentes: un proceso de Python carga un intérprete completo; una instancia de Wasm carga una memoria y un módulo ya compilado. Sirve para una conclusión limitada: con instancias de menos de un milisegundo, aislar cada petición es viable donde con procesos no lo sería. Esa es la razón por la que las plataformas de borde con muchos inquilinos eligen este modelo, y la razón por la que no se concluye nada de aquí sobre sus precios ni sobre su rendimiento real, que no se midió.

Según [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md):

No. El borde reduce la distancia al usuario y suele ofrecer arranques muy cortos, pero impone límites de CPU, memoria y tiempo y no siempre ofrece las mismas capacidades. Es una elección por carga de trabajo, y los números de esta clase no miden ninguna plataforma de borde.

## Ejemplo

Ejemplo de [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md) (sección «Preguntas frecuentes»):

No. El borde reduce la distancia al usuario y suele ofrecer arranques muy cortos, pero impone límites de CPU, memoria y tiempo y no siempre ofrece las mismas capacidades. Es una elección por carga de trabajo, y los números de esta clase no miden ninguna plataforma de borde.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Esa es la razón por la que las plataformas de borde con muchos inquilinos eligen este modelo, y la razón por la que no se concluye nada de aquí sobre sus precios ni sobre su rendimiento real, que no se midió. ([SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md))
- El borde reduce la distancia al usuario y suele ofrecer arranques muy cortos, pero impone límites de CPU, memoria y tiempo y no siempre ofrece las mismas capacidades. ([SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-277](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), [SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Inquilino](../i/inquilino.md), [Recurso](../r/recurso.md), [Almacén](../a/almacen.md), [Enlace](../e/enlace.md), [Instancia por petición](../i/instancia-por-peticion.md), [Módulo serializado](../m/modulo-serializado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-278 — WebAssembly en servidor y borde: component model](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (82 clases más lo mencionan; las que más):

[SE-519](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-519-pruebas-de-caracterizacion-y-seams/README.md), [SE-307](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md), [SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md), [SE-341](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md), [SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md), [SE-044](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md), [SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md), [SE-273](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Slack](../../../casos/exito/slack.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Bootstrap](./bootstrap.md) · [Borde de la red →](./borde-de-la-red.md)
