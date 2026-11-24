# Lenguaje ubicuo

[↑ Glosario](../../README.md) · [← Legibilidad](./legibilidad.md) · [Lentitud de la dependencia →](./lentitud-de-la-dependencia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

El **lenguaje ubicuo** (*ubiquitous language*) es el vocabulario que comparten las personas expertas del dominio y el equipo de desarrollo, y que se usa en la conversación, en la documentación y en el código. Es la definición de [SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md), tomada del diseño guiado por el dominio (DDD) de Evans, quien lo describe como el modelo hecho lenguaje.

## Por qué importa

La palabra «ubicuo» es una exigencia: no puede haber un vocabulario de negocio y otro de código con una traducción mental entre ambos. Esa traducción es una fuente constante de defectos: dos personas creen hablar de lo mismo y no es así, o un nombre de campo oculta que el negocio ya cambió su concepto. Adoptar el lenguaje ubicuo cambia cómo se nombran clases, funciones y campos, y cómo se discuten los requisitos.

## Cómo funciona

En la práctica ([SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md)):

- Los nombres de clases, funciones y campos **salen del glosario** acordado con el dominio.
- Cuando una palabra del negocio **cambia**, **cambia en el código**.
- No es un diccionario escrito una vez, sino un acuerdo que se **revisa con cada ejemplo de aceptación** ([SE-545](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md)): los ejemplos concretos con que se acuerda el comportamiento revelan si todos entienden lo mismo con cada palabra.

La causa de su eficacia: un término usado de dos formas es un defecto de requisito latente. Obligar a usar *una* palabra en conversación y en código saca esas discrepancias a la superficie cuando todavía son baratas de resolver. Además, el lenguaje ubicuo suele valer solo dentro de un contexto delimitado: la misma palabra («cliente») puede significar cosas distintas en dominios distintos, y cada contexto tiene el suyo.

## Ejemplo

[SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md) mide, con reglas burdas sobre un corpus de este mismo programa, qué términos se repiten con distinto sentido, y ensaya la traducción con ocho entregas sintéticas. Ilustración propia del mecanismo: en un sistema de entregas, el negocio habla de «aviso de entrega» y el código lo llama `Notification`; en una conversación, alguien dice «reenviar el aviso» y otra persona entiende que se vuelve a mandar el *mismo* mensaje, mientras que el código crea uno nuevo. Con lenguaje ubicuo, el código tendría `AvisoDeEntrega` y la regla «reenviar» estaría definida una sola vez.

## Errores y confusiones comunes

- **Un glosario escrito una vez y olvidado.** Es un acuerdo vivo, revisado con ejemplos.
- **Nombres técnicos en el código y negocio en las reuniones.** Es exactamente lo que el término prohíbe.
- **Confundirlo con un diccionario global de la empresa.** Cada contexto delimitado tiene el suyo.
- **Creer que basta con nombrar bien.** Hay que revisar que la palabra significa lo mismo para ambas partes.

## Límites y cuándo no aplica

[SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md) declara que sus recuentos usan reglas burdas sobre un corpus de este programa y que no se midió el efecto de DDD en un equipo; la técnica se presenta como práctica, no como resultado medido. Aplica sobre todo a dominios con complejidad de negocio; en un componente puramente técnico (un analizador sintáctico, una biblioteca de compresión) el «dominio» es técnico y el lenguaje ubicuo se reduce a la terminología de esa disciplina. Requiere acceso a las personas expertas del dominio: sin ellas, el glosario lo inventa el equipo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md), [SE-545](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capa anticorrupción](../c/capa-anticorrupcion.md), [Contexto delimitado](../c/contexto-delimitado.md), [Glosario](../g/glosario.md), [Mapa de contextos](../m/mapa-de-contextos.md), [Polisemia](../p/polisemia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-546 — DDD como lenguaje ubicuo y contexto para agentes](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md), [SE-547](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-547-diseno-por-contrato-y-pruebas-de-contrato-como-oraculo/README.md), [SE-545](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Legibilidad](./legibilidad.md) · [Lentitud de la dependencia →](./lentitud-de-la-dependencia.md)
