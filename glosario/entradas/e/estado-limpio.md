# Estado limpio

[↑ Glosario](../../README.md) · [← Estado inicial](./estado-inicial.md) · [Estado local, compartido y persistente →](./estado-local-compartido-y-persistente.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

Estado del repositorio que se podría integrar sin sorpresas.

Definición de trabajo de [SE-580 — Gestión de contexto, resets y handoffs](../../../classes/part-48-harness-y-agentic-engineering/se-580-gestion-de-contexto-resets-y-handoffs/README.md).

## Por qué importa

La clase donde se define, [SE-580 — Gestión de contexto, resets y handoffs](../../../classes/part-48-harness-y-agentic-engineering/se-580-gestion-de-contexto-resets-y-handoffs/README.md), existe con este propósito: la clase existe para que trates el contexto de un agente como un recurso escaso que se administra, no como una memoria que se llena sola.

## Cómo funciona

Según [SE-580 — Gestión de contexto, resets y handoffs](../../../classes/part-48-harness-y-agentic-engineering/se-580-gestion-de-contexto-resets-y-handoffs/README.md):

Anthropic describe el problema de los agentes que abarcan varias ventanas: cada sesión empieza sin memoria de la anterior, como un turno de ingenieros que llegan sin saber qué pasó en el anterior. Su solución es de entorno: un agente inicial prepara el repositorio y deja artefactos (una lista de funcionalidades con su estado, un registro de progreso, commits pequeños) y cada sesión siguiente hace un avance incremental y deja el entorno en un estado limpio. La lección transferible es que lo que sobrevive es lo que está en disco: notas, commits, pruebas.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-580 — Gestión de contexto, resets y handoffs](../../../classes/part-48-harness-y-agentic-engineering/se-580-gestion-de-contexto-resets-y-handoffs/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Su solución es de entorno: un agente inicial prepara el repositorio y deja artefactos (una lista de funcionalidades con su estado, un registro de progreso, commits pequeños) y cada sesión siguiente hace un avance incremental y deja el entorno en un estado limpio. ([SE-580](../../../classes/part-48-harness-y-agentic-engineering/se-580-gestion-de-contexto-resets-y-handoffs/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md), [SE-579](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](./estado.md), [Sorpresa](../s/sorpresa.md), [Archivo de relevo](../a/archivo-de-relevo.md), [Compactación](../c/compactacion.md), [Decisión declarada](../d/decision-declarada.md), [Ventana de contexto](../v/ventana-de-contexto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-580 — Gestión de contexto, resets y handoffs](../../../classes/part-48-harness-y-agentic-engineering/se-580-gestion-de-contexto-resets-y-handoffs/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-035](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-035-taller-preparar-y-reparar-un-entorno-reproducible/README.md), [SE-101](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md), [SE-203](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Estado inicial](./estado-inicial.md) · [Estado local, compartido y persistente →](./estado-local-compartido-y-persistente.md)
