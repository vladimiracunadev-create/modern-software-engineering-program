# Éxito y no éxito

[↑ Glosario](../../README.md) · [← Exhaustividad](./exhaustividad.md) · [Expandir y contraer →](./expandir-y-contraer.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Par de umbrales fijados antes de observar: por encima del primero se continúa y por debajo del segundo se abandona o se cambia de rumbo.

Definición de trabajo de [SE-130 — Criterios de no éxito y decisiones de abandono](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md).

## Por qué importa

En [SE-130 — Criterios de no éxito y decisiones de abandono](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md), el tema «Éxito y no éxito» importa porque si solo se define el éxito, cualquier resultado intermedio se interpreta como «casi» y la decisión se pospone.

## Cómo funciona

Según [SE-130 — Criterios de no éxito y decisiones de abandono](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md), en la sección «Éxito y no éxito»:

Un criterio de éxito dice qué resultado justifica continuar; uno de no éxito, qué resultado justifica detener. Entre ambos queda una zona intermedia que debe tener su propia decisión (extender hasta una fecha, cambiar el experimento). Un criterio útil tiene cinco elementos: comparador («menos de»), umbral (6 de 30), población (quienes entregaron desde móvil), ventana (4 semanas) y responsable (producto). «Si no funciona, lo dejamos» no tiene ninguno y por eso no se puede incumplir ni cumplir, que es la razón por la que a nadie le molesta escribirlo.

## Ejemplo

Caso medido en la sección «Éxito y no éxito» de [SE-130 — Criterios de no éxito y decisiones de abandono](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md):

Un criterio de éxito dice qué resultado justifica continuar; uno de no éxito, qué resultado justifica detener. Entre ambos queda una zona intermedia que debe tener su propia decisión (extender hasta una fecha, cambiar el experimento). Un criterio útil tiene cinco elementos: comparador («menos de»), umbral (6 de 30), población (quienes entregaron desde móvil), ventana (4 semanas) y responsable (producto). «Si no funciona, lo dejamos» no tiene ninguno y por eso no se puede incumplir ni cumplir, que es la razón por la que a nadie le molesta escribirlo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-130 — Criterios de no éxito y decisiones de abandono](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md)) son:

- **El piloto se extiende sin fin y siempre «casi funciona»** — causa: el criterio de no éxito no existía o no tenía umbral. Corrección: escribir comparador, umbral, población, ventana y responsable antes de empezar.
- **Se abandona una idea que luego otro equipo hace funcionar** — causa: la muestra era demasiado pequeña y el resultado era inconcluso, no negativo. Corrección: distinguir «no hay evidencia» de «hay evidencia en contra» y calcular la zona gris.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-130 — Criterios de no éxito y decisiones de abandono](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con tasas y criterios sintéticos en Windows y Ubuntu (WSL2) con salidas idénticas. No se probó la regla con un piloto real y no se midió el efecto del coste hundido en personas. La siguiente clase aplica todo lo anterior a un taller: convertir una petición en un problema investigable.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Abandonar y conservar](../a/abandonar-y-conservar.md), [Coste hundido y compromiso](../c/coste-hundido-y-compromiso.md), [Reglas de parada](../r/reglas-de-parada.md), [Zona gris](../z/zona-gris.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-130 — Criterios de no éxito y decisiones de abandono](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md).

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

[↑ Glosario](../../README.md) · [← Exhaustividad](./exhaustividad.md) · [Expandir y contraer →](./expandir-y-contraer.md)
