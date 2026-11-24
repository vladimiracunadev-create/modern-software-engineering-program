# Harness

[↑ Glosario](../../README.md) · [← Happy path](./happy-path.md) · [Harness gobernado →](./harness-gobernado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

El **harness** (arnés) es todo lo que rodea al modelo en un agente: instrucciones, contexto, herramientas, permisos, bucle, parada, verificación y registro. Es la definición de [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md), que cita la formulación de Böckeler: un agente es el modelo más todo lo que lo rodea.

## Por qué importa

El comportamiento observado depende del arnés tanto como del modelo. Cuando un asistente deja de ejecutar las pruebas, la causa puede estar en el modelo, en el prompt o en el entorno; sin separarlas por trazas, se culpa al modelo y el defecto queda.

## Cómo funciona

[SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md) acota la definición amplia al caso de los agentes de código: parte del arnés viene incorporada en el producto (el mensaje de sistema, la recuperación de código) y la persona construye un arnés *exterior* con lo que el producto ofrece: instrucciones del repositorio, ganchos, permisos y compuertas de verificación. El arnés decide qué acciones se traducen en efectos, cuándo se detiene el agente y qué se verifica.

## Ejemplo

En [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md), un asistente de código da por terminados tres cambios con pruebas en rojo. Las trazas muestran que no ejecutó pruebas porque una reorganización había movido la línea de verificación a un archivo que el producto ya no cargaba. Se corrige en el arnés y se añade una compuerta, sin tocar el modelo.

## Errores y confusiones comunes

Confundirlo con un *framework*: un framework es una biblioteca para construir agentes; el arnés es el entorno configurado alrededor de un agente concreto, y puede construirse con un framework, un producto o un script. Lo que lo define es qué decide (permisos, parada, verificación), no qué biblioteca usa.

## Límites y cuándo no aplica

Quitar una herramienta cambia el comportamiento sin avisar al agente; un arnés que no registra las herramientas ofrecidas deja trazas ambiguas. La definición es deliberadamente amplia y por eso conviene fijar qué parte se considera exterior.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-551](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-551-taller-un-mismo-cambio-con-cinco-metodologias/README.md), [SE-552](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-552-proyecto-politica-metodologica-de-equipo-con-evidencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Agente](../a/agente.md), [Contextos](../c/contextos.md), [Herramientas](./herramientas.md), [Instrucción](../i/instruccion.md), [Ablación](../a/ablacion.md), [Bucle del agente](../b/bucle-del-agente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-577 — Anatomía de un harness: modelo, contexto, herramientas y bucles](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (78 clases más lo mencionan; las que más):

[SE-588](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md), [SE-585](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md), [SE-587](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md), [SE-580](../../../classes/part-48-harness-y-agentic-engineering/se-580-gestion-de-contexto-resets-y-handoffs/README.md), [SE-582](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md), [SE-586](../../../classes/part-48-harness-y-agentic-engineering/se-586-ai-dlc-gobierno-y-vibe-coding-frente-a-agentic-engineering/README.md), [SE-581](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md), [SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Happy path](./happy-path.md) · [Harness gobernado →](./harness-gobernado.md)
