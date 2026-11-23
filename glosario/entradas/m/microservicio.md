# Microservicio

[↑ Glosario](../../README.md) · [← Microkernel](./microkernel.md) · [Microtarea →](./microtarea.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Servicio desplegable de forma independiente, organizado alrededor de una capacidad de negocio y dueño de sus datos.

Definición de trabajo de [SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md).

## Por qué importa

La clase donde se define, [SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), existe con este propósito: la clase existe para que puedas poner un precio a separar un sistema en servicios y compararlo con lo que se compra.

## Cómo funciona

[SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md)) son: El costo de HTTP es el de un servidor de la biblioteca estándar en la misma máquina; la cadena de servicios y la topología son simulaciones con parámetros del autor. No se midió ningún sistema de microservicios, ningún equipo ni el costo humano de operarlos. El siguiente paso, `SE-341`, estudia lo que se interpone entre los clientes y los servicios: el BFF, el gateway y la malla de servicios.

## Relación con otros conceptos

- **Prerrequisito:** [Servicio](../s/servicio.md).
- **Ver también:** [Capacidad](../c/capacidad.md), [Camino crítico](../c/camino-critico.md), [Contrato compatible](../c/contrato-compatible.md), [Latencia de cola](../l/latencia-de-cola.md), [Lector tolerante](../l/lector-tolerante.md), [Monolito distribuido](./monolito-distribuido.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (15 clases más lo mencionan; las que más):

[SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md), [SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md), [SE-341](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md), [SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md), [SE-002](../../../classes/part-00-ingenieria-de-software-como-profesion/se-002-historia-de-la-crisis-del-software-a-la-ingenieria-continua/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Shopify](../../../casos/exito/shopify.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Microkernel](./microkernel.md) · [Microtarea →](./microtarea.md)
