# Experimento de demanda

[↑ Glosario](../../README.md) · [← Experimento de aprendizaje](./experimento-de-aprendizaje.md) · [Experimento difuso →](./experimento-difuso.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Un **experimento de demanda** es una prueba que registra una acción costosa para la persona (hacer clic, registrarse, pagar, comprometer tiempo) como señal de interés ([SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md)). Se opone a preguntar si alguien lo usaría: observa comportamiento, no opinión.

## Por qué importa

Observar lo que la gente hace con un compromiso pequeño cuesta menos que construir y mide más que preguntar. Las personas dicen que sí con facilidad; actuar cuesta algo. Cambia la decisión de cuándo construir: antes de invertir en una función completa se comprueba si alguien da un paso concreto hacia ella.

## Cómo funciona

[SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md) describe tres formas con grado creciente de compromiso del equipo:

- una **puerta falsa**: se muestra la oferta y se mide cuántas personas hacen clic para pedirla;
- un **mago de Oz**: el servicio se entrega a mano a unas pocas personas, como si fuera automático;
- un **concierge**: se hace con acompañamiento total, para aprender cómo se hace.

Todas observan comportamiento y no opinión, y **todas deben ser honestas con la persona**: nadie debe creer que recibió algo que no existe sin una explicación posterior. El **compromiso exigido** importa: un clic cuesta casi nada y una señal así es débil; entregar un borrador, registrarse con un correo o pagar es una señal más fuerte. Cuanto más cuesta la acción, más informa, pero menos gente la hace.

La lectura exige el plan previo: la hipótesis, la diferencia mínima relevante, el tamaño por rama y la potencia, el calendario de análisis (una mirada o un método secuencial declarado), la población, el criterio de asignación, el intervalo esperado y las decisiones asociadas a cada resultado posible. El plan se fecha antes de empezar y no se reescribe tras mirar los datos. Y el resultado se interpreta con su incertidumbre: 8 % de clics en 20 personas es compatible con entre 3 % y 30 %, y si el intervalo atraviesa el umbral de decisión el resultado es inconcluso.

## Ejemplo

Una puerta falsa muestra «Recuperación de borradores con historial» a 500 estudiantes con un botón «Activar». Hacen clic 40 (8 %) y se les muestra un mensaje honesto («aún no está disponible; te avisaremos»). Con un umbral de decisión del 5 %, el intervalo para 40/500 está por encima del umbral y se justifica el siguiente paso. Un mago de Oz con diez docentes, donde el equipo restaura borradores a mano, mide si la usan una segunda vez. (Ilustración del método; cifras de ejemplo.)

## Errores y confusiones comunes

- **La prueba «ganadora» desaparece al repetirla**: se detuvo al primer resultado significativo tras mirar muchas veces; corrección: fijar tamaño y calendario.
- **«No hay diferencia» siempre**: muestra sin potencia.
- **Engañar a la persona**: debe haber explicación posterior.
- **Tomar un clic por demanda** sin considerar el costo de la acción.

## Límites y cuándo no aplica

Mide interés inicial, no valor sostenido ni disposición a pagar a largo plazo. Con poblaciones pequeñas, el intervalo es ancho. No es adecuado cuando hacerlo erosionaría la confianza (productos sensibles) o cuando la expectativa creada no puede cumplirse.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Interés](../i/interes.md), [Señal](../s/senal.md), [Incertidumbre residual](../i/incertidumbre-residual.md), [Mirar los resultados](../m/mirar-los-resultados.md), [Prototipo y pregunta](../p/prototipo-y-pregunta.md), [Tamaño y potencia](../t/tamano-y-potencia.md).
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

[↑ Glosario](../../README.md) · [← Experimento de aprendizaje](./experimento-de-aprendizaje.md) · [Experimento difuso →](./experimento-difuso.md)
