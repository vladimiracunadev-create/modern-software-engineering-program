# Hecho

[↑ Glosario](../../README.md) · [← Heartbeat](./heartbeat.md) · [Hecho observado →](./hecho-observado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Medición de un evento de negocio con su granularidad.

Definición de trabajo de [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-033 — Logs del sistema y diagnóstico de fallos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md): Observación respaldada por una fuente identificable.

## Por qué importa

En [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md), el tema «Hechos y dimensiones» importa porque separan lo que se mide de aquello por lo que se mide.

## Cómo funciona

Según [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md):

Un hecho es una medición de un evento de negocio: una línea de pedido, una entrega, una lectura. Una dimensión es el contexto con el que se agrupa o filtra: cliente, producto, curso, fecha. La frase que hace de contrato es «una fila de este hecho es un ____ por ____»: una línea de pedido por pedido y por producto. Todo lo que se sume debe pertenecer a ese grano: el importe de la línea sí; el costo de envío del pedido no, porque se repite en cada línea. Declarar el grano antes de diseñar columnas es la regla más barata y más ignorada del modelado.

Según [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md):

El equipo de *Avisos* modela los avisos leídos. Escribe la frase «una fila es una lectura de un aviso por un estudiante en un instante», sus dimensiones (estudiante, aviso, curso, fecha) y decide que la dimensión de estudiante conserva historia porque los estudiantes cambian de curso a mitad de año. Añade una prueba: la suma de lecturas del hecho debe coincidir con la cuenta de eventos de la zona intermedia cada día. A la tercera semana la prueba falla un día con un 8 % de diferencia; la causa es una unión con la dimensión de curso que no filtraba por vigencia y duplicaba las lecturas de quienes cambiaron de curso ese día.

## Ejemplo

Ejemplo de [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* modela los avisos leídos. Escribe la frase «una fila es una lectura de un aviso por un estudiante en un instante», sus dimensiones (estudiante, aviso, curso, fecha) y decide que la dimensión de estudiante conserva historia porque los estudiantes cambian de curso a mitad de año. Añade una prueba: la suma de lecturas del hecho debe coincidir con la cuenta de eventos de la zona intermedia cada día.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Las defensas son tres: declarar el grano de cada tabla, agregar cada lado a su grano antes de unir y escribir una prueba de conciliación («el total del hecho coincide con el total de la fuente»). ([SE-363](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md), [SE-031](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento](../e/evento.md), [Granularidad](../g/granularidad.md), [Medición](../m/medicion.md), [Observación](../o/observacion.md), [Abanico de uniones](../a/abanico-de-uniones.md), [Clave sustituta](../c/clave-sustituta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-033 — Logs del sistema y diagnóstico de fallos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (196 clases más lo mencionan; las que más):

[SE-593](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md), [SE-555](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-555-contexto-archivos-memoria-y-recuperacion/README.md), [SE-572](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md), [SE-580](../../../classes/part-48-harness-y-agentic-engineering/se-580-gestion-de-contexto-resets-y-handoffs/README.md), [SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md), [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md), [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md), [SE-531](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-531-comunicacion-facilitacion-y-conflicto/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft Learn — Event Logging](https://learn.microsoft.com/windows/win32/eventlog/event-logging) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [systemd — journalctl](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html) — define ciclo de vida, supervisión o consulta de eventos en systemd.
- [Apple Developer — Logging](https://developer.apple.com/documentation/os/logging) — delimita el contrato técnico que debe cumplirse al usar logs como observaciones parciales que deben correlacionarse con reloj, contexto y causalidad.
- [OpenTelemetry — Logs data model](https://opentelemetry.io/docs/specs/otel/logs/data-model/) — delimita el contrato técnico que debe cumplirse al usar logs como observaciones parciales que deben correlacionarse con reloj, contexto y causalidad.

---

[↑ Glosario](../../README.md) · [← Heartbeat](./heartbeat.md) · [Hecho observado →](./hecho-observado.md)
