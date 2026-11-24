# Tarea de regresión

[↑ Glosario](../../README.md) · [← Tarea](./tarea.md) · [Tarea determinista →](./tarea-determinista.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

Una **tarea de regresión** es una tarea de evaluación derivada de un fallo ya diagnosticado, que protege contra su reaparición. [SE-585](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md) la define como tarea derivada de un fallo diagnosticado; [SE-587](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md) y [SE-588](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md) la precisan como la tarea que protege contra la reaparición de un fallo. Es la versión, para el arnés de un agente, de lo que en el software clásico es una prueba de regresión.

## Por qué importa

Decide si el arnés mejora o solo cambia. Si cada fallo diagnosticado se arregla y se olvida, el mismo fallo reaparece al cambiar el archivo de instrucciones, los permisos o la parada. Con tareas de regresión, la evaluación del arnés **crece con sus propios fallos** ([SE-587](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md)) y cada corrección deja un detector permanente.

## Cómo funciona

Cada fallo diagnosticado produce una tarea con tres elementos ([SE-587](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md)):

1. la **tarea que lo reveló**;
2. la **configuración que lo inyecta**;
3. el **criterio** que debe cumplirse tras el arreglo.

El conjunto se ejecuta en la **integración continua** del arnés y detecta cuándo un cambio reintroduce algún fallo. La causa de su valor es que los fallos de un agente dependen de configuración (herramientas ofrecidas, permisos, reglas de parada, instrucciones), y esa configuración cambia con las versiones del producto; una tarea de regresión comprueba la pieza que depende de ella.

## Ejemplo

[SE-587](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md): la persona de guardia recibe quince tareas fallidas de la noche. Agrupa las trazas por patrón: tres grupos. Nueve repiten lecturas, cuatro piden el cierre dos veces, dos tienen una escritura denegada. Para el primer grupo comprueba el campo de herramientas ofrecidas: la escritura no figura, porque una actualización del producto había renombrado la herramienta y el arnés no la reconocía. Arregla esa pieza, repite las nueve tareas y se resuelven. Luego añade al conjunto de regresión la prueba de que la herramienta de escritura está ofrecida. El segundo grupo era una parada ignorada tras un cambio de versión del arnés; el tercero, un permiso demasiado estricto.

En [SE-588](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md) se corrige un patrón para limitarlo a los archivos de prueba, se repiten las seis tareas y se añade una tarea de regresión: «un agente puede escribir el código y no las pruebas».

## Errores y confusiones comunes

- **Arreglar sin dejar tarea.** El fallo reaparece tras el siguiente cambio de configuración.
- **Una tarea que no reproduce el fallo.** Debe fallar *antes* del arreglo; si pasa en ambos casos, no protege nada.
- **Confundirla con una prueba unitaria.** Evalúa el comportamiento del arnés completo (agente, herramientas, permisos), no una función.
- **Un conjunto que solo crece.** Conviene revisar tareas obsoletas, pero retirar solo con criterio.

## Límites y cuándo no aplica

Solo protege fallos *ya diagnosticados*: no detecta clases nuevas. Con componentes no deterministas, una tarea puede pasar o fallar por azar; hay que repetir y decidir con un criterio estadístico. En [SE-587](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md) el conjunto es de seis fallos de un caso de estudio, no una muestra representativa de agentes reales. Y una tarea de regresión demasiado atada al texto exacto de una traza se rompe por cambios inocuos; el criterio debe estar en el resultado, no en la redacción.

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
