# Rúbrica de investigabilidad

[↑ Glosario](../../README.md) · [← Rúbrica calibrada](./rubrica-calibrada.md) · [Ruido →](./ruido.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

La **rúbrica de investigabilidad** es un conjunto de criterios con los que dos personas deciden si un enunciado de problema puede investigarse ([SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md)). Sus cuatro criterios son: actor reconocible, obstáculo observable, consecuencia y ausencia de solución embebida. Es una herramienta de revisión, no un método de investigación.

## Por qué importa

Un enunciado que no se puede investigar no se puede confirmar ni refutar, y sobre él se construye por intuición. La rúbrica hace explícito qué hace investigable un enunciado y permite revisarlo entre personas, en lugar de depender del gusto de quien lo escribió. Cambia la calidad del punto de partida del descubrimiento de producto.

## Cómo funciona

Los cuatro criterios ([SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md)):

- **Actor reconocible**: se puede identificar a quién le ocurre («estudiantes que escriben entregas largas», no «los usuarios»).
- **Obstáculo observable**: hay algo que se pueda ver o registrar («pierden el texto al expirar la sesión»).
- **Consecuencia**: se dice qué cuesta («no pueden recuperarlo y deben reescribir»).
- **Ausencia de solución embebida**: el enunciado no es una solución disfrazada («falta un botón de guardar» ya propone la respuesta).

La rúbrica puede aplicarla una persona o un script. El valor está en el **acuerdo**: si dos personas puntúan igual, el criterio es claro; si no, hay que precisarlo. Un script automatiza lo mecánico (detectar palabras de solución, actores no listados) y deja en evidencia lo que no entiende, como vocabulario nuevo o actores que no estaban en su lista. La clase subraya una distinción importante: el acuerdo con **una sola persona** es coherencia propia, no acuerdo entre personas. Para medir el acuerdo real se usa un estadístico como el kappa de Cohen entre dos evaluadoras.

Y un límite que la clase destaca: una regla de forma pasa un enunciado que nadie reconoce como real. La comprobación de existencia exige que una segunda persona cite un registro o una observación que lo confirme.

## Ejemplo

Enunciado A: «Los usuarios están insatisfechos con las entregas». Falla actor (genérico), observable (ninguno) y consecuencia. Enunciado B: «Los estudiantes que entregan desde el móvil pierden el texto cuando la sesión expira y deben reescribirlo». Cumple actor, observable y consecuencia, y no contiene solución. Un enunciado C: «Falta guardado automático» falla el cuarto criterio: ya es una solución. (Ejemplos construidos con los criterios de [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md).)

## Errores y confusiones comunes

- **Enunciado que pasa la rúbrica y nadie lo reconoce como real**: la regla comprueba forma, no existencia; corrección: pedir una observación que lo confirme.
- **Un solo evaluador**: no se puede hablar de acuerdo.
- **Rúbrica con criterios que se solapan**: los puntajes no discriminan.
- **Confundir investigable con importante**: un problema investigable puede ser pequeño.

## Límites y cuándo no aplica

La rúbrica y el script de [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md) se afinaron con pocos ejemplos; sus pruebas con casos nuevos son de seis y tres elementos, de modo que su exactitud real es desconocida. No sustituye la investigación con personas. Para enunciados de dominios con vocabulario especializado, el script necesita ajuste.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Actor](../a/actor.md), [Conjunto](../c/conjunto.md), [Consecuencia](../c/consecuencia.md), [Evidencia](../e/evidencia.md), [Agrupar por necesidad](../a/agrupar-por-necesidad.md), [Descomponer la petición](../d/descomponer-la-peticion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-131 — Taller: convertir una petición en un problema investigable](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) — reformular una solución dada como problema; autoridad: Government Digital Service.
- [GOV.UK Service Manual: Learning about users and their needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs) — formato y validación de necesidades; autoridad: Government Digital Service.
- [The Mom Test](https://www.momtestbook.com/) — preguntar por hechos pasados; autoridad: autor (guía práctica, no estudio empírico).
- [Nielsen Norman Group: User Interviews 101](https://www.nngroup.com/articles/user-interviews/) — introducción a la entrevista de usuario; autoridad: Nielsen Norman Group.
- [McHugh: Interrater reliability, the kappa statistic](https://pmc.ncbi.nlm.nih.gov/articles/PMC3900052/) — kappa frente al acuerdo bruto; autoridad: revisión indexada en PubMed Central.

---

[↑ Glosario](../../README.md) · [← Rúbrica calibrada](./rubrica-calibrada.md) · [Ruido →](./ruido.md)
