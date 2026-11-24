# Pronóstico por simulación

[↑ Glosario](../../README.md) · [← Promoción](./promocion.md) · [Propagación →](./propagacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

El **pronóstico por simulación** es la distribución del resultado obtenida repitiendo muchas veces un modelo del proceso con datos extraídos de la historia ([SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md)). [SE-533](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-533-estimacion-organizacional-y-compromisos/README.md) lo formula como la estimación de la distribución de plazos remuestreando un historial de entrega. Es el enfoque de «Monte Carlo» aplicado a la pregunta «¿cuándo termina?».

## Por qué importa

Convierte la historia en una distribución de fechas sin suponer una fórmula. En lugar de una fecha única, se obtiene «el 85 % de las veces termina en 12 semanas o menos», que es una promesa con confianza. Cambia cómo se comunica un plazo: como rango con probabilidad, no como número exacto.

## Cómo funciona

[SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md) describe el procedimiento. Se toma la **historia de rendimiento semanal** (por ejemplo, ocho semanas con media 5,8 elementos terminados), se parte de un **desglose del trabajo pendiente** (62 elementos) y se **simula el futuro**: se eligen al azar semanas de esa historia, con reposición, hasta completar el trabajo pendiente, y se anota cuántas semanas tomó. Se repite miles de veces. El resultado es una **distribución de semanas hasta terminar**, de la que se leen **percentiles**.

Es la aplicación directa del **remuestreo** de Efron: no supone una forma para el rendimiento (normal, por ejemplo), solo que el futuro se parece a la historia observada. Su utilidad es que respeta la variabilidad real: semanas buenas y malas, sin necesidad de ajustar una distribución.

Dos fuentes de error, con su corrección. El percentil 85 que se cumple solo dos de cada tres veces ocurre porque el alcance se modeló fijo y la historia es corta; se corrige **incluyendo el crecimiento esperado del alcance** (en el ejemplo, entre 0 y 15 %, estimado con las últimas dos entregas) y **ensanchando el intervalo**. Y el margen de cada tarea que se consume mientras el plazo igual se pierde por expansión del trabajo; se corrige con un colchón compartido y vigilando su consumo. La calibración de la simulación se comprueba por retrospectiva: si el percentil 85 se cumple el 85 % de las veces. Con menos de unas doce semanas de historia conviene ensanchar el intervalo.

## Ejemplo

Historia: 4, 6, 5, 7, 6, 5, 8, 5 elementos por semana. Pendiente: 62 elementos. En cada simulación se sortean semanas de esa lista hasta sumar 62; tras 10.000 simulaciones, el percentil 50 de semanas es 11 y el percentil 85 es 13. Con crecimiento de alcance de 0 a 15 %, el percentil 85 sube a unas 15. Se comunica «entre 11 y 15 semanas, con 85 % de confianza». (Simulación ilustrativa con el método de [SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md); las cifras son de ejemplo.)

## Errores y confusiones comunes

- **El percentil 85 se cumple dos de cada tres veces**: alcance fijo y poca historia.
- **El margen de cada tarea se consume y el plazo se pierde**: expansión del trabajo.
- **Usar la media** como pronóstico único.
- **Remuestrear una historia no representativa** (con cambios de equipo).

## Límites y cuándo no aplica

Supone que el futuro se parece al pasado; si el equipo, el producto o el proceso cambian, la historia deja de valer. Con muy poca historia, la distribución es poco fiable. No sustituye la gestión del alcance ni las dependencias externas, que el modelo simple no incluye.

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
