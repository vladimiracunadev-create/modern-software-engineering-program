# Trazabilidad bidireccional

[↑ Glosario](../../README.md) · [← Trazabilidad](./trazabilidad.md) · [Trazas comparables →](./trazas-comparables.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Capacidad de seguir un elemento hacia su origen y hacia su implementación y verificación.

Definición de trabajo de [SE-151 — Trazabilidad desde necesidad hasta evidencia](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-450 — Casos de seguridad y trazabilidad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md): Vínculos de peligros a requisitos a pruebas y de vuelta.

## Por qué importa

En [SE-151 — Trazabilidad desde necesidad hasta evidencia](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md), el tema «Trazabilidad bidireccional» importa porque permite saber por qué existe algo y qué cubre cada prueba.

## Cómo funciona

Según [SE-151 — Trazabilidad desde necesidad hasta evidencia](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md), en la sección «Trazabilidad bidireccional»:

Hacia atrás, la trazabilidad responde «¿de dónde viene este requisito?»: necesidad, entrevista, norma. Hacia adelante, «¿qué lo implementa y cómo se verifica?»: diseño, código, prueba. Ambas direcciones son necesarias: la primera detecta requisitos sin origen (trabajo que nadie pidió); la segunda, requisitos sin evidencia (promesas que nadie comprueba). Gotel y Finkelstein muestran que el problema no es solo tener los enlaces sino mantenerlos cuando las personas y los documentos cambian.

## Ejemplo

Caso medido en la sección «Trazabilidad: bidireccional y con política de cambio» de [SE-450 — Casos de seguridad y trazabilidad](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md):

La trazabilidad hacia adelante responde «¿qué prueba verifica este requisito?» y hacia atrás «¿de qué requisito o peligro viene esta prueba?». Con 30 requisitos y 45 pruebas generados con semilla 47, 9 requisitos quedan sin ninguna prueba y 2 pruebas sin requisito: son hallazgos antes de que cualquier regulador los pregunte. Una trazabilidad que solo se construye al final suele fallar; una que se mantiene junto al código, con un comprobador en la integración continua, cuesta menos. La cobertura de enlaces mide que hay un enlace, no que la prueba compruebe el requisito: eso lo decide la revisión.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-151 — Trazabilidad desde necesidad hasta evidencia](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md)) son:

- **Una auditoría tarda un día en encontrar una prueba** — causa: la matriz está en un documento que nadie actualiza. Corrección: poner la etiqueta en la prueba y verificarla al integrar.
- **Casi todo cambio «afecta» a casi todo** — causa: se enlazó todo con todo. Corrección: reducir los enlaces a los que responden preguntas concretas.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-151 — Trazabilidad desde necesidad hasta evidencia](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se analizó ningún repositorio real, las tasas de deterioro son hipótesis y la traza cubre un módulo de juguete. La siguiente clase cruza la matriz con obligaciones externas: datos personales, seguridad y regulación.

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
