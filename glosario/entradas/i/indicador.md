# Indicador

[↑ Glosario](../../README.md) · [← Indexar](./indexar.md) · [Indicador de carga →](./indicador-de-carga.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Resumen numérico de una medición con un estadístico, una ventana y un alcance declarados.

Definición de trabajo de [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-495 — Métricas, dimensiones y cardinalidad](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md): Métrica que sube y baja y mide un estado en un instante.

## Por qué importa

En [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), el tema «Indicadores y estadísticos» importa porque la media oculta la cola y la ventana oculta los incidentes.

## Cómo funciona

Según [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md):

Un **indicador** resume un conjunto de mediciones en un número: una media, una mediana, un percentil, una tasa de errores. Cada estadístico responde una pregunta. La **media** responde «cuánto tarda en promedio» y la domina el cuerpo de la distribución; la **mediana** responde cuánto tarda la petición típica; el **percentil 95** responde cuánto tarda la peor de cada veinte y el **percentil 99** la peor de cada cien. Cuando una pequeña fracción de las peticiones es mucho más lenta, la media se desplaza poco y el percentil alto cambia de orden de magnitud. El mismo problema aparece con la **ventana**: un percentil sobre todo el mes diluye un incidente de tres horas porque 59 de cada 60 peticiones fueron normales, mientras que un percentil por día lo expone.

Según [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md):

No exactamente. Un objetivo de nivel de servicio (SLO) es un objetivo sobre un indicador durante un periodo, normalmente con un margen de error permitido; un escenario de calidad es una descripción más amplia que puede ser de latencia, de recuperación o de seguridad. Un escenario de latencia bien escrito se puede convertir en un SLO.

## Ejemplo

Ejemplo de [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md) (sección «Preguntas frecuentes»):

No exactamente. Un objetivo de nivel de servicio (SLO) es un objetivo sobre un indicador durante un periodo, normalmente con un margen de error permitido; un escenario de calidad es una descripción más amplia que puede ser de latencia, de recuperación o de seguridad. Un escenario de latencia bien escrito se puede convertir en un SLO.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El objetivo se cumple y la experiencia no mejora** — causa: el indicador se volvió meta. Corrección: añadir un indicador complementario y revisar su validez. ([SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md))
- **El indicador nunca muestra el pico** — causa: intervalo de lectura mayor que la duración del pico. Corrección: registrar un máximo por intervalo o un histograma. ([SE-495](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Existe además una trampa clásica: cuando un indicador se convierte en meta, deja de ser un buen indicador, porque la gente optimiza el indicador y no la necesidad. ([SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md))
- Un **indicador** (gauge) sube y baja y mide un estado instantáneo (conexiones abiertas, memoria usada, longitud de una cola); no se puede reconstruir lo que ocurrió entre dos lecturas. ([SE-495](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcance](../a/alcance.md), [Baja](../b/baja.md), [Estado](../e/estado.md), [Instante](./instante.md), [Característica de calidad](../c/caracteristica-de-calidad.md), [Cardinalidad](../c/cardinalidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.
- [SE-495 — Métricas, dimensiones y cardinalidad](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (64 clases más lo mencionan; las que más):

[SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md), [SE-172](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md), [SE-505](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md), [SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md), [SE-197](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md), [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md), [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md), [SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Knight Capital](../../../casos/fallo/knight-capital.md), [TSB Bank](../../../casos/fallo/tsb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) — indicadores, objetivos y percentiles; autoridad: Google, libro de ingeniería de confiabilidad.
- [Prometheus: tipos de métricas](https://prometheus.io/docs/concepts/metric_types/) — contador, indicador, histograma y resumen; autoridad: documentación del proyecto Prometheus.
- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) — modelo de calidad del producto con nueve características; autoridad: organismo de normalización (texto completo de pago).
- [Bass, Clements y Kazman, «Software Architecture in Practice»](https://www.sei.cmu.edu/library/software-architecture-in-practice-fourth-edition/) — escenarios de calidad y árbol de utilidad; autoridad: Software Engineering Institute.
- [Python: statistics](https://docs.python.org/3/library/statistics.html) — media, mediana y cuantiles usados en los experimentos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Indexar](./indexar.md) · [Indicador de carga →](./indicador-de-carga.md)
