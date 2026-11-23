# Puntuación de Brier

[↑ Glosario](../../README.md) · [← Punto de sensibilidad](./punto-de-sensibilidad.md) · [Puntuación de mutación →](./puntuacion-de-mutacion.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md)

## Definición

Error cuadrático medio entre las probabilidades pronosticadas y los resultados observados (0 o 1).

Definición de trabajo de [SE-539 — Taller: conducir una revisión de decisión difícil](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-539-taller-conducir-una-revision-de-decision-dificil/README.md).

## Por qué importa

La clase donde se define, [SE-539 — Taller: conducir una revisión de decisión difícil](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-539-taller-conducir-una-revision-de-decision-dificil/README.md), existe con este propósito: el taller existe para que conduzcas una revisión adversarial de una decisión difícil de modo que mejore la decisión y no solo valide a quien la tomó o la castigue.

## Cómo funciona

Según [SE-539 — Taller: conducir una revisión de decisión difícil](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-539-taller-conducir-una-revision-de-decision-dificil/README.md):

Una revisión que concluye con adjetivos («razonable», «arriesgada») no deja nada contrastable. Pedir **probabilidades escritas** («la restauración fallará en el próximo intento: 30 %») permite medir después qué tan bien se prevé. La **puntuación de Brier** (Brier078%3C0001:VOFEIT%3E2.0.CO;2)) es el error cuadrático medio entre la probabilidad declarada y el resultado (0 o 1); cuanto menor, mejor. Una persona **calibrada** acierta en la frecuencia que declara (de las veces que dice 80 %, ocurre el 80 %); una **sobreconfiada** declara más certeza de la que respalda su frecuencia de acierto. La práctica descrita en Superforecasting combina probabilidades explícitas, actualización con nueva información y puntuación posterior.

## Ejemplo

Ejemplo de [SE-539 — Taller: conducir una revisión de decisión difícil](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-539-taller-conducir-una-revision-de-decision-dificil/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula la puntuación de Brier de dos pronósticos de tres eventos. Antes de ejecutarlo, predice cuál es menor.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-539 — Taller: conducir una revisión de decisión difícil](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-539-taller-conducir-una-revision-de-decision-dificil/README.md)) son:

- **Se castiga una decisión razonable que salió mal** — causa: sesgo del resultado. Corrección: juzgar con el expediente de entonces.
- **La revisión repite los hallazgos de siempre** — causa: panel de un solo dominio. Corrección: componer con dominios y una persona ajena.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-539 — Taller: conducir una revisión de decisión difícil](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-539-taller-conducir-una-revision-de-decision-dificil/README.md)) son: Las definiciones son operativas para el equipo de plataforma educativa. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes primarias enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se revisó ninguna decisión ni persona reales; las probabilidades de calidad y de éxito, la precisión de la auditoría, la detección por dominio, el factor del ejercicio previo al fallo y las confianzas son construcciones del autor, y el modelo supone decisiones y revisoras independientes.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-538](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-538-portafolio-entrevistas-y-defensa-profesional/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Resultado](../r/resultado.md), [Calibración](../c/calibracion.md), [Ejercicio previo al fallo](../e/ejercicio-previo-al-fallo.md), [Expediente de la decisión](../e/expediente-de-la-decision.md), [Sesgo del resultado](../s/sesgo-del-resultado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-539 — Taller: conducir una revisión de decisión difícil](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-539-taller-conducir-una-revision-de-decision-dificil/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Baron y Hershey, «Outcome bias in decision evaluation»](https://doi.org/10.1037/0022-3514.54.4.569) — sesgo del resultado; autoridad: Journal of Personality and Social Psychology.
- [Mitchell, Russo y Pennington, «Back to the future: Temporal perspective in the explanation of events»](https://doi.org/10.1002/bdm.3960020103) — perspectiva temporal y razones generadas; autoridad: Journal of Behavioral Decision Making.
- [Klein, «Performing a Project Premortem»](https://hbr.org/2007/09/performing-a-project-premortem) — ejercicio previo al fallo; autoridad: Harvard Business Review.
- [Tetlock y Gardner, *Superforecasting*](https://openlibrary.org/isbn/9780804136716) — pronóstico probabilístico; autoridad: libro con ISBN 978-0-8041-3671-6.
- [Google SRE, «Postmortem Culture»](https://sre.google/sre-book/postmortem-culture/) — análisis posterior sin culpa; autoridad: equipo de SRE de Google.

---

[↑ Glosario](../../README.md) · [← Punto de sensibilidad](./punto-de-sensibilidad.md) · [Puntuación de mutación →](./puntuacion-de-mutacion.md)
