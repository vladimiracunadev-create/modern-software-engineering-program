# Ley de Goodhart

[↑ Glosario](../../README.md) · [← Ley de Fitts](./ley-de-fitts.md) · [Ley de Little →](./ley-de-little.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Cuando una medida se convierte en objetivo, deja de ser una buena medida.

Definición de trabajo de [SE-189 — Métricas de flujo, calidad y resultados](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-135 — Resultados, outputs, actividad y vanity metrics](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md): Una medida que se vuelve meta deja de informar sobre lo que se quería medir.

## Por qué importa

La clase donde se define, [SE-189 — Métricas de flujo, calidad y resultados](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md), existe con este propósito: la clase existe para que elijas métricas que informen decisiones y no que premien actividad: sabrás resumir tiempos con cola larga, detectar cuándo una métrica premiada se infla sin que mejore nada, y declarar cuántos datos hacen falta antes de creer un percentil.

## Cómo funciona

[SE-189 — Métricas de flujo, calidad y resultados](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-189 — Métricas de flujo, calidad y resultados](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md):

El equipo de la plataforma de entregas rediseña su tablero con cinco números que informan cinco decisiones. Plazo de los elementos (percentiles 50, 85 y 95 con el tamaño de la muestra) para prometer fechas. Rendimiento semanal y trabajo en curso para vigilar el límite de `SE-184`. Antigüedad del trabajo en curso para detectar lo que se atasca. Escapes por cada 100 elementos terminados, para vigilar las puertas de `SE-188`.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-189 — Métricas de flujo, calidad y resultados](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md)) son:

- **La fecha prometida con el promedio se incumple en un tercio de los casos** — causa: promedio sobre una distribución con cola larga. Corrección: prometer con un percentil y mostrar la muestra.
- **La velocidad sube y el plazo no cambia** — causa: métrica premiada que se infla. Corrección: retirarla de la vista externa y seguir rendimiento y escapes.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-189 — Métricas de flujo, calidad y resultados](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ningún equipo ni se observó manipulación real: la distribución de los plazos, la inflación del 4 % por sprint y la estacionariedad son construcciones del autor. La siguiente clase usa estas mediciones para decidir qué mejorar en el sistema de trabajo y cómo saber si funcionó.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Afirmación](../a/afirmacion.md), [Medida](../m/medida.md), [Sobre](../s/sobre.md), [Actividad](../a/actividad.md), [Antigüedad del trabajo en curso](../a/antiguedad-del-trabajo-en-curso.md), [Escape](../e/escape.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-135 — Resultados, outputs, actividad y vanity metrics](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.
- [SE-189 — Métricas de flujo, calidad y resultados](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Manheim y Garrabrant, «Categorizing variants of Goodhart's law» (2018)](https://arxiv.org/abs/1803.04585) — formas de la ley de Goodhart; autoridad: arXiv.
- [Forsgren et al., «The SPACE of developer productivity» (ACM Queue, 2021)](https://doi.org/10.1145/3454122.3454124) — dimensiones de la productividad; autoridad: ACM Queue.
- [DORA: investigación](https://dora.dev/research/) — métricas de entrega y estabilidad; autoridad: DORA (Google Cloud).
- [Efron, «Bootstrap methods: another look at the jackknife» (The Annals of Statistics, 1979)](https://doi.org/10.1214/aos/1176344552) — remuestreo para estimar la incertidumbre de un estadístico; autoridad: The Annals of Statistics.
- [The Kanban Guide](https://kanbanguides.org/english/) — métricas de flujo; autoridad: Scrum.org (Kanban Guide).

---

[↑ Glosario](../../README.md) · [← Ley de Fitts](./ley-de-fitts.md) · [Ley de Little →](./ley-de-little.md)
