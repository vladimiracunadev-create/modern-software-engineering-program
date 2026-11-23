# Sonda de preparación

[↑ Glosario](../../README.md) · [← Sonda de actividad](./sonda-de-actividad.md) · [Sonda de resiliencia →](./sonda-de-resiliencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Comprobación que decide si el servicio puede recibir tráfico.

Definición de trabajo de [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md).

## Por qué importa

La clase donde se define, [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md), existe con este propósito: la clase existe para diseñar un proceso que vive mucho tiempo —un servicio o daemon— con un ciclo de vida explícito: cómo arranca, cuándo está preparado, cómo se le pide que termine, qué hace al recibir esa petición y cómo se reinicia sin convertir un fallo de arranque en una avalancha.

## Cómo funciona

Según [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md):

Al recibir la petición de parada, un servicio ordenado deja de aceptar trabajo (la sonda de preparación pasa a fallar), termina lo que está en curso dentro de un plazo, vacía lo pendiente (búferes, colas, archivos temporales) y sale con un código. Un plazo demasiado corto trunca trabajo; uno demasiado largo retrasa los despliegues. El plazo se calcula con la duración del trabajo más largo que se acepta y se mide, no se supone.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md):

`notas servir` tiene cuatro estados (arrancando, preparado, drenando, detenido) y publica una ruta `/listo` que responde 200 solo cuando la configuración está cargada y el almacenamiento accesible, y otra `/vivo` que no consulta nada externo. Al recibir `SIGTERM` (Linux) o `CTRL_BREAK_EVENT` (Windows), la ruta `/listo` empieza a devolver 503, el servicio termina las exportaciones en curso durante un plazo de 20 s (el máximo observado más un margen), vacía sus archivos temporales y sale con 0 o con 75 si venció el plazo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Fallan peticiones tras cada despliegue** — causa: se envía tráfico antes de que el servicio esté preparado. Corrección: sonda de preparación que prueba lo mismo que el cliente. ([SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Al recibir la petición de parada, un servicio ordenado deja de aceptar trabajo (la sonda de preparación pasa a fallar), termina lo que está en curso dentro de un plazo, vacía lo pendiente (búferes, colas, archivos temporales) y sale con un código. ([SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-221](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Servicio](./servicio.md), [Dispersión](../d/dispersion.md), [Drenado](../d/drenado.md), [Sonda de actividad](./sonda-de-actividad.md), [Terminación](../t/terminacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

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

[↑ Glosario](../../README.md) · [← Sonda de actividad](./sonda-de-actividad.md) · [Sonda de resiliencia →](./sonda-de-resiliencia.md)
