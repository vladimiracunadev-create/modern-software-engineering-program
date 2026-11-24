# Zona gris

[↑ Glosario](../../README.md) · [← Zona cruda](./zona-cruda.md) · [Zona muerta →](./zona-muerta.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

La **zona gris** es el rango de resultados que no permite distinguir con la confianza declarada entre el éxito y el no éxito ([SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md)). Es el intervalo en que un experimento queda «inconcluso»: ni confirma la idea ni la descarta.

## Por qué importa

Con pocas personas, casi todo resultado cae entre «sí» y «no»; el diseño debe prever qué hacer ahí. Un criterio que solo admite éxito o fracaso esconde la decisión real en una conversación posterior, sesgada por lo que se quiere. Cambia el diseño de experimentos: se escribe de antemano qué se hará si el resultado es inconcluso.

## Cómo funciona

[SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md) lo ilustra: si la tasa buena es 15 % y la mala 5 %, con 30 personas **muchas pruebas no podrán decir cuál es la real**: el resultado «inconcluso» es frecuente. Con 30 personas, 2 conversiones (6,7 %) y 4 (13,3 %) son compatibles con ambas tasas. La zona gris es el rango de resultados observados donde la evidencia no discrimina.

Reconocerla **obliga a decidir de antemano** entre tres acciones: **ampliar la muestra**, **aceptar la incertidumbre** (decidir con lo que hay, asumiendo el riesgo) o **cambiar de prueba** (una más informativa). Equivale a admitir que **no todo experimento decide**. La zona gris se dimensiona con el tamaño de muestra: más personas la estrechan; con muestras muy pequeñas ocupa casi todo el rango.

El documento de abandono de la plataforma conserva por hipótesis el criterio de éxito, el criterio de no éxito, la **zona gris con su acción**, la regla de parada con su error simulado, la ventana, el responsable (externo al equipo que construye), la fecha de fijación y el cierre. El criterio se fecha antes de empezar. La zona gris se conecta con la incertidumbre residual (si el intervalo atraviesa el umbral, el resultado es inconcluso) y con las reglas de parada.

El error que previene es abandonar una idea que luego otro equipo hace funcionar: la muestra era demasiado pequeña y el resultado era inconcluso, no negativo. Se distingue «no hay evidencia» de «hay evidencia en contra».

## Ejemplo

Umbral de éxito: tasa ≥ 15 %; de no éxito: tasa ≤ 5 %. Con 30 personas: 0–1 conversiones, no éxito claro; 7 o más, éxito claro; entre 2 y 6, zona gris. Acción prevista para la zona gris: ampliar a 100 personas y reevaluar; si sigue en zona gris, parar y registrar «inconcluso». (Ilustración construida con las tasas de [SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md); los límites del recuento son aproximados.)

## Errores y confusiones comunes

- **Abandonar una idea con resultado inconcluso** como si fuera negativo.
- **Criterio sin zona gris**: la decisión se toma después, a conveniencia.
- **Ampliar la muestra sin límite.**
- **Confundir zona gris con empate de opciones.**

## Límites y cuándo no aplica

La zona gris depende de las tasas hipotéticas y de la confianza declarada; con otras tasas cambia. Con muestras grandes es estrecha y puede ignorarse. Las cifras de [SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md) provienen de simulaciones con supuestos del autor.

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
