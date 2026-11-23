# Tarea de regresión

[↑ Glosario](../../README.md) · [← Tarea](./tarea.md) · [Tarea determinista →](./tarea-determinista.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

Tarea derivada de un fallo ya diagnosticado.

Definición de trabajo de [SE-585 — Observabilidad y evals del propio harness](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-587 — Taller: diagnosticar el fallo de un harness](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md): Tarea que protege contra la reaparición de un fallo.
- En [SE-588 — Proyecto: harness mínimo gobernado y evaluado](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md): Tarea que protege un fallo diagnosticado.

## Por qué importa

En [SE-585 — Observabilidad y evals del propio harness](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md), el tema «Tareas de regresión» importa porque cada fallo observado se vuelve una tarea.

## Cómo funciona

Según [SE-587 — Taller: diagnosticar el fallo de un harness](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md):

Cada fallo diagnosticado produce una tarea de regresión: la tarea que lo reveló, la configuración que lo inyecta y el criterio que debe cumplirse tras el arreglo. El conjunto de seis fallos se ejecuta en la integración continua del harness y detecta cuando un cambio del archivo de instrucciones, de los permisos o de la parada reintroduce alguno. Es la versión operativa de `SE-585`: la evaluación del harness crece con sus propios fallos.

Según [SE-587 — Taller: diagnosticar el fallo de un harness](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md):

La persona de guardia recibe quince tareas fallidas de la noche. Aplica el procedimiento sin abrir la configuración: agrupa las trazas por patrón y encuentra tres grupos. Nueve repiten lecturas; cuatro piden el cierre dos veces; dos tienen una escritura denegada. Para el primer grupo comprueba el campo de herramientas ofrecidas: la escritura no figura; una actualización del producto había renombrado la herramienta y el harness no la reconocía. Arregla una pieza, repite las nueve tareas, se resuelven; añade la prueba de que la herramienta de escritura está ofrecida al conjunto de regresión. El segundo grupo es la parada ignorada tras un cambio de versión del harness; el tercero, un permiso demasiado estricto.

## Ejemplo

Ejemplo de [SE-585 — Observabilidad y evals del propio harness](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md) (sección «Caso conductor»):

Las trazas del arnés de *Avisos* alimentan el diagnóstico de `SE-587` y la evaluación del proyecto de `SE-588`. Cada fallo del taller se convierte en una tarea de regresión, y el conjunto de tareas de *Avisos* (corregir una función, añadir una prueba, actualizar un mensaje) es el que se usa para comparar versiones del harness.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Corrección.** Se restringe el patrón a los archivos de prueba, se repiten las seis tareas y se añade una tarea de regresión («un agente puede escribir el código y no las pruebas»). ([SE-588](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-549](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md), [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md), [SE-584](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Tarea](./tarea.md), [Evaluación del harness](../e/evaluacion-del-harness.md), [Fallo inyectado](../f/fallo-inyectado.md), [Graduador](../g/graduador.md), [Hipótesis refutable](../h/hipotesis-refutable.md), [Matriz de confusión](../m/matriz-de-confusion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-585 — Observabilidad y evals del propio harness](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.
- [SE-587 — Taller: diagnosticar el fallo de un harness](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.
- [SE-588 — Proyecto: harness mínimo gobernado y evaluado](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Tareas de regresión».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Tarea](./tarea.md) · [Tarea determinista →](./tarea-determinista.md)
