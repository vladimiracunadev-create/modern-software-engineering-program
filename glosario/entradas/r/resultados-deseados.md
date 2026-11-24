# Resultados deseados

[↑ Glosario](../../README.md) · [← Resultado explícito](./resultado-explicito.md) · [Resumen con pérdida →](./resumen-con-perdida.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Un **resultado deseado** es el enunciado de lo que la persona quiere lograr, con dirección de mejora, métrica, objeto y contexto, independiente de cómo se logre ([SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md)). Es la forma en que la propuesta de valor se vuelve medible: describe el progreso buscado sin nombrar la solución.

## Por qué importa

Un resultado deseado medible permite saber si hubo progreso sin depender de la solución. Cambia cómo se evalúan ideas y funciones: en lugar de preguntar «¿tenemos la función?», se pregunta «¿mejoró el resultado?». Varias soluciones distintas pueden compararse contra el mismo resultado.

## Cómo funciona

[SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md) da la estructura de cuatro partes: una **dirección** (minimizar, aumentar), una **métrica** (tiempo, probabilidad, número de), un **objeto** y un **contexto**. Ejemplo de la clase: «minimizar la probabilidad de perder el trabajo cuando se corta la conexión a pocas horas del plazo». Dirección: minimizar; métrica: probabilidad; objeto: perder el trabajo; contexto: corte de conexión cerca del plazo. Es medible sin decir si la solución es guardado automático, historial o recibo.

La lista típica de un trabajo reúne **decenas de resultados** posibles; no todos importan igual. Se valoran con una encuesta que pregunta cuán importante es cada uno y cuán satisfecho está quien responde con lo que usa hoy, y se priorizan los **importantes y mal atendidos**. La clase señala que con muestras pequeñas el ranking puede cambiar entre encuestas por ruido; por eso se reporta la **estabilidad del ranking**.

La regla de la plataforma: ninguna función entra al plan si no mueve al menos un resultado listado, y cada resultado declara el indicador con el que se sabrá si mejoró y el tiempo que tarda en notarse. Un fallo previsto: los resultados nombran la solución («tener un botón de guardado») porque se redactaron desde el producto y no desde el trabajo; se reescriben con dirección, métrica, objeto y contexto.

## Ejemplo

Resultado: «Minimizar el tiempo que tarda un docente en saber quiénes no han entregado, al revisar un lote desde el móvil». Indicador: minutos desde que abre el lote hasta tener la lista, medido en una prueba con docentes. Plazo para notarse: el primer ciclo de revisión tras el cambio. Una función (panel, lista exportable) se evalúa por cuánto reduce ese tiempo. (Ejemplo ilustrativo en el formato de [SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md).)

## Errores y confusiones comunes

- **Resultados que nombran la solución.**
- **Resultados sin métrica** («mejorar la experiencia»).
- **Priorizar con una encuesta pequeña sin estabilidad.**
- **Confundir resultado deseado con requisito**: el resultado es la meta del trabajo; el requisito, una decisión del equipo.

## Límites y cuándo no aplica

La encuesta de la clase usa datos sintéticos; muestra el método, no un ranking real. Los resultados descritos desde la persona pueden entrar en tensión (más rapidez, menos errores), y entonces son compromisos entre atributos. En productos para tareas muy simples, enumerar decenas de resultados es desproporcionado.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](../c/contextos.md), [Métrica](../m/metrica.md), [Objeto](../o/objeto.md), [Indicadores y demora](../i/indicadores-y-demora.md), [Oportunidad y ranking](../o/oportunidad-y-ranking.md), [Propuesta de valor](../p/propuesta-de-valor.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-125 — Propuesta de valor y resultados deseados](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md), [SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md), [SE-076](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md), [SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md), [SE-560](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md).

**Aparece en los casos de estudio:** [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Strategyn: Outcome-Driven Innovation](https://strategyn.com/outcome-driven-innovation-process/) — resultados deseados calificados por importancia y satisfacción; autoridad: Strategyn (fuente del autor del método).
- [Strategyzer: Value Proposition Canvas](https://www.strategyzer.com/library/the-value-proposition-canvas) — relación entre perfil de cliente y propuesta de valor; autoridad: Strategyzer.
- [Gourville: Eager Sellers and Stony Buyers (Harvard Business Review, 2006)](https://hbr.org/2006/06/eager-sellers-and-stony-buyers-understanding-the-psychology-of-new-product-adoption) — psicología de la adopción de productos nuevos; autoridad: Harvard Business Review (artículo de pago).
- [Know Your Customers' «Jobs to Be Done» (Harvard Business Review, 2016)](https://hbr.org/2016/09/know-your-customers-jobs-to-be-done) — describir el progreso que la persona busca; autoridad: Harvard Business Review (artículo parcialmente de pago).
- [The Lean Startup: principios](https://theleanstartup.com/principles) — aprendizaje validado y métricas accionables; autoridad: Eric Ries (fuente del autor).

---

[↑ Glosario](../../README.md) · [← Resultado explícito](./resultado-explicito.md) · [Resumen con pérdida →](./resumen-con-perdida.md)
