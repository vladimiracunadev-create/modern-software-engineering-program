# Muestreo de cola

[↑ Glosario](../../README.md) · [← Muestreo de auditoría](./muestreo-de-auditoria.md) · [Muestreo y saturación →](./muestreo-y-saturacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Decisión de conservar una traza tomada después de que termina, a la vista de su resultado.

Definición de trabajo de [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md).

## Por qué importa

La clase donde se define, [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md), existe con este propósito: la clase existe para que expliques cómo una traza sigue una petición a través de varios servicios, qué hay que hacer en cada frontera para que no se rompa, cómo se lee la ruta crítica para saber qué optimizar y qué se pierde al muestrear.

## Cómo funciona

Según [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md):

Guardar todas las trazas es caro. El **muestreo de cabeza** decide al empezar la petición, por ejemplo con probabilidad del 1 %, y es barato porque no retiene nada; descarta por igual lo normal y lo interesante. El **muestreo de cola** decide cuando la traza termina, a la vista de su duración y su estado: se conservan todas las que tuvieron error o fueron lentas, y una fracción del resto. Cuesta más: hay que mantener en memoria todos los spans de las trazas en curso (aproximadamente la tasa de llegada por la duración de la espera y por los spans de cada traza) y, sobre todo, hay que enrutar todos los spans de una traza al mismo recolector.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo hace el inventario de fronteras de la API de entregas: pasarela → API (HTTP, propaga solo), API → cola (el cliente de mensajería no copia propiedades), cola → trabajador (el trabajador lee el mensaje sin contexto), trabajador → hilo de procesamiento de archivos (grupo de hilos sin contexto) y trabajador → almacenamiento (HTTP, propaga solo). Tres de las cinco fronteras necesitan trabajo explícito.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El error del cliente no tiene traza** — causa: muestreo de cabeza descartó la petición. Corrección: muestreo de cola o regla por estado y duración. ([SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md))
- **El muestreo de cola decide mal** — causa: los spans de una traza llegan a recolectores distintos. Corrección: enrutar por hash del identificador de traza. ([SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Si cada span va a un recolector elegido al azar, ninguno ve la traza entera y el muestreo de cola decide con información parcial. ([SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-494](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Resultado](../r/resultado.md), [Traza](../t/traza.md), [Vista](../v/vista.md), [Contexto de traza](../c/contexto-de-traza.md), [Muestreo](./muestreo.md), [Propagación de contexto](../p/propagacion-de-contexto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [W3C Trace Context](https://www.w3.org/TR/trace-context/) — formato y reglas de `traceparent`; autoridad: Recomendación del W3C.
- [OpenTelemetry: propagación de contexto](https://opentelemetry.io/docs/concepts/context-propagation/) — cómo viaja el contexto; autoridad: proyecto OpenTelemetry (CNCF).
- [OpenTelemetry: muestreo](https://opentelemetry.io/docs/concepts/sampling/) — muestreo de cabeza y de cola; autoridad: proyecto OpenTelemetry (CNCF).
- [Sigelman et al., «Dapper»](https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/) — trazado distribuido de bajo coste; autoridad: informe técnico de Google Research.
- [Python: re](https://docs.python.org/3/library/re.html) — expresiones regulares usadas para validar el formato; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Muestreo de auditoría](./muestreo-de-auditoria.md) · [Muestreo y saturación →](./muestreo-y-saturacion.md)
