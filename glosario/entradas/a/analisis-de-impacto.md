# Análisis de impacto

[↑ Glosario](../../README.md) · [← Análisis de alcance](./analisis-de-alcance.md) · [Análisis de sensibilidad →](./analisis-de-sensibilidad.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Determinación de los elementos que un cambio puede afectar a partir de los enlaces.

Definición de trabajo de [SE-151 — Trazabilidad desde necesidad hasta evidencia](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md): Evaluación del efecto de un cambio sobre riesgos, requisitos y pruebas.

## Por qué importa

En [SE-151 — Trazabilidad desde necesidad hasta evidencia](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md), el tema «Análisis de impacto» importa porque dice a qué elementos afecta un cambio antes de hacerlo.

En [SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md), el tema «Análisis de impacto» importa porque estimar el alcance de un cambio decide cuánto revisar y cuánto cuesta cambiar.

## Cómo funciona

Según [SE-151 — Trazabilidad desde necesidad hasta evidencia](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md), en la sección «Análisis de impacto»:

Dado un cambio en un requisito, el alcance se obtiene recorriendo los enlaces: las pruebas que lo verifican, los módulos que esas pruebas ejercitan y los requisitos que dependen de él. El tamaño de ese conjunto es una estimación del costo del cambio y del riesgo de olvidar algo. Si el alcance de casi cualquier cambio es casi todo el sistema, la matriz no ayuda a decidir; si el alcance es siempre cero, probablemente faltan enlaces.

Según [SE-168 — Proyecto: paquete de especificaciones trazables](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md), en la sección «Análisis de impacto»:

Dado un artefacto que cambia, su alcance es el conjunto de artefactos alcanzables siguiendo los enlaces hacia sus consecuencias. Estimarlo antes de cambiar responde cuánto hay que revisar y a quién avisar. Es una cota superior (no todo lo alcanzable necesita cambiar) y depende de cuán denso sea el grafo: pocos enlaces por artefacto acotan el alcance; muchos lo disparan. Un alcance grande no es malo por sí mismo: es una señal de que el cambio merece una revisión específica.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-151 — Trazabilidad desde necesidad hasta evidencia](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md):

La cadena del requisito conductor, con una etiqueta en cada artefacto y un verificador al integrar:

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-151 — Trazabilidad desde necesidad hasta evidencia](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md)) son:

- **Una auditoría tarda un día en encontrar una prueba** — causa: la matriz está en un documento que nadie actualiza. Corrección: poner la etiqueta en la prueba y verificarla al integrar.
- **Casi todo cambio «afecta» a casi todo** — causa: se enlazó todo con todo. Corrección: reducir los enlaces a los que responden preguntas concretas.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-151 — Trazabilidad desde necesidad hasta evidencia](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se analizó ningún repositorio real, las tasas de deterioro son hipótesis y la traza cubre un módulo de juguete. La siguiente clase cruza la matriz con obligaciones externas: datos personales, seguridad y regulación.

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
