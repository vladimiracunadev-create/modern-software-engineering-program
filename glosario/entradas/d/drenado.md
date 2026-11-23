# Drenado

[↑ Glosario](../../README.md) · [← Dossier defendible](./dossier-defendible.md) · [Drenaje →](./drenaje.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Fase en que un servicio deja de aceptar trabajo nuevo y termina el que tiene.

Definición de trabajo de [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md).

## Por qué importa

La clase donde se define, [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md), existe con este propósito: la clase existe para diseñar un proceso que vive mucho tiempo —un servicio o daemon— con un ciclo de vida explícito: cómo arranca, cuándo está preparado, cómo se le pide que termine, qué hace al recibir esa petición y cómo se reinicia sin convertir un fallo de arranque en una avalancha.

## Cómo funciona

Según [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md):

Cumplen el mismo propósito con mecanismos distintos: el gestor de servicios de Windows envía órdenes de control (parar, pausar) en lugar de señales. La lógica de drenado es la misma; la forma de recibir la orden cambia.

## Ejemplo

Ejemplo de [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md) (sección «Caso conductor»):

La herramienta `notas` es el caso conductor de la [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md). Esta clase la convierte en un servicio con estados, sondas, drenado y reinicio con espera. `SE-223` añade lo que ese servicio hace por dentro: planificadores, trabajadores y lotes. Cambia después un solo detalle, el retardo de calentamiento de 0,8 s a 3 s, y revisa qué sonda, qué plazo y qué documentación dependían del valor anterior.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md)) son:

- **Fallan peticiones tras cada despliegue** — causa: se envía tráfico antes de que el servicio esté preparado. Corrección: sonda de preparación que prueba lo mismo que el cliente.
- **Un archivo queda truncado al detener el servicio** — causa: la terminación fue forzada o el manejador no vació. Corrección: cierre ordenado y escritura en archivo temporal.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md)) son: Las definiciones son operativas para la herramienta `notas`. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2): la terminación difirió por sistema, la ventana de preparación coincidió salvo una petición y la simulación fue idéntica. No se usó ningún gestor de servicios ni orquestador; los retardos y los tiempos de espera son supuestos del autor. La siguiente clase pregunta qué hace el servicio por dentro cuando debe programar y repartir trabajo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-221](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Servicio](../s/servicio.md), [Trabajo](../t/trabajo.md), [Dispersión](./dispersion.md), [Sonda de actividad](../s/sonda-de-actividad.md), [Sonda de preparación](../s/sonda-de-preparacion.md), [Terminación](../t/terminacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [systemd.service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html) — tipos de servicio, reinicio y plazos de parada; autoridad: proyecto systemd.
- [Kubernetes: sondas de actividad, preparación e inicio](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) — diferencia entre vivo y preparado; autoridad: documentación de Kubernetes.
- [Microsoft: Services](https://learn.microsoft.com/en-us/windows/win32/services/services) — servicios de Windows y su control; autoridad: Microsoft Learn.
- [Python: `signal`](https://docs.python.org/3/library/signal.html) — señales disponibles por sistema; autoridad: documentación de Python.
- [The Twelve-Factor App: Disposability](https://12factor.net/disposability) — arranque rápido y parada limpia; autoridad: guía de autores, de uso extendido.

---

[↑ Glosario](../../README.md) · [← Dossier defendible](./dossier-defendible.md) · [Drenaje →](./drenaje.md)
