# Asignación aleatoria

[↑ Glosario](../../README.md) · [← Asiento de doble entrada](./asiento-de-doble-entrada.md) · [Asignación masiva →](./asignacion-masiva.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Reparto por azar de las unidades entre grupos para que solo la intervención los distinga en promedio.

Definición de trabajo de [SE-138 — Experimentos, sesgos y causalidad básica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md).

## Por qué importa

La clase donde se define, [SE-138 — Experimentos, sesgos y causalidad básica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md), existe con este propósito: la clase existe para distinguir una diferencia observada de un efecto causado, y para saber cuándo un experimento con asignación al azar es posible, cuándo se ha roto y qué se puede afirmar sin él.

## Cómo funciona

Según [SE-138 — Experimentos, sesgos y causalidad básica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md):

Decir que una función «causó» una mejora es decir que sin ella la mejora no habría ocurrido. Ese «sin ella» no se observa para la misma persona. La asignación aleatoria crea dos grupos que, en promedio, solo difieren en la intervención; su diferencia estima el efecto. Para que valga, la unidad asignada (persona, centro, sesión) debe coincidir con la unidad analizada y los grupos no deben contaminarse.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-138 — Experimentos, sesgos y causalidad básica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md):

En la plataforma, `experiment-readout.md` registra por experimento: unidad asignada, mecanismo de asignación, proporciones esperadas y observadas con el resultado del control, población y ventana, métrica primaria con su métrica contraria, efecto estimado con intervalo y límites. El contrato es que ningún efecto se informa si el control de proporciones falló, y que toda comparación observacional se rotula como tal.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-138 — Experimentos, sesgos y causalidad básica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md)) son:

- **La función «mejora» las entregas en 2,6 y al desplegarla no ocurre nada** — causa: se comparó a quienes eligen adoptar. Corrección: asignar al azar o rotular como asociación.
- **Un experimento de 10 000 personas reparte 46 % y 54 % y nadie lo cuestiona** — causa: el control de proporciones no se aplicó. Corrección: aplicar el control antes de analizar y corregir la asignación.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La asignación aleatoria crea dos grupos que, en promedio, solo difieren en la intervención; su diferencia estima el efecto. ([SE-138](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contrafactual](../c/contrafactual.md), [Desajuste de proporción de muestra](../d/desajuste-de-proporcion-de-muestra.md), [Regresión a la media](../r/regresion-a-la-media.md), [Sesgo de selección](../s/sesgo-de-seleccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-138 — Experimentos, sesgos y causalidad básica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md), [SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md).

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

[↑ Glosario](../../README.md) · [← Asiento de doble entrada](./asiento-de-doble-entrada.md) · [Asignación masiva →](./asignacion-masiva.md)
