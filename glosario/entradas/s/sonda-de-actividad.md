# Sonda de actividad

[↑ Glosario](../../README.md) · [← Sonda](./sonda.md) · [Sonda de preparación →](./sonda-de-preparacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Comprobación que decide si el proceso debe reiniciarse.

Definición de trabajo de [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md).

## Por qué importa

La clase donde se define, [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md), existe con este propósito: la clase existe para diseñar un proceso que vive mucho tiempo —un servicio o daemon— con un ciclo de vida explícito: cómo arranca, cuándo está preparado, cómo se le pide que termine, qué hace al recibir esa petición y cómo se reinicia sin convertir un fallo de arranque en una avalancha.

## Cómo funciona

Según [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md):

Una **sonda de actividad** responde «¿sigo vivo o debo reiniciarme?»; una de **preparación** responde «¿puedo atender ahora?». Un proceso recién arrancado está vivo pero no preparado: abre el puerto, carga datos, calienta cachés. Si el balanceador envía tráfico al abrirse el puerto, las primeras peticiones fallan. La regla de las sondas: la de preparación comprueba lo mismo que hará el cliente (una petición real, de bajo costo) y la de actividad comprueba lo mínimo para decidir un reinicio, sin depender de servicios externos, porque un reinicio no arregla una base de datos caída.

Según [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md):

Porque el reinicio solo arregla fallos del propio proceso. Si la sonda depende de un servicio externo caído, reiniciar no ayuda y multiplica la carga cuando el externo vuelve. La sonda de actividad debe depender solo del proceso.

## Ejemplo

Ejemplo de [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md) (sección «Preguntas frecuentes»):

Porque el reinicio solo arregla fallos del propio proceso. Si la sonda depende de un servicio externo caído, reiniciar no ayuda y multiplica la carga cuando el externo vuelve. La sonda de actividad debe depender solo del proceso.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se reinicia por una caída de la base de datos** — causa: la sonda de actividad depende de un recurso externo. Corrección: limitarla al propio proceso. ([SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La sonda de actividad debe depender solo del proceso. ([SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-221](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Proceso](../p/proceso.md), [Dispersión](../d/dispersion.md), [Drenado](../d/drenado.md), [Servicio](./servicio.md), [Sonda de preparación](./sonda-de-preparacion.md), [Terminación](../t/terminacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Kubernetes: sondas de actividad, preparación e inicio](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) — diferencia entre vivo y preparado; autoridad: documentación de Kubernetes.
- [systemd.service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html) — tipos de servicio, reinicio y plazos de parada; autoridad: proyecto systemd.
- [Microsoft: Services](https://learn.microsoft.com/en-us/windows/win32/services/services) — servicios de Windows y su control; autoridad: Microsoft Learn.
- [Python: `signal`](https://docs.python.org/3/library/signal.html) — señales disponibles por sistema; autoridad: documentación de Python.
- [The Twelve-Factor App: Disposability](https://12factor.net/disposability) — arranque rápido y parada limpia; autoridad: guía de autores, de uso extendido.

---

[↑ Glosario](../../README.md) · [← Sonda](./sonda.md) · [Sonda de preparación →](./sonda-de-preparacion.md)
