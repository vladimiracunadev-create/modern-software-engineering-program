# Percentil

[↑ Glosario](../../README.md) · [← Peor caso de ejecución](./peor-caso-de-ejecucion.md) · [Percentil 75 →](./percentil-75.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Valor por debajo del cual queda una proporción dada de las mediciones; el p95 deja por debajo el 95 %.

Definición de trabajo de [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-185 — Estimación por tamaño, rango y evidencia histórica](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md): Valor por debajo del cual cae la proporción indicada de los resultados; el percentil 85 deja al 85 % por debajo.

## Por qué importa

La clase donde se define, [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), existe con este propósito: la clase existe para que conviertas una palabra como «rápido», «fiable» o «usable» en una promesa que se pueda comprobar: qué atributo de calidad importa, en qué situación, con qué estadístico, sobre qué ventana y con qué umbral.

## Cómo funciona

Según [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md):

Un **indicador** resume un conjunto de mediciones en un número: una media, una mediana, un percentil, una tasa de errores. Cada estadístico responde una pregunta. La **media** responde «cuánto tarda en promedio» y la domina el cuerpo de la distribución; la **mediana** responde cuánto tarda la petición típica; el **percentil 95** responde cuánto tarda la peor de cada veinte y el **percentil 99** la peor de cada cien. Cuando una pequeña fracción de las peticiones es mucho más lenta, la media se desplaza poco y el percentil alto cambia de orden de magnitud. El mismo problema aparece con la **ventana**: un percentil sobre todo el mes diluye un incidente de tres horas porque 59 de cada 60 peticiones fueron normales, mientras que un percentil por día lo expone.

Según [SE-185 — Estimación por tamaño, rango y evidencia histórica](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md):

Resultado, idéntico en Windows (CPython 3.12.9) y en Ubuntu bajo WSL2 (3.12.3): cumplir la suma de medianas ocurre en el **12,4 %** de los proyectos; la media del total es 108,9, la mediana 108,1, el percentil 85 es 120,8 y el 95 es 129,4. Con σ = 0,2 la probabilidad sube a 31,9 %, con σ = 0,8 baja a 4,1 % y con σ = 1,1 a 1,5 %. Un margen de 25 % en cada tarea (plan de 120 días) se cumple en el 83,5 %.

## Ejemplo

Ejemplo de [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md) (sección «Ejemplo mínimo»):

La media es 158 ms (por debajo de 200) mientras que 2 de cada 100 peticiones tardan 3 s: el percentil 98 ya vale 100 y el 99 vale 3 000. Registra versión de Python, comando y salida; después añade un percentil 99 al criterio y comprueba que el objetivo deja de cumplirse.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El informe dice «cumple» y hay quejas** — causa: ventana demasiado amplia o media como estadístico. Corrección: medir por ventana corta y con percentil. ([SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md))
- **Se pide «p99.99» sin datos suficientes** — causa: el percentil no se puede estimar con pocas muestras. Corrección: calcular cuántas peticiones hacen falta para estimarlo. ([SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** un objetivo diario exige cientos de peticiones por día para estimar un p95 estable; con 20 peticiones diarias el percentil es ruido. ([SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Percentil 85](./percentil-85.md), [Medición](../m/medicion.md), [Resultado](../r/resultado.md), [Valor](../v/valor.md), [Característica de calidad](../c/caracteristica-de-calidad.md), [Clase de referencia](../c/clase-de-referencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-185 — Estimación por tamaño, rango y evidencia histórica](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (111 clases más lo mencionan; las que más):

[SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md), [SE-533](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-533-estimacion-organizacional-y-compromisos/README.md), [SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md), [SE-189](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md), [SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md), [SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md), [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md), [SE-155](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) — modelo de calidad del producto con nueve características; autoridad: organismo de normalización (texto completo de pago).
- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) — indicadores, objetivos y percentiles; autoridad: Google, libro de ingeniería de confiabilidad.
- [Bass, Clements y Kazman, «Software Architecture in Practice»](https://www.sei.cmu.edu/library/software-architecture-in-practice-fourth-edition/) — escenarios de calidad y árbol de utilidad; autoridad: Software Engineering Institute.
- [Python: statistics](https://docs.python.org/3/library/statistics.html) — media, mediana y cuantiles usados en los experimentos; autoridad: documentación de Python.
- [Python: random](https://docs.python.org/3/library/random.html) — generador con semilla para reproducir las muestras; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Peor caso de ejecución](./peor-caso-de-ejecucion.md) · [Percentil 75 →](./percentil-75.md)
