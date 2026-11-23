# Latencia

[↑ Glosario](../../README.md) · [← Lápida](./lapida.md) · [Latencia de cola →](./latencia-de-cola.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

La **latencia** es el tiempo que transcurre entre un inicio y un resultado definidos. Es la formulación de [SE-046](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md) («tiempo entre un inicio definido y un resultado definido»), y las demás clases la aplican a objetos distintos: [SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md) el tiempo hasta completar una operación de memoria o almacenamiento, [SE-022](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md) el tiempo para una unidad de trabajo, y [SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md) el tiempo desde que llega una petición hasta que se responde. Lo esencial es que la palabra solo significa algo cuando se declaran el inicio y el fin.

## Por qué importa

Una cifra de latencia sin sus extremos no se puede comparar. [SE-046](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md) pide definir el inicio y el resultado precisamente para que dos mediciones se puedan comparar. Y en servicio de modelos ([SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md)), la latencia entra en tensión con el costo: agrandar el lote reduce el costo por petición hasta cierto punto y después añade latencia.

## Cómo funciona

La latencia se descompone en lo que ocurre entre los dos extremos definidos. En [SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md), el experimento de lotes mide costo por petición según el tamaño del lote: a partir de cierto tamaño el beneficio se acaba y la curva sube (con 1 024 peticiones el costo por petición fue 8,3 µs, más del triple que con 512), porque en una CPU las matrices dejan de caber en la caché o, en un acelerador, la memoria es limitada. Agrandar el lote deja de ayudar y añade latencia. La forma de la curva depende del hardware, del modelo y de las bibliotecas, por lo que se mide con el modelo propio y la máquina de producción; el experimento mostró además tiempos irregulares en lotes pequeños. En [SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md), la jerarquía de memoria explica por qué la latencia de una operación depende de dónde está el dato.

## Ejemplo

En [SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md), con lotes de 512 y 1 024 peticiones el costo por petición pasa a más del triple al duplicar el lote, y agrandarlo así deja de ayudar y añade latencia. Es un experimento de la clase sobre un modelo y una máquina concretos.

## Errores y confusiones comunes

- **Dar una latencia sin decir de dónde a dónde.** Sin inicio y resultado definidos no es comparable ([SE-046](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md)).
- **Asumir que un lote más grande siempre mejora.** El beneficio se acaba y la curva sube ([SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md)).
- **Transferir una curva medida a otro hardware.** Depende del hardware, del modelo y de las bibliotecas.

## Límites y cuándo no aplica

La latencia es una medida de tiempo, no de capacidad: [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md) la trata junto con rendimiento, saturación y capacidad como cosas distintas que se leen juntas. Los números de [SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md) salen de una máquina y un modelo concretos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Operación](../o/operacion.md), [Resultado](../r/resultado.md), [Trabajo](../t/trabajo.md), [Ancho de banda](../a/ancho-de-banda.md), [Benchmark](../b/benchmark.md), [Cuello de botella](../c/cuello-de-botella.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-018 — Memoria, cachés, almacenamiento y jerarquías](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-022 — Rendimiento, consumo energético y límites físicos](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-046 — Captura, medición y diagnóstico de tráfico](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.
- [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.
- [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (165 clases más lo mencionan; las que más):

[SE-293](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md), [SE-508](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), [SE-281](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md), [SE-598](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md), [SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Wilson (1927)](https://doi.org/10.1080/01621459.1927.10502953) — intervalo de confianza para una proporción; autoridad: Journal of the American Statistical Association.
- [Efron (1979)](https://doi.org/10.1214/aos/1176344552) — el bootstrap; autoridad: The Annals of Statistics.
- [Chen et al., «Evaluating Large Language Models Trained on Code»](https://arxiv.org/abs/2107.03374) — pass@k y evaluación por pruebas; autoridad: preprint de OpenAI.
- [Jimenez et al., «SWE-bench»](https://arxiv.org/abs/2310.06770) — evaluación con problemas reales de repositorios; autoridad: ICLR 2024.
- [Zheng et al., «Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena»](https://arxiv.org/abs/2306.05685) — jueces automáticos y sus sesgos; autoridad: NeurIPS 2023.

---

[↑ Glosario](../../README.md) · [← Lápida](./lapida.md) · [Latencia de cola →](./latencia-de-cola.md)
