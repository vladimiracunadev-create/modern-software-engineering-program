# Explicación fiel

[↑ Glosario](../../README.md) · [← Explicación](./explicacion.md) · [Exploración →](./exploracion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Descripción que coincide con lo que el código hace al ejecutarse, no con lo que dice su comentario.

Definición de trabajo de [SE-559 — Revisión, refactorización y explicación asistidas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md).

## Por qué importa

En [SE-559 — Revisión, refactorización y explicación asistidas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md), el tema «Explicación fiel» importa porque evita transmitir errores de comentarios

## Cómo funciona

[SE-559 — Revisión, refactorización y explicación asistidas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-559 — Revisión, refactorización y explicación asistidas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones define un procedimiento para los cambios asistidos. El revisor automático se fija con umbral 0,60 tras medir, en doscientos cambios etiquetados del año anterior, 58 % de precisión y 72 % de cobertura; la persona que revisa lee primero las alarmas y después el diff completo, y la aprobación nombra a quien responde.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-559 — Revisión, refactorización y explicación asistidas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md)) son:

- **El revisor automático se ignora** — causa: umbral bajo, precisión baja, fatiga. Corrección: medir con cambios etiquetados y subir el umbral.
- **Se pierden defectos que el revisor sí podía marcar** — causa: umbral alto sin medir la cobertura. Corrección: elegir el umbral con costos explícitos.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-559 — Revisión, refactorización y explicación asistidas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: una simulación del umbral de un revisor, una comparación diferencial real entre versiones de una función y una extracción real con `ast` frente a comentarios. No se evaluó ningún revisor, refactorizador ni explicador; las puntuaciones, la proporción de defectos, las funciones, la distribución de entradas y los comentarios desfasados son construcciones del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cobertura](../c/cobertura.md), [Comparación diferencial](../c/comparacion-diferencial.md), [Precisión](../p/precision.md), [Refactorización](../r/refactorizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-559 — Revisión, refactorización y explicación asistidas](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Bacchelli y Bird](https://doi.org/10.1109/ICSE.2013.6606617) — revisión de código moderna: expectativas, resultados y desafíos; autoridad: ICSE 2013.
- [Google: Engineering Practices, code review](https://google.github.io/eng-practices/review/) — guía pública de revisión; autoridad: documentación de Google.
- [Fowler, «Refactoring»](https://refactoring.com/) — definición y práctica de la refactorización; autoridad: autor del texto.
- [Claessen y Hughes, «QuickCheck»](https://doi.org/10.1145/351240.351266) — pruebas de propiedades con entradas aleatorias; autoridad: ICFP 2000.
- [Hypothesis](https://hypothesis.readthedocs.io/en/latest/) — biblioteca de pruebas de propiedades para Python; autoridad: documentación del proyecto.

---

[↑ Glosario](../../README.md) · [← Explicación](./explicacion.md) · [Exploración →](./exploracion.md)
