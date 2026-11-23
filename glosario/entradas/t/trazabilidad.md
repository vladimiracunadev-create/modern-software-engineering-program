# Trazabilidad

[↑ Glosario](../../README.md) · [← Traza enriquecida](./traza-enriquecida.md) · [Trazabilidad bidireccional →](./trazabilidad-bidireccional.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

La **trazabilidad** es la capacidad de seguir un artefacto hacia su origen y hacia sus consecuencias. [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md) la toma de Gotel y Finkelstein: seguir un requisito hacia atrás, hasta de dónde viene, y hacia adelante, hasta lo que produjo (contratos, ejemplos, pruebas). [SE-060](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-060-proyecto-especificacion-y-solucion-contrastable/README.md) la reduce al vínculo entre necesidad, regla, solución y evidencia; [SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md) la aplica a los cambios de un repositorio (motivo, cambio, uso); y [SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md) la exige en sistemas regulados como una relación verificable entre requisito, control, prueba y evidencia. El sentido común es el de un camino de ida y vuelta que alguien puede recorrer y comprobar.

## Por qué importa

Permite responder dos preguntas que se hacen siempre en el peor momento: «¿qué verifica este requisito?» y «¿por qué existe esto?». [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) la presenta como lo que un regulador pedirá y como hallazgo útil antes de que lo pregunte: con 30 requisitos y 45 pruebas generados con semilla, 9 requisitos quedan sin ninguna prueba y 2 pruebas sin requisito. Sin trazabilidad, el análisis de impacto de un cambio es una conjetura.

## Cómo funciona

Para que sirva, la trazabilidad debe tener **cobertura en ambos sentidos** ([SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md)): todo requisito tiene al menos un contrato, todo contrato tiene ejemplo y prueba, y todo ejemplo y prueba pertenece a algún contrato. [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) los nombra como trazabilidad **hacia adelante** («¿qué prueba verifica este requisito?») y **hacia atrás** («¿de qué requisito o peligro viene esta prueba?»).

La causa de que muchos proyectos la abandonen es el mantenimiento: los enlaces que nadie mantiene se convierten en ruido y la trazabilidad cae en desuso. Por eso [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md) aconseja un costo de mantenimiento bajo (identificadores estables, comprobación en integración continua) y un alcance acotado: no todo se enlaza con todo. [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) agrega que una trazabilidad construida al final suele fallar, y una mantenida junto al código, con un comprobador, cuesta menos.

En un repositorio, [SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md) usa una **matriz de trazabilidad** que relaciona cambios con motivos y expone huérfanos en ambos sentidos: commits sin motivo e issues sin cambio. No exige que todo commit tenga issue, pero exige decidir cuáles pueden no tenerlo.

## Ejemplo

[SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md) construye un paquete sintético de 41 artefactos (3 intenciones, 8 requisitos, 8 contratos, 12 ejemplos y 10 pruebas) y un validador que comprueba enlaces colgantes, tipos permitidos, requisitos y contratos sin descendiente, ciclos y huellas. Aplica 240 mutaciones de ocho tipos con semilla fija y el validador detecta todas las de forma (por ejemplo, 33 de 33 enlaces a un identificador inexistente y 32 de 32 requisitos sin contrato). No detecta un texto que cambia de sentido con el rastro intacto: prueba que los eslabones existen, no que digan la verdad.

En [SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md), sobre 60 cambios y 25 issues generados, el cierre `Fixes` de un commit integrado con *squash* se pierde: el único con squash no queda visible en `main` porque el commit de integración solo dice «Integra rama».

## Errores y confusiones comunes

- **Creer que un enlace garantiza que la prueba verifica el requisito.** La cobertura de enlaces mide que hay un enlace, no que la prueba compruebe el requisito; eso lo decide la revisión ([SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md)).
- **Enlazar todo con todo.** Aumenta el costo de mantenimiento y acaba abandonada ([SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md)).
- **Perder el vínculo al integrar.** Una integración con squash que descarta el cuerpo del mensaje borra la única referencia al issue ([SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md)).
- **Construirla al final.** Se reconstruye de memoria y falla ([SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md)).

## Límites y cuándo no aplica

El validador de [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md) comprueba forma y huellas sobre un paquete sintético; en uno real los enlaces los escribe una persona que puede enlazar mal, y un enlace válido puede apuntar al artefacto equivocado. En [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) el comprobador solo verifica estructura, no si el argumento es convincente. Los números de [SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md) son de un repositorio pequeño con una proporción de squash elegida por el autor: muestran el mecanismo, no cuántos vínculos pierde un proyecto real. Y no cubre los vínculos que viven en la descripción de una solicitud de integración, que el alojamiento puede conservar aparte.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Artefacto](../a/artefacto.md), [Capacidad](../c/capacidad.md), [Consecuencia](../c/consecuencia.md), [Control](../c/control.md), [Alcance de un cambio](../a/alcance-de-un-cambio.md), [Análisis de impacto](../a/analisis-de-impacto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-060 — Proyecto: especificación y solución contrastable](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-060-proyecto-especificacion-y-solucion-contrastable/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-198 — Issues, discusiones y trazabilidad del cambio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.
- [SE-450 — Casos de seguridad y trazabilidad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.
- [SE-466 — Cumplimiento, evidencia y límites legales](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.
- [SE-564 — Proyecto: cambio real con trazabilidad y revisión humana](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.
- [SE-565 — De la intención a la especificación durable](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (596 clases más lo mencionan; las que más):

[SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md), [SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md), [SE-448](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md), [SE-563](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md), [SE-123](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md), [SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md), [SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md), [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md).

**Aparece en los casos de estudio:** [Therac-25](../../../casos/fallo/therac-25.md), [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Gotel y Finkelstein, «An analysis of the requirements traceability problem» (ICRE, 1994)](https://doi.org/10.1109/ICRE.1994.292398) — definición y problemas de la trazabilidad de requisitos; autoridad: IEEE International Conference on Requirements Engineering.
- [Cleland-Huang et al., «Software traceability: trends and future directions» (FOSE, 2014)](https://doi.org/10.1145/2593882.2593891) — técnicas de creación y mantenimiento de enlaces; autoridad: ACM Future of Software Engineering.
- [FIPS 180-4: Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) — especificación de SHA-256; autoridad: NIST.
- [Git: gitattributes](https://git-scm.com/docs/gitattributes) — control de los saltos de línea y de las conversiones; autoridad: proyecto Git.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — requisitos, configuración y calidad de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Traza enriquecida](./traza-enriquecida.md) · [Trazabilidad bidireccional →](./trazabilidad-bidireccional.md)
