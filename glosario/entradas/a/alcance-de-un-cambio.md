# Alcance de un cambio

[↑ Glosario](../../README.md) · [← Alcance de la auditoría](./alcance-de-la-auditoria.md) · [Alcanzabilidad →](./alcanzabilidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Conjunto de artefactos alcanzables desde uno modificado siguiendo los enlaces.

Definición de trabajo de [SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md).

## Por qué importa

En [SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md), el tema «Trazabilidad» importa porque seguir cada afirmación hasta su origen permite revisar sin contexto y medir el alcance de un cambio.

## Cómo funciona

Según [SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md):

Los que permitan responder las preguntas de revisión y de impacto que importan, y no más: cada enlace es un coste de mantenimiento. El experimento de alcance muestra que la densidad de enlaces multiplica el alcance de un cambio, de modo que enlazar de más no es gratis.

## Ejemplo

Ejemplo de [SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md) (sección «Preguntas frecuentes»):

Los que permitan responder las preguntas de revisión y de impacto que importan, y no más: cada enlace es un coste de mantenimiento. El experimento de alcance muestra que la densidad de enlaces multiplica el alcance de un cambio, de modo que enlazar de más no es gratis.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md)) son:

- **Un revisor no sabe qué ejemplo respalda una cláusula** — causa: faltan enlaces entre contrato y ejemplo. Corrección: exigir cobertura en ambos sentidos y comprobarla en integración continua.
- **Al renombrar un artefacto se rompen enlaces** — causa: los identificadores dependen del título. Corrección: identificadores estables y comprobación de enlaces colgantes.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El experimento de alcance muestra que la densidad de enlaces multiplica el alcance de un cambio, de modo que enlazar de más no es gratis. ([SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-167](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Artefacto](./artefacto.md), [Conjunto](../c/conjunto.md), [Análisis de impacto](./analisis-de-impacto.md), [Huella reproducible](../h/huella-reproducible.md), [Manifiesto](../m/manifiesto.md), [Paquete trazable](../p/paquete-trazable.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md), [SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md), [SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md), [SE-328](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md).

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

[↑ Glosario](../../README.md) · [← Alcance de la auditoría](./alcance-de-la-auditoria.md) · [Alcanzabilidad →](./alcanzabilidad.md)
