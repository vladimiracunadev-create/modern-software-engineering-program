# Reglas de parada

[↑ Glosario](../../README.md) · [← Regla semántica](./regla-semantica.md) · [Regresión →](./regresion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Procedimiento que, tras cada observación o lote, decide continuar, detener por futilidad o detener por éxito, con tasas de error conocidas.

Definición de trabajo de [SE-130 — Criterios de no éxito y decisiones de abandono](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md).

## Por qué importa

En [SE-130 — Criterios de no éxito y decisiones de abandono](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md), el tema «Reglas de parada» importa porque una regla fijada de antemano ahorra recursos cuando la idea es mala y limita cuántas ideas buenas se pierden.

## Cómo funciona

Según [SE-130 — Criterios de no éxito y decisiones de abandono](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md), en la sección «Reglas de parada»:

Una regla de futilidad abandona si, dado lo observado, la probabilidad de que la tasa real supere el umbral cae por debajo de un valor declarado (por ejemplo, 5 %). Ahorra personas cuando la idea es mala, a costa de un pequeño porcentaje de ideas buenas abandonadas por mala suerte. Ese porcentaje es una elección: se calcula por simulación y se acepta o no. Lo que no vale es decidir sobre la marcha; las reglas secuenciales con garantías (y no el análisis repetido con una prueba clásica) son lo que permite parar antes sin inflar el error.

## Ejemplo

Ejemplo de [SE-130 — Criterios de no éxito y decisiones de abandono](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md) (sección «Ejemplo profesional»):

En la plataforma de entregas, el documento de abandono conserva por cada hipótesis: criterio de éxito, criterio de no éxito, zona gris con su acción, regla de parada y su error simulado, ventana, responsable (externo al equipo que construye), fecha de fijación, y el cierre: qué se aprendió, qué se desmonta, qué reabriría la idea. El contrato es que el criterio se fecha antes de empezar y que cualquier cambio se registra con quién lo aprobó.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La regla de parada abandona demasiadas ideas buenas** — causa: umbral de futilidad demasiado alto para el costo de perder una idea buena. Corrección: simular el error con tasas realistas y elegir el umbral con el costo en la mano. ([SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-130 — Criterios de no éxito y decisiones de abandono](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con tasas y criterios sintéticos en Windows y Ubuntu (WSL2) con salidas idénticas. No se probó la regla con un piloto real y no se midió el efecto del coste hundido en personas. La siguiente clase aplica todo lo anterior a un taller: convertir una petición en un problema investigable.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Lote](../l/lote.md), [Observación](../o/observacion.md), [Abandonar y conservar](../a/abandonar-y-conservar.md), [Coste hundido y compromiso](../c/coste-hundido-y-compromiso.md), [Éxito y no éxito](../e/exito-y-no-exito.md), [Zona gris](../z/zona-gris.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-130 — Criterios de no éxito y decisiones de abandono](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-581](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md), [SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md), [SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md), [SE-582](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md), [SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md), [SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md), [SE-190](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md), [SE-588](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) — decidir al final de la discovery si avanzar o detenerse; autoridad: Government Digital Service.
- [The Lean Startup: principios](https://theleanstartup.com/principles) — aprendizaje validado y decisión de pivotar o perseverar; autoridad: Eric Ries (fuente del autor).
- [Johari, Pekelis y Walsh: Always Valid Inference (arXiv:1512.04922)](https://arxiv.org/abs/1512.04922) — inferencia secuencial válida con monitoreo continuo; autoridad: preprint de investigación.
- [Brown, Cai y DasGupta: Interval Estimation for a Binomial Proportion (Statistical Science, 2001)](https://projecteuclid.org/journals/statistical-science/volume-16/issue-2/Interval-Estimation-for-a-Binomial-Proportion/10.1214/ss/1009213286.full) — intervalos para proporciones con muestras pequeñas; autoridad: Statistical Science.
- [Douglas Hubbard: How to Measure Anything](https://www.howtomeasureanything.com/) — valor de la información y costo de decidir con incertidumbre; autoridad: Hubbard Decision Research.

---

[↑ Glosario](../../README.md) · [← Regla semántica](./regla-semantica.md) · [Regresión →](./regresion.md)
