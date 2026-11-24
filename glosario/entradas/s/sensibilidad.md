# Sensibilidad

[↑ Glosario](../../README.md) · [← Señales, cancelación y atomicidad](./senales-cancelacion-y-atomicidad.md) · [Sensibilidad global →](./sensibilidad-global.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

La **sensibilidad** es el cambio del resultado de un modelo al variar un supuesto mientras los demás se mantienen fijos ([SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md), [SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md), [SE-281](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md)). [SE-421](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md) la formula como cuánto cambia un resultado cuando cambian los supuestos que lo producen. En ML y estadística, «sensibilidad» también designa la tasa de verdaderos positivos (otra entrada del glosario); este texto trata el análisis de sensibilidad de modelos y decisiones.

## Por qué importa

Ordena los supuestos por cuánto duele que fallen. Un modelo de plazo, de viabilidad o de decisión descansa en supuestos inciertos; no todos importan igual. La sensibilidad indica cuáles merecen atención, vigilancia o una primera prueba, y cuáles se pueden dejar. [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md) añade un criterio de robustez: una decisión que cambia con una unidad en una puntuación no es robusta.

## Cómo funciona

El método de **una variable cada vez** ([SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md)): se varía un supuesto dentro de un rango razonable, manteniendo los demás, y se compara el cambio del resultado (por ejemplo, el plazo). Se repite para cada supuesto y se ordenan por «oscilación». [SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md) precisa que el resultado **no dice cuál es más probable que falle, sino cuál duele más si falla**. Se vigilan primero los supuestos de **alta sensibilidad y baja credibilidad**: los que mueven mucho y de los que menos se sabe. La vigilancia se concreta en señales con umbral (por ejemplo, «si el rendimiento de las últimas cuatro semanas baja de cierto valor, se revisa el plan»).

En un embudo multiplicativo ([SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md)), el resultado es el producto de las tasas de cada paso; se varía cada tasa entre su mínimo y su máximo con las demás en su valor central, y la oscilación indica cuánto cambia el resultado final. El hallazgo habitual es que el supuesto que más mueve el resultado **no es el que el equipo mide por costumbre** (alcance, visitas) sino uno de comportamiento (interés, activación), que solo se aprende con prototipos y conversaciones.

Para decisiones con criterios ponderados ([SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md)), la sensibilidad se estudia sorteando pesos y contando con qué frecuencia gana cada opción: si la ganadora cambia con pequeños movimientos de pesos, la decisión no es robusta.

## Ejemplo

Un embudo con cuatro pasos: alcance 50 %–70 %, interés 5 %–15 %, activación 30 %–60 %, pago 10 %–20 %. Con las demás tasas en el centro, el interés mueve el resultado final por un factor de 3 (de 5 % a 15 %); el alcance, por 1,4. El supuesto a probar primero es el interés, no el alcance. (Rangos ilustrativos en la línea de [SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md).)

## Errores y confusiones comunes

- **Medir lo cómodo y no lo sensible.**
- **Variar todos los supuestos a la vez** y no saber cuál mueve el resultado.
- **Confundir sensibilidad con probabilidad de fallo.**
- **Ignorar la interacción entre supuestos**: con una variable cada vez no se ve.

## Límites y cuándo no aplica

El análisis de una variable cada vez no capta interacciones; para eso existe la sensibilidad global (otra entrada). Depende de los rangos elegidos: rangos arbitrarios dan oscilaciones arbitrarias. Con un modelo mal especificado, la sensibilidad se calcula sobre algo que no refleja la realidad.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-123](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Medida](../m/medida.md), [Modelo](../m/modelo.md), [Rango](../r/rango.md), [Resultado](../r/resultado.md), [Calibración](../c/calibracion.md), [Colchón de proyecto](../c/colchon-de-proyecto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.
- [SE-191 — Taller: planificar bajo incertidumbre explícita](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-255 — Nativo, híbrido, web wrapper y cross-platform](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-421 — Calidad por riesgo y propósito de las pruebas](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.
- [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.
- [SE-563 — Taller: comparar flujos manual, asistido y automatizado](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (48 clases más lo mencionan; las que más):

[SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md), [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md), [SE-535](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-535-compras-proveedores-y-evaluacion-tecnica/README.md), [SE-291](../../../classes/part-24-software-especializado-y-dominios/se-291-machine-learning-como-componente-de-producto/README.md), [SE-608](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md), [SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), [SE-299](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Efron, «Bootstrap methods: another look at the jackknife» (The Annals of Statistics, 1979)](https://doi.org/10.1214/aos/1176344552) — remuestreo; autoridad: The Annals of Statistics.
- [Malcolm et al., «Application of a technique for research and development program evaluation» (Operations Research, 1959)](https://doi.org/10.1287/opre.7.5.646) — PERT y combinación de varianzas; autoridad: Operations Research.
- [Flyvbjerg, «From Nobel Prize to project management: getting risks right» (Project Management Journal, 2006)](https://doi.org/10.1177/875697280603700302) — clases de referencia y optimismo; autoridad: Project Management Journal.
- [Buehler, Griffin y Ross, «Exploring the planning fallacy» (Journal of Personality and Social Psychology, 1994)](https://doi.org/10.1037/0022-3514.67.3.366) — subestimación del tiempo propio; autoridad: Journal of Personality and Social Psychology.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — gestión de ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Señales, cancelación y atomicidad](./senales-cancelacion-y-atomicidad.md) · [Sensibilidad global →](./sensibilidad-global.md)
