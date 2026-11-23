# Monolito

[↑ Glosario](../../README.md) · [← Monitor](./monitor.md) · [Monolito distribuido →](./monolito-distribuido.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Un **monolito** es un sistema que se despliega como una sola unidad ([SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md)). El término no habla del tamaño del código sino de la unidad de despliegue. [SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md) lo contrasta con el **monolito modular**, que mantiene una única unidad de despliegue pero impone fronteras entre módulos, y con los servicios o microservicios, que se despliegan por separado.

## Por qué importa

Elegir entre monolito, monolito modular y servicios es una decisión de fronteras y de costos operativos. [SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md) enumera las ventajas prácticas del monolito: las llamadas entre módulos son llamadas de función, una transacción de base de datos cubre varias entidades, una prueba de extremo a extremo corre en un proceso y el equipo opera una sola cosa.

## Cómo funciona

El defecto característico del monolito no es el tamaño sino la **falta de fronteras internas**: cuando cualquier módulo puede importar cualquier otro, un cambio en uno afecta a todos y desplegar una corrección pequeña exige probar el sistema entero. Dice [SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md): un monolito sin fronteras no es una decisión, es la ausencia de una.

El **monolito modular** mantiene la unidad de despliegue pero cada módulo expone una API pública y oculta sus detalles, y una regla comprobable prohíbe importar lo demás. Sigue el criterio de Parnas de ocultar la decisión que puede cambiar. Conserva las transacciones locales y las pruebas rápidas y deja abierta la puerta a separar un módulo más adelante, porque la frontera ya existe y se comprueba. Su riesgo es que la regla se erosione si nadie la verifica: por eso el comprobador es parte de la arquitectura.

## Ejemplo

En [SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md), un cambio pequeño exige probar todo el sistema porque el monolito no tiene fronteras internas; la corrección es imponer API públicas y un comprobador de importaciones, es decir, pasar a un monolito modular, sin pagar el costo de la red.

## Errores y confusiones comunes

- **Creer que «monolito» y «microservicios» son dos bandos.** Son extremos de un continuo de fronteras, y la mayor parte del beneficio de una frontera (límites claros entre módulos) puede obtenerse sin pagar el costo de la red ([SE-327](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md)).
- **Un monolito sin fronteras internas.** Un cambio pequeño exige probar todo el sistema.
- **Fronteras sin comprobador.** La regla se erosiona si nadie la verifica.

## Límites y cuándo no aplica

El monolito modular conserva una sola unidad de despliegue: si se necesita desplegar o escalar partes por separado, hay que cruzar fronteras de red, con los costos que [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md) trata. El ejemplo de la clase es sintético y no prescribe cuándo conviene cada opción.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Frontera de módulo](../f/frontera-de-modulo.md), [Monolito modular](./monolito-modular.md), [Saga](../s/saga.md), [Servicio](../s/servicio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-327 — Monolito, modular monolith y servicios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-327-monolito-modular-monolith-y-servicios/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

**También se usa en** (17 clases más lo mencionan; las que más):

[SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md), [SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md), [SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md), [SE-338](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md), [SE-348](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [Airbnb](../../../casos/exito/airbnb.md), [Slack](../../../casos/exito/slack.md), [Shopify](../../../casos/exito/shopify.md).

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
