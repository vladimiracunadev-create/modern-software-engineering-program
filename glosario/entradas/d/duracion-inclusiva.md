# Duración inclusiva

[↑ Glosario](../../README.md) · [← Durabilidad](./durabilidad.md) · [EBPF →](../e/ebpf.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Tiempo que mide un servicio para una llamada, que incluye el de las llamadas que a su vez hace.

Definición de trabajo de [SE-493 — Señales, eventos y observabilidad útil](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md).

## Por qué importa

En [SE-493 — Señales, eventos y observabilidad útil](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md), el tema «Localizar con señales inclusivas» importa porque la duración inclusiva desplaza la culpa hacia el borde.

## Cómo funciona

Según [SE-493 — Señales, eventos y observabilidad útil](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md):

Cuando un servicio A llama a B y B llama a C, la duración que mide A incluye la de B y la de C. Esa duración **inclusiva** es la que casi toda instrumentación simple registra, porque es la que se ve desde el cliente de cada llamada. Si C se vuelve lenta, la duración de B sube, la de A sube y la de la pasarela, que está en el borde, sube más que ninguna. Quien mira «¿qué servicio es el más lento?» elegirá siempre la pasarela, que es inocente. Hay dos maneras de salir de la trampa.

Según [SE-493 — Señales, eventos y observabilidad útil](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** la guardia despierta al equipo de la pasarela y el servicio degradado es el de almacenamiento. **Hipótesis rivales:** (a) la pasarela tiene un defecto; (b) la red entre pasarela y API está degradada; (c) la pasarela mide una duración que incluye a todos. **Prueba:** compara el p99 de cada servicio con su línea base; si el aumento relativo mayor está en el almacenamiento y la pasarela solo suma una constante, la hipótesis (c) explica la señal. **Conclusión:** una duración inclusiva sube por el servicio más profundo de la cadena. **Regresión:** añade una prueba que reproduzca la cadena, degrade cada servicio por turno y compruebe que el procedimiento de atribución lo localiza.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-493 — Señales, eventos y observabilidad útil](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo revisa el incidente de las 14:03 y escribe una tabla de preguntas para la API de entregas:

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Todos los paneles se ven mal a la vez** — causa: duración inclusiva: todos incluyen al servicio lento. Corrección: comparar con la línea base de cada servicio o medir el tiempo propio. ([SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La primera es comparar cada servicio **con su propia línea base**: lo que importa es cuánto creció en proporción, y el servicio culpable es aquel cuya duración inclusiva crece más en relativo, porque lo que suma lo sano es una constante. ([SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Servicio](../s/servicio.md), [Evento ancho](../e/evento-ancho.md), [Observabilidad](../o/observabilidad.md), [Señal](../s/senal.md), [Sonda sintética](../s/sonda-sintetica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-493 — Señales, eventos y observabilidad útil](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-508](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md).

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

[↑ Glosario](../../README.md) · [← Durabilidad](./durabilidad.md) · [EBPF →](../e/ebpf.md)
