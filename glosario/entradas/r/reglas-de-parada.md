# Reglas de parada

[↑ Glosario](../../README.md) · [← Regla semántica](./regla-semantica.md) · [Regresión →](./regresion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Una **regla de parada** es un procedimiento que, tras cada observación o lote, decide continuar, detener por futilidad o detener por éxito, con tasas de error conocidas ([SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md)). Se fija antes de empezar el experimento, junto con los criterios de éxito y de no éxito.

## Por qué importa

Una regla fijada de antemano ahorra recursos cuando la idea es mala y limita cuántas ideas buenas se pierden. Sin regla, la decisión de seguir o parar se toma mirando los datos y bajo presión, con tendencia a seguir con ideas que no funcionan o a parar con las que podrían. Cambia la gestión de experimentos: parar es una decisión prevista, no una improvisación.

## Cómo funciona

[SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md) describe la **regla de futilidad**: se abandona si, dado lo observado, la probabilidad de que la tasa real supere el umbral cae por debajo de un valor declarado (por ejemplo, 5 %). Por ejemplo, si el éxito exige una tasa de al menos 10 % y tras 60 personas se han observado 2 conversiones, la probabilidad posterior de que la tasa real supere 10 % es pequeña y la regla ordena parar.

El **costo** está declarado: ahorra personas cuando la idea es mala, **a costa de un pequeño porcentaje de ideas buenas abandonadas por mala suerte**. Ese porcentaje es una elección y se calcula por **simulación**: se simula una idea buena y se cuenta con qué frecuencia la regla la abandonaría. El umbral se elige con el costo en la mano: cuánto cuesta perder una idea buena frente a cuánto cuesta seguir con una mala. Lo que no vale es decidir sobre la marcha, mirando los resultados repetidamente y parando cuando conviene, lo que infla los errores.

El documento de abandono de la plataforma conserva por cada hipótesis: criterio de éxito, criterio de no éxito, **zona gris** con su acción, regla de parada y su error simulado, ventana, responsable (externo al equipo que construye, para evitar sesgos), fecha de fijación y el cierre: qué se aprendió, qué se desmonta y qué reabriría la idea. El criterio se fecha antes de empezar y no se reescribe tras mirar.

## Ejemplo

Hipótesis: tasa de interés ≥ 10 %. Regla: parar por futilidad si, tras al menos 50 personas, la probabilidad posterior de que la tasa real sea ≥ 10 % es menor que 5 %; parar por éxito si es mayor que 95 %. Simulación: con una tasa real del 12 %, la regla abandona por error el 4 % de las veces. Se acepta ese 4 % o se ajusta el umbral. (Ilustración del método de [SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md); las cifras son de ejemplo.)

## Errores y confusiones comunes

- **La regla abandona demasiadas ideas buenas**: umbral de futilidad demasiado alto para el costo de perder una; corrección: simular con tasas realistas y elegir el umbral con el costo en la mano.
- **Parar cuando el resultado «parece bueno».**
- **Responsable que construye y decide parar.**
- **No declarar la zona gris.**

## Límites y cuándo no aplica

Las tasas de error dependen de los supuestos de la simulación. Con muestras pequeñas el comportamiento es muy variable. Una regla estadística no tiene en cuenta consideraciones éticas o de seguridad que podrían exigir parar antes.

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
