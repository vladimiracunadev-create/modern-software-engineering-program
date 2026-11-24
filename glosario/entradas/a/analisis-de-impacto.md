# Análisis de impacto

[↑ Glosario](../../README.md) · [← Análisis de alcance](./analisis-de-alcance.md) · [Análisis de sensibilidad →](./analisis-de-sensibilidad.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

**Análisis de impacto** es la determinación de los elementos que un cambio puede afectar, a partir de los enlaces entre artefactos. El sentido principal es el de [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md) y [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md): dado un requisito o artefacto que cambia, su alcance es el conjunto de artefactos alcanzables siguiendo los enlaces hacia sus consecuencias. En [SE-449](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md) (dispositivos médicos, IEC 62304) el mismo término se aplica a la evaluación del efecto de un cambio sobre riesgos, requisitos y pruebas, con el rigor que la norma exige.

## Por qué importa

Responde, antes de tocar nada, cuánto hay que revisar y a quién avisar. Cambia la decisión de aceptar o no un cambio y la de estimar su costo. Sin él, el riesgo es olvidar algo: modificar un requisito y no actualizar la prueba que lo verificaba, o el módulo que dependía de él.

## Cómo funciona

El mecanismo es un recorrido de grafo. Según [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md), dado un cambio en un requisito se recorren los enlaces: las pruebas que lo verifican, los módulos que esas pruebas ejercitan y los requisitos que dependen de él. El tamaño del conjunto resultante estima el costo del cambio y el riesgo de olvido. [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md) precisa que es una **cota superior**: no todo lo alcanzable necesita cambiar, pero todo lo alcanzable merece mirarse.

La calidad del resultado depende de la densidad del grafo. Pocos enlaces por artefacto acotan el alcance; demasiados lo disparan. Dos síntomas diagnostican la matriz: si casi cualquier cambio alcanza casi todo el sistema, la matriz no ayuda a decidir (se enlazó todo con todo); si el alcance es siempre cero, probablemente faltan enlaces. Un alcance grande no es malo por sí mismo: señala que el cambio merece una revisión específica.

## Ejemplo

En la cadena del requisito conductor de [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md) cada artefacto lleva una etiqueta y un verificador comprueba los enlaces al integrar. Si cambia el tope de penalización por entrega tardía, se recorre el enlace hacia las pruebas que lo verifican y hacia el módulo de cálculo; el resultado es una lista concreta de artefactos a revisar y de personas a avisar, antes de modificar nada.

## Errores y confusiones comunes

- **Casi todo cambio «afecta» a casi todo.** Se enlazó todo con todo; corrección de [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md): reducir los enlaces a los que responden preguntas concretas.
- **Matriz en un documento que nadie actualiza.** Una auditoría tarda un día en encontrar una prueba; corrección: etiquetar la prueba y verificar al integrar.
- **Leer la cota superior como lista de cambios obligatorios.** Es lo que hay que revisar, no lo que hay que modificar.
- **Confundir enlace con evidencia.** Que exista un enlace no prueba que la verificación sea buena.

## Límites y cuándo no aplica

El análisis solo ve lo que está enlazado: dependencias implícitas (comportamiento compartido, datos comunes, configuración) no aparecen si nadie las registró. Las clases lo practican sobre un módulo de juguete con datos sintéticos, no sobre un repositorio real, y las tasas de deterioro de los enlaces son hipótesis. En un contexto regulado ([SE-449](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md)) el análisis es una obligación documentada; en uno informal puede bastar con una revisión de las pruebas y consumidores directos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Efecto](../e/efecto.md), [Evaluación](../e/evaluacion.md), [Riesgo](../r/riesgo.md), [Sobre](../s/sobre.md), [Alcance de un cambio](./alcance-de-un-cambio.md), [Enlace frente a evidencia](../e/enlace-frente-a-evidencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-151 — Trazabilidad desde necesidad hasta evidencia](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.
- [SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Gotel y Finkelstein: An analysis of the requirements traceability problem (1994)](https://doi.org/10.1109/ICRE.1994.292398) — definición y problemas de la trazabilidad; autoridad: IEEE International Conference on Requirements Engineering.
- [Cleland-Huang et al.: Software traceability, trends and future directions (2014)](https://doi.org/10.1145/2593882.2593891) — estado y retos; autoridad: ACM, Future of Software Engineering.
- [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) — trazabilidad entre necesidades, requisitos y verificación; autoridad: ISO, IEC e IEEE.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — gestión de requisitos y trazabilidad; autoridad: IEEE Computer Society.
- [Python: `sys.settrace`](https://docs.python.org/3/library/sys.html#sys.settrace) — registro de llamadas durante la ejecución.

---

[↑ Glosario](../../README.md) · [← Análisis de alcance](./analisis-de-alcance.md) · [Análisis de sensibilidad →](./analisis-de-sensibilidad.md)
