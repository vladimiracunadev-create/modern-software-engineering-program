# Diferencias de plataforma

[↑ Glosario](../../README.md) · [← Diario de pasos](./diario-de-pasos.md) · [Difusión por rumor →](./difusion-por-rumor.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Windows y Linux no ofrecen las mismas señales.

Es uno de los temas de [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md), donde se enseña como «Diferencias de plataforma».

## Por qué importa

En [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md), el tema «Diferencias de plataforma» importa porque windows y Linux no ofrecen las mismas señales.

En [SE-224 — Automatización idempotente y reanudable](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md), el tema «Diferencias de plataforma» importa porque el reemplazo no se comporta igual en Windows y Linux.

## Cómo funciona

[SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la herramienta `notas`. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md):

`notas servir` tiene cuatro estados (arrancando, preparado, drenando, detenido) y publica una ruta `/listo` que responde 200 solo cuando la configuración está cargada y el almacenamiento accesible, y otra `/vivo` que no consulta nada externo. Al recibir `SIGTERM` (Linux) o `CTRL_BREAK_EVENT` (Windows), la ruta `/listo` empieza a devolver 503, el servicio termina las exportaciones en curso durante un plazo de 20 s (el máximo observado más un margen), vacía sus archivos temporales y sale con 0 o con 75 si venció el plazo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md)) son:

- **Fallan peticiones tras cada despliegue** — causa: se envía tráfico antes de que el servicio esté preparado. Corrección: sonda de preparación que prueba lo mismo que el cliente.
- **Un archivo queda truncado al detener el servicio** — causa: la terminación fue forzada o el manejador no vació. Corrección: cierre ordenado y escritura en archivo temporal.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md)) son: Las definiciones son operativas para la herramienta `notas`. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2): la terminación difirió por sistema, la ventana de preparación coincidió salvo una petición y la simulación fue idéntica. No se usó ningún gestor de servicios ni orquestador; los retardos y los tiempos de espera son supuestos del autor. La siguiente clase pregunta qué hace el servicio por dentro cuando debe programar y repartir trabajo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-221](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Clave de idempotencia](../c/clave-de-idempotencia.md), [Dispersión](./dispersion.md), [Drenado](./drenado.md), [Entrega al menos una vez / como máximo una vez](../e/entrega-al-menos-una-vez-como-maximo-una-vez.md), [Escritura atómica](../e/escritura-atomica.md), [Idempotencia](../i/idempotencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-222 — Daemons, servicios y ciclo de vida](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-224 — Automatización idempotente y reanudable](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), [SE-029](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md), [SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md), [SE-113](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-113-cli-flags-configuracion-y-codigos-de-salida/README.md), [SE-522](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md), [SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md).

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

[↑ Glosario](../../README.md) · [← Diario de pasos](./diario-de-pasos.md) · [Difusión por rumor →](./difusion-por-rumor.md)
