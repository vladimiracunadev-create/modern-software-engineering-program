# Aprobación humana

[↑ Glosario](../../README.md) · [← Api y cli coherentes](./api-y-cli-coherentes.md) · [Aprovisionamiento →](./aprovisionamiento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

Confirmación explícita de una persona antes de una acción.

Definición de trabajo de [SE-579 — Herramientas, permisos y superficies de acción](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md).

## Por qué importa

En [SE-579 — Herramientas, permisos y superficies de acción](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md), el tema «Aprobación humana» importa porque es el último control, y se degrada si se concede por costumbre.

En [SE-586 — AI-DLC, gobierno y vibe coding frente a agentic engineering](../../../classes/part-48-harness-y-agentic-engineering/se-586-ai-dlc-gobierno-y-vibe-coding-frente-a-agentic-engineering/README.md), el tema «Aprobación humana» importa porque concentra la atención donde el costo del error es mayor.

## Cómo funciona

Según [SE-586 — AI-DLC, gobierno y vibe coding frente a agentic engineering](../../../classes/part-48-harness-y-agentic-engineering/se-586-ai-dlc-gobierno-y-vibe-coding-frente-a-agentic-engineering/README.md):

Gobernar el desarrollo con agentes es decidir cuánto control reciben distintos cambios. La proporcionalidad es la idea central de los marcos de riesgo: NIST organiza la gestión del riesgo de IA en funciones (gobernar, mapear, medir y gestionar) y su valor para esta clase es la secuencia, no el catálogo: se define quién decide, se identifica qué puede salir mal, se mide y se actúa. OWASP, por su parte, recomienda limitar la autonomía de un agente y exigir aprobación humana para acciones de alto impacto. Ambos coinciden en la forma: más control donde el daño potencial es mayor.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-579 — Herramientas, permisos y superficies de acción](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-579 — Herramientas, permisos y superficies de acción](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md)) son: Se analizaron treinta comandos del autor con dos políticas de texto, en Windows 11 con CPython 3.12.9, sin ejecutar ninguno. No se midió una política contra un adversario, ni un producto de agentes, ni el desgaste real de la aprobación humana. El siguiente paso, `SE-580`, trata el contexto: qué recuerda el agente cuando la sesión se alarga y qué debe quedar escrito fuera de ella.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md), [SE-578](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Confirmación](../c/confirmacion.md), [Agentic engineering](./agentic-engineering.md), [Comando compuesto](../c/comando-compuesto.md), [Confinamiento de rutas](../c/confinamiento-de-rutas.md), [Falsa denegación](../f/falsa-denegacion.md), [Gobierno](../g/gobierno.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-579 — Herramientas, permisos y superficies de acción](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.
- [SE-586 — AI-DLC, gobierno y vibe coding frente a agentic engineering](../../../classes/part-48-harness-y-agentic-engineering/se-586-ai-dlc-gobierno-y-vibe-coding-frente-a-agentic-engineering/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (13 clases más lo mencionan; las que más):

[SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md), [SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md), [SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md), [SE-023](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md), [SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md), [SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md), [SE-418](../../../classes/part-34-saas-y-plataformas-de-producto/se-418-comercio-electronico-carrito-inventario-pagos-y-devoluciones/README.md), [SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Api y cli coherentes](./api-y-cli-coherentes.md) · [Aprovisionamiento →](./aprovisionamiento.md)
