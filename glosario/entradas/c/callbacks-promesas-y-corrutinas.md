# Callbacks, promesas y corrutinas

[↑ Glosario](../../README.md) · [← Calificador](./calificador.md) · [Cambio compatible →](./cambio-compatible.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

Son formas distintas de expresar continuación.

Definición de trabajo de [SE-079 — Programación orientada a eventos](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md).

## Por qué importa

En [SE-079 — Programación orientada a eventos](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md), el tema «Callbacks, promesas y corrutinas» importa porque son formas distintas de expresar continuación.

## Cómo funciona

Según [SE-079 — Programación orientada a eventos](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md), en la sección «Callbacks, promesas y corrutinas»:

Son formas distintas de expresar continuación. `async/await` mejora lectura secuencial, pero no vuelve síncrono el sistema ni elimina cancelación. Una corrutina que no cede o una promesa ignorada puede bloquear o perder fallos tanto como un callback mal diseñado.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-079 — Programación orientada a eventos](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md):

En el motor de reglas comparado, una recomendación contiene acción, evidencia usada, versión de política y explicación. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si devuelve una cadena: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-079 — Programación orientada a eventos](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md)) son:

- **Un temporizador se retrasa cientos de milisegundos** — causa: un manejador bloquea el hilo del bucle. Corrección: usar `await` o delegar el trabajo a un ejecutor.
- **Un manejador no se ejecuta tras el fallo de otro** — causa: despacho síncrono que propaga la primera excepción. Corrección: aislar y registrar el error por manejador.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-079 — Programación orientada a eventos](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md)) son: Las definiciones son operativas para el motor de reglas comparado. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. La orientación a eventos organiza reacciones discretas, pero no compone necesariamente flujos largos, presión ni transformación continua. La siguiente clase modela secuencias observables.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Bucle de eventos y cola](../b/bucle-de-eventos-y-cola.md), [Cancelación y ciclo de vida](./cancelacion-y-ciclo-de-vida.md), [Evento, productor y manejador](../e/evento-productor-y-manejador.md), [Orden, duplicados e idempotencia](../o/orden-duplicados-e-idempotencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-079 — Programación orientada a eventos](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md) — [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md), Paradigmas de programación.

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

[↑ Glosario](../../README.md) · [← Calificador](./calificador.md) · [Cambio compatible →](./cambio-compatible.md)
