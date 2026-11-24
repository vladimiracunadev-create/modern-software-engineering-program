# Habilidad

[↑ Glosario](../../README.md) · [← Guion de inyección](../g/guion-de-inyeccion.md) · [Hallazgo →](./hallazgo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Una **habilidad** (*skill*) es un conjunto de instrucciones, a veces con scripts y documentos de apoyo, empaquetado con una descripción, que el agente carga cuando la tarea lo pide. Es la definición de [SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md). En Claude Code, una habilidad es un directorio con un archivo `SKILL.md` cuyo encabezado incluye un nombre y una descripción.

## Por qué importa

Resuelve el problema de poner todo el conocimiento en el contexto de partida. El agente ve las descripciones de todas las habilidades y carga el cuerpo solo cuando decide que una es relevante o cuando la persona la invoca: es **carga progresiva**. La descripción es siempre visible y barata; el cuerpo es caro y solo entra cuando se usa.

## Cómo funciona

El mecanismo crea otro problema: la **selección** depende de la descripción. Una descripción vaga o solapada con otra hace que se active la habilidad equivocada o que ninguna se active. Por eso se escriben con frases de activación concretas («úsala cuando…») y se eliminan los solapes entre habilidades.

## Ejemplo

[SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md) (escenario hipotético, sin datos reales): el equipo de *Avisos* reduce las habilidades cargadas al arrancar a las seis que usa el proyecto, reescribe sus descripciones con frases de activación y quita el solape entre dos de ellas.

## Errores y confusiones comunes

- **El agente carga mucho contexto al arrancar.** Todas las habilidades completas en memoria; cargar descripciones y cuerpos bajo demanda.
- **Se activa la habilidad equivocada.** Descripciones vagas o solapadas; frases de activación y sin solapes.

## Límites y cuándo no aplica

Una habilidad es una instrucción, no un control: no impone nada. Lo que debe cumplirse siempre (bloquear una acción peligrosa) pertenece a un gancho de política o a un permiso, no a una habilidad que el agente puede no cargar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Agente](../a/agente.md), [Conjunto](../c/conjunto.md), [Empaquetado](../e/empaquetado.md), [Instrucción](../i/instruccion.md), [Confinamiento de rutas](../c/confinamiento-de-rutas.md), [Entorno aislado](../e/entorno-aislado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-570 — Skills, plugins, hooks y entornos aislados](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (99 clases más lo mencionan; las que más):

[SE-538](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-538-portafolio-entrevistas-y-defensa-profesional/README.md), [SE-082](../../../classes/part-06-paradigmas-de-programacion/se-082-seleccion-y-combinacion-responsable-de-paradigmas/README.md), [SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md), [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-320](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-320-resiliencia-timeout-retry-con-jitter-y-circuit-breaker/README.md), [SE-323](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md), [SE-539](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-539-taller-conducir-una-revision-de-decision-dificil/README.md), [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Claude Code: habilidades](https://code.claude.com/docs/en/skills) — estructura de una habilidad, carga bajo demanda y presupuesto de descripciones; autoridad: documentación de Anthropic.
- [Claude Code: ganchos](https://code.claude.com/docs/en/hooks) — entrada, códigos de salida, errores que no bloquean y tiempos máximos; autoridad: documentación de Anthropic.
- [Claude Code: subagentes](https://code.claude.com/docs/en/sub-agents) — herramientas y ganchos por subagente; autoridad: documentación de Anthropic.
- [Claude Code: aislamiento (sandbox)](https://code.claude.com/docs/en/sandboxing) — aislamiento de sistema de archivos y red; autoridad: documentación de Anthropic.
- [Spec Kit — repositorio](https://github.com/github/spec-kit) — extensiones y catálogos, con la advertencia de revisar el código de la comunidad; autoridad: GitHub y mantenedores.

---

[↑ Glosario](../../README.md) · [← Guion de inyección](../g/guion-de-inyeccion.md) · [Hallazgo →](./hallazgo.md)
