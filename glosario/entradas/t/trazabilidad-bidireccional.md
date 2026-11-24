# Trazabilidad bidireccional

[↑ Glosario](../../README.md) · [← Trazabilidad](./trazabilidad.md) · [Trazas comparables →](./trazas-comparables.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

La **trazabilidad bidireccional** es la capacidad de seguir un elemento hacia su origen y hacia su implementación y verificación ([SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md)). [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) la formula para sistemas con peligros: vínculos de peligros a requisitos a pruebas y de vuelta.

## Por qué importa

Permite saber por qué existe algo y qué cubre cada prueba. Una sola dirección deja puntos ciegos: sin la trazabilidad hacia atrás, hay trabajo que nadie pidió; sin la de adelante, hay promesas que nadie comprueba. Cambia lo que una auditoría o una revisión puede responder.

## Cómo funciona

**Hacia atrás**, la trazabilidad responde «¿de dónde viene este requisito?»: necesidad, entrevista, norma. Detecta **requisitos sin origen** (trabajo que nadie pidió). **Hacia adelante** responde «¿qué lo implementa y cómo se verifica?»: diseño, código, prueba. Detecta **requisitos sin evidencia** (promesas que nadie comprueba). Ambas direcciones son necesarias.

[SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) la cuantifica con un ejemplo: con 30 requisitos y 45 pruebas generados con semilla 47, **9 requisitos quedan sin ninguna prueba y 2 pruebas sin requisito**. Son hallazgos antes de que cualquier regulador los pregunte: los 9 son promesas sin comprobar, y las 2 son pruebas huérfanas, que quizá prueban algo que ya no se necesita. La clase añade que una trazabilidad que solo se construye al final suele fallar; la que se mantiene durante el desarrollo, con política de cambio, funciona.

Para que no se vuelva una matriz muerta, [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md) propone poner una **etiqueta** en cada artefacto y verificar al integrar que los enlaces existen en ambas direcciones. Con una granularidad adecuada de enlaces (requisito–prueba–módulo, no línea de código), la matriz responde preguntas reales. Y se distingue el enlace de la evidencia: que la prueba esté enlazada no prueba que verifique el requisito.

En el sentido de [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md), el recorrido incluye los **peligros**: de un peligro identificado se llega a los requisitos que lo mitigan y a las pruebas que lo verifican, y a la inversa, de una prueba se sube al requisito y al peligro que cubre.

## Ejemplo

Hacia adelante: REQ-12 («un PDF de 10 MB se acepta y uno de 10,1 MB se rechaza») → TST-31, TST-32. Hacia atrás: TST-33 → REQ-15 → entrevista E-04 con docentes. Un verificador al integrar lista: «REQ-19 sin prueba», «TST-40 sin requisito». Esos dos son los hallazgos que la trazabilidad bidireccional exige corregir. (Ilustración con la lógica de [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md) y [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md).)

## Errores y confusiones comunes

- **Auditoría que tarda un día en encontrar una prueba**: matriz en un documento que nadie actualiza.
- **Casi todo cambio «afecta» a casi todo**: se enlazó todo con todo.
- **Mantener una sola dirección.**
- **Tomar el enlace por evidencia.**

## Límites y cuándo no aplica

Mantener la trazabilidad cuesta; en proyectos pequeños o de bajo riesgo una versión ligera basta. Los números de [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) son de una simulación con semilla fija y muestran el tipo de hallazgo, no una tasa real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Origen](../o/origen.md), [Peligro](../p/peligro.md), [Verificación](../v/verificacion.md), [Afirmación](../a/afirmacion.md), [Análisis de impacto](../a/analisis-de-impacto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-151 — Trazabilidad desde necesidad hasta evidencia](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.
- [SE-450 — Casos de seguridad y trazabilidad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-448](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md).

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

[↑ Glosario](../../README.md) · [← Trazabilidad](./trazabilidad.md) · [Trazas comparables →](./trazas-comparables.md)
