# Preguntas críticas

[↑ Glosario](../../README.md) · [← Prefijo](./prefijo.md) · [Preguntas de investigación →](./preguntas-de-investigacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Pregunta cuya respuesta, si fuera desfavorable, cambiaría o cancelaría la decisión; se prioriza por riesgo y por costo de responderla.

Definición de trabajo de [SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md).

## Por qué importa

En [SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md), el tema «Preguntas críticas» importa porque contrastar primero lo más riesgoso evita gastar semanas en lo que no podría hundir la idea.

## Cómo funciona

Según [SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md), en la sección «Preguntas críticas»:

No todos los supuestos merecen una prueba. Una pregunta es crítica cuando una respuesta negativa invalida la idea y no hay cómo compensarla («¿las docentes autorizarán que el sistema guarde borradores de sus alumnos?»). Se ordenan con dos ejes: cuánto mueve el resultado y cuán incierto es. Los supuestos de alto impacto y alta incertidumbre se contrastan primero; los de bajo impacto se aceptan; los de alto impacto bien conocidos se vigilan. La pregunta crítica se redacta como algo que puede responderse con una observación concreta.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md):

En la plataforma de entregas, el mapa de supuestos conserva por cada uno: enunciado, tipo (observado o esperado), rango, impacto en el resultado, costo de contrastarlo, hipótesis falsable, umbral, regla de decisión y fecha en que se fijó. El contrato es que ninguna hipótesis cambia de umbral después de observar y que cada informe indica cuántas hipótesis se miraron.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md)) son:

- **El piloto «confirma» la idea y la ampliación no** — causa: la conclusión se sacó de una muestra pequeña sin fijar umbral ni confianza. Corrección: declarar de antemano tamaño, umbral y probabilidad exigida y calcular la posterior.
- **El equipo mide el alcance durante semanas y no avanza** — causa: se contrastó el supuesto más cómodo, no el más sensible. Corrección: calcular la oscilación de cada supuesto y contrastar primero el de mayor sensibilidad e incertidumbre.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres cálculos y simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con salidas idénticas. Los rangos del embudo y el a priori son supuestos y no se contrastó ninguna hipótesis con personas reales. La siguiente clase transforma la hipótesis más sensible en una propuesta de valor con resultados medibles.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-123](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Costo](../c/costo.md), [Riesgo](../r/riesgo.md), [Evidencia y umbral](../e/evidencia-y-umbral.md), [Hipótesis falsable](../h/hipotesis-falsable.md), [Sensibilidad](../s/sensibilidad.md), [Supuestos](../s/supuestos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-123](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md), [SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md).

**Aparece en los casos de estudio:** [Quibi](../../../casos/fallo/quibi.md).

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

[↑ Glosario](../../README.md) · [← Prefijo](./prefijo.md) · [Preguntas de investigación →](./preguntas-de-investigacion.md)
