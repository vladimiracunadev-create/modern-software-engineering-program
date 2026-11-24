# Valor del aprendizaje

[↑ Glosario](../../README.md) · [← Valor definido](./valor-definido.md) · [Valor esperado →](./valor-esperado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

El **valor del aprendizaje** es la mejora esperada de una decisión gracias a información obtenida antes de decidir, menos el costo de obtenerla ([SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md)). Es la versión de producto del «valor de la información»: cuánto vale hacer una prueba antes de comprometerse.

## Por qué importa

Una prueba barata puede evitar construir lo que no funciona; una cara o poco fiable no compensa. Cambia la decisión de investigar: no se prueba «por si acaso», se calcula si la información mejora lo bastante la decisión como para pagarla.

## Cómo funciona

[SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md) da un ejemplo con números. Construir un ítem con **35 % de probabilidad de éxito**, ganancia de **100** y coste de **40** tiene un valor esperado de 0,35 × 100 − 40 = **−5**: no conviene.

Ahora una prueba previa que cuesta 5 y acierta el 90 % de las veces (detecta el éxito real con 90 % y da falso positivo con 10 %). La probabilidad de que salga positiva es 0,35 × 0,9 + 0,65 × 0,1 = 0,38. Si sale positiva, la probabilidad de éxito sube a 0,315 / 0,38 ≈ 0,83, y construir vale 0,83 × 100 − 40 ≈ 43. Se construye **solo si la prueba sale positiva**: valor esperado = 0,38 × 43 − 5 ≈ **+11,3**. La prueba convierte una apuesta perdedora en una decisión informada: el valor esperado neto sube de −5 a +11,3, de modo que el aprendizaje, descontado su costo, aporta valor.

Con una prueba que cuesta **15** y acierta solo el **70 %**, el valor esperado neto es **−8,1** y **conviene no hacerla**: la información es poco fiable y cara. El mecanismo general: la prueba vale lo que mejora la decisión menos lo que cuesta, y depende de tres cosas: la probabilidad previa (si ya es casi seguro, no hay qué aprender), la fiabilidad de la prueba y el costo de equivocarse.

La idea se conecta con las preguntas críticas, los experimentos de demanda y las reglas de parada: todas son formas de comprar información barata antes de gastar mucho.

## Ejemplo

Con los datos de [SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md): sin prueba, −5 (no construir, o construir perdiendo); con una prueba de 5 y 90 % de acierto, +11,3; con una de 15 y 70 %, −8,1. La conclusión práctica es hacer la primera y descartar la segunda. (Cifras de la clase; el cálculo detallado es propio y reproduce sus resultados.)

## Errores y confusiones comunes

- **Hacer pruebas por costumbre** sin calcular su valor.
- **Creer que toda información vale**: una prueba cara y poco fiable destruye valor.
- **Ignorar la probabilidad previa.**
- **Confundir valor de aprender con valor esperado del proyecto.**

## Límites y cuándo no aplica

Los cálculos suponen probabilidades y costos estimables; con estimaciones muy inciertas, el resultado también lo es. Para decisiones baratas y reversibles, aprender antes no compensa. El modelo simple supone una prueba con una sola tasa de acierto, que en la práctica varía.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Costo](../c/costo.md), [Coste del retraso](../c/coste-del-retraso.md), [Decisión revisable](../d/decision-revisable.md), [Riesgo y confianza](../r/riesgo-y-confianza.md), [Valor y esfuerzo](./valor-y-esfuerzo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-182](../../../classes/part-15-procesos-planificacion-y-estimacion/se-182-agile-como-principios-y-no-como-ceremonia/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Intercom: RICE, simple prioritization for product managers](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/) — definición de los cuatro factores de RICE; autoridad: Intercom (fuente del autor del método).
- [Scaled Agile Framework: Weighted Shortest Job First](https://scaledagileframework.com/wsjf/) — definición de WSJF y su relación con el coste del retraso; autoridad: Scaled Agile, Inc.
- [Douglas Hubbard: How to Measure Anything](https://www.howtomeasureanything.com/) — valor de la información y cuantificación de la incertidumbre; autoridad: Hubbard Decision Research.
- [Product Talk: Opportunity Solution Tree](https://www.producttalk.org/opportunity-solution-tree/) — estructura para conectar oportunidades, soluciones y experimentos; autoridad: Teresa Torres (fuente del autor).
- [The Lean Startup: principios](https://theleanstartup.com/principles) — aprendizaje validado como unidad de progreso; autoridad: Eric Ries (fuente del autor).

---

[↑ Glosario](../../README.md) · [← Valor definido](./valor-definido.md) · [Valor esperado →](./valor-esperado.md)
