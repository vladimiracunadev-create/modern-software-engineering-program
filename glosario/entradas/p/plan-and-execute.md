# Plan-and-execute

[↑ Glosario](../../README.md) · [← Plan y dry-run](./plan-y-dry-run.md) · [Planificación →](./planificacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Estrategia que produce un plan completo y lo ejecuta con código.

Definición de trabajo de [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md).

## Por qué importa

La clase donde se define, [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md), existe con este propósito: la clase existe para que diseñes el **bucle** de un agente sabiendo qué compra cada variante.

## Cómo funciona

Según [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md):

El plan-and-execute separa **planificar** (una llamada que produce la lista de pasos) de **ejecutar** (código que recorre la lista, llamando a herramientas sin modelo en cada paso). Con un entorno estable es la opción más barata y más revisable: el plan se puede mostrar, aprobar y registrar antes de ejecutar, y la ejecución es determinista. En el experimento, sin sorpresas, resuelve el 100 % con una sola llamada. Su debilidad es la **suposición de que el mundo es como se planeó**: con 15 % de sorpresas resuelve el 54,2 % y con 35 % el 21,1 %, porque ante un contacto que falta el paso siguiente falla o actúa sobre datos vacíos.

Según [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md):

El equipo implementa el aviso masivo a pendientes como plan-and-execute con replanificación. El plan lo produce el modelo con una salida estructurada (lista de pasos con herramienta y argumentos) que un validador comprueba antes de ejecutar: solo herramientas permitidas y como máximo 50 pasos. El ejecutor registra cada paso con su observación. Si falta un contacto, devuelve una sorpresa; el modelo recibe lo hecho y la observación y produce el resto del plan; se permite una replanificación por ejecución y, si vuelve a haber una sorpresa, la tarea se escala con la traza. Los envíos usan una clave de idempotencia por estudiante y por aviso. En las incidencias abiertas, que no tienen un plan posible, usan ReAct con un tope de ocho pasos.

## Ejemplo

Ejemplo de [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md) (sección «Ejemplo profesional»):

El equipo implementa el aviso masivo a pendientes como plan-and-execute con replanificación. El plan lo produce el modelo con una salida estructurada (lista de pasos con herramienta y argumentos) que un validador comprueba antes de ejecutar: solo herramientas permitidas y como máximo 50 pasos. El ejecutor registra cada paso con su observación. Si falta un contacto, devuelve una sorpresa; el modelo recibe lo hecho y la observación y produce el resto del plan; se permite una replanificación por ejecución y, si vuelve a haber una sorpresa, la tarea se escala con la traza. Los envíos usan una clave de idempotencia por estudiante y por aviso.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El plan-and-execute separa **planificar** (una llamada que produce la lista de pasos) de **ejecutar** (código que recorre la lista, llamando a herramientas sin modelo en cada paso). ([SE-592](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md), [SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estrategia](../e/estrategia.md), [Plan](./plan.md), [ReAct](../r/react.md), [Reflexión](../r/reflexion.md), [Replanificación](../r/replanificacion.md), [Señal de fallo](../s/senal-de-fallo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-592 — ReAct, plan-and-execute y reflexión](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-592-react-plan-and-execute-y-reflexion/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md), [SE-593](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Plan y dry-run](./plan-y-dry-run.md) · [Planificación →](./planificacion.md)
