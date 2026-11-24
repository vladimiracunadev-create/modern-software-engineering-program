# Segmentación por necesidad

[↑ Glosario](../../README.md) · [← Segmentación](./segmentacion.md) · [Segmento →](./segmento.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

La **segmentación por necesidad** agrupa a las personas que comparten un trabajo, un contexto y resultados insatisfechos, y que justifican una decisión de producto distinta de la del resto ([SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md)). Se opone a segmentar por rasgos de superficie como edad, cargo o región.

## Por qué importa

Un segmento útil se distingue por lo que necesita y hace, y **cambia qué se construye**. Segmentar por edad o cargo es fácil de medir y casi nunca cambia el producto: dos personas del mismo cargo pueden tener necesidades opuestas, y dos de cargos distintos, la misma. Cambia a quién se le diseña, cómo se llega a esa gente y cuánto está dispuesta a esforzarse.

## Cómo funciona

[SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md) plantea una prueba de utilidad con dos preguntas: ¿el segmento cambia una decisión (qué se construye, cómo se llega a él, cuánto está dispuesto a esforzarse)? ¿El equipo puede **reconocer** a una persona como parte de él? Un segmento que nadie puede identificar no se puede alcanzar ni validar. Un ejemplo de la clase: quienes entregan desde móvil con conexión débil. Lo define el contexto y el trabajo, no un dato demográfico.

El mapa de segmentos de la plataforma de entregas conserva, por segmento: el criterio de definición, los trabajos, los contextos, los resultados insatisfechos, el tamaño como rango con método y supuestos, el canal de acceso y las alternativas con los trabajos que cubren. Dos reglas del contrato: ningún segmento se declara sin decir cómo se reconocería a una persona de él, y ninguna cifra de mercado se publica sin su rango.

Cuando los segmentos se derivan con un algoritmo de agrupamiento, hay que añadir dos controles: la **estabilidad** (el agrupamiento debe reproducirse con otra semilla o submuestra, y compararse con la estabilidad sobre ruido) y el **significado** (los grupos deben diferir en comportamiento o necesidad). Un agrupamiento estable pero sin significado de negocio no es un segmento.

## Ejemplo

Segmentación por cargo: «docentes». Segmentación por necesidad: «docentes que corrigen en el móvil entre clases y necesitan ver quién entregó sin abrir cada entrega», «docentes que gestionan cursos de 200 estudiantes y necesitan correcciones por lote». El primero se resuelve con un panel compacto; el segundo, con flujos de lote. Dos decisiones de producto distintas dentro del mismo cargo. (Ejemplo ilustrativo apoyado en el patrón de [SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md).)

## Errores y confusiones comunes

- **Segmentos que cambian al repetir el análisis**: agrupamiento inestable.
- **Segmentos estables que nadie reconoce**: estabilidad sobre ruido o variables sin sentido de negocio.
- **Segmentar por lo que es fácil de medir.**
- **Publicar el tamaño de mercado como cifra única.**

## Límites y cuándo no aplica

Cuando hay un solo trabajo y un contexto homogéneo, segmentar no aporta. Los segmentos por necesidad exigen investigación cualitativa, que es costosa y se hace con pocas personas: son hipótesis con incertidumbre. Un segmento puede mezclar necesidades que solo se separan al construir. Y los segmentos cambian cuando cambia el contexto.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](../c/contextos.md), [Producto](../p/producto.md), [Resultado](../r/resultado.md), [Trabajo](../t/trabajo.md), [Alternativas existentes](../a/alternativas-existentes.md), [Estabilidad de segmentos](../e/estabilidad-de-segmentos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-126 — Segmentación, mercado y alternativas existentes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Strategyn: Outcome-Driven Innovation](https://strategyn.com/outcome-driven-innovation-process/) — segmentación por necesidades insatisfechas; autoridad: Strategyn (fuente del autor del método).
- [Ben-Hur, Elisseeff y Guyon (2002): A stability based method for discovering structure in clustered data](https://psb.stanford.edu/psb-online/proceedings/psb02/benhur.pdf) — estabilidad de agrupamientos ante submuestras; autoridad: Pacific Symposium on Biocomputing.
- [Douglas Hubbard: How to Measure Anything](https://www.howtomeasureanything.com/) — rangos e incertidumbre en la estimación; autoridad: Hubbard Decision Research.
- [Strategyzer: Value Proposition Canvas](https://www.strategyzer.com/library/the-value-proposition-canvas) — ajuste entre propuesta y perfil de cliente; autoridad: Strategyzer.
- [Know Your Customers' «Jobs to Be Done» (Harvard Business Review, 2016)](https://hbr.org/2016/09/know-your-customers-jobs-to-be-done) — trabajos como base de la competencia; autoridad: Harvard Business Review (artículo parcialmente de pago).

---

[↑ Glosario](../../README.md) · [← Segmentación](./segmentacion.md) · [Segmento →](./segmento.md)
