# Modelo de ingreso

[↑ Glosario](../../README.md) · [← Modelo de información](./modelo-de-informacion.md) · [Modelo de nivel de teclado →](./modelo-de-nivel-de-teclado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Regla que convierte uso o presencia de un cliente en dinero (por alumno, plano, gratuito con conversión).

Definición de trabajo de [SE-133 — Modelos de negocio y sostenibilidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md).

## Por qué importa

En [SE-133 — Modelos de negocio y sostenibilidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md), el tema «Modelos de ingreso» importa porque el mismo uso produce ingresos muy distintos según se cobre por alumno, por centro o con un nivel gratuito.

## Cómo funciona

Según [SE-133 — Modelos de negocio y sostenibilidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md), en la sección «Modelos de ingreso»:

Cobrar por alumno hace que el ingreso crezca con el tamaño del centro y con el costo de servirlo; un precio plano por centro simplifica la venta pero subsidia a los grandes; un nivel gratuito reduce la fricción de entrada y traslada el costo de servir a quienes pagan. Ninguno es mejor en abstracto: cada uno reparte de otra manera el riesgo (¿quién paga si el uso baja?) y el incentivo (¿qué se premia?). Elegir modelo es elegir qué hipótesis se apuesta a sostener, y el Business Model Canvas ayuda a nombrarla, no a probarla.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-133 — Modelos de negocio y sostenibilidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md):

En la plataforma de entregas, el modelo vive en `viability-log.md` con una fila por supuesto: nombre, unidad, mínimo, moda, máximo, fuente y estado (medido, derivado, suposición). El contrato del registro es que ningún resultado se informa sin la fila de supuestos que lo produjo y que cambiar una fila cambia la fecha del resultado. Esa separación permite que un revisor recalcule el modelo con otros valores.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-133 — Modelos de negocio y sostenibilidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md)) son:

- **La hoja muestra 11 veces y la dirección pide más ventas sin preguntar nada** — causa: se informó la razón con valores centrales y sin intervalo. Corrección: informar p5, mediana y p95 con el supuesto que más contribuye.
- **El plan se equilibra en el mes 4 y la caja se agota en el mes 8** — causa: se miró el flujo mensual y no la caja acumulada. Corrección: calcular la caja mínima y financiar hasta ese punto.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-133 — Modelos de negocio y sostenibilidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ningún centro, mercado ni empresa; los rangos, precios y costos son supuestos del autor en unidades monetarias ficticias, y los factores se muestrearon de forma independiente. La siguiente clase descompone el costo que aquí entró como un solo número.

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
