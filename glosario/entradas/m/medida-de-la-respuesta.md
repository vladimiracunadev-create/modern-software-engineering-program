# Medida de la respuesta

[↑ Glosario](../../README.md) · [← Medida de control de riesgo](./medida-de-control-de-riesgo.md) · [Medidas y ventanas →](./medidas-y-ventanas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Criterio con número y unidad que permite decidir si un escenario se cumple.

Definición de trabajo de [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md).

## Por qué importa

La clase donde se define, [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), existe con este propósito: la clase existe para que conviertas una palabra como «rápido», «fiable» o «usable» en una promesa que se pueda comprobar: qué atributo de calidad importa, en qué situación, con qué estadístico, sobre qué ventana y con qué umbral.

## Cómo funciona

Según [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md):

Un requisito como «el sistema debe ser seguro» no se puede probar. Un **escenario de calidad** lo vuelve comprobable con seis partes: la **fuente** del estímulo (una persona, otro sistema, un fallo), el **estímulo** (qué ocurre), el **artefacto** afectado (qué parte del sistema), el **entorno** (en qué condiciones: carga, datos, modo de operación), la **respuesta** esperada y la **medida de la respuesta**, que es lo que permite decidir. Cada parte elimina una ambigüedad: sin entorno, «p95 ≤ 300 ms» se cumple con un usuario y se rompe con doscientos; sin estadístico, «300 ms» puede significar media o máximo; sin unidad, el 300 puede ser milisegundos o segundos.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md):

El equipo de la plataforma elige cuatro atributos para el cierre de plazos: eficiencia de desempeño, fiabilidad, compatibilidad y capacidad de interacción. Para cada uno escribe un escenario completo. El de eficiencia dice: *fuente:* docente; *estímulo:* abre la lista de 300 entregas de un curso; *artefacto:* endpoint de listado; *entorno:* día laboral con 50 consultas por segundo y datos de producción del último mes; *respuesta:* se muestra la primera página;

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md)) son:

- **El informe dice «cumple» y hay quejas** — causa: ventana demasiado amplia o media como estadístico. Corrección: medir por ventana corta y con percentil.
- **Dos personas discuten si «300 ms» se cumple** — causa: falta estadístico, entorno o unidad. Corrección: escribir el escenario con las seis partes.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ninguna API real, ningún usuario ni ningún sistema de producción; la proporción de peticiones lentas, el incidente del día 17, los diez escenarios base y los operadores de mutación son construcciones del autor, el verificador se escribió conociendo las mutaciones que lo evalúan y el texto de la norma no se reprodujo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Escenario](../e/escenario.md), [Característica de calidad](../c/caracteristica-de-calidad.md), [Escenario de calidad](../e/escenario-de-calidad.md), [Indicador](../i/indicador.md), [Percentil](../p/percentil.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-433 — Modelos de calidad y atributos medibles](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) — modelo de calidad del producto con nueve características; autoridad: organismo de normalización (texto completo de pago).
- [Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) — indicadores, objetivos y percentiles; autoridad: Google, libro de ingeniería de confiabilidad.
- [Bass, Clements y Kazman, «Software Architecture in Practice»](https://www.sei.cmu.edu/library/software-architecture-in-practice-fourth-edition/) — escenarios de calidad y árbol de utilidad; autoridad: Software Engineering Institute.
- [Python: statistics](https://docs.python.org/3/library/statistics.html) — media, mediana y cuantiles usados en los experimentos; autoridad: documentación de Python.
- [Python: random](https://docs.python.org/3/library/random.html) — generador con semilla para reproducir las muestras; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Medida de control de riesgo](./medida-de-control-de-riesgo.md) · [Medidas y ventanas →](./medidas-y-ventanas.md)
