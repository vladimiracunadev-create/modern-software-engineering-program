# Flujo manual

[↑ Glosario](../../README.md) · [← Flujo huérfano](./flujo-huerfano.md) · [Flujo vertical →](./flujo-vertical.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Trabajo sin asistencia generativa.

Definición de trabajo de [SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md).

## Por qué importa

La clase donde se define, [SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md), existe con este propósito: el taller existe para que dejes de discutir si «la IA nos hace más rápidos» y aprendas a construir la respuesta con tus propias tareas: tres flujos de trabajo (manual, asistido por un humano que conduce y automatizado con un agente que ejecuta), un protocolo que registre tiempo, defectos y esfuerzo de revisión, un diseño que no confunda la dificultad de las tareas con el efecto de la herramienta y un informe que declare su incertidumbre.

## Cómo funciona

Según [SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md):

Un flujo **manual** produce el cambio sin asistencia generativa: el tiempo es el de escribir, probar y revisar. El flujo **asistido** mantiene a la persona al volante: el asistente sugiere, edita y explica, y la persona decide qué aceptar. Su tiempo se compone de generar, revisar lo generado y rehacer cuando falla. El flujo **automatizado** delega la ejecución de la tarea a un agente que lee, edita y ejecuta pruebas en bucle; la persona prepara el encargo y revisa el resultado. Su tiempo se reparte entre preparar, revisar el resultado final y rehacer, y su riesgo es que los pasos intermedios no pasan por ojos humanos (`SE-556`).

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones diseña el estudio. Selecciona 24 tareas de mantenimiento del último trimestre, estratificadas por tamaño y tipo, cada una con una prueba ejecutable y un periodo de observación de defectos de cuatro semanas.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md)) son:

- **«Ahorra el 50 %» a partir de cinco tareas** — causa: muestra pequeña y tareas no comparables. Corrección: diseño pareado y tamaño calculado.
- **Se informa solo de tiempo** — causa: no se midieron defectos ni revisión. Corrección: registro con horas activas, revisión y defectos.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un flujo **manual** produce el cambio sin asistencia generativa: el tiempo es el de escribir, probar y revisar. ([SE-563](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Trabajo](../t/trabajo.md), [Bootstrap](../b/bootstrap.md), [Diseño pareado](../d/diseno-pareado.md), [Flujo asistido](./flujo-asistido.md), [Flujo automatizado](./flujo-automatizado.md), [Métrica](../m/metrica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-564](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md), [SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Peng et al., «The Impact of AI on Developer Productivity»](https://arxiv.org/abs/2302.06590) — experimento controlado con una tarea acotada; autoridad: preprint de GitHub y Microsoft.
- [METR, «Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity»](https://arxiv.org/abs/2507.09089) — ensayo aleatorizado con desarrolladores expertos; autoridad: METR.
- [Sjøberg et al.](https://doi.org/10.1109/TSE.2005.97) — experimentos controlados en ingeniería de software; autoridad: IEEE Transactions on Software Engineering.
- [Wohlin et al., «Experimentation in Software Engineering»](https://doi.org/10.1007/978-3-642-29044-2) — diseño y análisis de experimentos; autoridad: Springer.
- [Efron (1979)](https://doi.org/10.1214/aos/1176344552) — el bootstrap; autoridad: The Annals of Statistics.

---

[↑ Glosario](../../README.md) · [← Flujo huérfano](./flujo-huerfano.md) · [Flujo vertical →](./flujo-vertical.md)
