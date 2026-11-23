# Replanificación

[↑ Glosario](../../README.md) · [← Replacement character](./replacement-character.md) · [Réplica →](./replica.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Nueva llamada al modelo con la sorpresa para obtener un plan de lo que queda.

Definición de trabajo de [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md).

## Por qué importa

En [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md), el tema «Replanificación» importa porque paga solo cuando el plan se rompe.

## Cómo funciona

Según [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md):

La variante con **replanificación** añade una regla: si una observación contradice lo que el plan suponía (un código de error, un campo vacío, un resultado inesperado), la ejecución se detiene y se llama al modelo con lo que ocurrió para obtener un plan nuevo para lo que queda. El costo es una llamada por sorpresa. En el experimento, con 15 % de sorpresas resuelve el 94,9 % con 1,6 llamadas de media; con 35 %, el 88,2 % con 2,3. Frente a ReAct (88-89 % con 11 llamadas), mantiene la calidad con una fracción del costo mientras las sorpresas sean la excepción. Cuando son la regla (cada paso es una sorpresa), el costo de replanificar se acerca al de ReAct y desaparece la ventaja.

Según [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md):

El equipo implementa el aviso masivo a pendientes como plan-and-execute con replanificación. El plan lo produce el modelo con una salida estructurada (lista de pasos con herramienta y argumentos) que un validador comprueba antes de ejecutar: solo herramientas permitidas y como máximo 50 pasos. El ejecutor registra cada paso con su observación. Si falta un contacto, devuelve una sorpresa; el modelo recibe lo hecho y la observación y produce el resto del plan; se permite una replanificación por ejecución y, si vuelve a haber una sorpresa, la tarea se escala con la traza. Los envíos usan una clave de idempotencia por estudiante y por aviso. En las incidencias abiertas, que no tienen un plan posible, usan ReAct con un tope de ocho pasos.

## Ejemplo

Ejemplo de [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md) (sección «Ejemplo profesional»):

El equipo implementa el aviso masivo a pendientes como plan-and-execute con replanificación. El plan lo produce el modelo con una salida estructurada (lista de pasos con herramienta y argumentos) que un validador comprueba antes de ejecutar: solo herramientas permitidas y como máximo 50 pasos. El ejecutor registra cada paso con su observación. Si falta un contacto, devuelve una sorpresa; el modelo recibe lo hecho y la observación y produce el resto del plan; se permite una replanificación por ejecución y, si vuelve a haber una sorpresa, la tarea se escala con la traza. Los envíos usan una clave de idempotencia por estudiante y por aviso.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Mira que el plan solo se hunde con las sorpresas, que ReAct casi no depende de ellas y que la replanificación y la reflexión quedan en medio; las llamadas medias de cada estrategia están en la nota. ([SE-592](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md), [SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Modelo](../m/modelo.md), [Plan](../p/plan.md), [Sorpresa](../s/sorpresa.md), [Plan-and-execute](../p/plan-and-execute.md), [ReAct](./react.md), [Reflexión](./reflexion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-192](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md), [SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md), [SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Replacement character](./replacement-character.md) · [Réplica →](./replica.md)
