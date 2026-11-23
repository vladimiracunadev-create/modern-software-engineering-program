# Evento, productor y manejador

[↑ Glosario](../../README.md) · [← Evento tope](./evento-tope.md) · [Evidencia →](./evidencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

Un evento afirma que ocurrió algo relevante; contiene identidad, tipo, instante observado y datos mínimos.

Definición de trabajo de [SE-079 — Programación orientada a eventos](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md).

## Por qué importa

En [SE-079 — Programación orientada a eventos](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md), el tema «Evento, productor y manejador» importa porque un evento afirma que ocurrió algo relevante; contiene identidad, tipo, instante observado y datos mínimos.

## Cómo funciona

Según [SE-079 — Programación orientada a eventos](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md), en la sección «Evento, productor y manejador»:

Un evento afirma que ocurrió algo relevante; contiene identidad, tipo, instante observado y datos mínimos. El productor no debería asumir qué consumidores existen. Un manejador transforma el evento o solicita un efecto, y debe declarar si puede repetirse.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-079 — Programación orientada a eventos](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md):

En el motor de reglas comparado, una recomendación contiene acción, evidencia usada, versión de política y explicación. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si devuelve una cadena: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-079 — Programación orientada a eventos](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md)) son:

- **Un temporizador se retrasa cientos de milisegundos** — causa: un manejador bloquea el hilo del bucle. Corrección: usar `await` o delegar el trabajo a un ejecutor.
- **Un manejador no se ejecuta tras el fallo de otro** — causa: despacho síncrono que propaga la primera excepción. Corrección: aislar y registrar el error por manejador.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-079 — Programación orientada a eventos](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md)) son: Las definiciones son operativas para el motor de reglas comparado. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. La orientación a eventos organiza reacciones discretas, pero no compone necesariamente flujos largos, presión ni transformación continua. La siguiente clase modela secuencias observables.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Evento](./evento.md), [Instante](../i/instante.md), [Tipo](../t/tipo.md), [Bucle de eventos y cola](../b/bucle-de-eventos-y-cola.md), [Callbacks, promesas y corrutinas](../c/callbacks-promesas-y-corrutinas.md), [Cancelación y ciclo de vida](../c/cancelacion-y-ciclo-de-vida.md).
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

[↑ Glosario](../../README.md) · [← Evento tope](./evento-tope.md) · [Evidencia →](./evidencia.md)
