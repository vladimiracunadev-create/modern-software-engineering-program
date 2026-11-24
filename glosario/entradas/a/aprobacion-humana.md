# Aprobación humana

[↑ Glosario](../../README.md) · [← Api y cli coherentes](./api-y-cli-coherentes.md) · [Aprovisionamiento →](./aprovisionamiento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

La **aprobación humana** es la confirmación explícita de una persona antes de una acción ([SE-586](../../../classes/part-48-harness-y-agentic-engineering/se-586-ai-dlc-gobierno-y-vibe-coding-frente-a-agentic-engineering/README.md)). En el desarrollo con agentes es uno de los controles que se aplican de forma proporcional al riesgo.

## Por qué importa

Gobernar el desarrollo con agentes es decidir cuánto control reciben distintos cambios. [SE-586](../../../classes/part-48-harness-y-agentic-engineering/se-586-ai-dlc-gobierno-y-vibe-coding-frente-a-agentic-engineering/README.md) apoya esa decisión en dos referencias: NIST organiza la gestión del riesgo de IA en funciones (gobernar, mapear, medir y gestionar), y su valor para la clase es la secuencia (quién decide, qué puede salir mal, medir, actuar); OWASP recomienda limitar la autonomía de un agente y exigir aprobación humana para acciones de alto impacto.

## Cómo funciona

La **proporcionalidad** es la idea central: no todo cambio exige la misma aprobación. Acciones reversibles y de bajo impacto avanzan sin interrupción; las de alto impacto (borrados, despliegues, gastos, envíos externos) se detienen hasta que una persona confirma. La aprobación solo sirve si la persona recibe la información necesaria para decidir.

## Ejemplo

Un agente puede leer archivos y proponer cambios sin aprobación; antes de ejecutar una migración que altera datos, detiene la ejecución y presenta qué hará y qué se perdería si se equivoca.

## Errores y confusiones comunes

Pedir aprobación para todo (se aprende a pulsar «sí» sin leer); pedirla sin mostrar el efecto de la acción.

## Límites y cuándo no aplica

No sustituye a los controles técnicos (confinamiento, permisos mínimos): una persona cansada o sin contexto aprueba lo que no debería. Es un control más, no el único.

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
