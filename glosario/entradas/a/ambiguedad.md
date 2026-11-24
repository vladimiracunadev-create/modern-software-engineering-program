# Ambigüedad

[↑ Glosario](../../README.md) · [← Ambassador](./ambassador.md) · [Amenaza a validez →](./amenaza-a-validez.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

La **ambigüedad** es la propiedad de un texto que admite más de una lectura razonable con consecuencias distintas ([SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md)). [SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md) la vuelve verificable: un enunciado es ambiguo si admite al menos dos implementaciones compatibles con el texto que dan resultados distintos para la misma entrada. [SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md) la mira como decisión no resuelta: un comportamiento que el documento no fija y que, por tanto, decide quien implementa. En [SE-059](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md) es, más simplemente, la pluralidad de interpretaciones de un problema.

## Por qué importa

Una frase con dos lecturas se implementa de dos maneras, y nadie lo nota porque cada persona lee una sola versión. El coste aparece tarde, en integración o producción. Y se multiplica: [SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md) observa que cuatro puntos abiertos binarios dan dieciséis comportamientos posibles. Con agentes de código ([SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md)) el efecto es mayor: el agente entrega algo que funciona y no es lo que se quería, porque resolvió por su cuenta las ambigüedades.

## Cómo funciona

[SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md), siguiendo a Berry y colegas, distingue fuentes:

- **léxica**: una palabra con varios sentidos;
- **sintáctica**: cómo se agrupa la frase;
- **de alcance**: qué abarca «todos» o «no»;
- **referencial**: a qué se refiere «lo» o «esto»;
- **de elipsis**: lo que se omite.

La estructural con «y» y «o» es la más fácil de contar y de pasar por alto. [SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md) la distingue del **silencio** (omitir un caso). Su causa no es descuido individual sino que el texto se lee frente a lectores con supuestos distintos. Por eso se detecta ejecutando: se escriben las lecturas, se calculan los resultados y se compara. Se corrige añadiendo ejemplos, una forma semiformal o formal, o resolviendo la decisión por escrito ([SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md)).

## Ejemplo

«Máximo tres reintentos por día»: ¿día natural o ventana de 24 horas? Dos implementaciones compatibles dan resultados distintos con una misma secuencia de intentos; eso demuestra la ambigüedad sin discutir opiniones (ejemplo de [SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md) en esencia: «por día»). En [SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md) el inventario de defectos sirve cuando cada uno tiene tipo, técnica y responsable.

## Errores y confusiones comunes

- **Entrega que funciona pero no es lo pedido.** Causa: ambigüedades sin resolver que el agente resolvió; corrección: resolver las de mayor costo y declarar las que se delegan ([SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md)).
- **Confundirla con contradicción o incompletitud** ([SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md)): la ambigüedad admite dos lecturas; la contradicción, dos reglas incompatibles; la incompletitud, un caso no cubierto.
- **Creer que es un fallo de redacción personal.** Es propiedad del texto frente a sus lectores.

## Límites y cuándo no aplica

No toda indeterminación es un defecto: algunos puntos se delegan a propósito. No se elimina escribiendo más; se reduce con ejemplos y comprobaciones. La medición por implementaciones alternativas solo cubre las lecturas que alguien imaginó.

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
