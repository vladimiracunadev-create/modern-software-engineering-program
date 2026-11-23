# Registro estructurado

[↑ Glosario](../../README.md) · [← Registro encadenado](./registro-encadenado.md) · [Regla →](./regla.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Línea de registro con campos nombrados y tipados, legible por máquinas sin interpretar el mensaje.

Definición de trabajo de [SE-494 — Logs estructurados y correlación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md).

## Por qué importa

La clase donde se define, [SE-494 — Logs estructurados y correlación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md), existe con este propósito: la clase existe para que escribas registros que una máquina pueda consultar sin adivinar el formato, para que correlaciones las líneas de una misma petición a través de varios servicios y para que decidas cuánto registrar, cuánto conservar y qué datos no escribir nunca.

## Cómo funciona

Según [SE-494 — Logs estructurados y correlación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md):

Un registro tiene dos lectores: la persona que lo lee durante un incidente y los programas que lo agregan, filtran y alertan. El texto libre sirve al primero y rompe al segundo, porque una expresión regular depende de la redacción exacta y la redacción es un detalle que cambia en cualquier refactorización. Un **registro estructurado** separa el mensaje (para personas) de los campos (para máquinas): `{"ts": ..., "level": "INFO", "msg": "entrega aceptada", "submission_id": 123, "course_id": 45, "duration_ms": 83}`. La separación no elimina la fragilidad, la traslada: los nombres de los campos pasan a ser un contrato. Si alguien renombra `duration_ms` a `duration`, todas las consultas, paneles y alertas que lo usaban dejan de ver datos sin error.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-494 — Logs estructurados y correlación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo define el contrato de registros de la API de entregas: siete campos obligatorios (`ts`, `level`, `service`, `version`, `msg`, `request_id`, `trace_id`), un catálogo de mensajes (`entrega aceptada`, `entrega rechazada`, `almacenamiento lento`) y una prueba en la integración continua que ejecuta cada servicio, captura su salida y verifica que cada línea cumple el esquema.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-494 — Logs estructurados y correlación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md)) son:

- **Un panel queda vacío tras un despliegue** — causa: la consulta dependía de la redacción del mensaje. Corrección: consultar campos, no texto, y probar el esquema.
- **Las trazas de algunas peticiones están incompletas** — causa: el identificador no se copia en colas o hilos. Corrección: propagar explícitamente y probar cada frontera asíncrona.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-494 — Logs estructurados y correlación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Registro](./registro.md), [Correlación](../c/correlacion.md), [Identificador de correlación](../i/identificador-de-correlacion.md), [Muestreo](../m/muestreo.md), [Redacción](./redaccion.md), [Retención](./retencion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-494 — Logs estructurados y correlación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-033](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md), [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md), [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md), [SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md), [SE-585](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md), [SE-495](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md), [SE-597](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md).

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

[↑ Glosario](../../README.md) · [← Registro encadenado](./registro-encadenado.md) · [Regla →](./regla.md)
