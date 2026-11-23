# Paralelismo

[↑ Glosario](../../README.md) · [← Par de independencia](./par-de-independencia.md) · [Parámetro →](./parametro.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Ejecución simultánea de varias tareas en unidades de cálculo distintas.

Definición de trabajo de [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md).

## Por qué importa

En [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md), el tema «Concurrencia y paralelismo» importa porque elegir mal significa pagar complejidad sin ganar tiempo.

## Cómo funciona

Según [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md):

La **concurrencia** es una propiedad de la estructura de un programa: varias tareas están en curso, cada una puede avanzar sin esperar a que otra termine. El **paralelismo** es una propiedad de la ejecución: dos tareas avanzan en el mismo instante porque hay dos unidades de cálculo. Un programa puede ser concurrente sin ser paralelo (un solo núcleo que alterna entre tareas) y puede ser paralelo sin ser concurrente en sentido interesante (cuatro núcleos que ejecutan cuatro copias independientes de lo mismo). La distinción importa porque cada una tiene un costo distinto: la concurrencia exige razonar sobre intercalaciones y estado compartido (`SE-386`), el paralelismo exige repartir datos y reunir resultados.

## Ejemplo

Caso medido en la sección «Concurrencia y paralelismo» de [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md):

La **concurrencia** es una propiedad de la estructura de un programa: varias tareas están en curso, cada una puede avanzar sin esperar a que otra termine. El **paralelismo** es una propiedad de la ejecución: dos tareas avanzan en el mismo instante porque hay dos unidades de cálculo. Un programa puede ser concurrente sin ser paralelo (un solo núcleo que alterna entre tareas) y puede ser paralelo sin ser concurrente en sentido interesante (cuatro núcleos que ejecutan cuatro copias independientes de lo mismo).

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md)) son:

- **El servicio «async» no mejora con carga de cálculo** — causa: el cálculo corre dentro del bucle de eventos. Corrección: enviarlo a un proceso o a un ejecutor.
- **El latido de salud se detiene a ratos** — causa: una corrutina calcula sin `await`. Corrección: trocear con `await` o sacar el cálculo del bucle.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos deterministas en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ningún servidor, ningún sistema operativo ni la escalabilidad real de hilos y procesos: el planificador, la proporción de espera y el cálculo de 200 000 vueltas son construcciones del autor, y los resultados no se extrapolan a una carga de producción.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Tarea](../t/tarea.md), [Concurrencia](../c/concurrencia.md), [Corrutina](../c/corrutina.md), [GIL](../g/gil.md), [Ley de Amdahl](../l/ley-de-amdahl.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (21 clases más lo mencionan; las que más):

[SE-081](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md), [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md), [SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md), [SE-280](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md), [SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-572](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: asyncio](https://docs.python.org/3/library/asyncio.html) — bucle de eventos y corrutinas; autoridad: documentación de Python.
- [Python: desarrollo con asyncio](https://docs.python.org/3/library/asyncio-dev.html) — modo de depuración y código bloqueante; autoridad: documentación de Python.
- [Python: glosario](https://docs.python.org/3/glossary.html) — definición del bloqueo global del intérprete; autoridad: documentación de Python.
- [Python: concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) — ejecutores de hilos y procesos; autoridad: documentación de Python.
- [Amdahl, «Validity of the single processor approach…»](https://doi.org/10.1145/1465482.1465560) — límite de aceleración; autoridad: artículo original (1967).

---

[↑ Glosario](../../README.md) · [← Par de independencia](./par-de-independencia.md) · [Parámetro →](./parametro.md)
