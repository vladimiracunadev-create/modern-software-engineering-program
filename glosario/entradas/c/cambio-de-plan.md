# Cambio de plan

[↑ Glosario](../../README.md) · [← Cambio de contrato](./cambio-de-contrato.md) · [Cambio dirigido →](./cambio-dirigido.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md)

## Definición

Alteración deliberada del enfoque tras detectar falta de progreso.

Definición de trabajo de [SE-581 — Loops de agentes y criterios de parada](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md).

## Por qué importa

En [SE-581 — Loops de agentes y criterios de parada](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md), el tema «Cambio de plan» importa porque convierte un atasco en una oportunidad.

En [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md), el tema «Cambio de plan» importa porque subir y bajar tienen casos distintos, sobre todo con exceso.

## Cómo funciona

Según [SE-581 — Loops de agentes y criterios de parada](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md):

El equipo ejecuta el asistente sobre una lista de cuarenta tareas de mantenimiento durante la noche con un tope de 30 vueltas. Por la mañana, once tareas terminaron en el tope y el informe dice solo «tope alcanzado». Revisando las trazas, nueve de ellas repetían el mismo error desde la vuelta cinco. Se añade el detector con cambio de plan y escalada que entrega, para cada tarea que no se resuelve, el objetivo, los tres últimos intentos y el último error. En la siguiente noche, el número de tareas sin resolver es parecido, pero el gasto baja y la mañana empieza con una lista que se puede leer. La lección: la mejora no estuvo en resolver más, sino en fallar mejor.

Según [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md):

Un pacto comercial («40 usuarios durante seis meses») es una excepción con vencimiento, no un cambio de plan ni un cambio de código. Se guarda como dato: cliente, clave, valor, vence, quién la autorizó y por qué. Al vencer, el motor vuelve al plan sin intervención y un trabajo avisa a comercial con anticipación. Dejar una excepción sin vencimiento convierte al cliente en un plan propio que nadie recuerda; el inventario de excepciones activas debería caber en una pantalla y revisarse cada trimestre.

## Ejemplo

Ejemplo de [SE-581 — Loops de agentes y criterios de parada](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md) (sección «Ejemplo profesional»):

El equipo ejecuta el asistente sobre una lista de cuarenta tareas de mantenimiento durante la noche con un tope de 30 vueltas. Por la mañana, once tareas terminaron en el tope y el informe dice solo «tope alcanzado». Revisando las trazas, nueve de ellas repetían el mismo error desde la vuelta cinco. Se añade el detector con cambio de plan y escalada que entrega, para cada tarea que no se resuelve, el objetivo, los tres últimos intentos y el último error. En la siguiente noche, el número de tareas sin resolver es parecido, pero el gasto baja y la mañana empieza con una lista que se puede leer.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un pacto comercial («40 usuarios durante seis meses») es una excepción con vencimiento, no un cambio de plan ni un cambio de código. ([SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md), [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md), [SE-475](../../../classes/part-39-build-release-y-cadena-de-suministro/se-475-feature-flags-y-entrega-progresiva/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Falta de progreso](../f/falta-de-progreso.md), [Progreso](../p/progreso.md), [Bandera de funcionalidad](../b/bandera-de-funcionalidad.md), [Criterio de parada](./criterio-de-parada.md), [Cuota](./cuota.md), [Derecho](../d/derecho.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-414 — Planes, derechos de uso y banderas de funcionalidad](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md) — [Parte 34](../../../classes/part-34-saas-y-plataformas-de-producto/README.md), SaaS y plataformas de producto.
- [SE-581 — Loops de agentes y criterios de parada](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-412](../../../classes/part-34-saas-y-plataformas-de-producto/se-412-suscripciones-ciclos-de-facturacion-y-dunning/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md), [SE-411](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md), [SE-138](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md), [SE-192](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Cambio de contrato](./cambio-de-contrato.md) · [Cambio dirigido →](./cambio-dirigido.md)
