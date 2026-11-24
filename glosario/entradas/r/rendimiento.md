# Rendimiento

[↑ Glosario](../../README.md) · [← Renderizado en servidor](./renderizado-en-servidor.md) · [Reordenador →](./reordenador.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

En este sentido, el **rendimiento** (*throughput*) es la cantidad de trabajo atendido por unidad de tiempo: peticiones por segundo en un servicio ([SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md)) o elementos terminados por unidad de tiempo en un proceso de desarrollo ([SE-189](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md)). No es el «rendimiento» en el sentido amplio de velocidad percibida (que se mide con latencia) ni el rendimiento como desempeño de una persona.

## Por qué importa

Dice cuánto trabajo cabe, y se contrasta con la latencia, que dice cuánto tarda cada pieza. Sirve para dimensionar capacidad y para seguir el flujo de un equipo. Cambia las decisiones de diseño: subir el rendimiento a costa de la latencia, o al revés, es un compromiso que se decide con el objetivo de nivel de servicio.

## Cómo funciona

[SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md) estudia la relación en un servicio con **lotes dinámicos**: se agrupan las peticiones que llegan hasta alcanzar un tamaño máximo o agotar una espera máxima, lo que ocurra primero. Agrupar mejora el rendimiento porque el costo fijo de cada invocación se reparte entre varias peticiones, pero **agrega espera**. La clase lo simula con 40.000 llegadas de Poisson a una tasa del 80 % de la capacidad sin lotes (18.391 por segundo, con una capacidad sin lotes de 22.989), con el tiempo de servicio medido. Con 0 ms de espera y lote de 1, el p50 fue 0,10 ms y el p99 0,47 ms; al ampliar la espera máxima, el rendimiento sostenible sube y la latencia de cola crece, porque la espera máxima se suma al p99. La regla práctica: fijar la espera máxima a partir del **presupuesto de latencia** (el SLO) y no del rendimiento.

En el flujo de trabajo ([SE-189](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md)), el rendimiento es el número de elementos terminados por unidad de tiempo, y se relaciona con el trabajo en curso y el plazo por la ley de Little. Una advertencia: **la velocidad sube y el plazo no cambia** cuando la métrica se premia y se infla (se dividen los elementos para contar más); la corrección es retirarla de la vista externa y seguir el rendimiento y los escapes juntos.

## Ejemplo

Un servicio con capacidad de 23.000 peticiones por segundo sin lotes y una carga del 80 % atiende unas 18.400 por segundo con p99 de 0,47 ms. Con lotes de hasta 8 peticiones y espera máxima de 2 ms, la capacidad sostenible sube, pero el p99 pasa a incluir hasta 2 ms de espera. Si el SLO de p99 es 5 ms, el ajuste es aceptable; si es 1 ms, no. (El primer dato es de [SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md); el segundo es un escenario ilustrativo.)

## Errores y confusiones comunes

- **Confundir rendimiento con latencia.**
- **Premiar la velocidad del equipo**: se infla sin cambiar el plazo.
- **Optimizar el rendimiento sin mirar la latencia de cola.**
- **Comparar rendimientos medidos con cargas distintas.**

## Límites y cuándo no aplica

El rendimiento máximo no es el operativo: a utilización alta, las colas crecen y la latencia se dispara. La simulación de [SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md) usa llegadas de Poisson y tiempos medidos de un caso concreto. En equipos, contar elementos terminados supone que son comparables en tamaño, lo que no siempre es cierto.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Antigüedad del trabajo en curso](../a/antiguedad-del-trabajo-en-curso.md), [Capacidad](../c/capacidad.md), [Combustible](../c/combustible.md), [Escape](../e/escape.md), [Importación](../i/importacion.md), [Instancia](../i/instancia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-189 — Métricas de flujo, calidad y resultados](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (131 clases más lo mencionan; las que más):

[SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md), [SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md), [SE-192](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md), [SE-183](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md), [SE-280](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md), [SE-185](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md), [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), [SE-281](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Amazon](../../../casos/exito/amazon.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md), [Shopify](../../../casos/exito/shopify.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Forsgren et al., «The SPACE of developer productivity» (ACM Queue, 2021)](https://doi.org/10.1145/3454122.3454124) — dimensiones de la productividad; autoridad: ACM Queue.
- [DORA: investigación](https://dora.dev/research/) — métricas de entrega y estabilidad; autoridad: DORA (Google Cloud).
- [Manheim y Garrabrant, «Categorizing variants of Goodhart's law» (2018)](https://arxiv.org/abs/1803.04585) — formas de la ley de Goodhart; autoridad: arXiv.
- [Efron, «Bootstrap methods: another look at the jackknife» (The Annals of Statistics, 1979)](https://doi.org/10.1214/aos/1176344552) — remuestreo para estimar la incertidumbre de un estadístico; autoridad: The Annals of Statistics.
- [The Kanban Guide](https://kanbanguides.org/english/) — métricas de flujo; autoridad: Scrum.org (Kanban Guide).

---

[↑ Glosario](../../README.md) · [← Renderizado en servidor](./renderizado-en-servidor.md) · [Reordenador →](./reordenador.md)
