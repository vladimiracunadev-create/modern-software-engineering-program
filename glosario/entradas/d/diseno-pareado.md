# Diseño pareado

[↑ Glosario](../../README.md) · [← Diseño desde consumidor](./diseno-desde-consumidor.md) · [Diseño responsive →](./diseno-responsive.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Diseño en que cada tarea se resuelve con todos los flujos, de modo que se compara cada tarea consigo misma.

Definición de trabajo de [SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md).

## Por qué importa

En [SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md), el tema «Diseño pareado» importa porque elimina la variación entre tareas

## Cómo funciona

Según [SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md):

La dificultad de las tareas varía más que el efecto de cualquier flujo: una tarea puede tardar diez minutos y otra diez horas. Si cada flujo se mide con tareas diferentes, esa variación domina y el efecto queda enterrado. El diseño **pareado** hace que cada tarea se resuelva con los tres flujos, de modo que se compara cada tarea consigo misma y la dificultad se cancela. Introduce un problema: la segunda vez que alguien resuelve una tarea la conoce, y aprende. La solución estándar es **alternar el orden** (la mitad de las personas empieza por un flujo y la otra mitad por otro) o usar personas distintas para cada flujo en la misma tarea, y declarar el efecto de aprendizaje que no se pudo eliminar.

Según [SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md):

Traslada el análisis a otro dominio (por ejemplo, el desarrollo de plantillas de informes para un taller mecánico): cambia las tareas, los flujos y el costo de un defecto y conserva el procedimiento de diseño pareado, registro de tiempo, defectos y revisión, intervalo bootstrap y punto de equilibrio. La transferencia está lograda cuando puedes decir qué tipo de tarea de ese dominio dejaría de ahorrar tiempo con un asistente y con qué tasa de aciertos, no cuando la tabla se parece a la del módulo de calificaciones.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones diseña el estudio. Selecciona 24 tareas de mantenimiento del último trimestre, estratificadas por tamaño y tipo, cada una con una prueba ejecutable y un periodo de observación de defectos de cuatro semanas.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **«Ahorra el 50 %» a partir de cinco tareas** — causa: muestra pequeña y tareas no comparables. Corrección: diseño pareado y tamaño calculado. ([SE-563](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: una simulación de tres flujos con bootstrap, un cálculo exacto del punto de equilibrio y una simulación de potencia para dos diseños.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Flujo](../f/flujo.md), [Tarea](../t/tarea.md), [Bootstrap](../b/bootstrap.md), [Flujo asistido](../f/flujo-asistido.md), [Flujo automatizado](../f/flujo-automatizado.md), [Flujo manual](../f/flujo-manual.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md), [SE-564](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-564-proyecto-cambio-real-con-trazabilidad-y-revision-humana/README.md).

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

[↑ Glosario](../../README.md) · [← Diseño desde consumidor](./diseno-desde-consumidor.md) · [Diseño responsive →](./diseno-responsive.md)
