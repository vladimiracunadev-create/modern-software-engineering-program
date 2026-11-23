# Horizonte de equilibrio

[↑ Glosario](../../README.md) · [← Hora civil](./hora-civil.md) · [Horizonte de predictibilidad →](./horizonte-de-predictibilidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Plazo a partir del cual el menor costo anual de una opción compensa su inversión inicial.

Definición de trabajo de [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md).

## Por qué importa

La clase donde se define, [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md), existe con este propósito: la clase existe para que la pregunta «¿reescribimos o seguimos con esto?» deje de decidirse por cansancio, por entusiasmo por una tecnología o por quien habla más fuerte, y se decida con un modelo de costos explícito, con incertidumbre y con las condiciones en que la respuesta cambia.

## Cómo funciona

Según [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md):

La comparación depende del plazo considerado. Una reescritura tiene un costo inicial alto y, si sale bien, un costo anual menor; evolucionar tiene un costo inicial menor y un costo anual que crece más despacio que el del legado sin tocar pero no baja. Hay un **horizonte de equilibrio** a partir del cual el menor costo anual de la reescritura compensa la inversión, y puede estar más lejos de lo que el sistema va a vivir. Si el sistema se va a retirar en cinco años por otras razones, la reescritura no recupera su inversión por mucho que el sistema nuevo sea mejor.

## Ejemplo

Caso medido en la sección «El horizonte de equilibrio» de [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md):

La diferencia de la mediana baja de 6,7 a 3,4 al pasar de 4 a 20 años y reescribir sigue sin ganar en la mayoría de escenarios ni siquiera a veinte años (36 %). Si el sistema no va a vivir más de seis años, reescribir gana menos del 1 % de las veces. El horizonte es una variable de negocio: un sistema con fecha de retiro conocida cambia la respuesta más que cualquier detalle técnico.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md)) son:

- **Se aprueba una reescritura con un solo número** — causa: falta incertidumbre y términos ocultos. Corrección: modelar con distribuciones y todos los términos.
- **El costo real duplica el presupuesto** — causa: no se presupuestó la deriva ni el legado paralelo. Corrección: añadir esos términos y medir la deriva.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con simulaciones sintéticas en Windows y Ubuntu (WSL2) con resultados idénticos. Todos los parámetros y distribuciones son construcciones del autor, el modelo ignora interacciones, riesgos de seguridad, costo de oportunidad, moral y rotación del equipo, y trata el sistema nuevo como un destino único y no como un conjunto de rebanadas. No se analizó ninguna reescritura real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-525](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Costo](../c/costo.md), [Opción](../o/opcion.md), [Plazo](../p/plazo.md), [Análisis de sensibilidad](../a/analisis-de-sensibilidad.md), [Costo acumulado](../c/costo-acumulado.md), [Criterio de abandono](../c/criterio-de-abandono.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-526 — Economía de reescribir frente a evolucionar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Spolsky, «Things You Should Never Do, Part I»](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/) — argumento contra reescribir desde cero; autoridad: ensayo de un autor reconocido, de opinión.
- [Brooks, «No Silver Bullet»](https://doi.org/10.1109/MC.1987.1663532) — complejidad esencial y accidental; autoridad: IEEE Computer, 1987.
- [Lehman, «Programs, life cycles, and laws of software evolution»](https://doi.org/10.1109/PROC.1980.11805) — evolución de sistemas en uso; autoridad: Proceedings of the IEEE, 1980.
- [Fowler, «TechnicalDebt»](https://martinfowler.com/bliki/TechnicalDebt.html) — principal e intereses; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Hora civil](./hora-civil.md) · [Horizonte de predictibilidad →](./horizonte-de-predictibilidad.md)
