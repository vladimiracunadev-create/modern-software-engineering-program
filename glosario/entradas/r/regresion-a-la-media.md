# Regresión a la media

[↑ Glosario](../../README.md) · [← Regresión](./regresion.md) · [Regresión de resiliencia →](./regresion-de-resiliencia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Tendencia de los casos extremos de una medición ruidosa a acercarse al promedio en la siguiente.

Definición de trabajo de [SE-138 — Experimentos, sesgos y causalidad básica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md).

## Por qué importa

En [SE-138 — Experimentos, sesgos y causalidad básica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md), el tema «Regresión a la media» importa porque los casos extremos en una medición ruidosa tienden a acercarse al promedio en la siguiente.

## Cómo funciona

Según [SE-138 — Experimentos, sesgos y causalidad básica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md), en la sección «Regresión a la media»:

Una medición es el valor verdadero más ruido. Si se selecciona a los peores por una primera medición, parte de su mala posición es ruido que no se repetirá: en la segunda medición se acercarán al promedio sin intervención. Un programa dirigido a los peores y evaluado «antes y después» atribuye esa mejora al programa. Cuanto menos fiable la medición, mayor la regresión.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-138 — Experimentos, sesgos y causalidad básica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md):

En la plataforma, `experiment-readout.md` registra por experimento: unidad asignada, mecanismo de asignación, proporciones esperadas y observadas con el resultado del control, población y ventana, métrica primaria con su métrica contraria, efecto estimado con intervalo y límites. El contrato es que ningún efecto se informa si el control de proporciones falló, y que toda comparación observacional se rotula como tal.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El programa de apoyo «funcionó» en el peor decil** — causa: regresión a la media. Corrección: comparar con un grupo seleccionado igual. ([SE-138](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-138 — Experimentos, sesgos y causalidad básica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con las fuentes enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se asignó a ninguna persona real, el efecto verdadero lo fija el generador y los parámetros de confusión, ruido y pérdida son supuestos del autor. La siguiente clase usa métricas con contrapesos para evitar que un experimento optimice una cifra a costa de otra.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Extremo](../e/extremo.md), [Medición](../m/medicion.md), [Asignación aleatoria](../a/asignacion-aleatoria.md), [Contrafactual](../c/contrafactual.md), [Desajuste de proporción de muestra](../d/desajuste-de-proporcion-de-muestra.md), [Sesgo de selección](../s/sesgo-de-seleccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-138 — Experimentos, sesgos y causalidad básica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Trustworthy Online Controlled Experiments](https://experimentguide.com/) — diseño, calidad y análisis de experimentos controlados en línea; autoridad: R. Kohavi, D. Tang y Y. Xu (Cambridge University Press).
- [Diagnosing Sample Ratio Mismatch in Online Controlled Experiments (KDD 2019)](https://exp-platform.com/Documents/2019_KDDFabijanGupchupFuptaOmhoverVermeerDmitriev.pdf) — taxonomía y reglas para diagnosticar un desajuste de asignación; autoridad: A. Fabijan y colaboradores (Microsoft).
- [GOV.UK Service Manual: Measuring success](https://www.gov.uk/service-manual/measuring-success) — usar datos para decidir cómo mejorar un servicio; autoridad: Government Digital Service.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — medición y evidencia empírica en ingeniería de software; autoridad: IEEE Computer Society.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generadores con semilla.

---

[↑ Glosario](../../README.md) · [← Regresión](./regresion.md) · [Regresión de resiliencia →](./regresion-de-resiliencia.md)
