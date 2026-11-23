# Monolito modular

[↑ Glosario](../../README.md) · [← Monolito distribuido](./monolito-distribuido.md) · [Montaje →](./montaje.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Monolito con fronteras entre módulos que se verifican, de modo que cada módulo expone una API y oculta sus detalles.

Definición de trabajo de [SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md).

## Por qué importa

En [SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md), el tema «Monolito modular» importa porque fronteras internas verificadas dan el orden sin el coste de la red.

## Cómo funciona

Según [SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md), en la sección «Monolito modular»:

Un **monolito modular** mantiene una única unidad de despliegue pero impone fronteras entre módulos: cada uno expone una API pública y oculta sus detalles, y una regla comprobable prohíbe importar lo demás. Sigue el criterio de Parnas: ocultar la decisión que puede cambiar. Conserva las transacciones locales y las pruebas rápidas y deja abierta la puerta a separar un módulo más adelante, porque la frontera ya existe y se comprueba. Su riesgo es que la regla se erosione si nadie la verifica; por eso el comprobador es parte de la arquitectura y no un añadido.

## Ejemplo

Ejemplo de [SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma mantiene el sistema como monolito modular y añade al CI un comprobador de fronteras que falla si un módulo importa algo que no sea la `api` de otro, y otro que prohíbe `importlib` y `__import__` con nombres de módulos internos. Mide que la operación «calificar» hace 14 llamadas entre `notas` y `entregas` y decide que, si algún día se separan, esas dos son una sola frontera mal puesta: primero deberían fusionarse o reducir las llamadas.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md)) son:

- **Un cambio pequeño exige probar todo el sistema** — causa: monolito sin fronteras internas. Corrección: imponer API públicas y un comprobador de importaciones.
- **La latencia sube al separar un módulo** — causa: la frontera cruza muchas llamadas por operación. Corrección: medir llamadas por operación y fusionar o engrosar la API.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un **monolito modular** mantiene una única unidad de despliegue pero impone fronteras entre módulos: cada uno expone una API pública y oculta sus detalles, y una regla comprobable prohíbe importar lo demás. ([SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Frontera](../f/frontera.md), [Módulo](./modulo.md), [Monolito](./monolito.md), [Frontera de módulo](../f/frontera-de-modulo.md), [Saga](../s/saga.md), [Servicio](../s/servicio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

**También se usa en** (10 clases más lo mencionan; las que más):

[SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md), [SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md), [SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md), [SE-328](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), [SE-348](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [Shopify](../../../casos/exito/shopify.md).

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

[↑ Glosario](../../README.md) · [← Monolito distribuido](./monolito-distribuido.md) · [Montaje →](./montaje.md)
