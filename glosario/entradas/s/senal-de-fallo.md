# Señal de fallo

[↑ Glosario](../../README.md) · [← Señal](./senal.md) · [Señal de terminación →](./senal-de-terminacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Evidencia externa de que un intento falló (error, verificador, prueba).

Definición de trabajo de [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md).

## Por qué importa

En [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md), el tema «Reflexión» importa porque una segunda oportunidad con una pista, si hay señal de fallo.

## Cómo funciona

Según [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md):

La reflexión (Shinn et al.) convierte el resultado de un intento fallido en un **texto de retroalimentación** («falló porque el estudiante 3 no tenía contacto; comprueba el contacto antes de enviar») que se añade al contexto del siguiente intento. Cuesta al menos dos llamadas más (reflexionar y volver a planificar) y solo ayuda si hay una **señal de fallo externa**: un código de error, un verificador, una prueba. Sin esa señal, el modelo reflexiona sobre su propia respuesta sin saber si falló, y es fácil que racionalice lo hecho.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cuesta al menos dos llamadas más (reflexionar y volver a planificar) y solo ayuda si hay una **señal de fallo externa**: un código de error, un verificador, una prueba. ([SE-592](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md), [SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evidencia](../e/evidencia.md), [Verificador](../v/verificador.md), [Plan-and-execute](../p/plan-and-execute.md), [ReAct](../r/react.md), [Reflexión](../r/reflexion.md), [Replanificación](../r/replanificacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Señal](./senal.md) · [Señal de terminación →](./senal-de-terminacion.md)
