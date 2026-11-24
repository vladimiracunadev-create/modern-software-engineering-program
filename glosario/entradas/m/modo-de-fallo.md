# Modo de fallo

[↑ Glosario](../../README.md) · [← Modelo sintáctico y semántico](./modelo-sintactico-y-semantico.md) · [Modo degradado →](./modo-degradado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

En el diseño de controles de agentes, el **modo de fallo** es el comportamiento de un control cuando no puede decidir: **abrirse** (dejar pasar) o **cerrarse** (bloquear). Es la definición de [SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md). (En análisis de peligros, «modo de fallo» también designa la forma en que falla un componente, como en el FMEA que menciona [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md).)

## Por qué importa

Todo control tiene dos modos de fallo y ninguno es correcto en general. Un control que protege un recurso irrecuperable debe fallar cerrado, y aceptar la molestia de bloquear cuando se rompe; uno de conveniencia (un formateador, un aviso) puede fallar abierto.

## Cómo funciona

La decisión se toma para cada gancho, se escribe y se prueba, incluidos los casos de caída, de excepción y de tiempo agotado, porque son los que ejercitan el modo de fallo. Una forma sencilla ([SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md)): el gancho termina con éxito solo cuando completó la comprobación y decidió permitir; con otro código bloquea; y cualquier otro resultado se interpreta en la capa que lo invoca como bloqueo.

## Ejemplo

[SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md) (escenario hipotético): el equipo de *Avisos* escribe un gancho que termina con 0 solo si comprobó y permite y con 2 cuando bloquea; lo prueba como proceso con cuatro eventos de simulación (caída, tiempo agotado, entrada vacía, JSON inválido) y comprueba que ninguna acción peligrosa llega a ejecutarse.

## Errores y confusiones comunes

**El control «no hace nada» y no hay error.** Falla abierto: el error del gancho no bloquea; usar el código de bloqueo para la política y probar la caída.

## Límites y cuándo no aplica

Fallar cerrado tiene costo de disponibilidad: si el control se cae con frecuencia, bloquea trabajo legítimo. Se decide por el daño del peor caso en cada control.

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
