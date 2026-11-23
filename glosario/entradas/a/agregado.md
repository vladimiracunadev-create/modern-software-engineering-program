# Agregado

[↑ Glosario](../../README.md) · [← Agregación y segmentos](./agregacion-y-segmentos.md) · [Agrupación →](./agrupacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Grupo de objetos que se modifica como una unidad a través de una raíz que protege un invariante.

Definición de trabajo de [SE-329 — Domain-Driven Design estratégico y táctico](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md).

## Por qué importa

En [SE-329 — Domain-Driven Design estratégico y táctico](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md), el tema «Agregados e invariantes» importa porque definen qué debe ser consistente al instante y qué puede esperar.

## Cómo funciona

Según [SE-329 — Domain-Driven Design estratégico y táctico](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md):

Un **agregado** es un grupo de objetos que se trata como una unidad en los cambios, con una **raíz** por la que pasan todos los comandos. Existe para proteger un **invariante**: una regla que debe cumplirse siempre dentro de esa unidad («una entrega admite como máximo tres reenvíos»). La consistencia dentro del agregado es inmediata (una transacción); entre agregados es eventual. El tamaño del agregado es una decisión de concurrencia: uno muy grande bloquea a todos los que lo tocan; uno muy pequeño no puede garantizar su invariante. Dos comandos que leen el mismo estado y escriben después pueden violarlo si no hay control.

Según [SE-329 — Domain-Driven Design estratégico y táctico](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md):

El equipo de la plataforma dibuja tres contextos (Aprendizaje, Evaluación, Administración) y un contrato de tres atributos entre ellos (identificador, estudiante, estado resumido), con una capa anticorrupción en Administración que traduce el estado de Evaluación. En Evaluación, `Entrega` es un agregado cuya raíz protege «como máximo tres reenvíos»; el repositorio guarda con comprobación de versión y el caso de uso reintenta una vez ante conflicto. La nota es un objeto de valor en décimas enteras con la regla «medio hacia arriba» y una prueba que compara los 3721 pares contra `Fraction`. Antes, el 56,8 % de los cambios de un atributo afectaba a más de un equipo; ahora, con el contrato pequeño, un 20,2 %.

## Ejemplo

Ejemplo de [SE-329 — Domain-Driven Design estratégico y táctico](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma dibuja tres contextos (Aprendizaje, Evaluación, Administración) y un contrato de tres atributos entre ellos (identificador, estudiante, estado resumido), con una capa anticorrupción en Administración que traduce el estado de Evaluación. En Evaluación, `Entrega` es un agregado cuya raíz protege «como máximo tres reenvíos»; el repositorio guarda con comprobación de versión y el caso de uso reintenta una vez ante conflicto. La nota es un objeto de valor en décimas enteras con la regla «medio hacia arriba» y una prueba que compara los 3721 pares contra `Fraction`.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-329 — Domain-Driven Design estratégico y táctico](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md)) son:

- **Cada cambio de un atributo exige coordinar a tres equipos** — causa: un modelo único compartido. Corrección: separar contextos y reducir el contrato a lo necesario.
- **La misma palabra significa cosas distintas en reuniones** — causa: hay varios contextos sin declarar. Corrección: escribir el significado en cada contexto y el mapa de relaciones.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El tamaño del agregado es una decisión de concurrencia: uno muy grande bloquea a todos los que lo tocan; uno muy pequeño no puede garantizar su invariante. ([SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-328](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Invariante](../i/invariante.md), [Objeto](../o/objeto.md), [Raíz](../r/raiz.md), [Contexto delimitado](../c/contexto-delimitado.md), [Mapa de contextos](../m/mapa-de-contextos.md), [Objeto de valor](../o/objeto-de-valor.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-329 — Domain-Driven Design estratégico y táctico](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

**También se usa en** (34 clases más lo mencionan; las que más):

[SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md), [SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md), [SE-369](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-369-gobierno-privacidad-y-retencion-de-datos/README.md), [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md), [SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md), [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md), [SE-194](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md), [SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «DDD Aggregate»](https://martinfowler.com/bliki/DDD_Aggregate.html) — agregado como unidad de consistencia; autoridad: Martin Fowler.
- [Evans, «Domain-Driven Design Reference»](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf) — resumen de patrones estratégicos y tácticos; autoridad: Eric Evans.
- [Fowler, «Bounded Context»](https://martinfowler.com/bliki/BoundedContext.html) — contexto delimitado; autoridad: Martin Fowler.
- [Fowler, «Value Object»](https://martinfowler.com/bliki/ValueObject.html) — objetos de valor; autoridad: Martin Fowler.
- [Python: `decimal`](https://docs.python.org/3/library/decimal.html) — aritmética decimal y modos de redondeo; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Agregación y segmentos](./agregacion-y-segmentos.md) · [Agrupación →](./agrupacion.md)
