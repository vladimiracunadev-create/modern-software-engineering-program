# Descomponer la petición

[↑ Glosario](../../README.md) · [← Descarte de carga](./descarte-de-carga.md) · [Descomposición →](./descomposicion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

**Descomponer la petición** es separar una petición en quién la hace, qué intenta lograr, qué hace hoy, qué consecuencia sufre y qué solución propone ([SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md)). La clase la resume en tres tipos de contenido: observación, inferencia y solución. Es un paso del descubrimiento de producto, previo a agrupar por necesidad y a reformular como problema.

## Por qué importa

Una petición mezcla un actor, una intención, una solución y una consecuencia; separarlos revela qué falta. Quien recibe una petición suele tratarla como un requisito y construir la solución pedida, sin saber qué problema resuelve. Descomponer permite ver qué parte es un hecho y cuál es una suposición.

## Cómo funciona

[SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md) lo ilustra con «un panel para ver quién no entregó». Contiene un **actor** (el docente), una **solución** (un panel), una **información deseada** (quién no entregó) y una **intención implícita** (hacer algo con esa información). Lo que falta es lo importante: qué hace hoy el docente con esa información, qué le cuesta, qué pasa si no la tiene y qué considera éxito.

La clase aclara que descomponer **no es cuestionar a la persona**: es identificar qué partes son **observación** (tarda 40 minutos en revisar entrega por entrega), cuáles son **inferencia** (necesita un panel) y cuál es la **solución** propuesta. Las observaciones se confirman con preguntas sobre episodios pasados; las inferencias se contrastan; las soluciones se mantienen como una opción entre varias.

El resultado se conserva en un archivo del taller: la petición original textual (quién la hizo y cuándo), su descomposición, el problema reformulado y la guía de preguntas. La regla de oro es que la **petición original no se sobrescribe**, y que el problema reformulado indica qué observación lo confirmaría. Esto evita que la interpretación del equipo sustituya a lo que la persona dijo.

## Ejemplo

Petición: «Necesito un panel para ver quién no entregó». Descomposición: actor, docente; observación, tarda 40 minutos en revisar entrega por entrega (a confirmar); inferencia, necesita ver pendientes de un vistazo; solución propuesta, panel; intención implícita, reclamar a quienes no entregaron; consecuencia si no lo tiene, entregas olvidadas. Problema reformulado: «docentes pierden 40 minutos por lote identificando entregas pendientes y reclaman tarde». Se puede confirmar con registros o entrevistas. (Caso de [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md) completado con un desarrollo ilustrativo.)

## Errores y confusiones comunes

- **«Sí» a todo y el panel no se usa**: las preguntas eran guiadas o hipotéticas; corrección: preguntar por episodios pasados.
- **Un backlog que crece con peticiones que parecen distintas y son iguales**: no se agruparon por necesidad.
- **Sobrescribir la petición original.**
- **Tomar la solución como requisito.**

## Límites y cuándo no aplica

Descomponer exige acceso a la persona para confirmar; sin él, las inferencias quedan como hipótesis. En peticiones triviales y reversibles, el costo no se justifica. Y la descomposición es un juicio de quien la hace: otra persona podría dividirla distinto.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Consecuencia](../c/consecuencia.md), [Evidencia](../e/evidencia.md), [Agrupar por necesidad](../a/agrupar-por-necesidad.md), [Preguntas de investigación](../p/preguntas-de-investigacion.md), [Reformular como problema](../r/reformular-como-problema.md), [Rúbrica de investigabilidad](../r/rubrica-de-investigabilidad.md).
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

[↑ Glosario](../../README.md) · [← Descarte de carga](./descarte-de-carga.md) · [Descomposición →](./descomposicion.md)
