# Correlación

[↑ Glosario](../../README.md) · [← Corrección total](./correccion-total.md) · [Correlación entre comprobaciones →](./correlacion-entre-comprobaciones.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Relación explícita entre señales de una operación.

Definición de trabajo de [SE-033 — Logs del sistema y diagnóstico de fallos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-046 — Captura, medición y diagnóstico de tráfico](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md): Vínculo entre señales que podrían pertenecer al mismo evento.

## Por qué importa

En [SE-494 — Logs estructurados y correlación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md), el tema «Correlación» importa porque un identificador propagado une líneas de servicios distintos.

En [SE-033 — Logs del sistema y diagnóstico de fallos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md), el tema «Correlación» importa porque relaciona señales de una operación

## Cómo funciona

Según [SE-494 — Logs estructurados y correlación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md), en la sección «Correlación»:

Una petición de entrega atraviesa la pasarela, la API, la cola, un trabajador y el almacenamiento, y cada uno escribe sus propias líneas. Para unirlas se necesita un identificador común que cada servicio **reciba** en la petición entrante, **incluya** en todas las líneas que escriba y **copie** a toda llamada saliente (cabecera HTTP, propiedad del mensaje en la cola). El estándar `traceparent` de W3C Trace Context fija un formato para esto y las bibliotecas de trazado lo hacen automáticamente en HTTP; en una cola o un grupo de hilos hay que hacerlo explícitamente, y es donde se rompe.

## Ejemplo

Ejemplo de [SE-494 — Logs estructurados y correlación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md) (sección «Ejemplo profesional»):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo define el contrato de registros de la API de entregas: siete campos obligatorios (`ts`, `level`, `service`, `version`, `msg`, `request_id`, `trace_id`), un catálogo de mensajes (`entrega aceptada`, `entrega rechazada`, `almacenamiento lento`) y una prueba en la integración continua que ejecuta cada servicio, captura su salida y verifica que cada línea cumple el esquema. Cada frontera asíncrona (la cola y el grupo de hilos) tiene una prueba que envía un mensaje con un identificador y comprueba que el trabajador lo escribe.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Hay mucho log pero no se relacionan eventos** — causa: faltan identificadores y estructura. Corrección: añadir eventos estables y correlación por operación. ([SE-033](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md))
- **Atribuir causa por coincidencia temporal** — causa: la correlación no es causalidad. Corrección: plantear una hipótesis con predicción y una intervención. ([SE-046](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La correlación aproxima relaciones; no demuestra causalidad por sí sola. ([SE-033](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md))
- Emite eventos sin correlación para dos ejecuciones simultáneas y demuestra la ambigüedad. ([SE-033](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md), [SE-031](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento](../e/evento.md), [Operación](../o/operacion.md), [Relación](../r/relacion.md), [Alcance](../a/alcance.md), [Diagnóstico](../d/diagnostico.md), [Garantía](../g/garantia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-033 — Logs del sistema y diagnóstico de fallos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-046 — Captura, medición y diagnóstico de tráfico](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.
- [SE-494 — Logs estructurados y correlación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (57 clases más lo mencionan; las que más):

[SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md), [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md), [SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md), [SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md), [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md), [SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md), [SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md), [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md).

**Aparece en los casos de estudio:** [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OpenTelemetry: modelo de datos de registros](https://opentelemetry.io/docs/specs/otel/logs/data-model/) — campos de un registro y su relación con trazas; autoridad: especificación de OpenTelemetry.
- [W3C Trace Context](https://www.w3.org/TR/trace-context/) — formato de `traceparent`; autoridad: Recomendación del W3C.
- [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) — formato de fecha y hora; autoridad: IETF.
- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) — qué registrar y qué no; autoridad: proyecto OWASP.
- [Python: logging](https://docs.python.org/3/library/logging.html) — módulo usado en el ejemplo mínimo; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Corrección total](./correccion-total.md) · [Correlación entre comprobaciones →](./correlacion-entre-comprobaciones.md)
