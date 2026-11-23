# Objeto de valor

[↑ Glosario](../../README.md) · [← Objeto alcanzable](./objeto-alcanzable.md) · [Objeto, identidad y estado válido →](./objeto-identidad-y-estado-valido.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Objeto inmutable sin identidad que se define por sus atributos y encapsula sus reglas.

Definición de trabajo de [SE-329 — Domain-Driven Design estratégico y táctico](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md).

## Por qué importa

En [SE-329 — Domain-Driven Design estratégico y táctico](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md), el tema «Entidades y objetos de valor» importa porque ponen la regla de igualdad y de redondeo en un solo sitio.

## Cómo funciona

Según [SE-329 — Domain-Driven Design estratégico y táctico](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md):

Una **entidad** tiene identidad y ciclo de vida (la entrega 4711 sigue siendo la misma aunque cambie su estado); un **objeto de valor** no tiene identidad y se define por sus atributos (la nota 5,5 es igual a otra nota 5,5), es inmutable y encapsula sus reglas. Una nota modelada como `float` deja el redondeo, el rango y la comparación repartidos por todo el código; una clase `Nota` los reúne en un lugar que se prueba una vez. Esa es la razón práctica del objeto de valor: convertir una regla repetida en un solo sitio con pruebas.

Según [SE-329 — Domain-Driven Design estratégico y táctico](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md):

El equipo de la plataforma dibuja tres contextos (Aprendizaje, Evaluación, Administración) y un contrato de tres atributos entre ellos (identificador, estudiante, estado resumido), con una capa anticorrupción en Administración que traduce el estado de Evaluación. En Evaluación, `Entrega` es un agregado cuya raíz protege «como máximo tres reenvíos»; el repositorio guarda con comprobación de versión y el caso de uso reintenta una vez ante conflicto. La nota es un objeto de valor en décimas enteras con la regla «medio hacia arriba» y una prueba que compara los 3721 pares contra `Fraction`. Antes, el 56,8 % de los cambios de un atributo afectaba a más de un equipo; ahora, con el contrato pequeño, un 20,2 %.

## Ejemplo

Ejemplo de [SE-329 — Domain-Driven Design estratégico y táctico](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md) (sección «Ejemplo mínimo»):

El fragmento muestra un objeto de valor con la regla de redondeo en un solo sitio. Antes de ejecutarlo, predice el promedio de 1,0 y 1,3.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El redondeo difiere entre pantallas** — causa: la regla vive repetida en el código. Corrección: encapsular en un objeto de valor y probar contra una referencia exacta. ([SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una **entidad** tiene identidad y ciclo de vida (la entrega 4711 sigue siendo la misma aunque cambie su estado); un **objeto de valor** no tiene identidad y se define por sus atributos (la nota 5,5 es igual a otra nota 5,5), es inmutable y encapsula sus reglas. ([SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-328](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Atributo](../a/atributo.md), [Objeto](./objeto.md), [Regla](../r/regla.md), [Agregado](../a/agregado.md), [Contexto delimitado](../c/contexto-delimitado.md), [Invariante](../i/invariante.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-329 — Domain-Driven Design estratégico y táctico](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-075](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md), [SE-543](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «Value Object»](https://martinfowler.com/bliki/ValueObject.html) — objetos de valor; autoridad: Martin Fowler.
- [Evans, «Domain-Driven Design Reference»](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf) — resumen de patrones estratégicos y tácticos; autoridad: Eric Evans.
- [Fowler, «Bounded Context»](https://martinfowler.com/bliki/BoundedContext.html) — contexto delimitado; autoridad: Martin Fowler.
- [Fowler, «DDD Aggregate»](https://martinfowler.com/bliki/DDD_Aggregate.html) — agregado como unidad de consistencia; autoridad: Martin Fowler.
- [Python: `decimal`](https://docs.python.org/3/library/decimal.html) — aritmética decimal y modos de redondeo; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Objeto alcanzable](./objeto-alcanzable.md) · [Objeto, identidad y estado válido →](./objeto-identidad-y-estado-valido.md)
