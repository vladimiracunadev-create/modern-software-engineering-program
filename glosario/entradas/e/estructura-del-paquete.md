# Estructura del paquete

[↑ Glosario](../../README.md) · [← Estructura](./estructura.md) · [Estructuras enlazadas →](./estructuras-enlazadas.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

La **estructura del paquete** es la forma declarada de un paquete de trabajo: qué tipos de artefacto contiene, cómo se identifican y qué enlaces entre ellos son válidos. En [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md) (paquete de especificaciones trazables) se compone de cinco tipos de artefacto (intención, requisito, contrato, ejemplo y prueba) con identificadores estables (`INT-1`, `REQ-4`, `CON-4`, `EJE-7`, `TST-3`). [SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md) y [SE-456](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md) aplican la misma idea a un paquete de seguridad verificable y a uno de aseguramiento de un controlador.

## Por qué importa

Cambia si el paquete se puede comprobar con una máquina y recorrer sin ayuda. Un paquete con tipos de artefacto y de enlace definidos permite comprobaciones mecánicas ([SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md)); sin campos obligatorios, faltan eslabones ([SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md)); con estructura clara, otra persona lo recorre sin que su autor esté presente ([SE-456](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md)).

## Cómo funciona

Los enlaces apuntan hacia el origen: un requisito enlaza a una intención, un contrato a un requisito, un ejemplo y una prueba a un contrato, y una prueba también a un ejemplo. Los **tipos de enlace permitidos están declarados**, de modo que un enlace no previsto (por ejemplo, una prueba directamente a una intención) se rechaza. Los identificadores son **estables**: no dependen del título, así que renombrar un artefacto no rompe enlaces.

Con esa estructura, un validador puede comprobar presencia, enlaces colgantes y cobertura en ambos sentidos (cada cláusula del contrato tiene ejemplo, cada ejemplo respalda una cláusula), y puede correrse en integración continua. En el paquete de seguridad de [SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md), cada requisito añade estado (cumple, no aplica, excepción), control, prueba, evidencia, fecha, alcance y dueño: «no aplica» exige justificación y una excepción exige dueño y fecha de vencimiento. La evidencia es el resultado ejecutable de una prueba, no una captura.

## Ejemplo

En la plataforma de entregas de [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md), el requisito `REQ-4` enlaza a `INT-1`; el contrato `CON-4` enlaza a `REQ-4`; el ejemplo `EJE-7` y la prueba `TST-3` enlazan a `CON-4`, y la prueba también a `EJE-7`. Si alguien renombra el título del requisito, el identificador no cambia y ningún enlace se rompe; si añade una prueba sin contrato, el validador la señala.

## Errores y confusiones comunes

- **Un revisor no sabe qué ejemplo respalda una cláusula.** Faltan enlaces entre contrato y ejemplo; exigir cobertura en ambos sentidos y comprobarla en integración continua.
- **Al renombrar se rompen enlaces.** Los identificadores dependen del título; usar identificadores estables y comprobar enlaces colgantes.
- **Confundir estructura con calidad.** Un paquete bien enlazado puede tener requisitos malos.
- **Evidencia como captura de pantalla.** Debe ser el resultado ejecutable de una prueba.

## Límites y cuándo no aplica

La estructura garantiza que los enlaces existen, no que sean ciertos: un validador que solo comprueba forma deja pasar un enlace erróneo. Los experimentos de [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md) usan datos sintéticos, y el alcance de sus mutaciones es el de la clase. Para un cambio pequeño, un paquete de cinco tipos puede ser más costo que beneficio.

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
