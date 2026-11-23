# System Usability Scale

[↑ Glosario](../../README.md) · [← Syscall](./syscall.md) · [Systems Programmer →](./systems-programmer.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Cuestionario de diez preguntas que da una puntuación de 0 a 100 de usabilidad percibida.

Definición de trabajo de [SE-178 — Investigación de usabilidad y medición](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md).

## Por qué importa

La clase donde se define, [SE-178 — Investigación de usabilidad y medición](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md), existe con este propósito: la clase existe para que planifiques una evaluación de usabilidad con un tamaño de muestra, unas métricas y unos intervalos que digan lo que realmente se puede concluir con pocas personas, y para que distingas un hallazgo cualitativo de una estimación cuantitativa.

## Cómo funciona

Según [SE-178 — Investigación de usabilidad y medición](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md):

Las métricas habituales son éxito de la tarea (binaria), tiempo, errores y una escala subjetiva como la System Usability Scale (SUS). Cada una responde a algo distinto y se informa con su incertidumbre. El criterio de éxito de cada tarea (por ejemplo, «el recibo es visible y la persona lo identifica») se escribe antes de la sesión, y también cuándo se da por rendida una tarea. Sin eso, el éxito se decide con la observación y cambia según quién observe.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-178 — Investigación de usabilidad y medición](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md):

En la plataforma, cada evaluación de la entrega comienza con un protocolo: la pregunta, tres tareas con su criterio de éxito escrito, las métricas, el número de participantes con su razón y lo que no se podrá concluir. Se hacen rondas de cinco participantes con arreglos entre rondas para encontrar problemas, y las cifras se informan como «k de n» con un intervalo de Wilson.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-178 — Investigación de usabilidad y medición](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md)) son:

- **«El 80 % lo logra» con cinco personas** — causa: se informó una proporción sin intervalo. Corrección: informar k de n con intervalo de Wilson o exacto.
- **Se cree que cinco personas hallan el 85 % de los problemas** — causa: se aplicó la fórmula con probabilidades iguales. Corrección: iterar con rondas pequeñas y no extrapolar el 85 %.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-178 — Investigación de usabilidad y medición](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se evaluó a ninguna persona ni se midió ningún producto, y la distribución de probabilidades de los problemas, la media y desviación de SUS y las 150 simulaciones por celda son supuestos del autor. La siguiente clase aplica la medición a un flujo excluyente.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-177](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evaluación formativa](../e/evaluacion-formativa.md), [Evaluación sumativa](../e/evaluacion-sumativa.md), [Intervalo de confianza](../i/intervalo-de-confianza.md), [Potencia estadística](../p/potencia-estadistica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-178 — Investigación de usabilidad y medición](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Bangor, Kortum y Miller, «An empirical evaluation of the System Usability Scale» (Int. J. Hum.-Comput. Interact., 2008)](https://doi.org/10.1080/10447310802205776) — uso y distribución de SUS; autoridad: International Journal of Human–Computer Interaction.
- [Nielsen y Landauer, «A mathematical model of the finding of usability problems» (INTERCHI, 1993)](https://doi.org/10.1145/169059.169166) — modelo de hallazgo de problemas; autoridad: ACM.
- [Virzi, «Refining the test phase of usability evaluation» (Human Factors, 1992)](https://doi.org/10.1177/001872089203400407) — tamaño de muestra y problemas hallados; autoridad: Human Factors.
- [Faulkner, «Beyond the five-user assumption» (Behavior Research Methods, 2003)](https://doi.org/10.3758/BF03195514) — variabilidad de los problemas hallados con pocos participantes; autoridad: Behavior Research Methods.
- [Nielsen Norman Group: por qué cinco usuarios](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/) — contexto y condiciones de la regla de cinco; autoridad: Nielsen Norman Group.

---

[↑ Glosario](../../README.md) · [← Syscall](./syscall.md) · [Systems Programmer →](./systems-programmer.md)
