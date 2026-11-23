# Estado inicial

[↑ Glosario](../../README.md) · [← Estado inalcanzable](./estado-inalcanzable.md) · [Estado limpio →](./estado-limpio.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Conjunto mínimo de condiciones antes de intervenir.

Definición de trabajo de [SE-035 — Taller: preparar y reparar un entorno reproducible](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md).

## Por qué importa

La clase donde se define, [SE-035 — Taller: preparar y reparar un entorno reproducible](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md), existe con este propósito: la clase existe para preparar, romper, diagnosticar y restaurar un entorno desde un runbook verificable.

## Cómo funciona

[SE-035 — Taller: preparar y reparar un entorno reproducible](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-035 — Taller: preparar y reparar un entorno reproducible](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md):

Una dependencia incompatible aparece después de corregir configuración. El equipo no deshace la primera conclusión: registra dos causas encadenadas, aísla la versión por proyecto y prueba ambos escenarios por separado.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-035 — Taller: preparar y reparar un entorno reproducible](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md)) son:

- **Se borra y reinstala al comienzo** — causa: se destruyó evidencia antes de formular hipótesis. Corrección: capturar y reproducir primero.
- **Varias cosas cambian a la vez** — causa: no puede atribuirse el resultado. Corrección: un cambio mínimo, medir y revertir si no explica.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-035 — Taller: preparar y reparar un entorno reproducible](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md)) son: El escenario es local, deliberadamente controlado y no autoriza intervenir equipos de terceros. La clase final convierte el procedimiento en un producto pequeño: el kit de diagnóstico multiplataforma, con contrato, adaptadores, pruebas y entrega profesional.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md), [SE-034](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-034-virtualizacion-wsl-y-aislamiento-local/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Conjunto](../c/conjunto.md), [Cambio mínimo](../c/cambio-minimo.md), [Hipótesis discriminante](../h/hipotesis-discriminante.md), [Hipótesis rival](../h/hipotesis-rival.md), [Prueba discriminante](../p/prueba-discriminante.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-035 — Taller: preparar y reparar un entorno reproducible](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

**También se usa en** (48 clases más lo mencionan; las que más):

[SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md), [SE-573](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md), [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md), [SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md), [SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md), [SE-023](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md), [SE-073](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md), [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Microsoft Learn — Sysinternals documentation](https://learn.microsoft.com/sysinternals/) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [The Open Group Base Specifications, Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [systemd manual pages](https://www.freedesktop.org/software/systemd/man/latest/) — define ciclo de vida, supervisión o consulta de eventos en systemd.
- [Python documentation — subprocess](https://docs.python.org/3/library/subprocess.html) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Estado inalcanzable](./estado-inalcanzable.md) · [Estado limpio →](./estado-limpio.md)
