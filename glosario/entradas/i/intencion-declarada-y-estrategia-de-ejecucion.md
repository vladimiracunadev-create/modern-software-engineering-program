# Intención declarada y estrategia de ejecución

[↑ Glosario](../../README.md) · [← Intención](./intencion.md) · [Intención perdida →](./intencion-perdida.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

Una descripción declarativa especifica qué relación debe cumplirse y delega parte del cómo a un motor.

Definición de trabajo de [SE-077 — Programación declarativa y basada en reglas](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md).

## Por qué importa

En [SE-077 — Programación declarativa y basada en reglas](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md), el tema «Intención declarada y estrategia de ejecución» importa porque una descripción declarativa especifica qué relación debe cumplirse y delega parte del cómo a un motor.

## Cómo funciona

Según [SE-077 — Programación declarativa y basada en reglas](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md), en la sección «Intención declarada y estrategia de ejecución»:

Una descripción declarativa especifica qué relación debe cumplirse y delega parte del cómo a un motor. SQL, CSS y sistemas de reglas no son equivalentes, pero comparten esa separación. El costo y el orden no desaparecen: quedan en el planificador, la especificidad o la estrategia de resolución.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-077 — Programación declarativa y basada en reglas](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md):

En el motor de reglas comparado, una recomendación contiene acción, evidencia usada, versión de política y explicación. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si devuelve una cadena: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-077 — Programación declarativa y basada en reglas](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md)) son:

- **Cambia una decisión al reordenar reglas** — causa: política de conflicto de «primera coincidencia» no documentada. Corrección: declarar la política y probar las observaciones en conflicto.
- **La consulta empeora al crear un índice** — causa: predicado poco selectivo. Corrección: revisar `EXPLAIN QUERY PLAN` y medir antes de conservarlo.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-077 — Programación declarativa y basada en reglas](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md)) son: Las definiciones son operativas para el motor de reglas comparado. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Una tabla de reglas no prueba consistencia ni completitud. La siguiente clase usa unificación y búsqueda para estudiar resolución lógica y sus costos.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Motor](../m/motor.md), [Relación](../r/relacion.md), [Evaluación incremental y explicación](../e/evaluacion-incremental-y-explicacion.md), [Hechos, reglas y condiciones](../h/hechos-reglas-y-condiciones.md), [Límites de lenguajes declarativos](../l/limites-de-lenguajes-declarativos.md), [Prioridad y conflictos](../p/prioridad-y-conflictos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-077 — Programación declarativa y basada en reglas](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md) — [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md), Paradigmas de programación.

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

[↑ Glosario](../../README.md) · [← Intención](./intencion.md) · [Intención perdida →](./intencion-perdida.md)
