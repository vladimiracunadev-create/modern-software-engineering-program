# Estimación puntual

[↑ Glosario](../../README.md) · [← Estimación con incertidumbre](./estimacion-con-incertidumbre.md) · [Estrangulamiento →](./estrangulamiento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Un único valor para una cantidad incierta, sin rango ni confianza.

Definición de trabajo de [SE-185 — Estimación por tamaño, rango y evidencia histórica](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md).

## Por qué importa

La clase donde se define, [SE-185 — Estimación por tamaño, rango y evidencia histórica](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md), existe con este propósito: la clase existe para que entregues una estimación como un rango con su evidencia y sus supuestos, y no como un número que alguien convertirá en compromiso; y para que sepas qué puede y qué no puede sostener una estimación por tamaño relativo o por historia.

## Cómo funciona

[SE-185 — Estimación por tamaño, rango y evidencia histórica](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-185 — Estimación por tamaño, rango y evidencia histórica](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md):

El equipo de la plataforma de entregas comunica la estimación de la recuperación de borradores como: «entre 15 y 19 semanas con 85 % de confianza, basado en 14 semanas de rendimiento propio (media 5,8 elementos) y en el desglose actual de 62 elementos; supone un equipo estable de cuatro personas, que la integración con la secretaría se entrega en la semana 10 y que no se agregan funciones; no incluye vacaciones de fin de año; se revisa cada dos semanas».

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-185 — Estimación por tamaño, rango y evidencia histórica](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md)) son:

- **La fecha prometida se cumple una de cada ocho veces** — causa: se sumaron valores típicos. Corrección: estimar el total con simulación o con historia y comunicar un rango.
- **El intervalo del 80 % falla la mitad de las veces** — causa: se construyó con pocas semanas de historia. Corrección: ensanchar el intervalo o usar una clase de referencia.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-185 — Estimación por tamaño, rango y evidencia histórica](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ninguna estimación de una persona ni de un equipo: las duraciones lognormales, el rendimiento gamma y las medianas por talla son construcciones del autor. La siguiente clase combina estimaciones en un plan con dependencias, donde la suma se convierte en un máximo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Confianza](../c/confianza.md), [Rango](../r/rango.md), [Valor](../v/valor.md), [Clase de referencia](../c/clase-de-referencia.md), [Cobertura](../c/cobertura.md), [Percentil](../p/percentil.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-185 — Estimación por tamaño, rango y evidencia histórica](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md), [SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Jørgensen, «A review of studies on expert estimation of software development effort» (Journal of Systems and Software, 2004)](https://doi.org/10.1016/S0164-1212%2802%2900156-5) — revisión de estudios de estimación por expertos; autoridad: Journal of Systems and Software.
- [Buehler, Griffin y Ross, «Exploring the planning fallacy» (Journal of Personality and Social Psychology, 1994)](https://doi.org/10.1037/0022-3514.67.3.366) — subestimación del tiempo propio; autoridad: Journal of Personality and Social Psychology.
- [Flyvbjerg, «From Nobel Prize to project management: getting risks right» (Project Management Journal, 2006)](https://doi.org/10.1177/875697280603700302) — clases de referencia y optimismo en proyectos; autoridad: Project Management Journal.
- [Efron, «Bootstrap methods: another look at the jackknife» (The Annals of Statistics, 1979)](https://doi.org/10.1214/aos/1176344552) — remuestreo para estimar la distribución de un estadístico; autoridad: The Annals of Statistics.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — gestión de ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Estimación con incertidumbre](./estimacion-con-incertidumbre.md) · [Estrangulamiento →](./estrangulamiento.md)
