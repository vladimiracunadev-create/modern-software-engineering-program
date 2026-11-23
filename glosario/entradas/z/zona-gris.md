# Zona gris

[↑ Glosario](../../README.md) · [← Zona cruda](./zona-cruda.md) · [Zona muerta →](./zona-muerta.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Rango de resultados que no permite distinguir con la confianza declarada entre el éxito y el no éxito.

Definición de trabajo de [SE-130 — Criterios de no éxito y decisiones de abandono](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md).

## Por qué importa

En [SE-130 — Criterios de no éxito y decisiones de abandono](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md), el tema «Zona gris» importa porque con pocas personas casi todo resultado cae entre «sí» y «no»; el diseño debe prever qué hacer ahí.

## Cómo funciona

Según [SE-130 — Criterios de no éxito y decisiones de abandono](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md), en la sección «Zona gris»:

Si la tasa buena es 15 % y la mala 5 %, con 30 personas muchas pruebas no podrán decir cuál es la real: el resultado «inconcluso» es frecuente. Reconocer la zona gris obliga a decidir de antemano si se amplía la muestra, se acepta la incertidumbre o se cambia de prueba. Equivale a admitir que no todo experimento decide. Un criterio que no admite zona gris suele esconder la decisión real en un empate al que se responde con lo que el equipo ya quería.

## Ejemplo

Ejemplo de [SE-130 — Criterios de no éxito y decisiones de abandono](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md) (sección «Ejemplo profesional»):

En la plataforma de entregas, el documento de abandono conserva por cada hipótesis: criterio de éxito, criterio de no éxito, zona gris con su acción, regla de parada y su error simulado, ventana, responsable (externo al equipo que construye), fecha de fijación, y el cierre: qué se aprendió, qué se desmonta, qué reabriría la idea. El contrato es que el criterio se fecha antes de empezar y que cualquier cambio se registra con quién lo aprobó.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se abandona una idea que luego otro equipo hace funcionar** — causa: la muestra era demasiado pequeña y el resultado era inconcluso, no negativo. Corrección: distinguir «no hay evidencia» de «hay evidencia en contra» y calcular la zona gris. ([SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Reconocer la zona gris obliga a decidir de antemano si se amplía la muestra, se acepta la incertidumbre o se cambia de prueba. ([SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Confianza](../c/confianza.md), [Rango](../r/rango.md), [Resultado](../r/resultado.md), [Abandonar y conservar](../a/abandonar-y-conservar.md), [Coste hundido y compromiso](../c/coste-hundido-y-compromiso.md), [Éxito y no éxito](../e/exito-y-no-exito.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-130 — Criterios de no éxito y decisiones de abandono](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md).

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

[↑ Glosario](../../README.md) · [← Zona cruda](./zona-cruda.md) · [Zona muerta →](./zona-muerta.md)
