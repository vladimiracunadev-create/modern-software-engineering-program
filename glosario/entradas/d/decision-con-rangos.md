# Decisión con rangos

[↑ Glosario](../../README.md) · [← Decisión con plazo](./decision-con-plazo.md) · [Decisión de entrega →](./decision-de-entrega.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Decisión que compara opciones con intervalos de beneficio y declara la probabilidad de que una supere a otra y el costo de equivocarse.

Definición de trabajo de [SE-132 — Proyecto: product brief respaldado por evidencia](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md).

## Por qué importa

En [SE-132 — Proyecto: product brief respaldado por evidencia](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md), el tema «Decisión con rangos» importa porque cuando los rangos de beneficio se solapan, declarar un ganador es fingir precisión.

## Cómo funciona

Según [SE-132 — Proyecto: product brief respaldado por evidencia](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md), en la sección «Decisión con rangos»:

Si dos opciones tienen beneficios de 30 y 33 con rangos amplios y solapados, la mediana más alta no basta: la probabilidad de que una supere a la otra puede ser cercana al 50 %. El brief entonces recomienda aprender más (con el plan de `SE-127`), elegir la opción reversible o la de menor peor caso, y no declarar un ganador. Cuando una opción domina claramente, lo dice con la probabilidad. La decisión incluye responsable y fecha para que no se difumine.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-132 — Proyecto: product brief respaldado por evidencia](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md):

En la plataforma de entregas, el brief se acompaña de un expediente: tickets y su agrupación, mapa de actores, transcripciones y códigos, mapa de hipótesis, propuesta, mapa de mercado, plan de experimento, registro de prioridad, protocolo ético, reglas de parada y petición descompuesta. El contrato es que `brief.md` remite a ellos por identificador, que cada afirmación declare sus evidencias, que la decisión indique responsable y fecha, y que el validador pase en un checkout limpio.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-132 — Proyecto: product brief respaldado por evidencia](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md)) son:

- **El brief pasa el validador pero una cifra no coincide con la evidencia** — causa: el validador solo comprueba estructura. Corrección: añadir una comparación de cifras con la fuente y una lectura humana antes de decidir.
- **La decisión no tiene responsable ni fecha** — causa: se redactó como recomendación general. Corrección: exigir responsable y fecha en el formato y rechazar briefs sin ellos.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-132 — Proyecto: product brief respaldado por evidencia](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos y un validador con evidencias y participantes sintéticos en Windows y Ubuntu (WSL2) con salidas idénticas. El validador solo comprueba estructura, las doce mutaciones no representan todos los defectos posibles y las ponderaciones y rangos son supuestos del autor. La [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md) termina aquí; la [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md) somete el brief a modelos de negocio, costos de construcción y operación, y métricas de producto.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md), [SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md), [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Costo](../c/costo.md), [Intervalo](../i/intervalo.md), [Opción](../o/opcion.md), [Abandono y límites](../a/abandono-y-limites.md), [Brief como contrato de evidencia](../b/brief-como-contrato-de-evidencia.md), [Evidencia trazable](../e/evidencia-trazable.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-132 — Proyecto: product brief respaldado por evidencia](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) — qué producir al terminar la discovery y cómo decidir si avanzar; autoridad: Government Digital Service.
- [GOV.UK Service Manual: User research](https://www.gov.uk/service-manual/user-research) — investigación con personas usuarias durante el desarrollo; autoridad: Government Digital Service.
- [Nielsen Norman Group: User Interviews 101](https://www.nngroup.com/articles/user-interviews/) — entrevista de usuario como método cualitativo; autoridad: Nielsen Norman Group.
- [Douglas Hubbard: How to Measure Anything](https://www.howtomeasureanything.com/) — rangos, incertidumbre y valor de la información; autoridad: Hubbard Decision Research.
- [The Menlo Report (U.S. Department of Homeland Security)](https://www.dhs.gov/publication/menlo-report) — principios éticos de la investigación en tecnologías de la información; autoridad: U.S. Department of Homeland Security.

---

[↑ Glosario](../../README.md) · [← Decisión con plazo](./decision-con-plazo.md) · [Decisión de entrega →](./decision-de-entrega.md)
