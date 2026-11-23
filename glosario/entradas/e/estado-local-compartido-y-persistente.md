# Estado local, compartido y persistente

[↑ Glosario](../../README.md) · [← Estado limpio](./estado-limpio.md) · [Estado seguro →](./estado-seguro.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

El estado local desaparece al terminar la activación; el compartido puede ser observado por varios componentes; el persistente sobrevive al proceso.

Definición de trabajo de [SE-073 — Programación imperativa y estado mutable](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md).

## Por qué importa

En [SE-073 — Programación imperativa y estado mutable](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md), el tema «Estado local, compartido y persistente» importa porque el estado local desaparece al terminar la activación; el compartido puede ser observado por varios componentes; el persistente sobrevive al proceso.

## Cómo funciona

Según [SE-073 — Programación imperativa y estado mutable](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md), en la sección «Estado local, compartido y persistente»:

El estado local desaparece al terminar la activación; el compartido puede ser observado por varios componentes; el persistente sobrevive al proceso. Tratarlos como equivalentes oculta concurrencia, fallos parciales y recuperación. El motor de reglas comparado empieza con estado local y documenta explícitamente cuándo una frontera obliga a otro modelo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-073 — Programación imperativa y estado mutable](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md):

En el motor de reglas comparado, una recomendación contiene acción, evidencia usada, versión de política y explicación. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si devuelve una cadena: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-073 — Programación imperativa y estado mutable](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md)) son:

- **La copia «aislada» cambia cuando se modifica la original** — causa: copia superficial con listas o diccionarios internos. Corrección: copiar en profundidad solo lo mutable o usar estructuras inmutables.
- **Un rechazo deja el puntaje distinto del inicial** — causa: mutación antes de decidir el resultado. Corrección: calcular sobre una copia y confirmar al final.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-073 — Programación imperativa y estado mutable](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md)) son: Las definiciones son operativas para el motor de reglas comparado. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. La ejecución secuencial no explica por sí sola concurrencia, persistencia ni consistencia distribuida. La siguiente clase reduce superficie mutable mediante procedimientos con contratos estrechos.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Activación](../a/activacion.md), [Componente](../c/componente.md), [Estado](./estado.md), [Proceso](../p/proceso.md), [Asignación, aliasing y mutación](../a/asignacion-aliasing-y-mutacion.md), [Comandos, expresiones y secuencia](../c/comandos-expresiones-y-secuencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-073 — Programación imperativa y estado mutable](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md) — [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md), Paradigmas de programación.

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

[↑ Glosario](../../README.md) · [← Estado limpio](./estado-limpio.md) · [Estado seguro →](./estado-seguro.md)
