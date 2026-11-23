# Bootstrap

[↑ Glosario](../../README.md) · [← Bomba de descompresión](./bomba-de-descompresion.md) · [Borde →](./borde.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Método que estima la variabilidad de un estadístico remuestreando los datos con reemplazo.

Definición de trabajo de [SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md).

## Por qué importa

La clase donde se define, [SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md), existe con este propósito: el taller existe para que dejes de discutir si «la IA nos hace más rápidos» y aprendas a construir la respuesta con tus propias tareas: tres flujos de trabajo (manual, asistido por un humano que conduce y automatizado con un agente que ejecuta), un protocolo que registre tiempo, defectos y esfuerzo de revisión, un diseño que no confunda la dificultad de las tareas con el efecto de la herramienta y un informe que declare su incertidumbre.

## Cómo funciona

Según [SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md):

Se generan 200 tareas con horas manuales lognormales (parámetros 0,9 y 0,5) y un 30 % de tareas difíciles. El flujo manual tarda lo que dice la tarea y deja escapar defectos con probabilidad 0,06. El asistido tiene una tasa de aciertos de 0,85 en tareas fáciles y 0,55 en difíciles; tarda 0,35 (generar) + 0,25 (revisar) del tiempo manual más 0,80 si hay que rehacer, y deja escapar defectos con probabilidad 0,05 si acierta y 0,12 si no. El automatizado acierta 0,75 y 0,40, tarda 0,10 + 0,30 más 1,00 si falla, y deja escapar 0,09 si acierta y 0,25 si no. Se calcula la mediana de horas con un intervalo bootstrap de 1 000 remuestreos.

Según [SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones diseña el estudio. Selecciona 24 tareas de mantenimiento del último trimestre, estratificadas por tamaño y tipo, cada una con una prueba ejecutable y un periodo de observación de defectos de cuatro semanas. Seis personas resuelven cada tarea una vez con un flujo asignado por un cuadrado latino (cada persona usa cada flujo en tareas distintas, y cada tarea se resuelve por flujos distintos en rondas alternadas), registran horas activas, horas de revisión por otra persona, resultado de las pruebas y defectos posteriores, y declaran los casos en que ya conocían la tarea.

## Ejemplo

Ejemplo de [SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones diseña el estudio. Selecciona 24 tareas de mantenimiento del último trimestre, estratificadas por tamaño y tipo, cada una con una prueba ejecutable y un periodo de observación de defectos de cuatro semanas. Seis personas resuelven cada tarea una vez con un flujo asignado por un cuadrado latino (cada persona usa cada flujo en tareas distintas, y cada tarea se resuelve por flujos distintos en rondas alternadas), registran horas activas, horas de revisión por otra persona, resultado de las pruebas y defectos posteriores, y declaran los casos en que ya conocían la tarea.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md)) son:

- **«Ahorra el 50 %» a partir de cinco tareas** — causa: muestra pequeña y tareas no comparables. Corrección: diseño pareado y tamaño calculado.
- **Se informa solo de tiempo** — causa: no se midieron defectos ni revisión. Corrección: registro con horas activas, revisión y defectos.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: una simulación de tres flujos con bootstrap, un cálculo exacto del punto de equilibrio y una simulación de potencia para dos diseños.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Reemplazo](../r/reemplazo.md), [Variabilidad](../v/variabilidad.md), [Diseño pareado](../d/diseno-pareado.md), [Flujo asistido](../f/flujo-asistido.md), [Flujo automatizado](../f/flujo-automatizado.md), [Flujo manual](../f/flujo-manual.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-108](../../../classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md), [SE-604](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), [SE-185](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md), [SE-189](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md), [SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md), [SE-192](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md), [SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Efron (1979)](https://doi.org/10.1214/aos/1176344552) — el bootstrap; autoridad: The Annals of Statistics.
- [Peng et al., «The Impact of AI on Developer Productivity»](https://arxiv.org/abs/2302.06590) — experimento controlado con una tarea acotada; autoridad: preprint de GitHub y Microsoft.
- [METR, «Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity»](https://arxiv.org/abs/2507.09089) — ensayo aleatorizado con desarrolladores expertos; autoridad: METR.
- [Sjøberg et al.](https://doi.org/10.1109/TSE.2005.97) — experimentos controlados en ingeniería de software; autoridad: IEEE Transactions on Software Engineering.
- [Wohlin et al., «Experimentation in Software Engineering»](https://doi.org/10.1007/978-3-642-29044-2) — diseño y análisis de experimentos; autoridad: Springer.

---

[↑ Glosario](../../README.md) · [← Bomba de descompresión](./bomba-de-descompresion.md) · [Borde →](./borde.md)
