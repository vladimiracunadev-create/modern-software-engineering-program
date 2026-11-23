# Tipos de evidencia

[↑ Glosario](../../README.md) · [← Tipo de programa](./tipo-de-programa.md) · [Tipos y flujo →](./tipos-y-flujo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Clasificación de la evidencia según su origen (dijo, hizo, comprometió, registro), con una ponderación explícita y revisable.

Definición de trabajo de [SE-132 — Proyecto: product brief respaldado por evidencia](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md).

## Por qué importa

En [SE-132 — Proyecto: product brief respaldado por evidencia](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md), el tema «Tipos de evidencia» importa porque lo que alguien hizo o comprometió pesa distinto de lo que dijo; el brief debe declarar el peso.

## Cómo funciona

Según [SE-132 — Proyecto: product brief respaldado por evidencia](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md), en la sección «Tipos de evidencia»:

Lo que una persona dice es el tipo más barato y el menos fiable; lo que hace (copia su texto a un documento aparte) es más fiable; lo que compromete (reserva tiempo, entrega un borrador real) lo es más; un registro (42 tickets) cuenta frecuencia pero no motivos. Al ponderar, el orden de opciones puede cambiar: por eso el peso es una decisión del brief, no un detalle interno, y se muestra la conclusión bajo varias ponderaciones. Una opción que gana solo con un peso es frágil.

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
- **Ver también:** [Evidencia](../e/evidencia.md), [Origen](../o/origen.md), [Registro](../r/registro.md), [Abandono y límites](../a/abandono-y-limites.md), [Brief como contrato de evidencia](../b/brief-como-contrato-de-evidencia.md), [Decisión con rangos](../d/decision-con-rangos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-132 — Proyecto: product brief respaldado por evidencia](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-010](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md), [SE-054](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md), [SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md), [SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md), [SE-517](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md), [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md), [SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md).

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

[↑ Glosario](../../README.md) · [← Tipo de programa](./tipo-de-programa.md) · [Tipos y flujo →](./tipos-y-flujo.md)
