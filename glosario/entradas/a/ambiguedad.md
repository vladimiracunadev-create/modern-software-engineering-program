# Ambigüedad

[↑ Glosario](../../README.md) · [← Ambassador](./ambassador.md) · [Amenaza a validez →](./amenaza-a-validez.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Propiedad de un texto que admite más de una lectura razonable con consecuencias distintas.

Definición de trabajo de [SE-154 — Ambigüedad, contradicción e incompletitud](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md): Propiedad de un enunciado que admite al menos dos implementaciones compatibles con el texto que dan resultados distintos para una misma entrada.
- En [SE-565 — De la intención a la especificación durable](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md): Decisión de comportamiento que el documento no resuelve y que, por tanto, toma quien implementa.
- En [SE-059 — Taller: descomponer un problema ambiguo](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md): Pluralidad de interpretaciones posibles.

## Por qué importa

En [SE-154 — Ambigüedad, contradicción e incompletitud](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md), el tema «Ambigüedad» importa porque una frase con dos lecturas se implementará de dos maneras.

En [SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md), el tema «Ambigüedad» importa porque una frase con varios puntos abiertos multiplica las lecturas: cuatro puntos binarios dan dieciséis comportamientos.

## Cómo funciona

Según [SE-154 — Ambigüedad, contradicción e incompletitud](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md), en la sección «Ambigüedad»:

Una frase es ambigua si admite más de una lectura razonable. Berry y colegas distinguen fuentes: léxica (una palabra con varios sentidos), sintáctica (agrupación de la frase), de alcance (qué abarca «todos» o «no»), referencial (a qué se refiere «lo» o «esto») y de elipsis. La ambigüedad estructural con «y» y «o» es la más fácil de contar y la más fácil de pasar por alto, porque cada persona lee una sola versión y no sabe que existe otra.

Según [SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md), en la sección «Ambigüedad»:

Meyer describió varios defectos de las especificaciones en lenguaje natural; dos importan aquí. El **silencio** omite un caso («¿qué pasa si el retraso es de 30 minutos?») y la **ambigüedad** admite dos lecturas con el mismo texto («por día», ¿día natural o bloque de 24 horas?). La ambigüedad no es un defecto de redacción individual sino una propiedad del texto frente a sus lectores: lo que a una persona le parece obvio, otra lo resuelve distinto. Por eso se mide ejecutando: si dos implementaciones compatibles con la frase dan resultados distintos sobre una misma entrada, la frase es ambigua con prueba, no por opinión.

## Ejemplo

Ejemplo de [SE-154 — Ambigüedad, contradicción e incompletitud](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md) (sección «Ejemplo profesional»):

Los identificadores, las fechas y los requisitos son ilustrativos. Compara con la ambigüedad que desaparece al añadir un ejemplo, la contradicción que solo aparece tras un cambio de `SE-153` y la celda abierta que resultó imposible por una regla de la interfaz. El inventario es apropiado cuando cada defecto tiene tipo, técnica y responsable; es peligroso cuando es una lista de observaciones sin dueño.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El agente entrega algo que funciona y no es lo que se quería** — causa: ambigüedades sin resolver que el agente resolvió. Corrección: resolver las de mayor costo y declarar las que se delegan. ([SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La ambigüedad estructural con «y» y «o» es la más fácil de contar y la más fácil de pasar por alto, porque cada persona lee una sola versión y no sabe que existe otra. ([SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md))
- La ambigüedad no es un defecto de redacción individual sino una propiedad del texto frente a sus lectores: lo que a una persona le parece obvio, otra lo resuelve distinto. ([SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Consecuencia](../c/consecuencia.md), [Documento](../d/documento.md), [Interpretación](../i/interpretacion.md), [Propiedad](../p/propiedad.md), [Actor](./actor.md), [Conflicto](../c/conflicto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-059 — Taller: descomponer un problema ambiguo](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-154 — Ambigüedad, contradicción e incompletitud](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.
- [SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-565 — De la intención a la especificación durable](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (52 clases más lo mencionan; las que más):

[SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md), [SE-552](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-552-proyecto-politica-metodologica-de-equipo-con-evidencia/README.md), [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md), [SE-234](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md), [SE-381](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md), [SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md), [SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md), [SE-538](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-538-portafolio-entrevistas-y-defensa-profesional/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Berry, Kamsties y Krieger: From contract drafting to software specification, linguistic sources of ambiguity (2003)](https://cs.uwaterloo.ca/~dberry/handbook/ambiguityHandbook.pdf) — tipos de ambigüedad en requisitos; autoridad: Universidad de Waterloo.
- [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) — características de un buen requisito, incluida la ausencia de ambigüedad; autoridad: ISO, IEC e IEEE.
- [Mavin et al.: Easy Approach to Requirements Syntax, EARS (2009)](https://doi.org/10.1109/RE.2009.9) — plantillas de redacción; autoridad: IEEE International Requirements Engineering Conference.
- [Heitmeyer, Jeffords y Labaw: Automated consistency checking of requirements specifications (1996)](https://doi.org/10.1145/234426.234431) — verificación de consistencia y completitud; autoridad: ACM Transactions on Software Engineering and Methodology.
- [Harel: Statecharts, a visual formalism for complex systems (1987)](https://doi.org/10.1016/0167-6423%2887%2990035-9) — estados y transiciones; autoridad: Science of Computer Programming.

---

[↑ Glosario](../../README.md) · [← Ambassador](./ambassador.md) · [Amenaza a validez →](./amenaza-a-validez.md)
