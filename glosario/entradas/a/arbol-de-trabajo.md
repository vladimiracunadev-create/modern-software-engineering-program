# Árbol de trabajo

[↑ Glosario](../../README.md) · [← Árbol de métricas](./arbol-de-metricas.md) · [Árbol de utilidad →](./arbol-de-utilidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

Copia de trabajo adicional del mismo repositorio.

Definición de trabajo de [SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md).

## Por qué importa

La clase donde se define, [SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md), existe con este propósito: la clase existe para que decidas cuándo añadir un segundo agente y cómo coordinarlo sin multiplicar los fallos.

## Cómo funciona

Según [SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md):

Cada agente trabaja en su propia rama y, si comparten máquina, en su propio árbol de trabajo (`git worktree`), de modo que los archivos en disco no se pisen mientras trabajan. El aislamiento evita la interferencia en tiempo real; no evita el conflicto en la integración. Es la misma idea que el entorno desechable de `SE-582` aplicada a la coordinación.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cada agente trabaja en su propia rama y, si comparten máquina, en su propio árbol de trabajo (`git worktree`), de modo que los archivos en disco no se pisen mientras trabajan. ([SE-584](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md), [SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Trabajo](../t/trabajo.md), [Canal de coordinación](../c/canal-de-coordinacion.md), [Conflicto semántico](../c/conflicto-semantico.md), [Conflicto textual](../c/conflicto-textual.md), [Integrador](../i/integrador.md), [Propiedad de archivos](../p/propiedad-de-archivos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md), [SE-582](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md), [SE-194](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md), [SE-117](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-117-licencias-procedencia-y-reutilizacion/README.md), [SE-572](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «worktree».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Árbol de métricas](./arbol-de-metricas.md) · [Árbol de utilidad →](./arbol-de-utilidad.md)
