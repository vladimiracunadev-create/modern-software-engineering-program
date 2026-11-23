# Evidencia y umbral

[↑ Glosario](../../README.md) · [← Evidencia trazable](./evidencia-trazable.md) · [Excedente del cliente →](./excedente-del-cliente.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Regla que convierte observaciones en una decisión: qué se mide, con qué muestra, con qué umbral y con qué control del error por contrastar varias cosas.

Definición de trabajo de [SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md).

## Por qué importa

En [SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md), el tema «Evidencia y umbral» importa porque cuánta evidencia basta depende del umbral, del tamaño de la muestra y de cuántas hipótesis se contrastan a la vez.

## Cómo funciona

Según [SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md), en la sección «Evidencia y umbral»:

Observar un 20 % cuando el umbral es 15 % no equivale a haber superado el umbral: con 20 personas la probabilidad posterior de que la tasa real lo supere es 0,80; con 200, 0,98. Además, cada hipótesis adicional que se mira aumenta la probabilidad de que alguna parezca confirmarse por azar: con veinte hipótesis falsas hay un 64 % de probabilidad de al menos un «hallazgo». Por eso la regla de decisión incluye el tamaño de muestra, la probabilidad exigida y, si hay varias hipótesis, una corrección o una sola hipótesis principal declarada de antemano.

## Ejemplo

Caso medido en la sección «Evidencia y umbral» de [SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md):

Observar un 20 % cuando el umbral es 15 % no equivale a haber superado el umbral: con 20 personas la probabilidad posterior de que la tasa real lo supere es 0,80; con 200, 0,98. Además, cada hipótesis adicional que se mira aumenta la probabilidad de que alguna parezca confirmarse por azar: con veinte hipótesis falsas hay un 64 % de probabilidad de al menos un «hallazgo». Por eso la regla de decisión incluye el tamaño de muestra, la probabilidad exigida y, si hay varias hipótesis, una corrección o una sola hipótesis principal declarada de antemano.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md)) son:

- **El piloto «confirma» la idea y la ampliación no** — causa: la conclusión se sacó de una muestra pequeña sin fijar umbral ni confianza. Corrección: declarar de antemano tamaño, umbral y probabilidad exigida y calcular la posterior.
- **El equipo mide el alcance durante semanas y no avanza** — causa: se contrastó el supuesto más cómodo, no el más sensible. Corrección: calcular la oscilación de cada supuesto y contrastar primero el de mayor sensibilidad e incertidumbre.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres cálculos y simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con salidas idénticas. Los rangos del embudo y el a priori son supuestos y no se contrastó ninguna hipótesis con personas reales. La siguiente clase transforma la hipótesis más sensible en una propuesta de valor con resultados medibles.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-123](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Control](../c/control.md), [Observación](../o/observacion.md), [Regla](../r/regla.md), [Hipótesis falsable](../h/hipotesis-falsable.md), [Preguntas críticas](../p/preguntas-criticas.md), [Sensibilidad](../s/sensibilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-124 — Hipótesis, supuestos y preguntas críticas](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

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

[↑ Glosario](../../README.md) · [← Evidencia trazable](./evidencia-trazable.md) · [Excedente del cliente →](./excedente-del-cliente.md)
