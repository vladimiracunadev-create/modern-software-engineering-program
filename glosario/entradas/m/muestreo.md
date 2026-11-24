# Muestreo

[↑ Glosario](../../README.md) · [← Muerte por excepción](./muerte-por-excepcion.md) · [Muestreo de auditoría →](./muestreo-de-auditoria.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

En observabilidad, **muestreo** es conservar solo una parte de los registros o trazas para limitar el volumen ([SE-494](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md), [SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md)).

## Por qué importa

Almacenar todo cuesta; muestrear mal borra justo lo que se necesitaba. La decisión es qué se conserva, y de ella depende que el incidente o el error raro dejen rastro.

## Cómo funciona

[SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md) distingue dos momentos. En el **muestreo de cabeza**, se decide al comenzar la traza (barato, pero ciego al resultado). En el **muestreo de cola**, se decide al terminar, con conocimiento del estado y la duración, de modo que se pueden conservar todas las trazas con error o lentas. Para que el de cola decida bien, todos los tramos de una traza deben llegar al mismo recolector; se consigue enrutando por hash del identificador de traza. [SE-494](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md) añade el criterio para registros: conservar por contenido (nivel, estado) en lugar de uniformemente.

## Ejemplo

Con muestreo uniforme del 1 %, un error que ocurre en 1 de cada 10 000 peticiones casi nunca queda registrado. Con una regla que conserva todo lo de estado de error y el 1 % del resto, el error siempre se ve.

## Errores y confusiones comunes

- **El error del cliente no tiene traza.** El muestreo de cabeza descartó la petición; usar de cola o reglas por estado y duración.
- **El muestreo de cola decide mal.** Los tramos llegan a recolectores distintos; enrutar por hash del identificador.
- **El muestreo borra el incidente.** Muestreo uniforme sobre eventos raros; conservar por contenido.

## Límites y cuándo no aplica

Las métricas agregadas conviene calcularlas antes de muestrear, o se sesgan. Muestrear reduce costo pero no sustituye a decidir qué señales importan.

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
