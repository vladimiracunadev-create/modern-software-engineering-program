# Actor, buzón y propiedad del estado

[↑ Glosario](../../README.md) · [← Actor](./actor.md) · [Actores y cadena de decisión →](./actores-y-cadena-de-decision.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

Cada actor posee estado privado y procesa mensajes de su buzón.

Definición de trabajo de [SE-081 — Programación concurrente y actores](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md).

## Por qué importa

En [SE-081 — Programación concurrente y actores](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md), el tema «Actor, buzón y propiedad del estado» importa porque cada actor posee estado privado y procesa mensajes de su buzón.

## Cómo funciona

Según [SE-081 — Programación concurrente y actores](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md), en la sección «Actor, buzón y propiedad del estado»:

Cada actor posee estado privado y procesa mensajes de su buzón. Otros actores no lo mutan directamente. Esto reduce memoria compartida, pero el orden suele garantizarse solo bajo condiciones específicas de emisor y receptor, no como orden global.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-081 — Programación concurrente y actores](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md):

En el motor de reglas comparado, una recomendación contiene acción, evidencia usada, versión de política y explicación. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si devuelve una cadena: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-081 — Programación concurrente y actores](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md)) son:

- **Totales distintos entre ejecuciones** — causa: leer-modificar-escribir sin exclusión mutua. Corrección: cerrojo, cola con dueño único u operación atómica.
- **Cuatro hilos no aceleran un cálculo** — causa: bloqueo global del intérprete. Corrección: usar procesos o liberar el GIL en código nativo.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-081 — Programación concurrente y actores](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md)) son: Las definiciones son operativas para el motor de reglas comparado. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Actores desplazan problemas hacia protocolos, supervisión y entrega; no vuelven distribuido ni resiliente cualquier programa. La siguiente clase construye un criterio para combinar modelos sin collage arquitectónico.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Actor](./actor.md), [Estado](../e/estado.md), [Concurrencia, paralelismo e intercalación](../c/concurrencia-paralelismo-e-intercalacion.md), [Consistencia y presión del buzón](../c/consistencia-y-presion-del-buzon.md), [Fallo, enlaces y supervisión](../f/fallo-enlaces-y-supervision.md), [Protocolos de mensajes](../p/protocolos-de-mensajes.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-081 — Programación concurrente y actores](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md) — [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md), Paradigmas de programación.

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

[↑ Glosario](../../README.md) · [← Actor](./actor.md) · [Actores y cadena de decisión →](./actores-y-cadena-de-decision.md)
