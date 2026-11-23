# Incertidumbre residual

[↑ Glosario](../../README.md) · [← Incertidumbre](./incertidumbre.md) · [Incidente →](./incidente.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Rango de valores de la tasa real que son compatibles con lo observado, expresado como intervalo de confianza o de credibilidad.

Definición de trabajo de [SE-127 — Prototipos, experimentos y reducción de incertidumbre](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md).

## Por qué importa

En [SE-127 — Prototipos, experimentos y reducción de incertidumbre](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md), el tema «Incertidumbre residual» importa porque toda prueba termina con un intervalo; ignorarlo convierte una estimación en un hecho.

## Cómo funciona

Según [SE-127 — Prototipos, experimentos y reducción de incertidumbre](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md), en la sección «Incertidumbre residual»:

Observar 8 % de clics en 20 personas no dice que la demanda sea de 8 %: es compatible con entre 3 % y 30 %. Con 200 personas el rango se reduce a 5–13 % y con 1 000 a 6,5–9,8 %. El intervalo de Wilson funciona razonablemente con muestras pequeñas y valores cercanos a 0 o 1, donde el intervalo clásico falla. Se reporta junto a la tasa y se compara con el umbral de decisión declarado en el plan: si el intervalo lo atraviesa, el resultado es inconcluso, no favorable.

## Ejemplo

Caso medido en la sección «Incertidumbre residual» de [SE-127 — Prototipos, experimentos y reducción de incertidumbre](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md):

Observar 8 % de clics en 20 personas no dice que la demanda sea de 8 %: es compatible con entre 3 % y 30 %. Con 200 personas el rango se reduce a 5–13 % y con 1 000 a 6,5–9,8 %. El intervalo de Wilson funciona razonablemente con muestras pequeñas y valores cercanos a 0 o 1, donde el intervalo clásico falla. Se reporta junto a la tasa y se compara con el umbral de decisión declarado en el plan: si el intervalo lo atraviesa, el resultado es inconcluso, no favorable.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-127 — Prototipos, experimentos y reducción de incertidumbre](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md)) son:

- **La prueba «ganadora» desaparece al repetirla** — causa: se detuvo al primer resultado significativo tras mirar muchas veces. Corrección: fijar el tamaño y el calendario de análisis o usar un método secuencial.
- **El experimento dice «no hay diferencia» siempre** — causa: la muestra no tenía potencia para el efecto buscado. Corrección: calcular el tamaño por rama antes de empezar y cambiar de método si es inalcanzable.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-127 — Prototipos, experimentos y reducción de incertidumbre](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres cálculos y simulaciones con tasas supuestas en Windows y Ubuntu (WSL2) con salidas idénticas. No se probó ningún prototipo con personas, no se midió efecto de novedad ni interferencia entre ramas. La siguiente clase usa lo aprendido para priorizar por valor, riesgo y aprendizaje.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Intervalo de confianza](./intervalo-de-confianza.md), [Confianza](../c/confianza.md), [Intervalo](./intervalo.md), [Rango](../r/rango.md), [Experimento de demanda](../e/experimento-de-demanda.md), [Mirar los resultados](../m/mirar-los-resultados.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-127 — Prototipos, experimentos y reducción de incertidumbre](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Johari, Pekelis y Walsh: Always Valid Inference (arXiv:1512.04922)](https://arxiv.org/abs/1512.04922) — inferencia válida bajo monitoreo continuo de pruebas A/B; autoridad: preprint de investigación revisado en varias versiones.
- [Brown, Cai y DasGupta: Interval Estimation for a Binomial Proportion (Statistical Science, 2001)](https://projecteuclid.org/journals/statistical-science/volume-16/issue-2/Interval-Estimation-for-a-Binomial-Proportion/10.1214/ss/1009213286.full) — comparación de intervalos para proporciones; autoridad: Statistical Science.
- [Kohavi, Tang y Xu: Trustworthy Online Controlled Experiments](https://experimentguide.com/) — guía de experimentos controlados en línea; autoridad: libro de referencia de los autores.
- [The Lean Startup: principios](https://theleanstartup.com/principles) — aprendizaje validado y producto mínimo viable como experimento; autoridad: Eric Ries (fuente del autor).
- [GOV.UK Service Manual: User research](https://www.gov.uk/service-manual/user-research) — cómo probar con personas usuarias durante el desarrollo; autoridad: Government Digital Service.

---

[↑ Glosario](../../README.md) · [← Incertidumbre](./incertidumbre.md) · [Incidente →](./incidente.md)
