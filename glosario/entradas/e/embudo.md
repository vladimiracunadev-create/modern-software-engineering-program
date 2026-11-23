# Embudo

[↑ Glosario](../../README.md) · [← Embedding](./embedding.md) · [Empaquetado →](./empaquetado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Serie de etapas cuya tasa de paso se multiplica para dar la tasa de completar la tarea.

Definición de trabajo de [SE-169 — Diseño centrado en personas y tareas](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md).

## Por qué importa

La clase donde se define, [SE-169 — Diseño centrado en personas y tareas](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md), existe con este propósito: la clase existe para que partas de lo que una persona intenta lograr, en qué condiciones y con qué margen de error, y no de la pantalla que alguien ya dibujó; así el diseño se discute con cálculos y observaciones y no con gustos.

## Cómo funciona

Según [SE-169 — Diseño centrado en personas y tareas](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md):

Un embudo de seis etapas con tasas de paso supuestas (0,97, 0,95, 0,90, 0,62, 0,93, 0,96) completa el 45,9 %. De 1 000 personas que empiezan se pierden 30, 49, 92, 315, 36 y 19 por etapa; completan 478 en el cálculo y 437 en una simulación de 1 000 personas con semilla fija. Mejorar cada etapa 2 puntos sube la tasa a 0,526 (+0,067); mejorar solo la cuarta 10 puntos, a 0,533 (+0,074); mejorar la primera 2 puntos, a 0,468 (+0,0095). La etapa 4 es subir el archivo, y la forma de la pérdida orienta qué observar: ¿falla, confunde o tarda?

Según [SE-169 — Diseño centrado en personas y tareas](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md):

En la plataforma, el equipo documenta la tarea «entregar una tarea y obtener constancia» con tres escenarios: estudiante con teclado y lector de pantalla, estudiante con teléfono y conexión lenta, y docente que corrige desde un portátil. Cada diseño candidato se descompone en operadores y se estima; el embudo se mide en un piloto con datos anónimos agregados y se compara con el supuesto. La decisión final se acompaña de la etapa que más pierde y de la señal que haría cambiarla.

## Ejemplo

Ejemplo de [SE-169 — Diseño centrado en personas y tareas](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md) (sección «Ejemplo profesional»):

En la plataforma, el equipo documenta la tarea «entregar una tarea y obtener constancia» con tres escenarios: estudiante con teclado y lector de pantalla, estudiante con teléfono y conexión lenta, y docente que corrige desde un portátil. Cada diseño candidato se descompone en operadores y se estima; el embudo se mide en un piloto con datos anónimos agregados y se compara con el supuesto. La decisión final se acompaña de la etapa que más pierde y de la señal que haría cambiarla.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-169 — Diseño centrado en personas y tareas](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md)) son:

- **«Es largo» sin ninguna cifra** — causa: no se descompuso la tarea en pasos. Corrección: estimar con operadores y comparar diseños.
- **Un diseño para la persona promedio falla a casi todos** — causa: se consideró una dimensión a la vez. Corrección: definir escenarios que cubran extremos relevantes y permitir ajustes.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un embudo de supuestos sirve para decidir qué medir, no para informar un resultado. ([SE-169](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Tarea](../t/tarea.md), [Escenario de uso](./escenario-de-uso.md), [Modelo de nivel de teclado](../m/modelo-de-nivel-de-teclado.md), [Persona de diseño](../p/persona-de-diseno.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-169 — Diseño centrado en personas y tareas](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md), [SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md), [SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md), [SE-008](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md), [SE-219](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md), [SE-289](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md), [SE-579](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md), [SE-586](../../../classes/part-48-harness-y-agentic-engineering/se-586-ai-dlc-gobierno-y-vibe-coding-frente-a-agentic-engineering/README.md).

**Aparece en los casos de estudio:** [Spotify](../../../casos/exito/spotify.md), [Quibi](../../../casos/fallo/quibi.md).

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

[↑ Glosario](../../README.md) · [← Embedding](./embedding.md) · [Empaquetado →](./empaquetado.md)
