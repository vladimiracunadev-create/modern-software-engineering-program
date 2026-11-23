# Colchón de proyecto

[↑ Glosario](../../README.md) · [← Cola y disciplina fifo](./cola-y-disciplina-fifo.md) · [Cold/warm →](./cold-warm.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Margen único reservado al final de una cadena de tareas y consumido cuando alguna se atrasa.

Definición de trabajo de [SE-191 — Taller: planificar bajo incertidumbre explícita](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md).

## Por qué importa

La clase donde se define, [SE-191 — Taller: planificar bajo incertidumbre explícita](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md), existe con este propósito: el taller integra lo que la parte midió por separado —rangos, dependencias, riesgos, métricas— en una forma de planificar que dice «cuándo» como una distribución con sus supuestos, comprueba si esa distribución estaba calibrada y señala qué supuesto vale más la pena vigilar.

## Cómo funciona

Según [SE-191 — Taller: planificar bajo incertidumbre explícita](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md):

Una cadena de diez tareas, cada una lognormal con mediana de 5 días y σ = 0,5. El percentil 85 de una tarea es 8,4 días. Tres planes: sumar medianas (50 días), añadir el percentil 85 a cada tarea (84,0 días) y sumar medianas más un colchón de proyecto de 10,74 días (la raíz de la suma de cuadrados de las diferencias entre percentil 85 y mediana), para 60,7 días. Se evalúan 20 000 ejecuciones en dos mundos: uno donde cada tarea termina cuando acaba su trabajo, y otro donde, si una tarea termina antes del 90 % de su margen, se entrega al agotarse el margen (el trabajo se expande para ocuparlo, supuesto del autor).

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
- **Ver también:** [Margen](../m/margen.md), [Tarea](../t/tarea.md), [Calibración](./calibracion.md), [Expansión del trabajo](../e/expansion-del-trabajo.md), [Pronóstico por simulación](../p/pronostico-por-simulacion.md), [Sensibilidad](../s/sensibilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-191 — Taller: planificar bajo incertidumbre explícita](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.

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

[↑ Glosario](../../README.md) · [← Cola y disciplina fifo](./cola-y-disciplina-fifo.md) · [Cold/warm →](./cold-warm.md)
