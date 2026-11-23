# Daemon/servicio

[↑ Glosario](../../README.md) · [← CVSS](../c/cvss.md) · [Daño →](./dano.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Proceso no interactivo administrado bajo una política de ciclo de vida.

Definición de trabajo de [SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md).

## Por qué importa

La clase donde se define, [SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md), existe con este propósito: la clase existe para modelar ciclo de vida, señales, supervisión y reinicio de procesos y servicios.

## Cómo funciona

[SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: consulta la clase para el mecanismo completo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md):

Un servicio reinicia cada segundo porque la configuración es inválida. Limitar reintentos y conservar el primer error evita saturación; corregir la configuración resuelve la causa. Aumentar prioridad o matar instancias repetidamente no lo hace.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md)) son:

- **Se mata un PID copiado minutos antes** — causa: el PID se trató como identidad permanente. Corrección: revalidar ejecutable, propietario e inicio antes de actuar.
- **CPU baja se interpreta como bloqueo** — causa: se ignoró espera útil. Corrección: correlacionar estado, tiempo, E/S y progreso funcional.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md)) son: No hacemos depuración de kernel ni análisis forense de memoria. La observabilidad disponible depende de permisos y plataforma. La próxima clase estudia la interfaz más común para coordinar procesos: terminal, shell, flujos y códigos de salida.

## Relación con otros conceptos

- **Prerrequisito:** [Proceso](../p/proceso.md).
- **Ver también:** [Ciclo de vida](../c/ciclo-de-vida.md), [Ciclo](../c/ciclo.md), [Código de salida](../c/codigo-de-salida.md), [Espera](../e/espera.md), [Hilo](../h/hilo.md), [Idempotencia](../i/idempotencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-221](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md), [SE-223](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md), [SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The Open Group — Process Concepts](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap03.html) — define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas.
- [Microsoft Learn — Processes and Threads](https://learn.microsoft.com/windows/win32/procthread/processes-and-threads) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.
- [systemd.service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html) — define ciclo de vida, supervisión o consulta de eventos en systemd.
- [Microsoft Learn — Services](https://learn.microsoft.com/windows/win32/services/services) — documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX.

---

[↑ Glosario](../../README.md) · [← CVSS](../c/cvss.md) · [Daño →](./dano.md)
