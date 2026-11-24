# Mirar los resultados

[↑ Glosario](../../README.md) · [← Mirada repetida](./mirada-repetida.md) · [Misión →](./mision.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

**Mirar los resultados** (en la literatura, *peeking*) es la decisión de cuándo analizar los datos de un experimento. Si se hace repetidamente y se detiene la prueba al primer resultado favorable, el error real supera al nominal ([SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md)). El término alude al hábito, no a una técnica estadística.

## Por qué importa

Es una de las causas más comunes de «ganadores» que no se reproducen. Un equipo que revisa el tablero cada día y detiene la prueba cuando aparece «significativo» cree que tiene un 5 % de falsos positivos y en realidad tiene bastante más. Cambia el plan de experimento: cuándo se mira, cuántas veces y bajo qué regla se detiene.

## Cómo funciona

Un p-valor está calibrado para un **único análisis planificado**: su garantía (probabilidad de falso positivo del 5 %, por ejemplo) vale si se calcula una vez, con tamaño fijado de antemano. Si se calcula cada día y se detiene al primer «significativo», se da al azar muchas oportunidades de cruzar el umbral, y la probabilidad de que alguna de las miradas lo cruce sea mucho mayor que 5 %. Es el mismo problema de comparaciones múltiples, repartido en el tiempo.

[SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md) ofrece dos salidas: **fijar de antemano el tamaño y mirar una sola vez**, o usar **métodos secuenciales** diseñados para monitorear (con umbrales que se ajustan en cada mirada). Lo que no vale es mirar libremente y aplicar la prueba clásica. La disciplina se materializa en el plan del experimento: la hipótesis, la diferencia mínima relevante, el tamaño por rama y la potencia, el calendario de análisis (una mirada o un método secuencial declarado), la población, el criterio de asignación, el intervalo esperado y las decisiones asociadas a cada resultado posible. El plan se fecha antes de empezar y no se reescribe después de mirar los datos.

## Ejemplo

Un equipo prueba dos versiones de una pantalla de entrega y revisa el valor p cada mañana durante 20 días; el día 9 aparece 0,04 y detiene la prueba declarando ganadora a la variante B. Al repetirla, el efecto desaparece. Con 20 miradas sobre una diferencia que no existe, la probabilidad de ver al menos un valor p menor a 0,05 es mucho mayor que 5 %. La corrección: fijar el tamaño en el plan y analizar el día 20, o declarar un método secuencial. (Ilustración del mecanismo; las cifras son de ejemplo.)

## Errores y confusiones comunes

- **La prueba «ganadora» desaparece al repetirla**: se detuvo al primer resultado significativo tras mirar muchas veces.
- **El experimento dice «no hay diferencia» siempre**: la muestra no tenía potencia; corrección: calcular el tamaño por rama antes y cambiar de método si es inalcanzable.
- **Mirar «solo para vigilar»** y luego decidir con lo visto.
- **Reescribir el plan después de ver los datos.**

## Límites y cuándo no aplica

Vigilar métricas de seguridad o de daño durante el experimento es legítimo y recomendable (reglas de parada por daño); lo que se evita es decidir la victoria por mirada repetida con una prueba no secuencial. Los métodos secuenciales pagan con algo más de muestra o con umbrales más estrictos. Para decisiones baratas y reversibles, el rigor puede relajarse siempre que el equipo lo haga con conocimiento del riesgo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Resultado](../r/resultado.md), [Experimento de demanda](../e/experimento-de-demanda.md), [Incertidumbre residual](../i/incertidumbre-residual.md), [Prototipo y pregunta](../p/prototipo-y-pregunta.md), [Tamaño y potencia](../t/tamano-y-potencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-127 — Prototipos, experimentos y reducción de incertidumbre](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

**También se usa en** (50 clases más lo mencionan; las que más):

[SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md), [SE-303](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md), [SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md), [SE-305](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md), [SE-306](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md), [SE-307](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md), [SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md), [SE-309](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md).

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

[↑ Glosario](../../README.md) · [← Mirada repetida](./mirada-repetida.md) · [Misión →](./mision.md)
