# Espera

[↑ Glosario](../../README.md) · [← Especificidad](./especificidad.md) · [Espera exponencial con aleatoriedad →](./espera-exponencial-con-aleatoriedad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Estado en que el progreso depende de un evento o recurso.

Definición de trabajo de [SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md).

## Por qué importa

En [SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md), el tema «Planificación» importa porque alterna unidades listas y esperas

## Cómo funciona

Según [SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md):

Muestrear CPU, memoria y espera a lo largo del tiempo aporta más que una captura. La medición altera algo el sistema y debe interpretarse junto con trabajo solicitado y duración.

Según [SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md):

En POSIX, es un proceso que ya terminó pero cuyo padre todavía no leyó su código de salida; ocupa una entrada en la tabla de procesos sin consumir CPU. Se resuelve cuando el padre llama a `wait` (o termina). Un servicio que lanza hijos y nunca los espera acumula zombis, un síntoma de un ciclo de vida mal diseñado.

## Ejemplo

Ejemplo de [SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md) (sección «Preguntas frecuentes»):

En POSIX, es un proceso que ya terminó pero cuyo padre todavía no leyó su código de salida; ocupa una entrada en la tabla de procesos sin consumir CPU. Se resuelve cuando el padre llama a `wait` (o termina). Un servicio que lanza hijos y nunca los espera acumula zombis, un síntoma de un ciclo de vida mal diseñado.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **CPU baja se interpreta como bloqueo** — causa: se ignoró espera útil. Corrección: correlacionar estado, tiempo, E/S y progreso funcional. ([SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md))
- **El servicio reinicia sin límite** — causa: se sustituyó recuperación por repetición. Corrección: clasificar fallo, aplicar espera creciente y cortar el bucle. ([SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Sirve para preguntar si el analizador local de eventos progresa, espera o terminó, no para adivinar internals del kernel. ([SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](./estado.md), [Evento](./evento.md), [Progreso](../p/progreso.md), [Recurso](../r/recurso.md), [Código de salida](../c/codigo-de-salida.md), [Daemon/servicio](../d/daemon-servicio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

**También se usa en** (236 clases más lo mencionan; las que más):

[SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md), [SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md), [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md), [SE-606](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md), [SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md), [SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md), [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-183](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The Open Group — Process Concepts](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap03.html) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [Microsoft Learn — Processes and Threads](https://learn.microsoft.com/windows/win32/procthread/processes-and-threads) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [systemd.service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html) — define ciclo de vida, supervisión o consulta de eventos en systemd.
- [Microsoft Learn — Services](https://learn.microsoft.com/windows/win32/services/services) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.

---

[↑ Glosario](../../README.md) · [← Especificidad](./especificidad.md) · [Espera exponencial con aleatoriedad →](./espera-exponencial-con-aleatoriedad.md)
