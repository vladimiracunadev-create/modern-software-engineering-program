# Abandono y límites

[↑ Glosario](../../README.md) · [← Abandonar y conservar](./abandonar-y-conservar.md) · [Abanico de uniones →](./abanico-de-uniones.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Criterio de abandono con comparador, umbral, ventana y responsable, más una lista de lo que no se midió ni a quién no se preguntó.

Definición de trabajo de [SE-132 — Proyecto: product brief respaldado por evidencia](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md).

## Por qué importa

En [SE-132 — Proyecto: product brief respaldado por evidencia](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md), el tema «Abandono y límites» importa porque un brief honesto dice cuándo se equivoca y qué no sabe.

## Cómo funciona

Según [SE-132 — Proyecto: product brief respaldado por evidencia](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md), en la sección «Abandono y límites»:

El criterio de abandono se hereda de `SE-130`: umbral, ventana y responsable externo. Los límites dicen qué población no participó, qué contexto no se cubrió y qué supuesto sigue sin contrastarse. Un brief sin límites sugiere que no hay nada que cuestionar. Declararlos no debilita la decisión: protege a quien decide de sorpresas y a las personas afectadas de que un uso no previsto se base en evidencia que no las incluía.

## Ejemplo

Caso medido en la sección «Abandono y límites» de [SE-132 — Proyecto: product brief respaldado por evidencia](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md):

El criterio de abandono se hereda de `SE-130`: umbral, ventana y responsable externo. Los límites dicen qué población no participó, qué contexto no se cubrió y qué supuesto sigue sin contrastarse. Un brief sin límites sugiere que no hay nada que cuestionar. Declararlos no debilita la decisión: protege a quien decide de sorpresas y a las personas afectadas de que un uso no previsto se base en evidencia que no las incluía.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-132 — Proyecto: product brief respaldado por evidencia](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md)) son:

- **El brief pasa el validador pero una cifra no coincide con la evidencia** — causa: el validador solo comprueba estructura. Corrección: añadir una comparación de cifras con la fuente y una lectura humana antes de decidir.
- **La decisión no tiene responsable ni fecha** — causa: se redactó como recomendación general. Corrección: exigir responsable y fecha en el formato y rechazar briefs sin ellos.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-132 — Proyecto: product brief respaldado por evidencia](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos y un validador con evidencias y participantes sintéticos en Windows y Ubuntu (WSL2) con salidas idénticas. El validador solo comprueba estructura, las doce mutaciones no representan todos los defectos posibles y las ponderaciones y rangos son supuestos del autor. La [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md) termina aquí; la [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md) somete el brief a modelos de negocio, costos de construcción y operación, y métricas de producto.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md), [SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md), [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Criterio de abandono](../c/criterio-de-abandono.md), [Ventana](../v/ventana.md), [Brief como contrato de evidencia](../b/brief-como-contrato-de-evidencia.md), [Decisión con rangos](../d/decision-con-rangos.md), [Evidencia trazable](../e/evidencia-trazable.md), [Tipos de evidencia](../t/tipos-de-evidencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-132 — Proyecto: product brief respaldado por evidencia](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md).

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

[↑ Glosario](../../README.md) · [← Abandonar y conservar](./abandonar-y-conservar.md) · [Abanico de uniones →](./abanico-de-uniones.md)
