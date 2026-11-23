# Enrutador

[↑ Glosario](../../README.md) · [← Enmascarado determinista](./enmascarado-determinista.md) · [Enrutador de celdas →](./enrutador-de-celdas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Componente que clasifica la entrada y elige el camino.

Definición de trabajo de [SE-590 — Encadenado, enrutamiento y paralelización](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md).

## Por qué importa

En [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md), el tema «Enrutador» importa porque componente compartido que debe ser mínimo.

## Cómo funciona

Según [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md):

El enrutador necesita una función que, dado un inquilino, devuelva su celda y que sea estable. La opción ingenua es el módulo: la celda es el hash del inquilino módulo el número de celdas. Funciona hasta que se añade una celda. Con 100 000 inquilinos y el paso de 8 a 9 celdas, el módulo reubicó 88 985, el 89,0 %: casi todos cambian de celda, y cada cambio es una migración de datos. El hash por encuentro (rendezvous) calcula para cada inquilino un puntaje con cada celda y elige la de mayor puntaje; al añadir una celda nueva, solo se mueven los inquilinos para los que la nueva obtiene el puntaje más alto: 11 176, el 11,2 %, cercano al mínimo teórico de un noveno (11,1 %).

Según [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md):

**Diagnóstico paso a paso.** (1) Se confirma que cada celda respondía a sus pruebas internas. (2) El enrutador, desplegado de una vez a toda la flota, contenía un cambio en la tabla de asignación que dejó a los inquilinos sin celda. (3) El enrutador era el componente compartido y se había tratado como cualquier otro servicio, sin despliegue escalonado. (4) El radio de impacto del enrutador era del 100 %.

## Ejemplo

Ejemplo de [SE-590 — Encadenado, enrutamiento y paralelización](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* implementa el silencio como una cadena de tres pasos: extracción (modelo, salida JSON), validación (código, con la puerta anterior) y confirmación (modelo, texto). Si la puerta falla, se repite la extracción una vez con el error de la puerta como contexto; si vuelve a fallar, la solicitud se escala a una persona con la extracción fallida adjunta. El enrutador es un clasificador con umbral y, bajo el umbral, la solicitud va a la cola humana. El informe semanal de ocho cursos se ejecuta en paralelo con un máximo de cuatro hilos para respetar la cuota del proveedor, y el resultado se une en un solo documento.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Lo que queda fuera es un punto de fallo para todos: el enrutador, el plano de control que crea celdas, el sistema de identidad, el DNS, la configuración global. ([SE-344](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md))
- Si el proceso recibe solicitudes variadas, diseña el enrutador con umbral y define qué pasa con lo que no se clasifica. ([SE-590](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-342](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Celda](../c/celda.md), [Cobertura con umbral](../c/cobertura-con-umbral.md), [Encadenado](./encadenado.md), [Enrutador de celdas](./enrutador-de-celdas.md), [Fragmentación aleatoria](../f/fragmentacion-aleatoria.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-590 — Encadenado, enrutamiento y paralelización](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (11 clases más lo mencionan; las que más):

[SE-234](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md), [SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md), [SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md), [SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), [SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md), [SE-599](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-599-taller-elegir-y-degradar-un-patron-agentico/README.md), [SE-600](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md), [SE-346](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Enmascarado determinista](./enmascarado-determinista.md) · [Enrutador de celdas →](./enrutador-de-celdas.md)
