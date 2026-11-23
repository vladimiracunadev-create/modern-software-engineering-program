# Modo de fallo

[↑ Glosario](../../README.md) · [← Modelo sintáctico y semántico](./modelo-sintactico-y-semantico.md) · [Modo degradado →](./modo-degradado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Comportamiento de un control cuando no puede decidir: abrirse (dejar pasar) o cerrarse (bloquear).

Definición de trabajo de [SE-570 — Skills, plugins, hooks y entornos aislados](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md).

## Por qué importa

En [SE-570 — Skills, plugins, hooks y entornos aislados](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md), el tema «Modo de fallo» importa porque un control que falla abierto es un control ausente.

En [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md), el tema «Modos de fallo» importa porque permite anticipar la confabulación, la omisión silenciosa y la inconsistencia

## Cómo funciona

Según [SE-570 — Skills, plugins, hooks y entornos aislados](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md):

Todo control tiene dos modos de fallo. **Falla abierto**: si no puede decidir, deja pasar. **Falla cerrado**: si no puede decidir, bloquea. Ninguno es correcto en general. Un control que protege un recurso irrecuperable debe fallar cerrado, y aceptar la molestia de bloquear cuando se rompe. Un control de conveniencia (un formateador, un aviso) puede fallar abierto. La decisión se toma para cada gancho, se escribe y se prueba, incluyendo los casos de caída, de excepción y de tiempo agotado, porque son los que ejercitan el modo de fallo. Una forma sencilla de hacerlo es que el gancho termine con éxito **solo** cuando ha completado la comprobación y ha decidido permitir, y que cualquier otro resultado se trate como bloqueo en la capa que lo invoca.

Según [SE-570 — Skills, plugins, hooks y entornos aislados](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* revisa sus controles. Escribe el gancho de política con tres decisiones explícitas: termina con 0 solo cuando ha comprobado y permite, con 2 cuando bloquea, y cualquier otro resultado se interpreta en la capa que lo invoca como bloqueo, para lo cual añade una regla de denegación de las órdenes que el gancho vigila como segunda barrera. Prueba el gancho como proceso con cuatro eventos de simulación (caída, tiempo agotado, entrada vacía y JSON inválido) y comprueba que ninguna acción peligrosa llega a ejecutarse. Reduce las habilidades cargadas al arrancar a las seis que usa el proyecto, reescribe sus descripciones con frases de activación y quita el solape entre dos de ellas.

## Ejemplo

Ejemplo de [SE-570 — Skills, plugins, hooks y entornos aislados](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* revisa sus controles. Escribe el gancho de política con tres decisiones explícitas: termina con 0 solo cuando ha comprobado y permite, con 2 cuando bloquea, y cualquier otro resultado se interpreta en la capa que lo invoca como bloqueo, para lo cual añade una regla de denegación de las órdenes que el gancho vigila como segunda barrera. Prueba el gancho como proceso con cuatro eventos de simulación (caída, tiempo agotado, entrada vacía y JSON inválido) y comprueba que ninguna acción peligrosa llega a ejecutarse.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-570 — Skills, plugins, hooks y entornos aislados](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md)) son:

- **El control «no hace nada» y no hay error** — causa: falla abierto: el error del gancho no bloquea. Corrección: usar el código de bloqueo para la política y probar la caída.
- **El agente carga mucho contexto al arrancar** — causa: todas las habilidades completas en memoria. Corrección: cargar descripciones y cuerpos bajo demanda.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-570 — Skills, plugins, hooks y entornos aislados](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md)) son: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos salvo la lectura de reloj: el gancho se ejecuta como proceso real y la comprobación de rutas es código real sobre cadenas; la carga de habilidades usa archivos sintéticos y una selección por palabras clave.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-540](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Control](../c/control.md), [Calibración](../c/calibracion.md), [Confabulación](../c/confabulacion.md), [Confinamiento de rutas](../c/confinamiento-de-rutas.md), [Entorno aislado](../e/entorno-aislado.md), [Extensión](../e/extension.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.
- [SE-570 — Skills, plugins, hooks y entornos aislados](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (18 clases más lo mencionan; las que más):

[SE-539](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-539-taller-conducir-una-revision-de-decision-dificil/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), [SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md), [SE-601](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-601-ciclo-de-vida-de-ml-y-por-que-falla-en-produccion/README.md), [SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md), [SE-338](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md), [SE-482](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-482-pipelines-jobs-matrices-y-caches/README.md).

**Aparece en los casos de estudio:** [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Modos de fallo».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Claude Code: ganchos](https://code.claude.com/docs/en/hooks) — entrada, códigos de salida, errores que no bloquean y tiempos máximos; autoridad: documentación de Anthropic.
- [Claude Code: habilidades](https://code.claude.com/docs/en/skills) — estructura de una habilidad, carga bajo demanda y presupuesto de descripciones; autoridad: documentación de Anthropic.
- [Claude Code: subagentes](https://code.claude.com/docs/en/sub-agents) — herramientas y ganchos por subagente; autoridad: documentación de Anthropic.
- [Claude Code: aislamiento (sandbox)](https://code.claude.com/docs/en/sandboxing) — aislamiento de sistema de archivos y red; autoridad: documentación de Anthropic.
- [Spec Kit — repositorio](https://github.com/github/spec-kit) — extensiones y catálogos, con la advertencia de revisar el código de la comunidad; autoridad: GitHub y mantenedores.

---

[↑ Glosario](../../README.md) · [← Modelo sintáctico y semántico](./modelo-sintactico-y-semantico.md) · [Modo degradado →](./modo-degradado.md)
