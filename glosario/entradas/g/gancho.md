# Gancho

[↑ Glosario](../../README.md) · [← Ganancia de información](./ganancia-de-informacion.md) · [Gap →](./gap.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Función que el sistema invoca al cambiar el estado de la aplicación y que dispone de un plazo limitado y no siempre garantizado.

Definición de trabajo de [SE-254 — Ciclo de vida, suspensión y reanudación](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-570 — Skills, plugins, hooks y entornos aislados](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md): Programa que el agente invoca en un punto fijo de su bucle, con el evento como entrada y un código de salida como respuesta.

## Por qué importa

En [SE-254 — Ciclo de vida, suspensión y reanudación](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md), el tema «Ganchos y plazos» importa porque un gancho que no se ejecuta, o que se ejecuta con un plazo corto, no es un lugar fiable donde guardar todo.

## Cómo funciona

Según [SE-254 — Ciclo de vida, suspensión y reanudación](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md):

Los ganchos de pausa y de paso a segundo plano son avisos de que la aplicación dejará de ejecutarse pronto. La documentación de Android advierte que no se debe confiar en que ciertos métodos se invoquen antes de terminar el proceso. Un plazo implícito significa que el gancho debe hacer poco y hacerlo rápido: guardar un estado pequeño, no sincronizar con un servidor. Lo largo se hace antes, de forma incremental.

Según [SE-254 — Ciclo de vida, suspensión y reanudación](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md):

El equipo del cliente define la política de guardado en una tabla con tres columnas: qué estado (borrador, adjuntos pendientes, posición), cuándo se guarda (al editar tras una pausa de un segundo, al pasar a segundo plano) y cómo se restaura (con la versión de formato en el archivo). La restauración se prueba con un estado de cada versión anterior almacenado en el repositorio, y el arranque en frío se fuerza en las pruebas de integración. El guardado en el gancho solo escribe el borrador; los adjuntos se suben antes.

## Ejemplo

Ejemplo de [SE-254 — Ciclo de vida, suspensión y reanudación](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md) (sección «Ejemplo profesional»):

El equipo del cliente define la política de guardado en una tabla con tres columnas: qué estado (borrador, adjuntos pendientes, posición), cuándo se guarda (al editar tras una pausa de un segundo, al pasar a segundo plano) y cómo se restaura (con la versión de formato en el archivo). La restauración se prueba con un estado de cada versión anterior almacenado en el repositorio, y el arranque en frío se fuerza en las pruebas de integración. El guardado en el gancho solo escribe el borrador; los adjuntos se suben antes.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El gancho de pausa tarda y el sistema lo corta** — causa: guarda un estado grande o sincroniza con el servidor. Corrección: guardar solo lo mínimo en el gancho y el resto antes. ([SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md))
- **El control «no hace nada» y no hay error** — causa: falla abierto: el error del gancho no bloquea. Corrección: usar el código de bloqueo para la política y probar la caída. ([SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Los ganchos de pausa y de paso a segundo plano son avisos de que la aplicación dejará de ejecutarse pronto. ([SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md))
- El gancho puede no ejecutarse, tener poco tiempo o fallar; el 10 % de fallos supuesto deja a un tercio de las sesiones con pérdida. ([SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Código de salida](../c/codigo-de-salida.md), [Agente](../a/agente.md), [Estado](../e/estado.md), [Evento](../e/evento.md), [Ciclo de vida](../c/ciclo-de-vida.md), [Confinamiento de rutas](../c/confinamiento-de-rutas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-254 — Ciclo de vida, suspensión y reanudación](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-570 — Skills, plugins, hooks y entornos aislados](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-318](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md), [SE-109](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-109-biblioteca-framework-runtime-plataforma-y-sdk/README.md), [SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md), [SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md), [SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md), [SE-098](../../../classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md), [SE-100](../../../classes/part-08-entornos-herramientas-y-depuracion/se-100-compiladores-linters-formatters-y-analisis-estatico/README.md), [SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Claude Code: ganchos](https://code.claude.com/docs/en/hooks) — entrada, códigos de salida, errores que no bloquean y tiempos máximos; autoridad: documentación de Anthropic.
- [Claude Code: subagentes](https://code.claude.com/docs/en/sub-agents) — herramientas y ganchos por subagente; autoridad: documentación de Anthropic.
- [Android Developers, «The activity lifecycle»](https://developer.android.com/guide/components/activities/activity-lifecycle) — estados y transiciones de una actividad; autoridad: Google.
- [Android Developers, «Save UI states»](https://developer.android.com/topic/libraries/architecture/saving-states) — qué estado guardar y dónde; autoridad: Google.
- [Android Developers, «Processes and app lifecycle»](https://developer.android.com/guide/components/activities/process-lifecycle) — prioridad de procesos y cuándo el sistema los termina; autoridad: Google.

---

[↑ Glosario](../../README.md) · [← Ganancia de información](./ganancia-de-informacion.md) · [Gap →](./gap.md)
