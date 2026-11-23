# Flujo automatizado

[↑ Glosario](../../README.md) · [← Flujo asistido](./flujo-asistido.md) · [Flujo de datos y dependencias →](./flujo-de-datos-y-dependencias.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Trabajo en que un agente ejecuta la tarea en bucle y la persona prepara el encargo y revisa el resultado.

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

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El flujo automatizado «gana» y aparecen defectos en producción** — causa: los pasos intermedios no se revisaron. Corrección: revisión humana del resultado y periodo de observación. ([SE-563](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: una simulación de tres flujos con bootstrap, un cálculo exacto del punto de equilibrio y una simulación de potencia para dos diseños.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Agente](../a/agente.md), [Encargo](../e/encargo.md), [Resultado](../r/resultado.md), [Tarea](../t/tarea.md), [Bootstrap](../b/bootstrap.md), [Diseño pareado](../d/diseno-pareado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

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

[↑ Glosario](../../README.md) · [← Flujo asistido](./flujo-asistido.md) · [Flujo de datos y dependencias →](./flujo-de-datos-y-dependencias.md)
