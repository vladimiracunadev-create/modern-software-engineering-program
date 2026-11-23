# Modelo de nivel de teclado

[↑ Glosario](../../README.md) · [← Modelo de ingreso](./modelo-de-ingreso.md) · [Modelo ejecutable de arquitectura →](./modelo-ejecutable-de-arquitectura.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Método que estima el tiempo de una tarea de una persona experta sumando operadores elementales.

Definición de trabajo de [SE-169 — Diseño centrado en personas y tareas](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md).

## Por qué importa

La clase donde se define, [SE-169 — Diseño centrado en personas y tareas](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md), existe con este propósito: la clase existe para que partas de lo que una persona intenta lograr, en qué condiciones y con qué margen de error, y no de la pantalla que alguien ya dibujó; así el diseño se discute con cálculos y observaciones y no con gustos.

## Cómo funciona

Según [SE-169 — Diseño centrado en personas y tareas](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md):

La entrega se descompuso en operadores del modelo de nivel de teclado: por cada campo, una pausa mental, apuntar, hacer clic, pasar la mano al teclado y doce teclas. El diseño A tiene nueve campos (147 operadores, 50,7 s); el B, tres campos con ratón (51 operadores, 18,6 s); el C, tres campos solo con teclado y Tab (44 operadores, 13,4 s). Si en el B tres campos generan una duda de qué escribir, se suman tres pausas mentales y el tiempo sube a 22,7 s. Quitar seis campos ahorra 32 s; evitar tres dudas, 4 s.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-169 — Diseño centrado en personas y tareas](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md):

En la plataforma, el equipo documenta la tarea «entregar una tarea y obtener constancia» con tres escenarios: estudiante con teclado y lector de pantalla, estudiante con teléfono y conexión lenta, y docente que corrige desde un portátil. Cada diseño candidato se descompone en operadores y se estima; el embudo se mide en un piloto con datos anónimos agregados y se compara con el supuesto. La decisión final se acompaña de la etapa que más pierde y de la señal que haría cambiarla.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-169 — Diseño centrado en personas y tareas](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md)) son:

- **«Es largo» sin ninguna cifra** — causa: no se descompuso la tarea en pasos. Corrección: estimar con operadores y comparar diseños.
- **Un diseño para la persona promedio falla a casi todos** — causa: se consideró una dimensión a la vez. Corrección: definir escenarios que cubran extremos relevantes y permitir ajustes.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La entrega se descompuso en operadores del modelo de nivel de teclado: por cada campo, una pausa mental, apuntar, hacer clic, pasar la mano al teclado y doce teclas. ([SE-169](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Tarea](../t/tarea.md), [Embudo](../e/embudo.md), [Escenario de uso](../e/escenario-de-uso.md), [Persona de diseño](../p/persona-de-diseno.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-169 — Diseño centrado en personas y tareas](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Gould y Lewis, «Designing for usability» (CACM, 1985)](https://doi.org/10.1145/3166.3170) — principios de diseño centrado en usuarios y tareas; autoridad: Communications of the ACM.
- [Card, Moran y Newell, «The keystroke-level model for user performance time with interactive systems» (CACM, 1980)](https://doi.org/10.1145/358886.358895) — modelo de operadores; autoridad: Communications of the ACM.
- [W3C WAI: principios de accesibilidad](https://www.w3.org/WAI/fundamentals/accessibility-principles/) — diversidad de capacidades y contextos; autoridad: W3C.
- [Nielsen Norman Group: 10 heurísticas de usabilidad](https://www.nngroup.com/articles/ten-usability-heuristics/) — criterios de revisión de interfaces; autoridad: Nielsen Norman Group.
- [Usability.gov: personas](https://www.usability.gov/how-to-and-tools/methods/personas.html) — qué son y cómo se usan las personas de diseño; autoridad: gobierno de EE. UU.

---

[↑ Glosario](../../README.md) · [← Modelo de ingreso](./modelo-de-ingreso.md) · [Modelo ejecutable de arquitectura →](./modelo-ejecutable-de-arquitectura.md)
