# Monolito distribuido

[↑ Glosario](../../README.md) · [← Monolito](./monolito.md) · [Monolito modular →](./monolito-modular.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Sistema de servicios que debe desplegarse en conjunto por acoplamiento de contratos.

Definición de trabajo de [SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md).

## Por qué importa

En [SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), el tema «Contratos y compatibilidad» importa porque decide si hay despliegue independiente o monolito distribuido.

## Cómo funciona

[SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Caso medido en la sección «Acoplamiento por contrato: el monolito distribuido» de [SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md):

Se construyó un grafo de ocho servicios (`s0` a `s7`) en dos formas: una cadena en la que cada uno llama al siguiente y una estrella en la que siete llaman a `s7`. Si `s7` cambia su contrato de forma incompatible, los servicios que deben coordinarse con él son 7 en ambas topologías contando los dependientes transitivos; los afectados directamente son 1 en la cadena y 7 en la estrella. Con un cambio compatible (un campo opcional añadido) y consumidores que ignoran lo que no usan (el lector tolerante de Fowler), el número de despliegues coordinados es 0.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md)) son: El costo de HTTP es el de un servidor de la biblioteca estándar en la misma máquina; la cadena de servicios y la topología son simulaciones con parámetros del autor. No se midió ningún sistema de microservicios, ningún equipo ni el costo humano de operarlos. El siguiente paso, `SE-341`, estudia lo que se interpone entre los clientes y los servicios: el BFF, el gateway y la malla de servicios.

## Relación con otros conceptos

- **Prerrequisito:** [Servicio](../s/servicio.md).
- **Ver también:** [Acoplamiento](../a/acoplamiento.md), [Conjunto](../c/conjunto.md), [Contrato](../c/contrato.md), [Camino crítico](../c/camino-critico.md), [Contrato compatible](../c/contrato-compatible.md), [Latencia de cola](../l/latencia-de-cola.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Monolito](./monolito.md) · [Monolito modular →](./monolito-modular.md)
