# Síntesis

[↑ Glosario](../../README.md) · [← Singleton](./singleton.md) · [Síntomas y peticiones →](./sintomas-y-peticiones.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Paso que reúne los resultados de los trabajadores.

Definición de trabajo de [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md).

## Por qué importa

La clase donde se define, [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md), existe con este propósito: la clase existe para que sepas cuándo un sistema necesita que un componente **decida en tiempo de ejecución cómo dividir el trabajo** (orquestador-trabajadores) y cuándo la calidad se consigue **iterando contra un criterio** (evaluador-optimizador).

## Cómo funciona

Según [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md):

En una paralelización (`SE-590`) las subtareas se conocen de antemano. En un **orquestador-trabajadores**, un modelo (o una regla) inspecciona la entrada, decide en cuántas partes dividirla, asigna cada una a un trabajador y luego sintetiza los resultados. La documentación de Anthropic lo recomienda cuando no se pueden predecir las subtareas, y pone el ejemplo de cambios de código que tocan un número variable de archivos. Lo que hace especial al patrón es la **decisión de división en tiempo de ejecución**; el resto (trabajadores, síntesis) es infraestructura. Su costo mínimo son dos llamadas: la que divide y la que sintetiza.

Según [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md):

El equipo implementa el repaso semanal con un orquestador que lee la lista de cursos con su número de entregas y decide los grupos: los tres cursos más grandes van cada uno a un trabajador y el resto se agrupa. Cada trabajador usa tres herramientas de solo lectura y devuelve un JSON con pendientes, vencidos y anomalías. La síntesis redacta el informe y el verificador comprueba que cada curso aparezca una vez y que los totales coincidan con la suma de los JSON. Si falla, el generador de la síntesis recibe las fallas exactas y rehace; con tres intentos sin pasar, el informe se envía a una persona marcado como «incompleto» con la lista de cursos que no cuadran.

## Ejemplo

Ejemplo de [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md) (sección «Ejemplo profesional»):

El equipo implementa el repaso semanal con un orquestador que lee la lista de cursos con su número de entregas y decide los grupos: los tres cursos más grandes van cada uno a un trabajador y el resto se agrupa. Cada trabajador usa tres herramientas de solo lectura y devuelve un JSON con pendientes, vencidos y anomalías. La síntesis redacta el informe y el verificador comprueba que cada curso aparezca una vez y que los totales coincidan con la suma de los JSON.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Con trabajadores, cada uno ve solo su curso y devuelve un resumen estructurado; la síntesis lee resúmenes, no historiales. ([SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md), [SE-590](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Resultado](../r/resultado.md), [Trabajador](../t/trabajador.md), [Evaluador](../e/evaluador.md), [LPT](../l/lpt.md), [Orquestador](../o/orquestador.md), [Tope de vueltas](../t/tope-de-vueltas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-530](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Singleton](./singleton.md) · [Síntomas y peticiones →](./sintomas-y-peticiones.md)
