# Orquestación

[↑ Glosario](../../README.md) · [← Origen](./origen.md) · [Orquestador →](./orquestador.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Un componente central lleva el estado de la saga y llama a cada paso.

Definición de trabajo de [SE-411 — Alta, aprovisionamiento y configuración por cliente](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md).

## Por qué importa

La clase donde se define, [SE-411 — Alta, aprovisionamiento y configuración por cliente](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md), existe con este propósito: la clase existe para que diseñes el momento en que un cliente nuevo entra a un producto SaaS como lo que es: una operación distribuida con varios sistemas, que debe poder fallar a la mitad, repetirse sin duplicar nada y dejar al cliente en un estado conocido.

## Cómo funciona

Según [SE-411 — Alta, aprovisionamiento y configuración por cliente](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md):

Una saga es una secuencia de transacciones locales, cada una confirmada en su propio sistema, con acciones compensatorias para deshacer los efectos cuando un paso posterior falla. El alta de un cliente encaja exactamente: crear el registro del inquilino (base del producto), sembrar sus datos (base del producto), crear al administrador (proveedor de identidad), crear al cliente de facturación (procesador de pagos) y enviar el correo de bienvenida. No existe una transacción única que abarque cinco sistemas; existe un orden de pasos y una política para cada falla. La orquestación (un componente que lleva el estado y llama a cada paso) es más fácil de observar que la coreografía (cada paso reacciona a eventos del anterior), y para un alta con pocos pasos es la elección habitual.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-411 — Alta, aprovisionamiento y configuración por cliente](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md):

*Escenario ilustrativo: las cifras y los resultados de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-411 — Alta, aprovisionamiento y configuración por cliente](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md)) son: Se ejecutó un alta de cinco pasos con sqlite3 en memoria y un fallo inyectado, y se midió la creación de 200 inquilinos como fila y como esquema de 12 tablas; no se probó una base de producción, un proveedor de identidad ni un procesador de pagos, y el cociente de tiempos varió entre ejecuciones.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md), [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Estado](../e/estado.md), [Saga](../s/saga.md), [Aprovisionamiento](../a/aprovisionamiento.md), [Compensación](../c/compensacion.md), [Configuración por capas](../c/configuracion-por-capas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-411 — Alta, aprovisionamiento y configuración por cliente](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.

**También se usa en** (14 clases más lo mencionan; las que más):

[SE-399](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md), [SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md), [SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md), [SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md), [SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md), [SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md), [SE-398](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-398-maquinas-virtuales-contenedores-y-aislamiento/README.md), [SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Origen](./origen.md) · [Orquestador →](./orquestador.md)
