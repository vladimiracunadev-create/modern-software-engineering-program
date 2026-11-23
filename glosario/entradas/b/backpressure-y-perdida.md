# Backpressure y pérdida

[↑ Glosario](../../README.md) · [← Backpressure](./backpressure.md) · [Backtracking →](./backtracking.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

Si el productor supera al consumidor hay que bloquear, almacenar, agrupar, muestrear o descartar con política.

Definición de trabajo de [SE-080 — Programación reactiva y flujos](../../../classes/part-06-paradigmas-de-programacion/se-080-programacion-reactiva-y-flujos/README.md).

## Por qué importa

En [SE-080 — Programación reactiva y flujos](../../../classes/part-06-paradigmas-de-programacion/se-080-programacion-reactiva-y-flujos/README.md), el tema «Backpressure y pérdida» importa porque si el productor supera al consumidor hay que bloquear, almacenar, agrupar, muestrear o descartar con política.

## Cómo funciona

Según [SE-080 — Programación reactiva y flujos](../../../classes/part-06-paradigmas-de-programacion/se-080-programacion-reactiva-y-flujos/README.md), en la sección «Backpressure y pérdida»:

Si el productor supera al consumidor hay que bloquear, almacenar, agrupar, muestrear o descartar con política. Una cola infinita solo pospone el fallo a memoria. El motor de reglas comparado registra volumen perdido y explica por qué la política sigue siendo válida para diagnóstico.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-080 — Programación reactiva y flujos](../../../classes/part-06-paradigmas-de-programacion/se-080-programacion-reactiva-y-flujos/README.md):

En el motor de reglas comparado, una recomendación contiene acción, evidencia usada, versión de política y explicación. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si devuelve una cadena: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-080 — Programación reactiva y flujos](../../../classes/part-06-paradigmas-de-programacion/se-080-programacion-reactiva-y-flujos/README.md)) son:

- **La memoria crece con el tiempo en un pipeline** — causa: cola ilimitada con productor más rápido. Corrección: fijar un límite y decidir entre frenar, descartar o rechazar.
- **El segundo recorrido de un generador sale vacío** — causa: el generador se agotó. Corrección: volver a crearlo o materializarlo si hace falta repetir.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-080 — Programación reactiva y flujos](../../../classes/part-06-paradigmas-de-programacion/se-080-programacion-reactiva-y-flujos/README.md)) son: Las definiciones son operativas para el motor de reglas comparado. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Los operadores no eliminan límites de recursos ni garantizan entrega distribuida. La siguiente clase compara memoria compartida con actores y mensajes.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Errores, reintentos y cancelación](../e/errores-reintentos-y-cancelacion.md), [Flujos calientes y fríos](../f/flujos-calientes-y-frios.md), [Observable y contrato de notificaciones](../o/observable-y-contrato-de-notificaciones.md), [Operadores como álgebra de flujos](../o/operadores-como-algebra-de-flujos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-080 — Programación reactiva y flujos](../../../classes/part-06-paradigmas-de-programacion/se-080-programacion-reactiva-y-flujos/README.md) — [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md), Paradigmas de programación.

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

[↑ Glosario](../../README.md) · [← Backpressure](./backpressure.md) · [Backtracking →](./backtracking.md)
