# Contrafactual

[↑ Glosario](../../README.md) · [← Contraejemplo mínimo](./contraejemplo-minimo.md) · [Contrapresión →](./contrapresion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Lo que habría ocurrido a las mismas personas sin la intervención; no se observa.

Definición de trabajo de [SE-138 — Experimentos, sesgos y causalidad básica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md).

## Por qué importa

En [SE-138 — Experimentos, sesgos y causalidad básica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md), el tema «Contrafactual y asignación» importa porque un efecto causal es la diferencia con lo que habría ocurrido sin intervención; la aleatorización fabrica un contrafactual comparable.

## Cómo funciona

[SE-138 — Experimentos, sesgos y causalidad básica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con las fuentes enlazadas al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-138 — Experimentos, sesgos y causalidad básica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md):

En la plataforma, `experiment-readout.md` registra por experimento: unidad asignada, mecanismo de asignación, proporciones esperadas y observadas con el resultado del control, población y ventana, métrica primaria con su métrica contraria, efecto estimado con intervalo y límites. El contrato es que ningún efecto se informa si el control de proporciones falló, y que toda comparación observacional se rotula como tal.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-138 — Experimentos, sesgos y causalidad básica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md)) son:

- **La función «mejora» las entregas en 2,6 y al desplegarla no ocurre nada** — causa: se comparó a quienes eligen adoptar. Corrección: asignar al azar o rotular como asociación.
- **Un experimento de 10 000 personas reparte 46 % y 54 % y nadie lo cuestiona** — causa: el control de proporciones no se aplicó. Corrección: aplicar el control antes de analizar y corregir la asignación.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-138 — Experimentos, sesgos y causalidad básica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con las fuentes enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se asignó a ninguna persona real, el efecto verdadero lo fija el generador y los parámetros de confusión, ruido y pérdida son supuestos del autor. La siguiente clase usa métricas con contrapesos para evitar que un experimento optimice una cifra a costa de otra.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Asignación aleatoria](../a/asignacion-aleatoria.md), [Desajuste de proporción de muestra](../d/desajuste-de-proporcion-de-muestra.md), [Regresión a la media](../r/regresion-a-la-media.md), [Sesgo de selección](../s/sesgo-de-seleccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-138 — Experimentos, sesgos y causalidad básica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md).

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

[↑ Glosario](../../README.md) · [← Contraejemplo mínimo](./contraejemplo-minimo.md) · [Contrapresión →](./contrapresion.md)
