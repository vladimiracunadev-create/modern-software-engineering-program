# Estructura del paquete

[↑ Glosario](../../README.md) · [← Estructura](./estructura.md) · [Estructuras enlazadas →](./estructuras-enlazadas.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

El paquete se compone de cinco tipos de artefacto (intención, requisito, contrato, ejemplo y prueba) con identificadores estables (`INT-1`, `REQ-4`, `CON-4`, `EJE-7`, `TST-3`) y una lista de enlaces que apuntan hacia el origen: un requisito enlaza a una intención, un contrato a un requisito, un ejemplo y una prueba a un contrato, y una prueba también a un ejemplo. Los tipos de enlace permitidos están declarados, de modo que una prueba enlazada directamente a una intención es un error de estructura.

Explicación de la sección «Estructura del paquete» de [SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md).

## Por qué importa

En [SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md), el tema «Estructura del paquete» importa porque un paquete con tipos de artefacto y de enlace definidos permite comprobaciones mecánicas.

En [SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md), el tema «Estructura del paquete» importa porque sin campos obligatorios, faltan eslabones.

En [SE-456 — Proyecto: paquete de aseguramiento de un controlador](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md), el tema «Estructura del paquete» importa porque permite a otra persona recorrerlo sin ayuda.

## Cómo funciona

Según [SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md), en la sección «Estructura del paquete»:

El paquete se compone de cinco tipos de artefacto (intención, requisito, contrato, ejemplo y prueba) con identificadores estables (`INT-1`, `REQ-4`, `CON-4`, `EJE-7`, `TST-3`) y una lista de enlaces que apuntan hacia el origen: un requisito enlaza a una intención, un contrato a un requisito, un ejemplo y una prueba a un contrato, y una prueba también a un ejemplo. Los tipos de enlace permitidos están declarados, de modo que una prueba enlazada directamente a una intención es un error de estructura. El identificador no cambia cuando cambia el título, y el contenido tiene una huella.

Según [SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md), en la sección «Estructura del paquete»:

Cada requisito tiene estado (cumple, no aplica, excepción), control, prueba, evidencia, fecha, alcance (versión del producto) y dueño. «No aplica» exige justificación; una excepción exige dueño y fecha de vencimiento. La evidencia es el resultado ejecutable de una prueba, no una captura.

## Ejemplo

Caso medido en la sección «Estructura del paquete» de [SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md):

El paquete se compone de cinco tipos de artefacto (intención, requisito, contrato, ejemplo y prueba) con identificadores estables (`INT-1`, `REQ-4`, `CON-4`, `EJE-7`, `TST-3`) y una lista de enlaces que apuntan hacia el origen: un requisito enlaza a una intención, un contrato a un requisito, un ejemplo y una prueba a un contrato, y una prueba también a un ejemplo. Los tipos de enlace permitidos están declarados, de modo que una prueba enlazada directamente a una intención es un error de estructura. El identificador no cambia cuando cambia el título, y el contenido tiene una huella.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md)) son:

- **Un revisor no sabe qué ejemplo respalda una cláusula** — causa: faltan enlaces entre contrato y ejemplo. Corrección: exigir cobertura en ambos sentidos y comprobarla en integración continua.
- **Al renombrar un artefacto se rompen enlaces** — causa: los identificadores dependen del título. Corrección: identificadores estables y comprobación de enlaces colgantes.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2): mutaciones y alcance idénticos, huella distinta con el modo de texto por defecto e idéntica con el salto de línea fijo, tiempos distintos. El paquete es sintético, el validador comprueba forma y huellas, y los grafos de alcance son supuestos del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-167](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcance de un cambio](../a/alcance-de-un-cambio.md), [Análisis de impacto](../a/analisis-de-impacto.md), [Disparador de revisión](../d/disparador-de-revision.md), [Evidencia obsoleta](./evidencia-obsoleta.md), [Hueco de contenido](../h/hueco-de-contenido.md), [Huella reproducible](../h/huella-reproducible.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-456 — Proyecto: paquete de aseguramiento de un controlador](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.
- [SE-468 — Proyecto: producto con seguridad verificable](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

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

[↑ Glosario](../../README.md) · [← Estructura](./estructura.md) · [Estructuras enlazadas →](./estructuras-enlazadas.md)
