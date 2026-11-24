# Entrevista como método

[↑ Glosario](../../README.md) · [← Entrelazamiento](./entrelazamiento.md) · [Entrevista estructurada →](./entrevista-estructurada.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

La **entrevista como método** es una conversación estructurada con una persona para obtener descripciones de su experiencia, que se registran y analizan como evidencia situada ([SE-123](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md)). «Situada» significa que vale para esa persona, en ese momento y contexto, y no para una población.

## Por qué importa

Una entrevista produce evidencia declarada y situada, no una medición representativa. Cambia qué se le pide y qué se le atribuye: la entrevista es excelente para descubrir problemas, vocabulario y razones, y mala para estimar cuánta gente comparte una experiencia. Confundir ambas cosas lleva a conclusiones con apariencia estadística sin fundamento.

## Cómo funciona

La entrevista recoge **lo que una persona recuerda y decide contar a otra en un momento concreto**. Lo que dice depende de quién pregunta, cómo y para qué; por eso se registra la guía de preguntas, el contexto y también lo que **no** se preguntó. El registro de la plataforma de entregas conserva: participante (un código, no el nombre), fecha, quién entrevistó, la guía usada, el motivo de selección, la transcripción o notas literales y los códigos asignados con quién los asignó.

El contrato de uso: el informe solo puede citar fragmentos que existan en el registro, y cada afirmación declara cuántas personas la respaldan. Tratar un conjunto de entrevistas como encuesta (porcentajes, representatividad) es el error principal. Una consecuencia concreta es la lectura de las ausencias: con una muestra pequeña, que nadie mencione un tema no prueba que el tema no importe. [SE-123](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md) propone calcular la probabilidad de **no oír** un tema aunque lo viva una fracción apreciable de la población: si el 20 % de las personas lo vive y se entrevista a 8, la probabilidad de no oírlo es 0,8⁸ ≈ 17 %.

Otro factor es la **forma de las preguntas**: las preguntas hipotéticas o guiadas invitan a la cortesía, y las respuestas suenan todas iguales y amables. Se corrige preguntando por episodios pasados concretos y sondeando con «¿y entonces qué hiciste?». La entrevista se complementa con observación y con datos de uso.

## Ejemplo

Se entrevista a ocho docentes sobre cómo revisan entregas. Seis mencionan que abren cada entrega una a una; dos, que usan una hoja propia. El informe puede decir «seis de ocho entrevistados describen revisar entrega por entrega», pero no «el 75 % de los docentes». Y si nadie mencionó la accesibilidad, no puede concluir que no importa. (Ilustración del uso correcto de la entrevista según [SE-123](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md).)

## Errores y confusiones comunes

- **«Nadie mencionó X, así que X no importa»**: se interpretó la ausencia en muestra pequeña como ausencia en la población; corrección: calcular la probabilidad de no oír el tema.
- **Respuestas amables y uniformes**: preguntas hipotéticas o guiadas.
- **Citar fragmentos que no existen en el registro.**
- **Presentar porcentajes** de una muestra no representativa.

## Límites y cuándo no aplica

No estima prevalencia ni mide comportamiento real; lo que la gente dice que hace puede diferir de lo que hace. Con muestras muy pequeñas, los hallazgos son pistas. Para cuantificar se complementa con encuestas bien diseñadas o con datos de uso.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evidencia](./evidencia.md), [Codificación y acuerdo](../c/codificacion-y-acuerdo.md), [De la cita a la afirmación](../d/de-la-cita-a-la-afirmacion.md), [Muestreo y saturación](../m/muestreo-y-saturacion.md), [Preguntas sobre el pasado](../p/preguntas-sobre-el-pasado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-123 — Investigación, entrevistas y evidencia cualitativa](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Nielsen Norman Group: Why You Only Need to Test with 5 Users](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/) — argumento y límites de las muestras pequeñas en pruebas de usabilidad; autoridad: Nielsen Norman Group.
- [Nielsen Norman Group: User Interviews 101](https://www.nngroup.com/articles/user-interviews/) — introducción a la entrevista de usuario como método cualitativo; autoridad: Nielsen Norman Group.
- [McHugh: Interrater reliability, the kappa statistic (Biochemia Medica)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3900052/) — definición e interpretación de kappa frente al acuerdo bruto; autoridad: revisión indexada en PubMed Central.
- [GOV.UK Service Manual: User research](https://www.gov.uk/service-manual/user-research) — cómo planificar y conducir investigación con personas usuarias; autoridad: Government Digital Service.
- [The Mom Test](https://www.momtestbook.com/) — enfoque práctico para preguntar por hechos pasados y evitar la cortesía; autoridad: autor (guía práctica, no estudio empírico).

---

[↑ Glosario](../../README.md) · [← Entrelazamiento](./entrelazamiento.md) · [Entrevista estructurada →](./entrevista-estructurada.md)
