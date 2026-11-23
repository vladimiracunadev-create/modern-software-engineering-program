# Evento ancho

[↑ Glosario](../../README.md) · [← Evento](./evento.md) · [Evento de dominio →](./evento-de-dominio.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Registro estructurado con muchos campos, escrito una vez por unidad de trabajo.

Definición de trabajo de [SE-493 — Señales, eventos y observabilidad útil](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md).

## Por qué importa

La clase donde se define, [SE-493 — Señales, eventos y observabilidad útil](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md), existe con este propósito: la clase existe para que distingas lo que un sistema emite (señales) de lo que una persona puede preguntarle durante un incidente (observabilidad), para que elijas qué señal responde qué pregunta y para que sepas cuándo un panel que parece completo deja una falla sin explicar.

## Cómo funciona

Según [SE-493 — Señales, eventos y observabilidad útil](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md):

Una **señal** es cualquier dato que un sistema emite sobre su propio comportamiento. Las clases habituales son los **registros** (un evento discreto con contexto: «entrega 123 aceptada en 83 ms»), las **métricas** (un número agregado en el tiempo: «peticiones por segundo por endpoint»), las **trazas** (el recorrido de una petición por varios servicios, formado por tramos llamados spans) y los **perfiles** (dónde gasta tiempo o memoria el código). Un **evento ancho** es un registro estructurado con muchos campos (versión, cliente, curso, duración, identificador de traza) escrito una vez por unidad de trabajo. La **telemetría** es el conjunto de lo que se recoge y se envía fuera del proceso.

## Ejemplo

Ejemplo de [SE-493 — Señales, eventos y observabilidad útil](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md) (sección «Ejemplo mínimo»):

El fragmento escribe un evento ancho como una línea de JSON. Antes de ejecutarlo, predice cuántos bytes ocupa.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-493 — Señales, eventos y observabilidad útil](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md)) son:

- **Todos los paneles se ven mal a la vez** — causa: duración inclusiva: todos incluyen al servicio lento. Corrección: comparar con la línea base de cada servicio o medir el tiempo propio.
- **El panel global está sano y un cliente protesta** — causa: promedio dominado por los clientes grandes. Corrección: agrupar por segmento o usar una sonda rotativa.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Las métricas con tres dimensiones previstas responden solo las que se previeron; los eventos anchos responden todas porque guardan todos los campos de cada petición; las métricas con todas las combinaciones también responden todas, pero necesitan un número de series que ningún almacén de métricas aguanta. ([SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Registro estructurado](../r/registro-estructurado.md), [Registro](../r/registro.md), [Trabajo](../t/trabajo.md), [Duración inclusiva](../d/duracion-inclusiva.md), [Observabilidad](../o/observabilidad.md), [Señal](../s/senal.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-493 — Señales, eventos y observabilidad útil](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-494](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md).

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

[↑ Glosario](../../README.md) · [← Evento](./evento.md) · [Evento de dominio →](./evento-de-dominio.md)
