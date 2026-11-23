# Monolito

[↑ Glosario](../../README.md) · [← Monitor](./monitor.md) · [Monolito distribuido →](./monolito-distribuido.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Sistema que se despliega como una sola unidad.

Definición de trabajo de [SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md).

## Por qué importa

En [SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md), el tema «Monolito» importa porque una unidad de despliegue y transacciones locales: simple de operar y de probar.

## Cómo funciona

Según [SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md), en la sección «Monolito»:

Un **monolito** se despliega como una sola unidad. Sus ventajas son prácticas: las llamadas entre módulos son llamadas de función, una transacción de base de datos cubre varias entidades, una prueba de extremo a extremo corre en un proceso y el equipo opera una cosa. Su defecto característico no es el tamaño sino la falta de fronteras internas: cuando cualquier módulo puede importar cualquier otro, el cambio en uno afecta a todos y el despliegue de una corrección pequeña exige probar el sistema entero. Un monolito sin fronteras no es una decisión: es la ausencia de una.

## Ejemplo

Ejemplo de [SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma mantiene el sistema como monolito modular y añade al CI un comprobador de fronteras que falla si un módulo importa algo que no sea la `api` de otro, y otro que prohíbe `importlib` y `__import__` con nombres de módulos internos. Mide que la operación «calificar» hace 14 llamadas entre `notas` y `entregas` y decide que, si algún día se separan, esas dos son una sola frontera mal puesta: primero deberían fusionarse o reducir las llamadas.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un cambio pequeño exige probar todo el sistema** — causa: monolito sin fronteras internas. Corrección: imponer API públicas y un comprobador de importaciones. ([SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un monolito sin fronteras no es una decisión: es la ausencia de una. ([SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Frontera de módulo](../f/frontera-de-modulo.md), [Monolito modular](./monolito-modular.md), [Saga](../s/saga.md), [Servicio](../s/servicio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

**También se usa en** (17 clases más lo mencionan; las que más):

[SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md), [SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md), [SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md), [SE-338](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md), [SE-348](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [Airbnb](../../../casos/exito/airbnb.md), [Slack](../../../casos/exito/slack.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «MonolithFirst»](https://martinfowler.com/bliki/MonolithFirst.html) — empezar por un monolito modular; autoridad: Martin Fowler.
- [Fowler y Lewis, «Microservices»](https://martinfowler.com/articles/microservices.html) — características, ventajas y costes de los servicios; autoridad: Martin Fowler y James Lewis.
- [Parnas, «On the criteria to be used in decomposing systems into modules» (CACM, 1972)](https://doi.org/10.1145/361598.361623) — ocultación de información como criterio de descomposición; autoridad: Communications of the ACM.
- [García-Molina y Salem, «Sagas» (SIGMOD, 1987)](https://doi.org/10.1145/38713.38742) — transacciones largas con compensación; autoridad: ACM SIGMOD.
- [Microsoft Learn, patrón Saga](https://learn.microsoft.com/en-us/azure/architecture/patterns/saga) — coordinación de transacciones distribuidas con compensaciones; autoridad: Microsoft.

---

[↑ Glosario](../../README.md) · [← Monitor](./monitor.md) · [Monolito distribuido →](./monolito-distribuido.md)
