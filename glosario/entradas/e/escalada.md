# Escalada

[↑ Glosario](../../README.md) · [← Errores, reintentos y cancelación](./errores-reintentos-y-cancelacion.md) · [Escalada de privilegios →](./escalada-de-privilegios.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

Entrega de la tarea a una persona con la evidencia necesaria.

Definición de trabajo de [SE-581 — Loops de agentes y criterios de parada](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-588 — Proyecto: harness mínimo gobernado y evaluado](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md): Entrega de la tarea a una persona con la traza.

## Por qué importa

En [SE-581 — Loops de agentes y criterios de parada](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md), el tema «Escalada» importa porque el fallo llega a una persona con evidencia.

## Cómo funciona

Según [SE-581 — Loops de agentes y criterios de parada](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md):

El equipo ejecuta el asistente sobre una lista de cuarenta tareas de mantenimiento durante la noche con un tope de 30 vueltas. Por la mañana, once tareas terminaron en el tope y el informe dice solo «tope alcanzado». Revisando las trazas, nueve de ellas repetían el mismo error desde la vuelta cinco. Se añade el detector con cambio de plan y escalada que entrega, para cada tarea que no se resuelve, el objetivo, los tres últimos intentos y el último error. En la siguiente noche, el número de tareas sin resolver es parecido, pero el gasto baja y la mañana empieza con una lista que se puede leer. La lección: la mejora no estuvo en resolver más, sino en fallar mejor.

Según [SE-588 — Proyecto: harness mínimo gobernado y evaluado](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md):

El informe contesta las tres preguntas del comité con evidencia: qué puede tocar (la superficie de acción y el confinamiento), cómo se detiene (la parada y la escalada) y cómo se verifica (el menú y la protección de pruebas). Y declara cuatro límites: lo que no se probó (un adversario adaptativo, un modelo real), lo que el confinamiento no cubre (procesos hijos, red), lo que el menú no ve (un error que ninguna prueba ejerce y una prueba que replica el error) y lo que no se midió (productividad, costo). Un informe sin límites es un anuncio.

## Ejemplo

Ejemplo de [SE-581 — Loops de agentes y criterios de parada](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md) (sección «Ejemplo profesional»):

El equipo ejecuta el asistente sobre una lista de cuarenta tareas de mantenimiento durante la noche con un tope de 30 vueltas. Por la mañana, once tareas terminaron en el tope y el informe dice solo «tope alcanzado». Revisando las trazas, nueve de ellas repetían el mismo error desde la vuelta cinco. Se añade el detector con cambio de plan y escalada que entrega, para cada tarea que no se resuelve, el objetivo, los tres últimos intentos y el último error. En la siguiente noche, el número de tareas sin resolver es parecido, pero el gasto baja y la mañana empieza con una lista que se puede leer.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-581 — Loops de agentes y criterios de parada](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md)) son: Se simularon cinco reglas sobre 4 000 tareas sintéticas con parámetros del autor y semilla 497, en Windows 11 con CPython 3.12.9. No se midió ningún agente real, ni el costo en dinero, ni el efecto de cambiar de plan en un modelo concreto. El siguiente paso, `SE-582`, trata lo que ocurre cuando, pese a las reglas, el agente hace algo dañino: cómo se acota y se deshace.

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
