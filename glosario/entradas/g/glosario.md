# Glosario

[↑ Glosario](../../README.md) · [← Given-When-Then](./given-when-then.md) · [Gobernanza federada y computacional →](./gobernanza-federada-y-computacional.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

Lista de términos del dominio con su sentido en cada contexto.

Definición de trabajo de [SE-546 — DDD como lenguaje ubicuo y contexto para agentes](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md).

## Por qué importa

En [SE-546 — DDD como lenguaje ubicuo y contexto para agentes](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md), el tema «Glosario e instrucciones» importa porque es lo único que ve un agente antes de decidir qué significa una palabra.

## Cómo funciona

Según [SE-546 — DDD como lenguaje ubicuo y contexto para agentes](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md):

El **lenguaje ubicuo** es el vocabulario que comparten las personas expertas del dominio y el equipo de desarrollo, y que se usa en la conversación, en la documentación y en el código. La palabra «ubicuo» es una exigencia: no puede haber un vocabulario de negocio y otro de código con una traducción mental entre ambos. Evans lo describe como el modelo hecho lenguaje. En la práctica significa que los nombres de clases, funciones y campos salen del glosario y que, cuando una palabra del negocio cambia, cambia en el código. No es un diccionario escrito una vez: es un acuerdo que se revisa con cada ejemplo de aceptación (`SE-545`).

Según [SE-546 — DDD como lenguaje ubicuo y contexto para agentes](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md):

Al empezar el silencio, el equipo hace un glosario de siete términos con la persona experta: entrega, silencio, curso, aviso, umbral, vencimiento y estudiante. Para cada uno anota su sentido, en qué contexto vale y cuál es su nombre en el código. Descubren que «silencio» significa dos cosas: para la docente es «no molestar por este curso» y para el servicio de mensajería es «el canal rechazó el envío». Deciden nombrar al segundo «rechazo del canal» y reservar «silencio» para el primero. Cambian dos nombres en el código, añaden el glosario al repositorio y enlazan en las instrucciones («los términos del dominio se definen en `docs/glosario.md`; si dudas del sentido de una palabra, pregunta antes de nombrar»).

## Ejemplo

Ejemplo de [SE-546 — DDD como lenguaje ubicuo y contexto para agentes](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md) (sección «Ejemplo profesional»):

Al empezar el silencio, el equipo hace un glosario de siete términos con la persona experta: entrega, silencio, curso, aviso, umbral, vencimiento y estudiante. Para cada uno anota su sentido, en qué contexto vale y cuál es su nombre en el código. Descubren que «silencio» significa dos cosas: para la docente es «no molestar por este curso» y para el servicio de mensajería es «el canal rechazó el envío». Deciden nombrar al segundo «rechazo del canal» y reservar «silencio» para el primero.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- No es un defecto del texto: es el tipo de ambigüedad que un glosario con contexto resuelve. ([SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md))
- Si trabajas con un agente, mide si respeta el glosario: pídele una funcionalidad que use el término y comprueba qué nombres elige. ([SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md), [SE-545](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](../c/contextos.md), [Dominio](../d/dominio.md), [Capa anticorrupción](../c/capa-anticorrupcion.md), [Contexto delimitado](../c/contexto-delimitado.md), [Lenguaje ubicuo](../l/lenguaje-ubicuo.md), [Mapa de contextos](../m/mapa-de-contextos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-546 — DDD como lenguaje ubicuo y contexto para agentes](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (611 clases más lo mencionan; las que más):

[SE-213](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md), [SE-212](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md), [SE-214](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md), [SE-216](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md), [SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md), [SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md), [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md), [SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Given-When-Then](./given-when-then.md) · [Gobernanza federada y computacional →](./gobernanza-federada-y-computacional.md)
