# Composición y tipos de resultado

[↑ Glosario](../../README.md) · [← Composición y nivel de abstracción](./composicion-y-nivel-de-abstraccion.md) · [Composite →](./composite.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

Funciones pequeñas se conectan cuando la salida de una satisface la entrada de otra.

Definición de trabajo de [SE-076 — Programación funcional, composición e inmutabilidad](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md).

## Por qué importa

En [SE-076 — Programación funcional, composición e inmutabilidad](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md), el tema «Composición y tipos de resultado» importa porque funciones pequeñas se conectan cuando la salida de una satisface la entrada de otra.

## Cómo funciona

Según [SE-076 — Programación funcional, composición e inmutabilidad](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md), en la sección «Composición y tipos de resultado»:

Funciones pequeñas se conectan cuando la salida de una satisface la entrada de otra. Un resultado explícito distingue éxito y error sin lanzar a distancia. La composición falla si cada paso usa convenciones distintas para ausencia, error o contexto.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-076 — Programación funcional, composición e inmutabilidad](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md):

En el motor de reglas comparado, una recomendación contiene acción, evidencia usada, versión de política y explicación. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si devuelve una cadena: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-076 — Programación funcional, composición e inmutabilidad](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md)) son:

- **Todas las funciones de una lista devuelven el último valor** — causa: cierre que captura la variable y no su valor. Corrección: capturar con argumento por defecto o `partial`.
- **Una «tupla inmutable» cambia** — causa: contiene un objeto mutable. Corrección: usar contenidos inmutables o copiar al construir.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-076 — Programación funcional, composición e inmutabilidad](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md)) son: Las definiciones son operativas para el motor de reglas comparado. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Pureza y composición no resuelven automáticamente interacción, latencia ni grandes flujos. La siguiente clase expresa el resultado deseado como reglas declarativas.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Función](../f/funcion.md), [Funciones de orden superior](../f/funciones-de-orden-superior.md), [Funciones puras y transparencia referencial](../f/funciones-puras-y-transparencia-referencial.md), [Inmutabilidad y evolución de valores](../i/inmutabilidad-y-evolucion-de-valores.md), [Recursión, evaluación y efectos](../r/recursion-evaluacion-y-efectos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-076 — Programación funcional, composición e inmutabilidad](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md) — [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md), Paradigmas de programación.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python Language Reference](https://docs.python.org/3/reference/) — Semántica de sentencias, funciones, clases, generadores y corrutinas; autoridad: Python Software Foundation.
- [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) — Ownership, enums, traits, errores y concurrencia sin carreras de datos; autoridad: Rust project.
- [SWI-Prolog Reference Manual](https://www.swi-prolog.org/pldoc/man?section=intro) — Hechos, reglas, unificación, búsqueda y límites operacionales; autoridad: SWI-Prolog project.
- [ReactiveX Observable Contract](https://reactivex.io/documentation/contract.html) — Notificaciones, terminación, errores y control de flujo observable; autoridad: ReactiveX project.
- [Erlang System Documentation: Processes](https://www.erlang.org/doc/system/ref_man_processes.html) — Procesos, buzones, envío de mensajes, enlaces y monitores; autoridad: Erlang/OTP project.

---

[↑ Glosario](../../README.md) · [← Composición y nivel de abstracción](./composicion-y-nivel-de-abstraccion.md) · [Composite →](./composite.md)
