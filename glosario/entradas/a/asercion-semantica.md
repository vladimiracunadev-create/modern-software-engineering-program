# Aserción semántica

[↑ Glosario](../../README.md) · [← Aserción](./asercion.md) · [Asiento →](./asiento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Comprobación de un significado observable por el usuario, no de la representación exacta.

Definición de trabajo de [SE-424 — End-to-end, aceptación y recorridos críticos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md).

## Por qué importa

En [SE-424 — End-to-end, aceptación y recorridos críticos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md), el tema «Instantánea frente a aserción semántica» importa porque una comparación exacta genera ruido que se aprueba sin leer.

## Cómo funciona

Según [SE-424 — End-to-end, aceptación y recorridos críticos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md):

Una instantánea guarda la salida (por ejemplo el HTML) y falla ante cualquier diferencia. Detecta todo cambio y no distingue uno que importa de uno que no: un espacio, el orden de los atributos o una fecha nueva rompen la prueba igual que un botón que desaparece. Cuando la mayoría de las diferencias son ruido, el equipo aprende a aprobarlas sin leerlas, y la instantánea deja de proteger. Una aserción semántica afirma lo que el usuario percibe (el título, la nota de la entrega, la presencia del botón) y es insensible al resto; su costo es que solo ve lo que se le pidió mirar.

Según [SE-424 — End-to-end, aceptación y recorridos críticos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md):

El equipo de la plataforma analiza el registro de uso del último trimestre (con datos anonimizados) y la tabla de riesgos de `SE-421`, calcula la cobertura voraz y elige cinco recorridos: ingreso, entrega de una tarea, consulta de la nota, calificación por un docente y cierre de un curso. Cada recorrido se limita a ocho pasos o menos, tiene un criterio de aceptación en Dado/Cuando/Entonces con un resultado observable («el estudiante ve «calificada» y la nota 6,5»), usa aserciones semánticas y declara lo que no mira (estilos, rendimiento, accesibilidad). El presupuesto de inestabilidad es de 0,5 % por paso, lo que da más del 96 % de ejecuciones limpias por recorrido; un recorrido que supere el presupuesto se acorta o se baja de nivel.

## Ejemplo

Ejemplo de [SE-424 — End-to-end, aceptación y recorridos críticos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma analiza el registro de uso del último trimestre (con datos anonimizados) y la tabla de riesgos de `SE-421`, calcula la cobertura voraz y elige cinco recorridos: ingreso, entrega de una tarea, consulta de la nota, calificación por un docente y cierre de un curso. Cada recorrido se limita a ocho pasos o menos, tiene un criterio de aceptación en Dado/Cuando/Entonces con un resultado observable («el estudiante ve «calificada» y la nota 6,5»), usa aserciones semánticas y declara lo que no mira (estilos, rendimiento, accesibilidad).

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Las instantáneas se aprueban sin leerlas** — causa: casi todas las diferencias son ruido. Corrección: aserciones semánticas y una instantánea solo para salidas pequeñas. ([SE-424](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una aserción semántica afirma lo que el usuario percibe (el título, la nota de la entrega, la presencia del botón) y es insensible al resto; su costo es que solo ve lo que se le pidió mirar. ([SE-424](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md))
- Traslada el análisis a otra aplicación (por ejemplo, una tienda de entradas): construye un registro de uso, elige recorridos con dos métricas, calcula la inestabilidad de cada uno y compara una instantánea con una aserción semántica. ([SE-424](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md), [SE-423](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-423-integracion-componentes-y-contratos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Representación](../r/representacion.md), [Criterio de aceptación](../c/criterio-de-aceptacion.md), [Fallo espurio](../f/fallo-espurio.md), [Instantánea](../i/instantanea.md), [Recorrido crítico](../r/recorrido-critico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-424 — End-to-end, aceptación y recorridos críticos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-424-end-to-end-aceptacion-y-recorridos-criticos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Martin Fowler, «BroadStackTest»](https://martinfowler.com/bliki/BroadStackTest.html) — pruebas de banda ancha; autoridad: autor del texto.
- [Google Testing Blog: Just Say No to More End-to-End Tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html) — costo de las pruebas de extremo a extremo; autoridad: equipo de pruebas de Google.
- [Martin Fowler, «TestPyramid»](https://martinfowler.com/bliki/TestPyramid.html) — reparto por nivel; autoridad: autor del texto.
- [Playwright: buenas prácticas](https://playwright.dev/docs/best-practices) — pruebas centradas en el usuario; autoridad: documentación oficial.
- [Cucumber: referencia de Gherkin](https://cucumber.io/docs/gherkin/reference/) — criterios de aceptación; autoridad: documentación oficial.

---

[↑ Glosario](../../README.md) · [← Aserción](./asercion.md) · [Asiento →](./asiento.md)
