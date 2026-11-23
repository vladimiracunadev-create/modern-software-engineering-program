# Pronóstico por simulación

[↑ Glosario](../../README.md) · [← Promoción](./promocion.md) · [Propagación →](./propagacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Distribución del resultado obtenida repitiendo muchas veces un modelo del proceso con datos extraídos de la historia.

Definición de trabajo de [SE-191 — Taller: planificar bajo incertidumbre explícita](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-533 — Estimación organizacional y compromisos](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-533-estimacion-organizacional-y-compromisos/README.md): Estimación de la distribución de plazos remuestreando un historial de entrega.

## Por qué importa

En [SE-191 — Taller: planificar bajo incertidumbre explícita](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md), el tema «Pronóstico por simulación» importa porque convierte la historia en una distribución de fechas sin suponer una fórmula.

## Cómo funciona

Según [SE-191 — Taller: planificar bajo incertidumbre explícita](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md), en la sección «Pronóstico por simulación»:

Para «cuándo termina» se toma la historia de rendimiento semanal, se simula el futuro eligiendo al azar semanas de esa historia hasta completar el trabajo pendiente y se repite muchas veces. El resultado es una distribución de semanas hasta terminar de la que se leen percentiles. Es la aplicación directa del remuestreo de Efron: no supone una forma para el rendimiento, solo que el futuro se parece al pasado observado. Esas dos suposiciones —que el pasado representa el futuro y que las semanas son intercambiables— son las que hay que declarar y vigilar.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-191 — Taller: planificar bajo incertidumbre explícita](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md):

El equipo de la plataforma de entregas arma su plan con el procedimiento del taller. Toma ocho semanas de rendimiento (media 5,8), un desglose de 62 elementos y un crecimiento de alcance estimado en 0 a 15 % con las últimas dos entregas.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-191 — Taller: planificar bajo incertidumbre explícita](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md)) son:

- **El percentil 85 se cumple dos de cada tres veces** — causa: alcance fijo en el modelo y poca historia. Corrección: incluir el crecimiento esperado y ensanchar el intervalo.
- **El margen de cada tarea se consume y el plazo igual se pierde** — causa: expansión del trabajo. Corrección: compartir el colchón y vigilar su consumo.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-191 — Taller: planificar bajo incertidumbre explícita](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se pronosticó ningún proyecto real ni se observó expansión del trabajo: el rendimiento gamma, las tareas lognormales, la regla de expansión del 90 % y los valores base del plan son construcciones del autor. La siguiente clase convierte este plan en un proyecto adaptativo con reglas de replanificación y barreras.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-190](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Modelo](../m/modelo.md), [Plazo](./plazo.md), [Proceso](./proceso.md), [Resultado](../r/resultado.md), [Calibración](../c/calibracion.md), [Colchón de proyecto](../c/colchon-de-proyecto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-191 — Taller: planificar bajo incertidumbre explícita](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-533 — Estimación organizacional y compromisos](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-533-estimacion-organizacional-y-compromisos/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Efron, «Bootstrap methods: another look at the jackknife» (The Annals of Statistics, 1979)](https://doi.org/10.1214/aos/1176344552) — remuestreo; autoridad: The Annals of Statistics.
- [Malcolm et al., «Application of a technique for research and development program evaluation» (Operations Research, 1959)](https://doi.org/10.1287/opre.7.5.646) — PERT y combinación de varianzas; autoridad: Operations Research.
- [Flyvbjerg, «From Nobel Prize to project management: getting risks right» (Project Management Journal, 2006)](https://doi.org/10.1177/875697280603700302) — clases de referencia y optimismo; autoridad: Project Management Journal.
- [Buehler, Griffin y Ross, «Exploring the planning fallacy» (Journal of Personality and Social Psychology, 1994)](https://doi.org/10.1037/0022-3514.67.3.366) — subestimación del tiempo propio; autoridad: Journal of Personality and Social Psychology.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — gestión de ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Promoción](./promocion.md) · [Propagación →](./propagacion.md)
