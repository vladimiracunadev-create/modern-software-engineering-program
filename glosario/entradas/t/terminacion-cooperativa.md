# Terminación cooperativa

[↑ Glosario](../../README.md) · [← Terminación](./terminacion.md) · [Terminación en falso →](./terminacion-en-falso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Solicitud que permite al programa cerrar ordenadamente.

Definición de trabajo de [SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md).

## Por qué importa

La clase donde se define, [SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md), existe con este propósito: la clase existe para modelar ciclo de vida, señales, supervisión y reinicio de procesos y servicios.

## Cómo funciona

Según [SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md):

La terminación cooperativa permite dejar de aceptar trabajo, finalizar operaciones y liberar recursos. La terminación forzada reduce esa oportunidad. El código de salida comunica una categoría de resultado al proceso padre; no sustituye un diagnóstico detallado, pero forma parte del contrato.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md):

Un servicio reinicia cada segundo porque la configuración es inválida. Limitar reintentos y conservar el primer error evita saturación; corregir la configuración resuelve la causa. Aumentar prioridad o matar instancias repetidamente no lo hace.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md)) son:

- **Se mata un PID copiado minutos antes** — causa: el PID se trató como identidad permanente. Corrección: revalidar ejecutable, propietario e inicio antes de actuar.
- **CPU baja se interpreta como bloqueo** — causa: se ignoró espera útil. Corrección: correlacionar estado, tiempo, E/S y progreso funcional.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md)) son: No hacemos depuración de kernel ni análisis forense de memoria. La observabilidad disponible depende de permisos y plataforma. La próxima clase estudia la interfaz más común para coordinar procesos: terminal, shell, flujos y códigos de salida.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Código de salida](../c/codigo-de-salida.md), [Daemon/servicio](../d/daemon-servicio.md), [Espera](../e/espera.md), [Hilo](../h/hilo.md), [Idempotencia](../i/idempotencia.md), [PID](../p/pid.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The Open Group — Process Concepts](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap03.html) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [Microsoft Learn — Processes and Threads](https://learn.microsoft.com/windows/win32/procthread/processes-and-threads) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [systemd.service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html) — define ciclo de vida, supervisión o consulta de eventos en systemd.
- [Microsoft Learn — Services](https://learn.microsoft.com/windows/win32/services/services) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.

---

[↑ Glosario](../../README.md) · [← Terminación](./terminacion.md) · [Terminación en falso →](./terminacion-en-falso.md)
