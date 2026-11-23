# Hipótesis falsable

[↑ Glosario](../../README.md) · [← Hipótesis discriminante](./hipotesis-discriminante.md) · [Hipótesis inductiva →](./hipotesis-inductiva.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Afirmación sobre el mundo, con un umbral y una regla de decisión fijados antes de observar, que algún resultado posible refutaría.

Definición de trabajo de [SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-505 — Principios de la ingeniería del caos: estado estable e hipótesis](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md): Afirmación de que el estado estable se mantendrá bajo una condición, con una regla que dice qué observación la refuta.

## Por qué importa

En [SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md), el tema «Hipótesis falsable» importa porque una hipótesis que ninguna observación puede contradecir no orienta ninguna decisión.

## Cómo funciona

Según [SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md), en la sección «Hipótesis falsable»:

La falsabilidad —que exista un resultado observable que contradiga la afirmación— distingue una hipótesis de una esperanza. «Los estudiantes valoran la confirmación de entrega» no puede fallar; «al menos 6 de cada 10 estudiantes que ven la confirmación no repiten la entrega en 48 horas» sí. Se completa con la regla: qué se hará si el resultado queda por debajo, por encima o en medio. Fijar umbral y regla antes de ver los datos evita ajustar la vara a la medida del resultado, el error más común y más difícil de notar desde dentro.

## Ejemplo

Ejemplo de [SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md) (sección «Ejemplo mínimo»):

Un fragmento mínimo con una hipótesis falsable y su regla de decisión. Antes de ejecutarlo, predice el resultado para 4 de 20 y para 40 de 200.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md)) son:

- **El piloto «confirma» la idea y la ampliación no** — causa: la conclusión se sacó de una muestra pequeña sin fijar umbral ni confianza. Corrección: declarar de antemano tamaño, umbral y probabilidad exigida y calcular la posterior.
- **El equipo mide el alcance durante semanas y no avanza** — causa: se contrastó el supuesto más cómodo, no el más sensible. Corrección: calcular la oscilación de cada supuesto y contrastar primero el de mayor sensibilidad e incertidumbre.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres cálculos y simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con salidas idénticas. Los rangos del embudo y el a priori son supuestos y no se contrastó ninguna hipótesis con personas reales. La siguiente clase transforma la hipótesis más sensible en una propuesta de valor con resultados medibles.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-123](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Regla de decisión](../r/regla-de-decision.md), [Estado estable](../e/estado-estable.md), [Afirmación](../a/afirmacion.md), [Condición](../c/condicion.md), [Banda](../b/banda.md), [Evidencia y umbral](../e/evidencia-y-umbral.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.
- [SE-505 — Principios de la ingeniería del caos: estado estable e hipótesis](../../../classes/part-42-ingenieria-del-caos/se-505-principios-de-la-ingenieria-del-caos-estado-estable-e-hipotesis/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md), [SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md), [SE-409](../../../classes/part-34-saas-y-plataformas-de-producto/se-409-que-hace-distinto-a-un-producto-saas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Stanford Encyclopedia of Philosophy: Karl Popper](https://plato.stanford.edu/entries/popper/) — falsabilidad como criterio de demarcación; autoridad: Stanford University.
- [The Lean Startup: principios](https://theleanstartup.com/principles) — aprendizaje validado y ciclo construir-medir-aprender; autoridad: Eric Ries (fuente del autor).
- [Douglas Hubbard: How to Measure Anything](https://www.howtomeasureanything.com/) — cuantificar la incertidumbre con rangos y valor de la información; autoridad: Hubbard Decision Research.
- [Product Talk: Opportunity Solution Tree](https://www.producttalk.org/opportunity-solution-tree/) — estructura para conectar resultados, oportunidades y experimentos; autoridad: Teresa Torres (fuente del autor).
- [GOV.UK Service Manual: How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) — qué averiguar en una discovery y cómo compartir lo aprendido; autoridad: Government Digital Service.

---

[↑ Glosario](../../README.md) · [← Hipótesis discriminante](./hipotesis-discriminante.md) · [Hipótesis inductiva →](./hipotesis-inductiva.md)
