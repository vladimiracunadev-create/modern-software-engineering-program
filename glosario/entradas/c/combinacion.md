# Combinación

[↑ Glosario](../../README.md) · [← Comandos, expresiones y secuencia](./comandos-expresiones-y-secuencia.md) · [Combinación de prácticas →](./combinacion-de-practicas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

Cubren interacciones que los ejemplos sueltos no ven.

Es uno de los temas de [SE-545 — ATDD y Specification by Example: aceptación ejecutable](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md), donde se enseña como «Combinaciones».

## Por qué importa

En [SE-551 — Taller: un mismo cambio con cinco metodologías](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-551-taller-un-mismo-cambio-con-cinco-metodologias/README.md), el tema «Combinación» importa porque dos prácticas de naturaleza distinta cubren más.

En [SE-545 — ATDD y Specification by Example: aceptación ejecutable](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md), el tema «Combinaciones» importa porque cubren interacciones que los ejemplos sueltos no ven.

## Cómo funciona

Según [SE-551 — Taller: un mismo cambio con cinco metodologías](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-551-taller-un-mismo-cambio-con-cinco-metodologias/README.md):

Los siete mutantes del silencio son: S1 ignora el silencio; S2 lo aplica también a la última hora; S3 silencia a la persona en todos sus cursos; S4 silencia el curso para todas las personas; S5 deja pasar el aviso de 24 horas; S6 solo silencia el de 72 horas; S7 silencia por curso o por persona (la combinación mal hecha). Se producen con un cambio mínimo en la línea que decide el silencio, y se comprobó que todos difieren del original en al menos un caso.

Según [SE-551 — Taller: un mismo cambio con cinco metodologías](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-551-taller-un-mismo-cambio-con-cinco-metodologias/README.md):

El equipo decide la combinación para el silencio. Descarta el modelo ejecutable completo (duplicaría la regla y un solo malentendido los afectaría a ambos) y conserva tres cosas: los tres escenarios de BDD con las docentes, como acuerdo y documentación; las dos pruebas de TDD, como protección de los bordes; y el contrato de propiedades, que añade la propiedad de aislamiento (silenciar un par persona-curso no cambia los avisos de otras entregas). Añade el ejemplo de dos personas en un curso. Antes de aceptar el cambio siembra los siete mutantes y comprueba que mueren todos. Registra el tamaño de cada artefacto y una nota:

## Ejemplo

Ejemplo de [SE-551 — Taller: un mismo cambio con cinco metodologías](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-551-taller-un-mismo-cambio-con-cinco-metodologias/README.md) (sección «Ejemplo profesional»):

El equipo decide la combinación para el silencio. Descarta el modelo ejecutable completo (duplicaría la regla y un solo malentendido los afectaría a ambos) y conserva tres cosas: los tres escenarios de BDD con las docentes, como acuerdo y documentación; las dos pruebas de TDD, como protección de los bordes; y el contrato de propiedades, que añade la propiedad de aislamiento (silenciar un par persona-curso no cambia los avisos de otras entregas). Añade el ejemplo de dos personas en un curso. Antes de aceptar el cambio siembra los siete mutantes y comprueba que mueren todos. Registra el tamaño de cada artefacto y una nota:

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La combinación razonable para este cambio, entonces, son pocos ejemplos acordados (que sirven de documentación y de aceptación) más un contrato (que cubre lo que nadie imaginó) y no un modelo completo, que duplica la regla. ([SE-551](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-551-taller-un-mismo-cambio-con-cinco-metodologias/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-544](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-544-bdd-ejemplos-conversacion-y-lenguaje-compartido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Artefacto de verificación](../a/artefacto-de-verificacion.md), [ATDD](../a/atdd.md), [Combinación de prácticas](./combinacion-de-practicas.md), [Conjunto combinatorio](./conjunto-combinatorio.md), [Dimensión](../d/dimension.md), [Dimensión no variada](../d/dimension-no-variada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-545 — ATDD y Specification by Example: aceptación ejecutable](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.
- [SE-551 — Taller: un mismo cambio con cinco metodologías](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-551-taller-un-mismo-cambio-con-cinco-metodologias/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (161 clases más lo mencionan; las que más):

[SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md), [SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md), [SE-309](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md), [SE-172](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md), [SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md), [SE-219](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md), [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md), [SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md).

**Aparece en los casos de estudio:** [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [Therac-25](../../../casos/fallo/therac-25.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Combinaciones».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Comandos, expresiones y secuencia](./comandos-expresiones-y-secuencia.md) · [Combinación de prácticas →](./combinacion-de-practicas.md)
