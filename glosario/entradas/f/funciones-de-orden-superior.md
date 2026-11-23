# Funciones de orden superior

[↑ Glosario](../../README.md) · [← Función pura](./funcion-pura.md) · [Funciones puras y transparencia referencial →](./funciones-puras-y-transparencia-referencial.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

Pasar una regla como valor permite parametrizar evaluación sin condicionales globales.

Definición de trabajo de [SE-076 — Programación funcional, composición e inmutabilidad](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md).

## Por qué importa

En [SE-076 — Programación funcional, composición e inmutabilidad](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md), el tema «Funciones de orden superior» importa porque pasar una regla como valor permite parametrizar evaluación sin condicionales globales.

## Cómo funciona

Según [SE-076 — Programación funcional, composición e inmutabilidad](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md), en la sección «Funciones de orden superior»:

Pasar una regla como valor permite parametrizar evaluación sin condicionales globales. `map`, `filter` y `reduce` expresan transformaciones, pero una cadena excesiva puede ocultar orden, errores o complejidad. La forma debe servir al modelo y no demostrar virtuosismo sintáctico.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-076 — Programación funcional, composición e inmutabilidad](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md):

En el motor de reglas comparado, una recomendación contiene acción, evidencia usada, versión de política y explicación. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si devuelve una cadena: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-076 — Programación funcional, composición e inmutabilidad](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md)) son:

- **Todas las funciones de una lista devuelven el último valor** — causa: cierre que captura la variable y no su valor. Corrección: capturar con argumento por defecto o `partial`.
- **Una «tupla inmutable» cambia** — causa: contiene un objeto mutable. Corrección: usar contenidos inmutables o copiar al construir.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-076 — Programación funcional, composición e inmutabilidad](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md)) son: Las definiciones son operativas para el motor de reglas comparado. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Pureza y composición no resuelven automáticamente interacción, latencia ni grandes flujos. La siguiente clase expresa el resultado deseado como reglas declarativas.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Evaluación](../e/evaluacion.md), [Regla](../r/regla.md), [Valor](../v/valor.md), [Composición y tipos de resultado](../c/composicion-y-tipos-de-resultado.md), [Funciones puras y transparencia referencial](./funciones-puras-y-transparencia-referencial.md), [Inmutabilidad y evolución de valores](../i/inmutabilidad-y-evolucion-de-valores.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-076 — Programación funcional, composición e inmutabilidad](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md) — [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md), Paradigmas de programación.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-305](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md).

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

[↑ Glosario](../../README.md) · [← Función pura](./funcion-pura.md) · [Funciones puras y transparencia referencial →](./funciones-puras-y-transparencia-referencial.md)
