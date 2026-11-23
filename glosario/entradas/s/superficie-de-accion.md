# Superficie de acción

[↑ Glosario](../../README.md) · [← Superficie compartida](./superficie-compartida.md) · [Superficie de ataque →](./superficie-de-ataque.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

Conjunto de efectos que un agente puede producir.

Definición de trabajo de [SE-579 — Herramientas, permisos y superficies de acción](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md).

## Por qué importa

En [SE-579 — Herramientas, permisos y superficies de acción](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md), el tema «Superficie de acción» importa porque lo que no está en la superficie no puede ocurrir.

## Cómo funciona

Según [SE-579 — Herramientas, permisos y superficies de acción](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md):

La superficie de acción de un agente es el conjunto de efectos que puede producir en el mundo: archivos que lee y escribe, procesos que lanza, servicios a los que se conecta, credenciales que ve. OWASP lo trata como el riesgo de **agencia excesiva**: funcionalidad que el agente no necesita para su tarea, permisos más amplios que los necesarios y autonomía que actúa sin que nadie confirme. La respuesta tiene la misma forma que en cualquier sistema: pocas herramientas, de alcance estrecho, con los permisos mínimos y con confirmación para lo grave. La primera pregunta de diseño no es «qué permisos le doy», es «qué herramientas necesita» y, de cada una, «qué argumentos acepta».

Según [SE-579 — Herramientas, permisos y superficies de acción](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md):

El protocolo especifica cómo se exponen herramientas, no cuáles son seguras. Cada servidor añade superficie de acción y debe tratarse como una dependencia: revisar qué expone, con qué credenciales y con qué alcance.

## Ejemplo

Ejemplo de [SE-579 — Herramientas, permisos y superficies de acción](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md) (sección «Preguntas frecuentes»):

El protocolo especifica cómo se exponen herramientas, no cuáles son seguras. Cada servidor añade superficie de acción y debe tratarse como una dependencia: revisar qué expone, con qué credenciales y con qué alcance.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cada servidor añade superficie de acción y debe tratarse como una dependencia: revisar qué expone, con qué credenciales y con qué alcance. ([SE-579](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md), [SE-578](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Agente](../a/agente.md), [Conjunto](../c/conjunto.md), [Efecto](../e/efecto.md), [Aprobación humana](../a/aprobacion-humana.md), [Comando compuesto](../c/comando-compuesto.md), [Confinamiento de rutas](../c/confinamiento-de-rutas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-579 — Herramientas, permisos y superficies de acción](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-580](../../../classes/part-48-harness-y-agentic-engineering/se-580-gestion-de-contexto-resets-y-handoffs/README.md), [SE-578](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md), [SE-584](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md), [SE-588](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Superficie compartida](./superficie-compartida.md) · [Superficie de ataque →](./superficie-de-ataque.md)
