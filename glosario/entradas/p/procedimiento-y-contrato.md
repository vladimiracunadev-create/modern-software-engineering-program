# Procedimiento y contrato

[↑ Glosario](../../README.md) · [← Procedencia](./procedencia.md) · [Procedimientos de verificación →](./procedimientos-de-verificacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

Un procedimiento agrupa una secuencia bajo un nombre y una interfaz.

Definición de trabajo de [SE-074 — Programación procedural y descomposición funcional](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md).

## Por qué importa

En [SE-074 — Programación procedural y descomposición funcional](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md), el tema «Procedimiento y contrato» importa porque un procedimiento agrupa una secuencia bajo un nombre y una interfaz.

## Cómo funciona

Según [SE-074 — Programación procedural y descomposición funcional](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md), en la sección «Procedimiento y contrato»:

Un procedimiento agrupa una secuencia bajo un nombre y una interfaz. Su valor no está en reducir líneas, sino en establecer qué recibe, qué devuelve, qué puede modificar y qué error comunica. Un procedimiento sin contrato solo desplaza la complejidad detrás de una llamada.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-074 — Programación procedural y descomposición funcional](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md):

En el motor de reglas comparado, una recomendación contiene acción, evidencia usada, versión de política y explicación. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si devuelve una cadena: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-074 — Programación procedural y descomposición funcional](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md)) son:

- **`RecursionError` en un recorrido largo** — causa: descomposición recursiva sobre una entrada lineal. Corrección: convertir a bucle con acumulador o pila explícita.
- **Un efecto «desaparece» tras añadir `lru_cache`** — causa: se memoizó una función con efectos. Corrección: memoizar solo la parte pura.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-074 — Programación procedural y descomposición funcional](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md)) son: Las definiciones son operativas para el motor de reglas comparado. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. La descomposición procedural no define por sí misma cómo representar entidades con identidad o ciclos de vida largos. La siguiente clase contrasta objetos y mensajes.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Interfaz](../i/interfaz.md), [Secuencia](../s/secuencia.md), [Composición y nivel de abstracción](../c/composicion-y-nivel-de-abstraccion.md), [Descomposición por responsabilidad](../d/descomposicion-por-responsabilidad.md), [Efectos en los bordes](../e/efectos-en-los-bordes.md), [Flujo de datos y dependencias](../f/flujo-de-datos-y-dependencias.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-074 — Programación procedural y descomposición funcional](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md) — [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md), Paradigmas de programación.

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

[↑ Glosario](../../README.md) · [← Procedencia](./procedencia.md) · [Procedimientos de verificación →](./procedimientos-de-verificacion.md)
