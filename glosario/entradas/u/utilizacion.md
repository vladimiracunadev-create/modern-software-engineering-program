# Utilización

[↑ Glosario](../../README.md) · [← Utilidad graduada](./utilidad-graduada.md) · [Validación →](../v/validacion.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

La **utilización** es la fracción de la capacidad de un recurso que está ocupada. El programa la usa en nueve clases con el mismo núcleo y una fórmula distinta según el recurso, por lo que conviene identificar cuál es en cada caso:

- **De un servidor o una cola** ([SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md), [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md)): la fracción del tiempo en que el recurso está ocupado; en una cola, la tasa de llegadas dividida por la tasa de servicio. Se escribe ρ.
- **De un procesador y sus tareas** ([SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md), [SE-451](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md)): la fracción de CPU que consume una tarea, igual a su cómputo dividido por su periodo.
- **De la capacidad comprada** ([SE-281](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md), [SE-343](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md), [SE-404](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md)): la fracción de la capacidad de servicio (o de una unidad de aceleración) que ocupa la demanda.
- **De un equipo** ([SE-533](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-533-estimacion-organizacional-y-compromisos/README.md)): la fracción del tiempo disponible que el equipo, o una persona, dedica a trabajo asignado.

Sentido común: cuánto del tiempo o de la capacidad disponible está en uso. No es lo mismo que eficiencia: [SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md) lo señala como la confusión de pedir «llegar al 100 % de ocupación».

## Por qué importa

Según [SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md), la espera crece de forma explosiva con la utilización, no lineal: un sistema que «da abasto» en promedio puede acumular cola cuando se acerca a la saturación. Por eso la utilización objetivo es una decisión de diseño y no un valor a maximizar: decide cuánta holgura se deja para absorber la variación. En costos ([SE-281](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md)) y en capacidad ([SE-404](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md)) es además la medida de cuánta de la capacidad pagada se aprovecha.

## Cómo funciona

En una cola de un servidor con llegadas aleatorias, [SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md) presenta la relación que explica la no linealidad: la espera media en cola es ρ/(1 − ρ) veces el tiempo medio de servicio. A 50 % de utilización la espera equivale a un servicio; a 80 %, cuatro; a 90 %, nueve; a 95 %, diecinueve. La razón es que el servidor pierde capacidad cada vez que está libre y no puede recuperarla, mientras que las llegadas siguen acumulándose cuando está ocupado. La consecuencia de gestión que la clase destaca es incómoda: la última fracción de utilización es la más cara, y un equipo sin holgura no puede absorber ninguna variación.

En tiempo real ([SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md), [SE-451](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md)) la utilización de un conjunto de tareas se compara con cotas de planificabilidad. [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md) muestra que la cota es suficiente y no necesaria: en su simulación, todos los conjuntos con U ≤ 0,8 son planificables aunque 0,8 supere la cota, y entre 0,9 y 0,95 la fracción de conjuntos planificables cae del 92,5 % al 49,7 % según el número de tareas.

En costos ([SE-281](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md)), la utilización se mezcla con las unidades enteras que se compran: con los supuestos del autor, el acelerador gana a partir de unos 1 000 a 2 000 peticiones por segundo; por debajo de eso, se paga capacidad que no se usa.

## Ejemplo

En [SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md), una cola de un servidor con llegadas y servicios exponenciales de media 1 se simula con 300 000 elementos por nivel de utilización (descartando los primeros 20 000). La simulación coincide con la fórmula hasta el 90 %; al 95 % queda un 6 % por debajo, porque cerca de la saturación la convergencia es lenta y 280 000 elementos aún no bastan. La clase usa la curva para fijar una utilización objetivo del equipo en lugar de buscar el 100 %.

## Errores y confusiones comunes

- **Pedir llegar al 100 % de ocupación.** Se confunde ocupación con eficiencia; corrección ([SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md)): mostrar la curva de espera y fijar una utilización objetivo.
- **Un plazo que se incumple con baja utilización media.** El tiempo de ejecución varía y se analiza con la media; hay que usar el peor caso o un percentil alto y medir la cola ([SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md)).
- **Confiar en la cota como condición necesaria.** Se confunde suficiente con necesaria; hay que aplicar el análisis exacto de tiempo de respuesta ([SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md)).
- **Mezclar los sentidos.** Una utilización del 80 % de CPU, de un servidor de cola y de un equipo no se interpretan igual: hay que confirmar a qué recurso se refiere.

## Límites y cuándo no aplica

La fórmula ρ/(1 − ρ) vale para una cola de un servidor con llegadas y servicios exponenciales; con otra variabilidad o con lotes la espera cambia, y [SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md) mide cuánto añaden la variabilidad y los lotes. Las cifras de costo de [SE-281](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md) dependen de los precios y capacidades supuestos por el autor, y los resultados de planificabilidad de [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md) son de conjuntos generados con un algoritmo y periodos concretos. Una utilización media baja no garantiza cumplir plazos si el tiempo de ejecución varía mucho.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-183](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Conjunto](../c/conjunto.md), [Recurso](../r/recurso.md), [Servicio](../s/servicio.md), [Backpressure](../b/backpressure.md), [Cola de muertos](../c/cola-de-muertos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-184 — Lean, teoría de colas y límites de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-268 — Sistemas de tiempo real y deadlines](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.
- [SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-343 — Data mesh y propiedad de los datos](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-436 — Latencia, throughput, saturación y capacidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.
- [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.
- [SE-533 — Estimación organizacional y compromisos](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-533-estimacion-organizacional-y-compromisos/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

**También se usa en** (17 clases más lo mencionan; las que más):

[SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md), [SE-508](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md), [SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md), [SE-529](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-529-liderazgo-tecnico-sin-autoridad-formal/README.md), [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), [SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md), [SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md), [SE-280](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Liu y Layland, «Scheduling algorithms for multiprogramming in a hard-real-time environment» (JACM, 1973)](https://doi.org/10.1145/321738.321743) — planificación por prioridades por periodo y cota de utilización; autoridad: Journal of the ACM.
- [Little, «A proof for the queuing formula: L = λW» (Operations Research, 1961)](https://doi.org/10.1287/opre.9.3.383) — demostración de la ley; autoridad: Operations Research.
- [Little, «Little's law as viewed on its 50th anniversary» (Operations Research, 2011)](https://doi.org/10.1287/opre.1110.0940) — condiciones y usos de la ley; autoridad: Operations Research.
- [Kingman, «The single server queue in heavy traffic» (Math. Proc. Cambridge Philos. Soc., 1961)](https://doi.org/10.1017/S0305004100036094) — aproximación de la espera con carga alta; autoridad: Cambridge Philosophical Society.
- [The Kanban Guide](https://kanbanguides.org/english/) — límites de trabajo y gestión del flujo; autoridad: Scrum.org (Kanban Guide).

---

[↑ Glosario](../../README.md) · [← Utilidad graduada](./utilidad-graduada.md) · [Validación →](../v/validacion.md)
