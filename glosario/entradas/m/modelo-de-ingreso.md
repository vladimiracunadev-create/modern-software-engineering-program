# Modelo de ingreso

[↑ Glosario](../../README.md) · [← Modelo de información](./modelo-de-informacion.md) · [Modelo de nivel de teclado →](./modelo-de-nivel-de-teclado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Un **modelo de ingreso** es la regla que convierte el uso o la presencia de un cliente en dinero: cobrar por alumno, un precio plano por centro, un nivel gratuito con conversión a pago ([SE-133](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md)). Es una de las decisiones de un modelo de negocio y se distingue del precio concreto: el modelo dice *por qué unidad* y *bajo qué condiciones* se cobra.

## Por qué importa

El mismo uso produce ingresos muy distintos según el modelo. Elegirlo es elegir quién asume el riesgo y qué conducta se premia. Cambia decisiones de producto: qué funcionalidad se limita, a quién se vende, qué métrica se vigila y cuánto cuesta servir a cada cliente.

## Cómo funciona

[SE-133](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md) compara tres modelos de la plataforma de entregas con su mecanismo:

- **Por alumno**: el ingreso crece con el tamaño del centro y con el costo de servirlo; el riesgo de que el uso baje recae en quien vende, porque el ingreso baja con el uso.
- **Precio plano por centro**: simplifica la venta, pero subsidia a los grandes (pagan lo mismo que los pequeños aunque cuesten más de servir) y desconecta el ingreso del uso.
- **Nivel gratuito**: reduce la fricción de entrada y traslada el costo de servir a quienes pagan; solo funciona si una fracción suficiente convierte.

Ninguno es mejor en abstracto: cada uno reparte de otra manera el riesgo («¿quién paga si el uso baja?») y el incentivo («¿qué se premia?»). Por eso la clase dice que elegir modelo es elegir qué hipótesis se apuesta a sostener, y que el Business Model Canvas ayuda a nombrarla, no a probarla. La prueba viene de un modelo de viabilidad con supuestos explícitos: una fila por supuesto (nombre, unidad, mínimo, moda, máximo, fuente y estado: medido, derivado o suposición), de modo que cambiar una fila cambia la fecha del resultado y alguien puede recalcular con otros valores.

## Ejemplo

[SE-133](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md) muestra con un modelo de viabilidad por qué no basta un número: la hoja da «11 veces» (ingreso sobre costo) y la dirección pide más ventas sin preguntar nada, porque se informó la razón con valores centrales y sin intervalo; la corrección es informar p5, mediana y p95 con el supuesto que más contribuye. Y un plan que se equilibra en el mes 4 puede agotar la caja en el mes 8 si se miró el flujo mensual y no la caja acumulada: se calcula la caja mínima y se financia hasta ese punto.

## Errores y confusiones comunes

- **Informar la razón con valores centrales y sin intervalo.**
- **Mirar el flujo mensual y no la caja acumulada.**
- **Confundir modelo de ingreso con precio**: el precio puede cambiar sin cambiar el modelo.
- **Elegir un modelo copiando a otro sector** sin revisar quién paga el costo de servir.

## Límites y cuándo no aplica

El modelo depende de supuestos que el equipo no controla (disposición a pagar, tasa de conversión). Los rangos de [SE-133](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md) son del autor y su modelo no reemplaza datos reales; las cifras sirven para mostrar el razonamiento. En productos con un solo cliente grande o contrato a medida, el «modelo» es una negociación, no una regla general.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Regla](../r/regla.md), [Concentración](../c/concentracion.md), [Margen de contribución](./margen-de-contribucion.md), [Pagador, usuario y decisor](../p/pagador-usuario-y-decisor.md), [Valor de vida y costo de adquisición](../v/valor-de-vida-y-costo-de-adquisicion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-133 — Modelos de negocio y sostenibilidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Modelos de ingreso».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Open Source Guides: Getting paid for open source work](https://opensource.guide/getting-paid/) — decisiones de financiación y sostenimiento de un proyecto; autoridad: GitHub, con contribuciones de la comunidad.
- [Strategyzer: The Business Model Canvas](https://www.strategyzer.com/library/the-business-model-canvas) — descripción de un modelo de negocio por bloques; autoridad: Strategyzer (Osterwalder y Pigneur).
- [Why Business Models Matter (Harvard Business Review, 2002)](https://hbr.org/2002/05/why-business-models-matter) — qué es un modelo de negocio y por qué debe poder contrastarse; autoridad: Harvard Business Review (artículo parcialmente de pago).
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — economía de la ingeniería de software y medición; autoridad: IEEE Computer Society.
- [GOV.UK Service Manual: Measuring success](https://www.gov.uk/service-manual/measuring-success) — cómo medir si un servicio cumple su propósito; autoridad: Government Digital Service (Reino Unido).

---

[↑ Glosario](../../README.md) · [← Modelo de información](./modelo-de-informacion.md) · [Modelo de nivel de teclado →](./modelo-de-nivel-de-teclado.md)
