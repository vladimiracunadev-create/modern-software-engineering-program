# Escalada

[↑ Glosario](../../README.md) · [← Errores, reintentos y cancelación](./errores-reintentos-y-cancelacion.md) · [Escalada de privilegios →](./escalada-de-privilegios.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

En el trabajo con agentes, la **escalada** es la entrega de la tarea a una persona con la evidencia necesaria. [SE-581](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md) la define así y [SE-588](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md) precisa que se entrega *con la traza*. Es la salida honesta de un agente que no pudo resolver algo: en lugar de seguir intentándolo o de declarar un éxito falso, devuelve el control con el contexto para que alguien decida.

## Por qué importa

Cambia qué significa fallar bien. [SE-581](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md) lo resume: la mejora no estuvo en resolver más, sino en **fallar mejor**. Un informe que solo dice «tope alcanzado» obliga a reconstruir qué pasó; una escalada con evidencia deja la mañana empezando con una lista que se puede leer y actuar.

## Cómo funciona

Una escalada es la acción asociada a una condición de parada que no es convergencia. Lo que la hace útil es lo que lleva consigo. En [SE-581](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md), el detector con cambio de plan y escalada entrega, para cada tarea sin resolver:

- el **objetivo** original,
- los **tres últimos intentos**,
- el **último error**.

Con eso la persona no repite lo ya intentado. La causa de su valor es el costo de contexto: una tarea entregada sin traza cuesta casi lo mismo que empezarla de nuevo; con traza, se retoma en el punto de fallo. En [SE-588](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md) la escalada aparece también como parte de la respuesta a la pregunta «cómo se detiene»: junto con la parada, es uno de los controles que un comité querrá ver.

## Ejemplo

El caso de [SE-581](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md): un asistente ejecuta cuarenta tareas de mantenimiento durante la noche con un tope de 30 vueltas. Por la mañana, once terminaron en el tope y el informe dice solo «tope alcanzado». Revisando las trazas, nueve repetían el mismo error desde la vuelta cinco. Se añade el detector con cambio de plan y escalada. La noche siguiente, el número de tareas sin resolver es parecido, pero el gasto baja y la lista de la mañana se puede leer. Es una simulación con datos sintéticos, no una medición de un agente real.

## Errores y confusiones comunes

- **Informar solo «tope alcanzado».** Es parar sin escalar: se pierde la información que permite decidir.
- **Seguir hasta agotar el presupuesto.** Nueve de las once tareas de la clase repetían el mismo error desde la vuelta cinco: seguir no aportaba nada.
- **Entregar la traza completa sin resumen.** La evidencia útil es la mínima para decidir (objetivo, últimos intentos, último error), no todo el registro.
- **Escalar tarde.** La escalada debe dispararse por sin progreso o repetición, no solo por el tope.

## Límites y cuándo no aplica

En [SE-581](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md) se simularon cinco reglas sobre 4 000 tareas sintéticas con parámetros del autor y semilla 497; no se midió ningún agente real, ni el costo en dinero, ni el efecto de cambiar de plan en un modelo concreto. [SE-588](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md) declara también lo que un informe de este tipo no cubre: un adversario adaptativo, procesos hijos y red fuera del confinamiento, y la productividad. La escalada supone que hay una persona disponible y con autoridad; si nadie recibe el aviso, es una parada con otro nombre.

## Relación con otros conceptos

- **Prerrequisito:** [Traza](../t/traza.md).
- **Ver también:** [Evidencia](./evidencia.md), [Tarea](../t/tarea.md), [Cambio de plan](../c/cambio-de-plan.md), [Contención](../c/contencion.md), [Criterio de parada](../c/criterio-de-parada.md), [Escenario adverso](./escenario-adverso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-581 — Loops de agentes y criterios de parada](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.
- [SE-588 — Proyecto: harness mínimo gobernado y evaluado](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (11 clases más lo mencionan; las que más):

[SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), [SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md), [SE-183](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md), [SE-211](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md), [SE-229](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md), [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), [SE-370](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md), [SE-395](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Errores, reintentos y cancelación](./errores-reintentos-y-cancelacion.md) · [Escalada de privilegios →](./escalada-de-privilegios.md)
