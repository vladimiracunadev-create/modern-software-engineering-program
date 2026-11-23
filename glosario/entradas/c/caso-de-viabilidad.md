# Caso de viabilidad

[↑ Glosario](../../README.md) · [← Caso de seguridad](./caso-de-seguridad.md) · [Caso mínimo y representatividad →](./caso-minimo-y-representatividad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Documento que expone supuestos, modelo, resultado con incertidumbre, regla de salida y decisión, de modo que otra persona pueda recalcularlo.

Definición de trabajo de [SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md).

## Por qué importa

La clase donde se define, [SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md), existe con este propósito: el proyecto existe para reunir modelo de negocio, costos, métricas, riesgos y reversibilidad en un caso de viabilidad que otra persona puede recalcular, cuestionar y decidir sin pedir contexto: un valor presente con rango, un supuesto dominante, una regla de abandono y una decisión con responsable y fecha.

## Cómo funciona

Según [SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md):

**Cómo leer la figura.** Cada barra es un grupo de mutaciones del caso de viabilidad, con su número entre paréntesis; el tramo teal son las que detecta el validador y el coral las que sobreviven. Estructura y completitud, coherencia y trazabilidad se detectan por completo (12 de 12); las cuatro que sobreviven respetan la forma y no la verdad. **Dónde deja de valer:** las mutaciones las escribió quien escribió el validador, y 12 de 16 es una estimación optimista. Es el mismo reparto que en un brief: la forma se comprueba, la verdad no. Para los cuatro supervivientes hace falta una persona que recalcule el modelo y compare cada afirmación con su evidencia.

## Ejemplo

Ejemplo de [SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md) (sección «Caso conductor»):

La plataforma de entregas de tareas cierra aquí su recorrido por la [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md) con un caso de viabilidad. Reúne el modelo de negocio (`SE-133`), el costo de propiedad (`SE-134`), las definiciones de adopción y retención (`SE-136`), el árbol de métricas (`SE-143`) y las reglas de reversibilidad (`SE-142`). La [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md) usará este caso como contexto para elicitar, analizar y especificar requisitos. Cambia después un supuesto —por ejemplo, el tamaño de los centros— y revisa qué conclusiones del caso cambian.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md)) son:

- **El caso se aprueba con un valor presente de 34 mil y falla** — causa: se informó solo el punto. Corrección: informar el intervalo y la probabilidad de valor positivo.
- **El equipo mide el costo de construcción y no el tamaño de los centros** — causa: no se calculó la oscilación por supuesto. Corrección: ordenar los supuestos por oscilación y medir el primero.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con las fuentes enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se evaluó ninguna plataforma, mercado ni empresa real; los rangos, la forma del modelo, la independencia entre supuestos, el ruido de la señal del mes 6 y las dieciséis mutaciones son supuestos o elecciones del autor, de modo que la exactitud real del validador es desconocida.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Documento](../d/documento.md), [Incertidumbre](../i/incertidumbre.md), [Modelo](../m/modelo.md), [Regla](../r/regla.md), [Compuerta de abandono](./compuerta-de-abandono.md), [Decisión revisable](../d/decision-revisable.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md), [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), [SE-140](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md), [SE-141](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md), [SE-142](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-142-decisiones-reversibles-e-irreversibles/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [HM Treasury: The Green Book](https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-governent/the-green-book-2020) — evaluación de opciones, descuento, sensibilidad y sesgo de optimismo; autoridad: HM Treasury (Reino Unido).
- [GOV.UK Service Manual: How the beta phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-beta-phase-works) — fases con puntos de decisión y evidencia; autoridad: Government Digital Service.
- [GOV.UK Service Manual: How the alpha phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works) — probar incertidumbres antes de construir; autoridad: Government Digital Service.
- [GOV.UK Service Manual: Measuring success](https://www.gov.uk/service-manual/measuring-success) — indicadores con cálculo, fuente y uso; autoridad: Government Digital Service.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — economía de la ingeniería de software, riesgo e incertidumbre; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Caso de seguridad](./caso-de-seguridad.md) · [Caso mínimo y representatividad →](./caso-minimo-y-representatividad.md)
