# Incertidumbre residual

[↑ Glosario](../../README.md) · [← Incertidumbre](./incertidumbre.md) · [Incidente →](./incidente.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

La **incertidumbre residual** es el rango de valores de la tasa real que son compatibles con lo observado, expresado como intervalo de confianza o de credibilidad ([SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md)). Es lo que queda de duda después de hacer una prueba, por bien que se haya hecho.

## Por qué importa

Toda prueba termina con un intervalo; ignorarlo convierte una estimación en un hecho. Cambia la decisión que se toma al leer el resultado: «8 % de clics» no es una demanda del 8 %, y quien decide con ese número sin su intervalo puede invertir donde no hay demanda o descartar donde sí la hay.

## Cómo funciona

[SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md) da un ejemplo con números. Observar 8 % de clics en 20 personas es compatible con una tasa real entre 3 % y 30 %. Con 200 personas el rango se reduce a 5–13 %, y con 1.000 a 6,5–9,8 %. El ancho del intervalo baja con la raíz del tamaño de la muestra: cuadruplicar los datos reduce el intervalo a la mitad, de modo que reducir la duda es cada vez más caro.

La clase recomienda el **intervalo de Wilson**, que funciona razonablemente con muestras pequeñas y con tasas cercanas a 0 o 1, donde el intervalo clásico (el de la aproximación normal) falla y puede salirse de [0, 1] o quedar de ancho cero. El intervalo se reporta junto a la tasa y se compara con el **umbral de decisión declarado en el plan**: si el intervalo atraviesa el umbral, el resultado es **inconcluso**, no favorable. Esa regla evita decidir por el valor puntual.

La incertidumbre residual se conecta con otras prácticas del mismo tema: fijar el tamaño y el calendario de análisis antes de empezar (mirar repetidamente y detenerse al primer resultado favorable infla los falsos positivos) y calcular el tamaño por rama para tener potencia suficiente.

## Ejemplo

Una prueba de interés de la plataforma: 20 personas ven una oferta y 2 hacen clic (10 %). Con el umbral de decisión fijado en el 5 %, el intervalo de Wilson para 2 de 20 va aproximadamente de 3 % a 30 %: atraviesa el umbral, y el resultado es inconcluso. Con 1.000 personas y la misma tasa, el intervalo se estrecha hasta quedar claramente por encima del umbral y la decisión es defendible. (Cifras de ejemplo en la línea de las que usa [SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md); no son los mismos datos.)

## Errores y confusiones comunes

- **La prueba «ganadora» desaparece al repetirla**: se detuvo al primer resultado significativo tras mirar muchas veces; corrección: fijar tamaño y calendario o usar un método secuencial.
- **«No hay diferencia» siempre**: la muestra no tenía potencia para el efecto buscado; corrección: calcular el tamaño por rama antes.
- **Reportar solo el valor puntual.**
- **Interpretar el intervalo de confianza como «hay 95 % de probabilidad de que el valor esté dentro»**: la lectura estricta es sobre el procedimiento; el intervalo de credibilidad bayesiano sí admite esa lectura bajo sus supuestos.

## Límites y cuándo no aplica

El intervalo solo cubre el error de muestreo, no los sesgos: una muestra no representativa o una medición mal definida producen un intervalo estrecho y equivocado. Supone observaciones independientes. Con datos agregados por persona o por sesión hay que cuidar qué unidad se cuenta. Para decisiones baratas y reversibles, esperar a un intervalo estrecho puede costar más que decidir con el valor puntual.

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
