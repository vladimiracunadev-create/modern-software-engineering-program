# Observabilidad

[↑ Glosario](../../README.md) · [← Obligaciones externas](./obligaciones-externas.md) · [Observabilidad de datos →](./observabilidad-de-datos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

La **observabilidad** es la propiedad de un sistema que permite explicar su comportamiento interno a partir de lo que emite, incluidas preguntas que nadie previó al diseñarlo. Las clases coinciden en el núcleo y varían el énfasis: [SE-033](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md) la define como capacidad de inferir el estado interno a partir de las salidas disponibles, [SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md) como capacidad de inferir el estado interno de un sistema a partir de lo que emite, [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md) añade «incluidas preguntas no previstas» y [SE-585](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md) la aplica a agentes: explicar el comportamiento a partir de lo registrado. Hereda la idea de la teoría de control, donde un sistema es observable si su estado interno se deduce de sus salidas; la ingeniería de software la usa en sentido práctico.

## Por qué importa

Un sistema que falla de una forma nueva solo se diagnostica si ya emitía la información necesaria. La diferencia con monitorear es decisiva en un incidente: el monitoreo avisa de lo que se esperaba, la observabilidad permite investigar lo inesperado. [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md) propone un criterio empírico para saber si la tienes: puedes responder «¿qué tienen en común las peticiones lentas de las 14:03?» sin desplegar código nuevo para poder preguntarlo.

## Cómo funciona

Un sistema es más observable cuanto más preguntas permiten responder sus señales ([SE-033](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md)). Las tres señales clásicas cumplen funciones distintas: los **logs** describen eventos, las **métricas** agregan medidas y las **trazas** relacionan los pasos de una operación a través de componentes. En un diagnóstico local también cuentan los códigos de salida, la configuración efectiva, la versión y el estado del sistema.

[SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md) ordena el diseño con dos miradas complementarias:

- **Caja negra:** una sonda se comporta como una persona usuaria, llama al endpoint y mide lo que recibe; detecta síntomas con independencia de la causa y es la que suele despertar a alguien.
- **Caja blanca:** la instrumentación mira el interior (colas, caches, errores internos); explica lo que ocurrió y permite decidir qué hacer.

Se necesitan las dos. Y la causa de que ninguna señal aislada baste la da [SE-033](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md): un log registra lo que el programa alcanzó a emitir, y un cierre abrupto puede dejar eventos sin emitir. En sistemas con agentes, [SE-585](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md) pide que la traza sea un contrato: por paso, la acción, el resultado, la observación resumida y el contexto visible, de modo que cada decisión de diagnóstico tenga un campo del que salir.

## Ejemplo

Una consulta tarda 4 segundos a las 14:03. Con solo un panel que muestra la latencia media, sabes que algo empeoró. Con trazas que llevan atributos (versión, tenant, región, tipo de consulta), puedes agrupar las peticiones lentas y ver qué comparten, sin añadir instrumentación nueva. Esa segunda capacidad es la que [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md) llama observabilidad; la primera es monitoreo. (Ilustración construida con el criterio de la clase; no es un caso medido.)

## Errores y confusiones comunes

- **Equiparar observabilidad con tener un panel.** Un panel responde preguntas previstas; la observabilidad se mide por las que no se previeron.
- **Confundirla con monitoreo.** El monitoreo comprueba condiciones conocidas («disco por encima del 90 %»); [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md) los distingue explícitamente.
- **Creer que las cuatro señales de oro la garantizan.** Latencia, tráfico, errores y saturación son un buen mínimo de monitoreo, no garantizan observabilidad ([SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md)).
- **Confiar en una sola señal.** Un log no cuenta lo que el programa no alcanzó a emitir ([SE-033](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md)).

## Límites y cuándo no aplica

Las clases advierten que las cuatro señales de oro no garantizan observabilidad ([SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md)) y que ninguna señal aislada es verdad completa: un log solo registra lo que el programa alcanzó a emitir ([SE-033](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md)). La observabilidad se define por la capacidad de explicar, no por tener herramientas; la clase la mide con una pregunta no prevista, no con el número de paneles.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md), [SE-031](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Estado](../e/estado.md), [Correlación](../c/correlacion.md), [Decisión oculta](../d/decision-oculta.md), [Determinismo de una prueba](../d/determinismo-de-una-prueba.md), [Evento](../e/evento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-033 — Logs del sistema y diagnóstico de fallos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-308 — Diseño para cambio, prueba y operación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-493 — Señales, eventos y observabilidad útil](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.
- [SE-585 — Observabilidad y evals del propio harness](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (46 clases más lo mencionan; las que más):

[SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md), [SE-279](../../../classes/part-23-runtimes-y-plataformas-modernas/se-279-ebpf-observabilidad-red-y-seguridad-en-el-kernel/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-381](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md), [SE-383](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md), [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md), [SE-513](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md), [SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) — monitoreo de caja negra y blanca y señales de oro; autoridad: libro de ingeniería de confiabilidad de Google.
- [OpenTelemetry: Signals](https://opentelemetry.io/docs/concepts/signals/) — definición de trazas, métricas y registros; autoridad: proyecto OpenTelemetry (CNCF).
- [Sigelman et al., «Dapper»](https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/) — trazado distribuido de bajo coste; autoridad: informe técnico de Google Research.
- [Prometheus: modelo de datos](https://prometheus.io/docs/concepts/data_model/) — identidad de una serie por nombre y etiquetas; autoridad: documentación del proyecto Prometheus.
- [Python: json](https://docs.python.org/3/library/json.html) — serialización usada en el ejemplo mínimo; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Obligaciones externas](./obligaciones-externas.md) · [Observabilidad de datos →](./observabilidad-de-datos.md)
