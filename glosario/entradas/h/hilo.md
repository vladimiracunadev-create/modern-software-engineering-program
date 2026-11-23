# Hilo

[↑ Glosario](../../README.md) · [← HIL](./hil.md) · [Hipervisor →](./hipervisor.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Secuencia planificable dentro de un proceso.

Definición de trabajo de [SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md): Flujo de ejecución planificable dentro de un proceso.

## Por qué importa

En [SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), el tema «Hilo» importa porque comparte proceso y mantiene ejecución

## Cómo funciona

Según [SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md):

Hilos de un proceso comparten memoria y recursos, pero mantienen pila y estado de ejecución propios. Compartir reduce copia y permite trabajo concurrente; introduce carreras, orden y necesidad de sincronización. Más hilos agregan overhead y no crean núcleos.

Según [SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md):

Un servidor atiende muchas conexiones con I/O asíncrono para evitar un hilo bloqueado por conexión. Si el cuello es cálculo, se consideran procesos o trabajo vectorizado, siempre midiendo costos de coordinación.

## Ejemplo

Ejemplo de [SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md) (sección «Ejemplo mínimo»):

`time.sleep()` aumenta tiempo de pared casi sin aumentar CPU: el hilo espera. Un bucle numérico aumenta ambos y añadir hilos de CPython no garantiza paralelismo de bytecode.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **hilos duplican velocidad** — causa: concurrencia = paralelismo. Corrección: identifica carga, núcleos y runtime. ([SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Más hilos agregan overhead y no crean núcleos. ([SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md))
- Actualiza un contador compartido desde hilos sin contrato. ([SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md), [SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Flujo](../f/flujo.md), [Proceso](../p/proceso.md), [Secuencia](../s/secuencia.md), [Código de salida](../c/codigo-de-salida.md), [Concurrencia](../c/concurrencia.md), [Daemon/servicio](../d/daemon-servicio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-019 — Procesos, hilos, interrupciones y entrada/salida](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

**También se usa en** (78 clases más lo mencionan; las que más):

[SE-280](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md), [SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md), [SE-305](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md), [SE-223](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md), [SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md), [SE-081](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md), [SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md), [SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Slack](../../../casos/exito/slack.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The Open Group — Process Concepts](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap03.html) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [Microsoft Learn — Processes and Threads](https://learn.microsoft.com/windows/win32/procthread/processes-and-threads) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [systemd.service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html) — define ciclo de vida, supervisión o consulta de eventos en systemd.
- [Microsoft Learn — Services](https://learn.microsoft.com/windows/win32/services/services) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.

---

[↑ Glosario](../../README.md) · [← HIL](./hil.md) · [Hipervisor →](./hipervisor.md)
