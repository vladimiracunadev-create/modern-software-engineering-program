# Preguntas críticas

[↑ Glosario](../../README.md) · [← Prefijo](./prefijo.md) · [Preguntas de investigación →](./preguntas-de-investigacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Una **pregunta crítica** es una pregunta cuya respuesta, si fuera desfavorable, cambiaría o cancelaría la decisión; se prioriza por riesgo y por costo de responderla ([SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md)). Es la pregunta sobre un supuesto del que depende toda la idea.

## Por qué importa

Contrastar primero lo más riesgoso evita gastar semanas en lo que no podría hundir la idea. Los equipos tienden a investigar lo que es fácil de medir (alcance, visitas) y a postergar lo que podría invalidar el plan. Cambia el orden de la investigación: se empieza por lo que más puede fallar.

## Cómo funciona

No todos los supuestos merecen una prueba. [SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md) define: una pregunta es crítica cuando **una respuesta negativa invalida la idea y no hay cómo compensarla**. Ejemplo de la clase: «¿las docentes autorizarán que el sistema guarde borradores de sus alumnos?». Si la respuesta es no, la propuesta no funciona, y ninguna otra característica lo compensa.

Se ordenan los supuestos con **dos ejes**: **cuánto mueve el resultado** (impacto, medido con la sensibilidad) y **cuán incierto es**. Los de alto impacto y alta incertidumbre se contrastan primero; los de bajo impacto se aceptan sin probar; los de alto impacto y baja incertidumbre se vigilan. El tercer criterio es el **costo de contrastar**: entre dos preguntas críticas, la barata va antes.

Cada pregunta crítica se convierte en una **hipótesis falsable** con umbral y regla de decisión fijados antes de observar. El mapa de supuestos de la plataforma conserva por cada uno: enunciado, tipo (observado o esperado), rango, impacto en el resultado, costo de contrastarlo, hipótesis falsable, umbral, regla de decisión y fecha en que se fijó. Dos reglas del contrato: ninguna hipótesis cambia de umbral después de observar, y cada informe indica cuántas hipótesis se miraron (para controlar comparaciones múltiples).

Un síntoma de no usarlas: el equipo mide el alcance durante semanas y no avanza porque contrastó el supuesto más cómodo, no el más sensible; se corrige calculando la oscilación de cada supuesto y contrastando primero el de mayor sensibilidad e incertidumbre.

## Ejemplo

Supuestos: (a) el alcance mensual es de 5.000 docentes (impacto bajo; incierto); (b) las docentes permiten guardar borradores (impacto alto, incierto, barato de preguntar); (c) la conversión de prueba a pago es del 10 % (impacto alto, incierto, caro de contrastar). Orden: primero (b), por barata y letal si falla; después (c) con un experimento de demanda; (a) se acepta con un rango. (Priorización ilustrativa según los ejes de [SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md).)

## Errores y confusiones comunes

- **Medir lo cómodo**: el alcance durante semanas sin avanzar.
- **Piloto que «confirma» con muestra pequeña** sin umbral previo.
- **Tratar todas las preguntas con la misma prioridad.**
- **Mirar muchas hipótesis sin declarar cuántas.**

## Límites y cuándo no aplica

La priorización depende de estimaciones de impacto e incertidumbre que son juicios. Algunas preguntas críticas solo se responden construyendo algo. Y una respuesta favorable a la pregunta crítica no valida el resto de la idea.

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
