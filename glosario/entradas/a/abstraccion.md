# Abstracción

[↑ Glosario](../../README.md) · [← Abstención](./abstencion.md) · [Abstracción de rama →](./abstraccion-de-rama.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Modelo que conserva solo propiedades relevantes.

Definición de trabajo de [SE-049 — Descomposición, abstracción y reconocimiento de patrones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-070 — Legibilidad, nombres y mantenimiento básico](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md): Concepto que oculta detalle bajo contrato.

## Por qué importa

La clase donde se define, [SE-049 — Descomposición, abstracción y reconocimiento de patrones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md), existe con este propósito: la clase existe para descomponer un problema por responsabilidades y contratos sin perder restricciones transversales.

## Cómo funciona

Según [SE-049 — Descomposición, abstracción y reconocimiento de patrones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md):

Abstraer es conservar propiedades relevantes para una pregunta y omitir las demás. Para ordenar diagnósticos basta una categoría de costo y poder discriminante; la marca del comando puede omitirse. Si el modelo decide permisos, omitir quién ejecuta sería una pérdida crítica. Toda abstracción declara propósito y exclusiones.

Según [SE-070 — Legibilidad, nombres y mantenimiento básico](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md):

Un buen nombre también puede mentir. Si `cost` dejara de ser un entero de unidades abstractas y pasara a ser dinero, el nombre seguiría prometiendo lo anterior; y `timeout_seconds` frente a `t` hace visible la unidad, pero solo mientras sea cierta. Los nombres necesitan mantenimiento igual que el código. La función `select_next` dice lo que hace; `_partition_size` explica que mide el tamaño del grupo más grande; ambos mantienen un mismo nivel de abstracción en su cuerpo (no mezclan detalles de bajo nivel con decisiones de alto nivel).

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-049 — Descomposición, abstracción y reconocimiento de patrones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md):

El modelo de decisión diagnóstica representa el diagnóstico como un grafo: nodos de observación, hipótesis y prueba; aristas de dependencia. Una política impide ejecutar una prueba si falta autorización o si otra prueba barata ya descarta su rama. El grafo puede cambiar sin alterar el contrato del informe.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-049 — Descomposición, abstracción y reconocimiento de patrones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md)) son:

- **El árbol enumera funciones del programa** — causa: se describe la implementación, no el problema. Corrección: reescribir con decisión, hipótesis, pruebas y restricciones.
- **Una prueba aparece sin resultado bajo alguna hipótesis** — causa: la matriz está incompleta. Corrección: completar cada celda o declarar `unknown` y puntuar en cero.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- *¿qué descarte podría invalidar la conclusión y cómo me daría cuenta?* Si ninguna observación podría delatar el descarte, la abstracción no es una simplificación sino una apuesta. ([SE-049](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Contrato](../c/contrato.md), [Modelo](../m/modelo.md), [Propiedad](../p/propiedad.md), [Caracterización](../c/caracterizacion.md), [Control](../c/control.md), [Descomposición](../d/descomposicion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-049 — Descomposición, abstracción y reconocimiento de patrones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-049-descomposicion-abstraccion-y-reconocimiento-de-patrones/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-070 — Legibilidad, nombres y mantenimiento básico](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.

**También se usa en** (25 clases más lo mencionan; las que más):

[SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md), [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md), [SE-025](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-025-windows-linux-macos-y-sus-modelos-operativos/README.md), [SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md), [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md), [SE-074](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md), [SE-048](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md), [SE-050](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.
- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.
- [Python Tutorial](https://docs.python.org/3/tutorial/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Language Reference](https://docs.python.org/3/reference/) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Abstención](./abstencion.md) · [Abstracción de rama →](./abstraccion-de-rama.md)
