# Propuesta de valor

[↑ Glosario](../../README.md) · [← Proposición](./proposicion.md) · [Prorrateo →](./prorrateo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Una **propuesta de valor** es una promesa específica de un progreso que una persona logra en su trabajo con este producto y no con la alternativa actual ([SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md)). No es un eslogan ni una lista de funciones: nombra un trabajo concreto, la alternativa con que se compite y el progreso que la persona notaría.

## Por qué importa

Dice qué progreso se promete a qué trabajo, y eso da criterio para decidir qué construir. Una lista de funciones deja la decisión sin criterio: toda función suena razonable. Con una promesa clara, cada función se evalúa por si mueve algún resultado deseado.

## Cómo funciona

[SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md) contrasta dos formulaciones. «Recuperación de borradores con historial» describe una **función**. «Cuando se acerca el plazo, comprobar en menos de diez segundos que mi trabajo está a salvo» describe un **progreso**. La segunda se redacta como «cuando… puedo… sin…» y permite medir si se cumple.

El lienzo de propuesta de valor organiza la relación en dos lados: del cliente, sus trabajos, frustraciones y ganancias; del producto, sus aliviadores de frustraciones y creadores de ganancias. La clase subraya que es una **hipótesis estructurada, no un resultado**: se completa con suposiciones que luego se contrastan.

En la plataforma de entregas, la propuesta conserva la promesa en una frase, el trabajo al que responde, la alternativa actual, los resultados deseados con su métrica, la fecha de la encuesta, el tamaño de la muestra y la estabilidad del ranking. La regla es que ninguna función entra al plan si no mueve al menos un resultado listado, y que cada resultado declara el indicador con el que se sabrá si mejoró y el tiempo que tarda en notarse. La estabilidad del ranking importa porque, con muestras pequeñas, el ruido reordena los primeros puestos; la clase simula esa estabilidad y propone ampliar la muestra antes de decidir.

## Ejemplo

Función: «historial de versiones del borrador». Promesa: «cuando se acerca el plazo, comprobar en menos de diez segundos que mi trabajo está a salvo, sin abrir cada versión». Resultado deseado: tiempo de verificación; indicador: tiempo medido en una prueba con personas; plazo para notarse: el primer ciclo de entregas. Una función que no mueva ninguno de los resultados listados queda fuera del plan.

## Errores y confusiones comunes

- **Plan con nueve funciones y ninguna promesa**: se describió la solución, no el progreso; corrección: redactar la promesa como «cuando… puedo… sin…» y vincular cada función a un resultado.
- **Prioridades que cambian en cada encuesta**: muestra pequeña; corrección: reportar la estabilidad simulada o ampliar la muestra.
- **Confundirla con un eslogan de marketing**: el eslogan persuade; la propuesta se puede contrastar.
- **Tratar el lienzo como validación**: ayuda a nombrar la hipótesis, no a probarla.

## Límites y cuándo no aplica

Una propuesta clara no garantiza que alguien pague o use el producto: se valida con experimentos. En productos que sirven a varios trabajos muy distintos, una sola propuesta es insuficiente y hace falta una por segmento. Los datos de [SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md) son sintéticos, de modo que muestran el método y no el ranking real de ningún producto.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Producto](./producto.md), [Progreso](./progreso.md), [Trabajo](../t/trabajo.md), [Indicadores y demora](../i/indicadores-y-demora.md), [Oportunidad y ranking](../o/oportunidad-y-ranking.md), [Resultados deseados](../r/resultados-deseados.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-125 — Propuesta de valor y resultados deseados](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md), [SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md), [SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md), [SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md).

**Aparece en los casos de estudio:** [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md), [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Strategyzer: Value Proposition Canvas](https://www.strategyzer.com/library/the-value-proposition-canvas) — relación entre perfil de cliente y propuesta de valor; autoridad: Strategyzer.
- [Strategyn: Outcome-Driven Innovation](https://strategyn.com/outcome-driven-innovation-process/) — resultados deseados calificados por importancia y satisfacción; autoridad: Strategyn (fuente del autor del método).
- [Gourville: Eager Sellers and Stony Buyers (Harvard Business Review, 2006)](https://hbr.org/2006/06/eager-sellers-and-stony-buyers-understanding-the-psychology-of-new-product-adoption) — psicología de la adopción de productos nuevos; autoridad: Harvard Business Review (artículo de pago).
- [Know Your Customers' «Jobs to Be Done» (Harvard Business Review, 2016)](https://hbr.org/2016/09/know-your-customers-jobs-to-be-done) — describir el progreso que la persona busca; autoridad: Harvard Business Review (artículo parcialmente de pago).
- [The Lean Startup: principios](https://theleanstartup.com/principles) — aprendizaje validado y métricas accionables; autoridad: Eric Ries (fuente del autor).

---

[↑ Glosario](../../README.md) · [← Proposición](./proposicion.md) · [Prorrateo →](./prorrateo.md)
