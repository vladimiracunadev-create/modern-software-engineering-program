# Principal

[↑ Glosario](../../README.md) · [← Primera respuesta / resolución](./primera-respuesta-resolucion.md) · [Principio ágil →](./principio-agil.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Costo de eliminar el atajo que originó la deuda.

Definición de trabajo de [SE-310 — Deuda técnica, interés y opciones](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md).

## Por qué importa

En [SE-310 — Deuda técnica, interés y opciones](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md), el tema «Interés y principal» importa porque distinguen lo que cuesta arreglar de lo que cuesta no arreglar.

## Cómo funciona

Según [SE-310 — Deuda técnica, interés y opciones](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md):

Cunningham comparó entregar código con una comprensión incompleta con pedir un préstamo: sirve para llegar antes, y cada vez que se trabaja sobre ese código se paga un interés en forma de esfuerzo extra. La metáfora es útil porque permite discutir con negocio una decisión de plazo (llegar antes a cambio de un costo futuro) en lugar de un juicio de gusto sobre el código. Su riesgo es la analogía literal: la deuda de código no tiene un acreedor, ni un calendario de pagos, ni siempre un principal claro.

Según [SE-310 — Deuda técnica, interés y opciones](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md):

El equipo de `tarifas` no paga el tablero de 140 elementos. Estima, para los diez candidatos con más actividad en `git log`, tres cosas: la fricción por cambio (medida en una encuesta de tres preguntas al equipo y contrastada con el tiempo de los últimos cambios), la frecuencia de cambio (de la historia del repositorio) y el principal (una estimación en puntos, con rango). Calcula el interés anual y el plazo de recuperación. El módulo de descuentos, con tres cambios por trimestre y medio día de fricción, se paga ya; el de exportación, sin cambios en dos años, se deja con una nota; los demás se pagan al primer cambio con la regla de que quien lo toque lo deja mejor.

## Ejemplo

Ejemplo de [SE-310 — Deuda técnica, interés y opciones](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md) (sección «Ejemplo mínimo»):

El interés de un año supera el principal: pagar compensa en menos de un año. Registra versión, comando y salida; cambia a un cambio por año y predice la decisión.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se dedica un porcentaje fijo a «pagar deuda» sin resultados visibles** — causa: no se estimó el interés de cada elemento. Corrección: estimar interés y principal y ordenar por plazo de recuperación. ([SE-310](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Su riesgo es la analogía literal: la deuda de código no tiene un acreedor, ni un calendario de pagos, ni siempre un principal claro. ([SE-310](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-306](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md), [SE-307](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md), [SE-309](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Costo](../c/costo.md), [Deuda](../d/deuda.md), [Deuda deliberada](../d/deuda-deliberada.md), [Deuda técnica](../d/deuda-tecnica.md), [Interés](../i/interes.md), [Opción de refactorizar](../o/opcion-de-refactorizar.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-310 — Deuda técnica, interés y opciones](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

**También se usa en** (106 clases más lo mencionan; las que más):

[SE-572](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md), [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md), [SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md), [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md), [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md), [SE-174](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md), [SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md), [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Cunningham, «The WyCash Portfolio Management System» (OOPSLA, 1992)](http://c2.com/doc/oopsla92.html) — origen de la metáfora de la deuda; autoridad: su autor.
- [Kruchten, Nord y Ozkaya (IEEE Software, 2012)](https://doi.org/10.1109/MS.2012.167) — la metáfora y sus límites; autoridad: IEEE Software.
- [Tornhill y Borg (TechDebt, 2022)](https://doi.org/10.1145/3524843.3528091) — estudio cuantitativo de calidad del código y negocio; autoridad: Proceedings of the International Conference on Technical Debt.
- [Fowler, «Technical Debt»](https://martinfowler.com/bliki/TechnicalDebt.html) — la metáfora y el interés; autoridad: Martin Fowler.
- [Fowler, «Technical Debt Quadrant»](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html) — deuda deliberada e inadvertida; autoridad: Martin Fowler.

---

[↑ Glosario](../../README.md) · [← Primera respuesta / resolución](./primera-respuesta-resolucion.md) · [Principio ágil →](./principio-agil.md)
