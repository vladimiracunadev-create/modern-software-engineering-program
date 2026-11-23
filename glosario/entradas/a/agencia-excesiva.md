# Agencia excesiva

[↑ Glosario](../../README.md) · [← Afirmación refutable](./afirmacion-refutable.md) · [Agente →](./agente.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Conceder al modelo más funciones, permisos o autonomía de los que la tarea necesita.

Definición de trabajo de [SE-589 — Workflows frente a agentes: cuándo no usar un agente](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md).

## Por qué importa

La clase donde se define, [SE-589 — Workflows frente a agentes: cuándo no usar un agente](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md), existe con este propósito: la clase existe para que, antes de escribir un bucle de agente, te preguntes si el sistema necesita uno.

## Cómo funciona

Según [SE-589 — Workflows frente a agentes: cuándo no usar un agente](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md):

La segunda pregunta del árbol —¿las acciones son reversibles y acotadas?— decide si un agente es admisible. Un agente que lee es barato de equivocar: se descarta el resultado. Uno que envía mensajes, borra registros o cambia configuración produce efectos que no se deshacen leyendo otra vez. OWASP incluye la **agencia excesiva** entre los riesgos de las aplicaciones con LLM: dar al modelo más funciones, permisos o autonomía de los que la tarea requiere. La respuesta de diseño es reducir la superficie (herramientas mínimas, de solo lectura cuando se pueda), poner una persona en las acciones irreversibles y registrar cada paso. En el experimento, 1 % de cada llamada es irreversible; con seis llamadas eso es un 6 % de ejecuciones con un daño que ningún reintento corrige.

## Ejemplo

Caso medido en la sección «Reversibilidad y agencia excesiva» de [SE-589 — Workflows frente a agentes: cuándo no usar un agente](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md):

La segunda pregunta del árbol —¿las acciones son reversibles y acotadas?— decide si un agente es admisible. Un agente que lee es barato de equivocar: se descarta el resultado. Uno que envía mensajes, borra registros o cambia configuración produce efectos que no se deshacen leyendo otra vez. OWASP incluye la **agencia excesiva** entre los riesgos de las aplicaciones con LLM: dar al modelo más funciones, permisos o autonomía de los que la tarea requiere.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-589 — Workflows frente a agentes: cuándo no usar un agente](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md)) son: El experimento usa un modelo sintético con tasas de error declaradas, tres tipos de solicitud inventados por el autor y 2 000 solicitudes con semilla; no se midió ningún modelo de lenguaje real, ningún producto ni ningún equipo. El siguiente paso, `SE-590`, estudia los tres patrones de workflow más simples que sirven para construir el híbrido: encadenar pasos con puertas, enrutar solicitudes y paralelizar subtareas independientes.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-551](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-551-taller-un-mismo-cambio-con-cinco-metodologias/README.md), [SE-552](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-552-proyecto-politica-metodologica-de-equipo-con-evidencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Función](../f/funcion.md), [Modelo](../m/modelo.md), [Permiso](../p/permiso.md), [Tarea](../t/tarea.md), [Agente](./agente.md), [Escalar](../e/escalar.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-589 — Workflows frente a agentes: cuándo no usar un agente](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md), [SE-579](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Afirmación refutable](./afirmacion-refutable.md) · [Agente →](./agente.md)
