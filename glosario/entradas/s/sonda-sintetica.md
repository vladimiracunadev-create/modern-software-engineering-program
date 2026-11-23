# Sonda sintética

[↑ Glosario](../../README.md) · [← Sonda de resiliencia](./sonda-de-resiliencia.md) · [Sondeo →](./sondeo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Petición programada que imita a una persona usuaria para medir el servicio desde fuera.

Definición de trabajo de [SE-493 — Señales, eventos y observabilidad útil](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md).

## Por qué importa

La clase donde se define, [SE-493 — Señales, eventos y observabilidad útil](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md), existe con este propósito: la clase existe para que distingas lo que un sistema emite (señales) de lo que una persona puede preguntarle durante un incidente (observabilidad), para que elijas qué señal responde qué pregunta y para que sepas cuándo un panel que parece completo deja una falla sin explicar.

## Cómo funciona

Según [SE-493 — Señales, eventos y observabilidad útil](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md):

Un promedio global es una suma ponderada por tráfico. Un cliente que aporta el 0,58 % de las peticiones puede estar caído por completo y mover la tasa global de errores menos que el ruido normal. La asimetría es una propiedad del reparto del tráfico: en la plataforma educativa un puñado de universidades concentra casi todas las entregas y cientos de instituciones pequeñas generan una fracción mínima cada una. Una **sonda sintética** que prueba un solo cliente es una pregunta sobre ese cliente y nada más; una sonda que rota por todos detecta a todos con el retraso de una vuelta completa. Una tercera vía es agrupar métricas por segmento (cliente, plan) y alertar por segmento, a un coste de cardinalidad que se verá en `SE-495`.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-493 — Señales, eventos y observabilidad útil](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo revisa el incidente de las 14:03 y escribe una tabla de preguntas para la API de entregas:

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-493 — Señales, eventos y observabilidad útil](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md)) son:

- **Todos los paneles se ven mal a la vez** — causa: duración inclusiva: todos incluyen al servicio lento. Corrección: comparar con la línea base de cada servicio o medir el tiempo propio.
- **El panel global está sano y un cliente protesta** — causa: promedio dominado por los clientes grandes. Corrección: agrupar por segmento o usar una sonda rotativa.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una **sonda sintética** que prueba un solo cliente es una pregunta sobre ese cliente y nada más; una sonda que rota por todos detecta a todos con el retraso de una vuelta completa. ([SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Servicio](./servicio.md), [Duración inclusiva](../d/duracion-inclusiva.md), [Evento ancho](../e/evento-ancho.md), [Observabilidad](../o/observabilidad.md), [Señal](./senal.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-493 — Señales, eventos y observabilidad útil](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md).

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

[↑ Glosario](../../README.md) · [← Sonda de resiliencia](./sonda-de-resiliencia.md) · [Sondeo →](./sondeo.md)
