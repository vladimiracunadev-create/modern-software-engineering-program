# Señal

[↑ Glosario](../../README.md) · [← Semver](./semver.md) · [Señal de fallo →](./senal-de-fallo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Una **señal** es cualquier dato que un sistema emite sobre su propio comportamiento. [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md) distingue cuatro clases: **registros** (un evento discreto con contexto), **métricas** (un número agregado en el tiempo), **trazas** (el recorrido de una petición por varios servicios, formado por tramos llamados *spans*) y **perfiles** (dónde gasta tiempo o memoria el código). La **telemetría** es el conjunto de lo que se recoge y se envía fuera del proceso.

## Por qué importa

Lo que no emite señal no se puede diagnosticar. Elegir qué señales emitir decide qué preguntas podrán responderse cuando algo falle: [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md) pone la vara en la capacidad de decir qué pregunta *no* se podría responder y qué señal habría que añadir, no en que el servicio tenga un panel.

## Cómo funciona

Cada clase responde a preguntas distintas. El registro dice qué pasó en una unidad de trabajo («entrega 123 aceptada en 83 ms»); la métrica dice cuánto y con qué tendencia («peticiones por segundo por endpoint»); la traza dice por dónde pasó una petición; el perfil, por qué el código gasta recursos. Un **evento ancho** es un registro estructurado con muchos campos (versión, cliente, curso, duración, identificador de traza) escrito una vez por unidad de trabajo, de modo que se puede agrupar por cualquier campo.

## Ejemplo

[SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md): la guardia despierta al equipo de la pasarela, pero el servicio degradado es el de almacenamiento. Hipótesis rivales: defecto en la pasarela, red degradada, o duración inclusiva. Se compara el p99 de cada servicio con su línea base; si el mayor aumento relativo está en almacenamiento y la pasarela solo suma una constante, la duración inclusiva explica la señal.

## Errores y confusiones comunes

- **Todos los paneles se ven mal a la vez.** Duración inclusiva: todos incluyen al servicio lento; comparar con la línea base de cada servicio o medir el tiempo propio.
- **El panel global está sano y un cliente protesta.** El promedio lo dominan los clientes grandes; agrupar por segmento.

## Límites y cuándo no aplica

Más señales no equivalen a más comprensión: cuestan almacenamiento y atención, y una señal sin pregunta asociada es ruido. Una señal es un síntoma, no la causa.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Métrica](../m/metrica.md), [Registro](../r/registro.md), [Sobre](./sobre.md), [Traza](../t/traza.md), [Duración inclusiva](../d/duracion-inclusiva.md), [Evento ancho](../e/evento-ancho.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-493 — Señales, eventos y observabilidad útil](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (227 clases más lo mencionan; las que más):

[SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md), [SE-608](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md), [SE-273](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md), [SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md), [SE-175](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md), [SE-508](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md), [SE-601](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md), [SE-581](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md).

**Aparece en los casos de estudio:** [Cloudflare](../../../casos/exito/cloudflare.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Therac-25](../../../casos/fallo/therac-25.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

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

[↑ Glosario](../../README.md) · [← Semver](./semver.md) · [Señal de fallo →](./senal-de-fallo.md)
