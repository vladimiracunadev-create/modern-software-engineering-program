# Minimización

[↑ Glosario](../../README.md) · [← Minificación](./minificacion.md) · [Minimización de datos →](./minimizacion-de-datos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Principio de recoger y conservar solo los datos necesarios para una finalidad declarada.

Definición de trabajo de [SE-358 — Privacidad, retención y ciclo de vida del dato](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-137 — Telemetría de producto y consentimiento](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md): Recoger solo los datos, el tiempo y la granularidad que una decisión necesita.

## Por qué importa

En [SE-033 — Logs del sistema y diagnóstico de fallos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md), el tema «Minimización» importa porque selecciona y redacta antes de persistir

## Cómo funciona

Según [SE-358 — Privacidad, retención y ciclo de vida del dato](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md):

El primer paso es una lista de qué datos personales hay, para qué se recogen (la **finalidad**), quién accede, cuánto tiempo se conservan y en qué lugares viven: base, índices, cachés, respaldos, registros, exportaciones. La **minimización** pregunta si hace falta cada dato: el que no se recoge no se puede filtrar ni hay que borrarlo. En la plataforma, el correo es necesario para el acceso; la fecha de nacimiento completa quizá no, y un rango de edad podría bastar. Cada dato que se añade al esquema debería llegar con su finalidad escrita; el inventario es un artefacto vivo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-033 — Logs del sistema y diagnóstico de fallos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md):

Un servicio presenta latencia y errores coincidentes con presión de disco. El equipo compara operaciones con y sin presión y conserva una hipótesis rival de dependencia externa. La correlación orienta el experimento; no se publica como causalidad cerrada.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-033 — Logs del sistema y diagnóstico de fallos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md)) son:

- **Hay mucho log pero no se relacionan eventos** — causa: faltan identificadores y estructura. Corrección: añadir eventos estables y correlación por operación.
- **Se culpa al evento anterior** — causa: se confundió proximidad con causalidad. Corrección: formular alternativas y diseñar una prueba discriminante.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **minimización** pregunta si hace falta cada dato: el que no se recoge no se puede filtrar ni hay que borrarlo. ([SE-358](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md), [SE-031](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Granularidad](../g/granularidad.md), [Consentimiento](../c/consentimiento.md), [Correlación](../c/correlacion.md), [Evento](../e/evento.md), [Evento de telemetría](../e/evento-de-telemetria.md), [Hecho](../h/hecho.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-033 — Logs del sistema y diagnóstico de fallos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-137 — Telemetría de producto y consentimiento](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.
- [SE-358 — Privacidad, retención y ciclo de vida del dato](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (28 clases más lo mencionan; las que más):

[SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md), [SE-463](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-463-privacidad-por-diseno-y-minimizacion/README.md), [SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md), [SE-046](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md), [SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md), [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md), [SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md), [SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Reglamento (UE) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — principios de minimización, limitación del plazo y supresión; autoridad: texto oficial de la Unión Europea.
- [Microsoft Learn — Event Logging](https://learn.microsoft.com/windows/win32/eventlog/event-logging) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [systemd — journalctl](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html) — define ciclo de vida, supervisión o consulta de eventos en systemd.
- [Apple Developer — Logging](https://developer.apple.com/documentation/os/logging) — delimita el contrato técnico que debe cumplirse al usar logs como observaciones parciales que deben correlacionarse con reloj, contexto y causalidad.
- [OpenTelemetry — Logs data model](https://opentelemetry.io/docs/specs/otel/logs/data-model/) — delimita el contrato técnico que debe cumplirse al usar logs como observaciones parciales que deben correlacionarse con reloj, contexto y causalidad.

---

[↑ Glosario](../../README.md) · [← Minificación](./minificacion.md) · [Minimización de datos →](./minimizacion-de-datos.md)
