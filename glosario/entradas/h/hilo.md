# Hilo

[↑ Glosario](../../README.md) · [← HIL](./hil.md) · [Hipervisor →](./hipervisor.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Un **hilo** (*thread*) es una secuencia de ejecución planificable dentro de un proceso ([SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md)). Los hilos de un proceso comparten memoria y recursos, pero cada uno mantiene su pila y su estado de ejecución propios. Es la unidad que el planificador del sistema reparte entre los núcleos.

## Por qué importa

Permite hacer varias cosas dentro de un mismo programa sin copiar memoria, pero introduce el problema central de la programación concurrente: varios flujos tocando los mismos datos. La idea de que «más hilos son más velocidad» es un error clásico: [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md) recuerda que más hilos agregan *overhead* y no crean núcleos. La decisión que cambia es cuándo usar hilos, procesos o entrada/salida asíncrona.

## Cómo funciona

Compartir memoria reduce copia y permite trabajo concurrente, pero introduce **carreras**, dependencia del orden y necesidad de sincronización ([SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md)). Comparado con un proceso: un proceso tiene memoria virtual propia; un hilo comparte la del proceso. El sistema operativo interrumpe y cambia de hilo; cada cambio tiene costo. La causa de que muchos hilos no ayuden es que la CPU solo ejecuta tantos hilos a la vez como núcleos tiene, y el resto espera turno.

La alternativa depende de dónde está el cuello: si el programa espera entrada/salida (muchas conexiones), un servidor atiende con E/S asíncrona para evitar un hilo bloqueado por conexión; si el cuello es cálculo, se consideran procesos o trabajo vectorizado, siempre midiendo costos de coordinación ([SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md)).

## Ejemplo

```python
n = 0
def inc():
    global n
    for _ in range(100_000): n += 1     # lectura-modificación-escritura sin exclusión

hilos = [threading.Thread(target=inc) for _ in range(4)]
```

El resultado puede ser menor que 400 000 porque las actualizaciones se pisan: es el contador compartido sin contrato que [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md) usa para mostrar una carrera.

## Errores y confusiones comunes

- **«Los hilos duplican la velocidad».** Causa: concurrencia igualada a paralelismo; corrección: identificar carga, núcleos y runtime ([SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md)).
- **Compartir estado mutable sin sincronización.** Produce resultados distintos en cada ejecución.
- **Confundir hilo con proceso.** El proceso aísla memoria; el hilo la comparte.

## Límites y cuándo no aplica

Los hilos no ayudan cuando el cuello es un solo recurso secuencial, y en algunos runtimes un bloqueo global del intérprete limita el paralelismo de cálculo en hilos. La sincronización excesiva puede anular el beneficio. Y para aislar fallos o código no confiable, los hilos no sirven: un fallo en un hilo puede derribar el proceso entero.

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

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Slack](../../../casos/exito/slack.md), [Cloudflare](../../../casos/exito/cloudflare.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [Therac-25](../../../casos/fallo/therac-25.md).

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
