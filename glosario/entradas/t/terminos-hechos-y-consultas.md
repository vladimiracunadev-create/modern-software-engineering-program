# Términos, hechos y consultas

[↑ Glosario](../../README.md) · [← Terminal](./terminal.md) · [Texto alternativo →](./texto-alternativo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

Un programa lógico describe relaciones mediante términos.

Definición de trabajo de [SE-078 — Programación lógica y resolución](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md).

## Por qué importa

En [SE-078 — Programación lógica y resolución](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md), el tema «Términos, hechos y consultas» importa porque un programa lógico describe relaciones mediante términos.

## Cómo funciona

Según [SE-078 — Programación lógica y resolución](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md), en la sección «Términos, hechos y consultas»:

Un programa lógico describe relaciones mediante términos. Una consulta pregunta qué sustituciones vuelven verdadera una relación. La dirección no siempre está fijada como en una función, aunque la implementación y los modos de uso sí afectan terminación y rendimiento.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-078 — Programación lógica y resolución](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md):

En el motor de reglas comparado, una recomendación contiene acción, evidencia usada, versión de política y explicación. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si devuelve una cadena: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-078 — Programación lógica y resolución](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md)) son:

- **La consulta no termina** — causa: recursión por la izquierda sobre datos con ciclos. Corrección: memorizar subobjetivos (tabling) o llevar un conjunto de visitados.
- **La respuesta es correcta pero tarda mucho** — causa: metas poco restrictivas primero. Corrección: ordenar de más a menos restrictiva.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-078 — Programación lógica y resolución](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md)) son: Las definiciones son operativas para el motor de reglas comparado. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. La resolución lógica depende de supuestos operacionales y no gestiona por sí sola una secuencia temporal de eventos. La siguiente clase convierte entradas externas en eventos con contrato y ciclo de vida.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Relación](../r/relacion.md), [Negación y mundo cerrado](../n/negacion-y-mundo-cerrado.md), [Resolución y backtracking](../r/resolucion-y-backtracking.md), [Restricciones y explicación](../r/restricciones-y-explicacion.md), [Unificación](../u/unificacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-078 — Programación lógica y resolución](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md) — [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md), Paradigmas de programación.

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

[↑ Glosario](../../README.md) · [← Terminal](./terminal.md) · [Texto alternativo →](./texto-alternativo.md)
