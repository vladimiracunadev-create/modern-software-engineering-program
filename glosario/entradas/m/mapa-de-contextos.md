# Mapa de contextos

[↑ Glosario](../../README.md) · [← Mapa](./mapa.md) · [Mapa y conjunto →](./mapa-y-conjunto.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Descripción de los contextos y de la naturaleza de cada relación entre ellos.

Definición de trabajo de [SE-329 — Domain-Driven Design estratégico y táctico](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-546 — DDD como lenguaje ubicuo y contexto para agentes](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md): Diagrama de contextos y relaciones entre ellos.

## Por qué importa

En [SE-329 — Domain-Driven Design estratégico y táctico](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md), el tema «Mapa de contextos» importa porque declara cómo se relacionan los equipos y qué se traduce.

## Cómo funciona

Según [SE-329 — Domain-Driven Design estratégico y táctico](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md), en la sección «Mapa de contextos»:

El **mapa de contextos** dibuja los contextos y la naturaleza de cada relación: socios que coordinan cambios, cliente y proveedor donde uno depende de otro, un contexto conformista que acepta el modelo del vecino, o una **capa anticorrupción** que traduce el modelo ajeno al propio para que no lo contamine. Lo importante es que cada relación se declare, porque define quién debe coordinar con quién. Un contrato pequeño y estable entre contextos (tres atributos compartidos, no catorce) concentra el acoplamiento donde puede gestionarse y deja el resto libre para cambiar.

## Ejemplo

Ejemplo de [SE-329 — Domain-Driven Design estratégico y táctico](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md) (sección «Caso conductor»):

La plataforma de entregas y corrección de tareas sigue siendo el caso conductor. Esta clase deja el quinto artefacto: un mapa de contextos con un contrato pequeño, un agregado con su invariante protegido y la nota como objeto de valor. `SE-330` usará esos límites para decidir qué se comunica por eventos entre contextos. Cambia después una sola decisión, el tamaño del contrato, y observa cuánto crece el acoplamiento.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-329 — Domain-Driven Design estratégico y táctico](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md)) son:

- **Cada cambio de un atributo exige coordinar a tres equipos** — causa: un modelo único compartido. Corrección: separar contextos y reducir el contrato a lo necesario.
- **La misma palabra significa cosas distintas en reuniones** — causa: hay varios contextos sin declarar. Corrección: escribir el significado en cada contexto y el mapa de relaciones.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El **mapa de contextos** dibuja los contextos y la naturaleza de cada relación: socios que coordinan cambios, cliente y proveedor donde uno depende de otro, un contexto conformista que acepta el modelo del vecino, o una **capa anticorrupción** que traduce el modelo ajeno al propio para que no lo contamine. ([SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-328](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](../c/contextos.md), [Diagrama](../d/diagrama.md), [Relación](../r/relacion.md), [Agregado](../a/agregado.md), [Capa anticorrupción](../c/capa-anticorrupcion.md), [Contexto delimitado](../c/contexto-delimitado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-329 — Domain-Driven Design estratégico y táctico](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-546 — DDD como lenguaje ubicuo y contexto para agentes](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Evans, «Domain-Driven Design Reference»](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf) — resumen de patrones estratégicos y tácticos; autoridad: Eric Evans.
- [Fowler, «Bounded Context»](https://martinfowler.com/bliki/BoundedContext.html) — contexto delimitado; autoridad: Martin Fowler.
- [Fowler, «DDD Aggregate»](https://martinfowler.com/bliki/DDD_Aggregate.html) — agregado como unidad de consistencia; autoridad: Martin Fowler.
- [Fowler, «Value Object»](https://martinfowler.com/bliki/ValueObject.html) — objetos de valor; autoridad: Martin Fowler.
- [Python: `decimal`](https://docs.python.org/3/library/decimal.html) — aritmética decimal y modos de redondeo; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Mapa](./mapa.md) · [Mapa y conjunto →](./mapa-y-conjunto.md)
