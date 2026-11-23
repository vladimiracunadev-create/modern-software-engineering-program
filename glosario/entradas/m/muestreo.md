# Muestreo

[↑ Glosario](../../README.md) · [← Muerte por excepción](./muerte-por-excepcion.md) · [Muestreo de auditoría →](./muestreo-de-auditoria.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Conservar solo una parte de los registros para limitar el volumen.

Definición de trabajo de [SE-494 — Logs estructurados y correlación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md).

## Por qué importa

En [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md), el tema «Muestreo» importa porque decidir antes de saber descarta lo interesante.

## Cómo funciona

Según [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md), en la sección «Muestreo»:

Guardar todas las trazas es caro. El **muestreo de cabeza** decide al empezar la petición, por ejemplo con probabilidad del 1 %, y es barato porque no retiene nada; descarta por igual lo normal y lo interesante. El **muestreo de cola** decide cuando la traza termina, a la vista de su duración y su estado: se conservan todas las que tuvieron error o fueron lentas, y una fracción del resto. Cuesta más: hay que mantener en memoria todos los spans de las trazas en curso (aproximadamente la tasa de llegada por la duración de la espera y por los spans de cada traza) y, sobre todo, hay que enrutar todos los spans de una traza al mismo recolector.

## Ejemplo

Ejemplo de [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md) (sección «Ejemplo profesional»):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo hace el inventario de fronteras de la API de entregas: pasarela → API (HTTP, propaga solo), API → cola (el cliente de mensajería no copia propiedades), cola → trabajador (el trabajador lee el mensaje sin contexto), trabajador → hilo de procesamiento de archivos (grupo de hilos sin contexto) y trabajador → almacenamiento (HTTP, propaga solo). Tres de las cinco fronteras necesitan trabajo explícito. Escriben una prueba por frontera: enviar un identificador en la entrada y comprobar que el span de salida lo tiene como padre.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El error del cliente no tiene traza** — causa: muestreo de cabeza descartó la petición. Corrección: muestreo de cola o regla por estado y duración. ([SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md))
- **El muestreo de cola decide mal** — causa: los spans de una traza llegan a recolectores distintos. Corrección: enrutar por hash del identificador de traza. ([SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md))
- **El muestreo borra el incidente** — causa: muestreo uniforme sobre eventos raros. Corrección: conservar por contenido (nivel, estado). ([SE-494](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El **muestreo de cabeza** decide al empezar la petición, por ejemplo con probabilidad del 1 %, y es barato porque no retiene nada; descarta por igual lo normal y lo interesante. ([SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Registro](../r/registro.md), [Volumen](../v/volumen.md), [Contexto de traza](../c/contexto-de-traza.md), [Correlación](../c/correlacion.md), [Identificador de correlación](../i/identificador-de-correlacion.md), [Muestreo de cola](./muestreo-de-cola.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-494 — Logs estructurados y correlación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.
- [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (35 clases más lo mencionan; las que más):

[SE-293](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md), [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md), [SE-099](../../../classes/part-08-entornos-herramientas-y-depuracion/se-099-profilers-de-cpu-memoria-i-o-y-red/README.md), [SE-466](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-466-cumplimiento-evidencia-y-limites-legales/README.md), [SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md), [SE-495](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md), [SE-540](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md), [SE-123](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OpenTelemetry: muestreo](https://opentelemetry.io/docs/concepts/sampling/) — muestreo de cabeza y de cola; autoridad: proyecto OpenTelemetry (CNCF).
- [W3C Trace Context](https://www.w3.org/TR/trace-context/) — formato y reglas de `traceparent`; autoridad: Recomendación del W3C.
- [OpenTelemetry: propagación de contexto](https://opentelemetry.io/docs/concepts/context-propagation/) — cómo viaja el contexto; autoridad: proyecto OpenTelemetry (CNCF).
- [Sigelman et al., «Dapper»](https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/) — trazado distribuido de bajo coste; autoridad: informe técnico de Google Research.
- [Python: re](https://docs.python.org/3/library/re.html) — expresiones regulares usadas para validar el formato; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Muerte por excepción](./muerte-por-excepcion.md) · [Muestreo de auditoría →](./muestreo-de-auditoria.md)
