# Indicador

[↑ Glosario](../../README.md) · [← Indexar](./indexar.md) · [Indicador de carga →](./indicador-de-carga.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Un **indicador** es el resumen numérico de una medición con un estadístico, una ventana y un alcance declarados ([SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md)). «p95 de latencia, ventana de 10 s, endpoint de entregas» es un indicador; «latencia» a secas no.

## Por qué importa

Un número sin estadístico, ventana y alcance no se puede interpretar ni comparar. Además, un indicador acaba siendo objetivo de decisiones: cuando se vuelve meta, se optimiza el número y no lo que representa ([SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md)).

## Cómo funciona

Cada declaración elimina una ambigüedad: el **estadístico** (media, percentil, máximo), la **ventana** (sobre qué intervalo) y el **alcance** (qué eventos entran). [SE-495](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md) añade un caso: un indicador leído a intervalos mayores que la duración de un pico nunca lo muestra; se registra un máximo por intervalo o un histograma. Los indicadores de servicio (SLI) son indicadores sobre eventos buenos y válidos, base de los objetivos (SLO).

## Ejemplo

Un panel muestra la latencia media por minuto; los usuarios se quejan de picos de 3 s. La media los diluye. Se sustituye por el p99 con un máximo por intervalo, y los picos aparecen.

## Errores y confusiones comunes

- **El objetivo se cumple y la experiencia no mejora.** El indicador se volvió meta; añadir uno complementario y revisar su validez ([SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md)).
- **El indicador nunca muestra el pico.** Intervalo de lectura mayor que el pico ([SE-495](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md)).

## Límites y cuándo no aplica

Ningún indicador agota lo que se quiere saber; es un resumen y descarta información. Se elige junto a la pregunta que debe responder.

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

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Shopify](../../../casos/exito/shopify.md), [Knight Capital](../../../casos/fallo/knight-capital.md), [TSB Bank](../../../casos/fallo/tsb.md).

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
