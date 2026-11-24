# Contexto delimitado

[↑ Glosario](../../README.md) · [← Contexto del inquilino](./contexto-del-inquilino.md) · [Contextos →](./contextos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Un **contexto delimitado** (*bounded context*) es la frontera dentro de la cual un modelo y su lenguaje son consistentes y tienen un significado único y preciso ([SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md), [SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md), [SE-381](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md)). Es un concepto del diseño orientado al dominio: la consistencia se garantiza dentro del límite, no en todo el sistema.

## Por qué importa

La misma palabra significa cosas distintas en áreas distintas del negocio. Pretender un modelo único para todo el sistema produce, según [SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md), un objeto con campos para todos los usos que nadie entiende por completo. La decisión que cambia es dónde trazar las fronteras: en lugar de unificar definiciones, se acepta que cada contexto tiene la suya y se invierte en una traducción explícita entre ellas.

## Cómo funciona

[SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md) da un ejemplo sobre la palabra «entrega». En el contexto académico, una entrega es el trabajo de una persona estudiante, con un estado «pendiente» o «recibida». En el contexto de avisos, una entrega es un elemento con vencimiento y un indicador de si ya se entregó. Los dos contextos no necesitan acordar una definición única; necesitan una **traducción explícita en su frontera**.

Esa traducción es el punto de contacto: la capa anticorrupción convierte el vocabulario de un contexto al del otro, y es el único lugar donde se conocen ambos. Dentro de cada contexto, el modelo puede ser simple y coherente, porque no tiene que servir a usos ajenos. Las fronteras se relacionan en el mapa de contextos, que registra qué contexto depende de cuál y de qué manera: por ejemplo, adoptando el modelo ajeno tal cual (conformista) o traduciéndolo. [SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md) lo trata como una decisión de arquitectura de dominio y [SE-381](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md) como una frontera de integración, donde un modelo y su vocabulario tienen un significado único.

## Ejemplo

El contexto académico guarda `entrega` con `estado = recibida`. El contexto de avisos guarda `entrega` con `vence_en` y `entregada = true/false`. Entre ambos, una función traduce `recibida` a `true`. Si mañana el contexto académico añade «en revisión», se decide en un solo lugar si cuenta como entregada. Ejemplo de [SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md).

## Errores y confusiones comunes

- **Un modelo único para todo el sistema**: produce un objeto con campos para todos los usos.
- **Creer que un contexto es un servicio**: un contexto delimitado es una frontera de modelo y lenguaje; puede o no coincidir con un servicio desplegable.
- **Fronteras sin traducción explícita**: el vocabulario de uno se filtra al otro.
- **Dibujar el contexto por organigrama** en vez de por significado de las palabras.

## Límites y cuándo no aplica

[SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md) lo limita expresamente: los contextos delimitados importan cuando hay dos o más modelos con la misma palabra; en un sistema con un solo modelo no hacen falta. Trazar fronteras tiene costo (traducción, mantenimiento) y un sistema pequeño o con un vocabulario único no lo recupera. Y las fronteras no se descubren por decreto: dependen de entender el dominio con quienes lo conocen.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-328](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Frontera](../f/frontera.md), [Modelo](../m/modelo.md), [Agregado](../a/agregado.md), [Capa anticorrupción](./capa-anticorrupcion.md), [Conformista](./conformista.md), [Cuarentena](./cuarentena.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-329 — Domain-Driven Design estratégico y táctico](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-381 — Anti-corruption layers y traducción de modelos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.
- [SE-546 — DDD como lenguaje ubicuo y contexto para agentes](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «Bounded Context»](https://martinfowler.com/bliki/BoundedContext.html) — contexto delimitado; autoridad: Martin Fowler.
- [Evans, «Domain-Driven Design Reference»](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf) — resumen de patrones estratégicos y tácticos; autoridad: Eric Evans.
- [Fowler, «DDD Aggregate»](https://martinfowler.com/bliki/DDD_Aggregate.html) — agregado como unidad de consistencia; autoridad: Martin Fowler.
- [Fowler, «Value Object»](https://martinfowler.com/bliki/ValueObject.html) — objetos de valor; autoridad: Martin Fowler.
- [Python: `decimal`](https://docs.python.org/3/library/decimal.html) — aritmética decimal y modos de redondeo; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Contexto del inquilino](./contexto-del-inquilino.md) · [Contextos →](./contextos.md)
