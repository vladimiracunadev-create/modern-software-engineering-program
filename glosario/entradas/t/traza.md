# Traza

[↑ Glosario](../../README.md) · [← Traversal de rutas](./traversal-de-rutas.md) · [Traza enriquecida →](./traza-enriquecida.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Registro ordenado de cada acción, su resultado y el estado del harness en ese paso.

Definición de trabajo de [SE-577 — Anatomía de un harness: modelo, contexto, herramientas y bucles](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md): Registro estructurado de los tramos de una solicitud.
- En [SE-326 — Vistas lógica, runtime, datos y despliegue](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md): Registro de los pasos de una petición a través de los componentes del sistema.
- En [SE-382 — Observabilidad y seguridad de integraciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md): Recorrido de una petición o de un flujo por varios componentes, formado por tramos relacionados.
- En [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md): Conjunto de spans que describen el recorrido de una petición por un sistema.

## Por qué importa

En [SE-577 — Anatomía de un harness: modelo, contexto, herramientas y bucles](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md), el tema «Traza» importa porque sin ella, ninguna de las demás se puede diagnosticar.

En [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md), el tema «Traza» importa porque sin ella no se atribuye costo ni falla.

## Cómo funciona

Según [SE-577 — Anatomía de un harness: modelo, contexto, herramientas y bucles](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md):

La consecuencia práctica es que existen dos grupos de fallas con tratamientos opuestos. Una falla del modelo (razona mal, inventa una función) se trata cambiando de modelo, dividiendo la tarea o dándole más información. Una falla del entorno (no ve el resultado, no puede escribir, nadie verifica) se trata cambiando el entorno, y cambiar de modelo no la arregla. La traza es lo que permite distinguirlas.

Según [SE-577 — Anatomía de un harness: modelo, contexto, herramientas y bucles](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md):

El equipo adopta un asistente de código para el mantenimiento de *Avisos*. Durante dos semanas todo va bien; en la tercera, tres cambios llegan a revisión con las pruebas en rojo. La revisión encuentra que el asistente los dio por terminados. Tres hipótesis compiten: el modelo empeoró, el prompt cambió, el entorno cambió. La persona responsable revisa las trazas de los tres casos y encuentra que ninguno ejecutó las pruebas. Revisa el archivo de instrucciones: una reorganización había movido la línea de verificación a un archivo que el producto ya no cargaba. La corrección no toca el modelo: restaura la línea y añade una compuerta (`SE-583`) que rechaza la terminación sin pruebas en verde.

## Ejemplo

Ejemplo de [SE-577 — Anatomía de un harness: modelo, contexto, herramientas y bucles](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md) (sección «Ejemplo mínimo»):

La tarea `T1`: `add(a, b)` devuelve `a - b`. El harness completo hace cuatro pasos: lee `calc.py`; aplica el reemplazo `a - b` por `a + b`; ejecuta las pruebas, que pasan; y el agente declara la tarea terminada. En la traza aparecen exactamente `read`, `write`, `run_tests` y la solicitud de cierre. Quitar la herramienta de escritura produce una traza de doce lecturas; quitar el contexto, otra de doce lecturas. Las dos trazas son iguales y los fallos distintos: por eso la traza necesita más que el nombre de la herramienta.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El código tiene dependencias que nadie dibujó** — causa: la vista lógica declara lo permitido y no se verifica. Corrección: comparar con trazas o con el código en cada cambio. ([SE-326](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md))
- **Hay trazas huérfanas de 3 segundos** — causa: contexto perdido en un grupo de hilos o en una cola. Corrección: copiar el contexto explícitamente y probar la frontera. ([SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md))
- **Una traza está completa pero la mejora no llega** — causa: se optimizó un span fuera de la ruta crítica. Corrección: calcular la ruta crítica antes de elegir. ([SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Quitar la herramienta de escritura deja al agente leyendo en bucle, porque la política no tiene otra salida: el agente no «sabe» que no puede escribir hasta que lo intenta, y el harness que no lo registra deja una traza idéntica a la del contexto perdido. ([SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md))
- Para unir tramos de procesos distintos hace falta que cada uno reciba y reenvíe un **identificador de correlación** o un contexto de traza. ([SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md), [SE-031](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Registro estructurado](../r/registro-estructurado.md), [Agente](../a/agente.md), [Componente](../c/componente.md), [Conjunto](../c/conjunto.md), [Alcance](../a/alcance.md), [Correlación](../c/correlacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-033 — Logs del sistema y diagnóstico de fallos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-047 — Taller: seguir una petición de extremo a extremo](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.
- [SE-326 — Vistas lógica, runtime, datos y despliegue](../../../classes/part-27-arquitectura-de-software-y-dominio/se-326-vistas-logica-runtime-datos-y-despliegue/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-382 — Observabilidad y seguridad de integraciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.
- [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.
- [SE-577 — Anatomía de un harness: modelo, contexto, herramientas y bucles](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.
- [SE-585 — Observabilidad y evals del propio harness](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.
- [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (132 clases más lo mencionan; las que más):

[SE-587](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md), [SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md), [SE-588](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md), [SE-518](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md), [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md), [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), [SE-218](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md), [SE-592](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [W3C Trace Context](https://www.w3.org/TR/trace-context/) — encabezados para propagar el contexto de una traza; autoridad: W3C.
- [OpenTelemetry: convenciones semánticas de mensajería](https://opentelemetry.io/docs/specs/semconv/messaging/) — trazas y atributos de productores y consumidores; autoridad: proyecto OpenTelemetry.
- [Lee et al., «Deduplicating training data makes language models better»](https://arxiv.org/abs/2107.06499) — duplicados en los datos de entrenamiento y memorización; autoridad: artículo de investigación (arXiv).
- [Kirkpatrick et al., «Overcoming catastrophic forgetting in neural networks»](https://arxiv.org/abs/1612.00796) — pérdida de capacidades previas al entrenar en una tarea nueva; autoridad: artículo de investigación (arXiv).
- [Kruchten, «The 4+1 View Model of Architecture» (IEEE Software, 1995)](https://doi.org/10.1109/52.469759) — vistas lógica, de procesos, de desarrollo y física; autoridad: IEEE Software.

---

[↑ Glosario](../../README.md) · [← Traversal de rutas](./traversal-de-rutas.md) · [Traza enriquecida →](./traza-enriquecida.md)
