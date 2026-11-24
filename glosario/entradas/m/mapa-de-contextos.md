# Mapa de contextos

[↑ Glosario](../../README.md) · [← Mapa](./mapa.md) · [Mapa y conjunto →](./mapa-y-conjunto.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Un **mapa de contextos** es la descripción de los contextos delimitados de un sistema y de la naturaleza de cada relación entre ellos ([SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md)). [SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md) lo usa como el diagrama de contextos y relaciones. Es un artefacto del diseño orientado al dominio que hace explícito quién depende de quién y de qué manera.

## Por qué importa

Cuando varios modelos coexisten y no se declara cómo se relacionan, cada cambio es una negociación improvisada y el acoplamiento se reparte sin control. La decisión que cambia es dónde se concentra el acoplamiento: en contratos pequeños y declarados entre contextos, no en un modelo compartido por todos.

## Cómo funciona

[SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md) enumera los tipos de relación que el mapa declara:

- **Socios** que coordinan cambios.
- **Cliente y proveedor**, donde uno depende de otro.
- **Conformista**: un contexto que acepta el modelo del vecino tal cual.
- **Capa anticorrupción**: un contexto que traduce el modelo ajeno al propio para que no lo contamine.

Lo importante es que **cada relación se declare**, porque define quién debe coordinar con quién. Un contrato pequeño y estable entre contextos (tres atributos compartidos, no catorce) concentra el acoplamiento donde puede gestionarse y deja el resto libre para cambiar.

La causa de su utilidad es que convierte lo implícito en explícito. Los síntomas que enumera la clase apuntan a su ausencia: cada cambio de un atributo exige coordinar a tres equipos (un modelo único compartido), o la misma palabra significa cosas distintas en reuniones (hay varios contextos sin declarar). En ambos casos, la corrección es separar contextos, escribir el significado en cada uno y dibujar el mapa de relaciones. [SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md) lo aplica al diseño de un sistema pequeño con avisos y entregas.

## Ejemplo

Un sistema tiene los contextos Académico, Avisos y Facturación. El mapa declara: Avisos es cliente de Académico y adopta su modelo de entrega a través de una capa anticorrupción; Facturación es conformista respecto de Académico; Académico y Avisos coordinan cambios como socios en un contrato de tres atributos. Con eso queda claro quién debe hablar con quién antes de cambiar algo. Ejemplo ilustrativo siguiendo [SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md).

## Errores y confusiones comunes

- **Cada cambio de un atributo exige coordinar a tres equipos**: un modelo único compartido; se corrige separando contextos y reduciendo el contrato a lo necesario.
- **La misma palabra significa cosas distintas en reuniones**: hay varios contextos sin declarar.
- **Dibujar solo cajas**: sin declarar la naturaleza de cada relación no es un mapa.
- **Confundirlo con un diagrama de despliegue**: muestra relaciones entre modelos, no entre servidores.

## Límites y cuándo no aplica

El mapa solo tiene sentido si hay dos o más contextos; en un sistema con un único modelo no hace falta. Un mapa deja de valer en cuanto la realidad cambia y nadie lo actualiza. Y declarar una relación no la hace cumplirse: la capa anticorrupción o el contrato pequeño deben existir en el código, no solo en el diagrama.

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
