# Mensajes y despacho

[↑ Glosario](../../README.md) · [← Mensaje venenoso](./mensaje-venenoso.md) · [Mentoría →](./mentoria.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md)

## Definición

Invocar un método envía una solicitud a un receptor que decide cómo responder según su tipo y estado.

Definición de trabajo de [SE-075 — Orientación a objetos, mensajes y encapsulación](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md).

## Por qué importa

En [SE-075 — Orientación a objetos, mensajes y encapsulación](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md), el tema «Mensajes y despacho» importa porque invocar un método envía una solicitud a un receptor que decide cómo responder según su tipo y estado.

## Cómo funciona

Según [SE-075 — Orientación a objetos, mensajes y encapsulación](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md), en la sección «Mensajes y despacho»:

Invocar un método envía una solicitud a un receptor que decide cómo responder según su tipo y estado. El despacho polimórfico permite sustituir comportamientos detrás de un contrato. No elimina condicionales: los distribuye, y puede volver difícil seguir el flujo si las jerarquías son opacas.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-075 — Orientación a objetos, mensajes y encapsulación](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md):

En el motor de reglas comparado, una recomendación contiene acción, evidencia usada, versión de política y explicación. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si devuelve una cadena: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-075 — Orientación a objetos, mensajes y encapsulación](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md)) son:

- **Un método de la base se ejecuta dos veces o nunca** — causa: `A.m(self)` en lugar de `super().m()` en herencia múltiple. Corrección: usar `super()` en todas las clases del diamante.
- **Se asigna un valor inválido a un atributo «privado»** — causa: la privacidad era un guion bajo. Corrección: validar en el método que escribe o usar una propiedad con setter.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-075 — Orientación a objetos, mensajes y encapsulación](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md)) son: Las definiciones son operativas para el motor de reglas comparado. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Los objetos reducen estados inválidos solo si sus fronteras son reales. La siguiente clase elimina identidad innecesaria y razona mediante valores y composición funcional.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Estado](../e/estado.md), [Tipo](../t/tipo.md), [Composición frente a herencia](../c/composicion-frente-a-herencia.md), [Encapsulación como protección](../e/encapsulacion-como-proteccion.md), [Objetos de valor y entidades](../o/objetos-de-valor-y-entidades.md), [Objeto, identidad y estado válido](../o/objeto-identidad-y-estado-valido.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-075 — Orientación a objetos, mensajes y encapsulación](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md) — [Parte 06](../../../classes/part-06-paradigmas-de-programacion/README.md), Paradigmas de programación.

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

[↑ Glosario](../../README.md) · [← Mensaje venenoso](./mensaje-venenoso.md) · [Mentoría →](./mentoria.md)
