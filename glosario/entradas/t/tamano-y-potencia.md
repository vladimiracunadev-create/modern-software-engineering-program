# Tamaño y potencia

[↑ Glosario](../../README.md) · [← Tamaño del mercado](./tamano-del-mercado.md) · [Tapado →](./tapado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Número de personas por rama necesario para detectar, con una probabilidad dada, una diferencia mínima relevante; la probabilidad de detectarla es la potencia.

Definición de trabajo de [SE-127 — Prototipos, experimentos y reducción de incertidumbre](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md).

## Por qué importa

En [SE-127 — Prototipos, experimentos y reducción de incertidumbre](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md), el tema «Tamaño y potencia» importa porque un experimento sin potencia suficiente no puede decidir, aunque se ejecute impecablemente.

## Cómo funciona

Según [SE-127 — Prototipos, experimentos y reducción de incertidumbre](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md), en la sección «Tamaño y potencia»:

Para detectar un cambio de 10 % a 12 % con 80 % de potencia y 5 % de error se necesitan unas 3 841 personas por rama; para 10 % a 20 %, 199. Cuanto menor la diferencia, mayor la muestra: crece con el inverso del cuadrado de la diferencia. Con una muestra más pequeña el experimento sigue siendo válido pero casi siempre «no concluyente». Por eso se decide antes cuál es la diferencia mínima que justifica actuar, se calcula el tamaño y, si es inalcanzable, se elige otro tipo de prueba (cualitativa, de efecto grande) o se acepta la incertidumbre.

## Ejemplo

Caso medido en la sección «Tamaño y potencia» de [SE-127 — Prototipos, experimentos y reducción de incertidumbre](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md):

Para detectar un cambio de 10 % a 12 % con 80 % de potencia y 5 % de error se necesitan unas 3 841 personas por rama; para 10 % a 20 %, 199. Cuanto menor la diferencia, mayor la muestra: crece con el inverso del cuadrado de la diferencia. Con una muestra más pequeña el experimento sigue siendo válido pero casi siempre «no concluyente».

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-127 — Prototipos, experimentos y reducción de incertidumbre](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md)) son:

- **La prueba «ganadora» desaparece al repetirla** — causa: se detuvo al primer resultado significativo tras mirar muchas veces. Corrección: fijar el tamaño y el calendario de análisis o usar un método secuencial.
- **El experimento dice «no hay diferencia» siempre** — causa: la muestra no tenía potencia para el efecto buscado. Corrección: calcular el tamaño por rama antes de empezar y cambiar de método si es inalcanzable.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-127 — Prototipos, experimentos y reducción de incertidumbre](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres cálculos y simulaciones con tasas supuestas en Windows y Ubuntu (WSL2) con salidas idénticas. No se probó ningún prototipo con personas, no se midió efecto de novedad ni interferencia entre ramas. La siguiente clase usa lo aprendido para priorizar por valor, riesgo y aprendizaje.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Potencia](../p/potencia.md), [Experimento de demanda](../e/experimento-de-demanda.md), [Incertidumbre residual](../i/incertidumbre-residual.md), [Mirar los resultados](../m/mirar-los-resultados.md), [Prototipo y pregunta](../p/prototipo-y-pregunta.md).
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

[↑ Glosario](../../README.md) · [← Tamaño del mercado](./tamano-del-mercado.md) · [Tapado →](./tapado.md)
