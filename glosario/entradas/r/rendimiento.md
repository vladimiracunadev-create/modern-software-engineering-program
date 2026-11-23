# Rendimiento

[↑ Glosario](../../README.md) · [← Renderizado en servidor](./renderizado-en-servidor.md) · [Reordenador →](./reordenador.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Peticiones atendidas por unidad de tiempo.

Definición de trabajo de [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-189 — Métricas de flujo, calidad y resultados](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md): Número de elementos terminados por unidad de tiempo.

## Por qué importa

En [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md), el tema «Rendimiento» importa porque wasm es rápido frente a un intérprete, no frente a código vectorizado.

## Cómo funciona

Según [SE-277 — WebAssembly y WASI](../../../classes/part-23-runtimes-y-plataformas-modernas/se-277-webassembly-y-wasi/README.md):

El aislamiento de memoria no hace nada contra un bucle infinito. El módulo `spin` del laboratorio (`loop $l (br $l)`) es válido, no toca memoria ni importa nada, y se queda ejecutando para siempre. El anfitrión necesita un mecanismo propio: en `wasmtime` es el **combustible**. Se activa en la configuración (`consume_fuel`), se asigna una cantidad al almacén con `set_fuel`, y cada instrucción ejecutada la consume; al agotarse hay una trampa (`all fuel consumed by WebAssembly`). Con 5 000 000 de unidades, el bucle infinito se detuvo en unos 11 ms. Dos consecuencias de diseño: el combustible mide trabajo, no tiempo de reloj (una importación lenta del anfitrión no gasta combustible), y activar la medición tiene un costo de ejecución que se paga en toda llamada.

Según [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md):

Un lote dinámico agrupa las peticiones que llegan hasta alcanzar un tamaño máximo o agotar una espera máxima, lo que ocurra primero. Se simularon 40 000 llegadas de Poisson a una tasa del 80 % de la capacidad sin lotes (18 391 por segundo, con una capacidad sin lotes de 22 989), con el tiempo de servicio medido (interpolado). Con 0 ms de espera y lote de 1, el p50 fue 0,10 ms y el p99 0,47 ms. Con 0,5 ms de espera y lote máximo de 8: 0,32 y 0,64 ms. Con 2 ms y lote de 32: 1,12 y 2,21 ms. Con 5 ms y 64: 2,03 y 4,25 ms. Con 20 ms y 256: 7,67 y 15,16 ms.

## Ejemplo

Ejemplo de [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md) (sección «Preguntas frecuentes»):

Lo que permita tu presupuesto de latencia: la espera máxima se suma al p99. Fíjala a partir del SLO, no del rendimiento.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La velocidad sube y el plazo no cambia** — causa: métrica premiada que se infla. Corrección: retirarla de la vista externa y seguir rendimiento y escapes. ([SE-189](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- A esa carga, esperar solo costó latencia: el rendimiento servido fue el mismo (18 340 por segundo), porque el servicio sin lotes ya tenía holgura. ([SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md))

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

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Amazon](../../../casos/exito/amazon.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md).

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
