# Redacción

[↑ Glosario](../../README.md) · [← Red de seguridad](./red-de-seguridad.md) · [Redirección →](./redireccion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Sustitución de datos sensibles por una marca antes de almacenar el registro.

Definición de trabajo de [SE-494 — Logs estructurados y correlación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md): Transformación previa a salida que oculta información sensible.

## Por qué importa

La clase donde se define, [SE-494 — Logs estructurados y correlación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md), existe con este propósito: la clase existe para que escribas registros que una máquina pueda consultar sin adivinar el formato, para que correlaciones las líneas de una misma petición a través de varios servicios y para que decidas cuánto registrar, cuánto conservar y qué datos no escribir nunca.

## Cómo funciona

Según [SE-494 — Logs estructurados y correlación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md):

Un registro tiene dos lectores: la persona que lo lee durante un incidente y los programas que lo agregan, filtran y alertan. El texto libre sirve al primero y rompe al segundo, porque una expresión regular depende de la redacción exacta y la redacción es un detalle que cambia en cualquier refactorización. Un **registro estructurado** separa el mensaje (para personas) de los campos (para máquinas): `{"ts": ..., "level": "INFO", "msg": "entrega aceptada", "submission_id": 123, "course_id": 45, "duration_ms": 83}`. La separación no elimina la fragilidad, la traslada: los nombres de los campos pasan a ser un contrato. Si alguien renombra `duration_ms` a `duration`, todas las consultas, paneles y alertas que lo usaban dejan de ver datos sin error.

Según [SE-494 — Logs estructurados y correlación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo define el contrato de registros de la API de entregas: siete campos obligatorios (`ts`, `level`, `service`, `version`, `msg`, `request_id`, `trace_id`), un catálogo de mensajes (`entrega aceptada`, `entrega rechazada`, `almacenamiento lento`) y una prueba en la integración continua que ejecuta cada servicio, captura su salida y verifica que cada línea cumple el esquema. Cada frontera asíncrona (la cola y el grupo de hilos) tiene una prueba que envía un mensaje con un identificador y comprueba que el trabajador lo escribe. La política de conservación guarda todo lo de nivel `WARNING` o superior durante 90 días y una de cada diez líneas `INFO` durante 14.

## Ejemplo

Ejemplo de [SE-494 — Logs estructurados y correlación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md) (sección «Ejemplo profesional»):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo define el contrato de registros de la API de entregas: siete campos obligatorios (`ts`, `level`, `service`, `version`, `msg`, `request_id`, `trace_id`), un catálogo de mensajes (`entrega aceptada`, `entrega rechazada`, `almacenamiento lento`) y una prueba en la integración continua que ejecuta cada servicio, captura su salida y verifica que cada línea cumple el esquema. Cada frontera asíncrona (la cola y el grupo de hilos) tiene una prueba que envía un mensaje con un identificador y comprueba que el trabajador lo escribe.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un panel queda vacío tras un despliegue** — causa: la consulta dependía de la redacción del mensaje. Corrección: consultar campos, no texto, y probar el esquema. ([SE-494](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md))
- **El token aparece en una excepción** — causa: la redacción se aplicó solo al log normal. Corrección: centralizar serialización segura y probar fallos. ([SE-031](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El texto libre sirve al primero y rompe al segundo, porque una expresión regular depende de la redacción exacta y la redacción es un detalle que cambia en cualquier refactorización. ([SE-494](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md))
- **un cambio de redacción que vacía un panel sin ningún error**. ([SE-494](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-030](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Registro](./registro.md), [Sustitución](../s/sustitucion.md), [Configuración efectiva](../c/configuracion-efectiva.md), [Correlación](../c/correlacion.md), [Esquema](../e/esquema.md), [Herencia](../h/herencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-494 — Logs estructurados y correlación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (33 clases más lo mencionan; las que más):

[SE-033](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md), [SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md), [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), [SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md), [SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md), [SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md), [SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md), [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md).

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

[↑ Glosario](../../README.md) · [← Red de seguridad](./red-de-seguridad.md) · [Redirección →](./redireccion.md)
