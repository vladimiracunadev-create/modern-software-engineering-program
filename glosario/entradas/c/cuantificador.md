# Cuantificador

[↑ Glosario](../../README.md) · [← CTO / Dirección de Tecnología](./cto-direccion-de-tecnologia.md) · [Cuantización →](./cuantizacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Operador sobre elementos de un dominio.

Definición de trabajo de [SE-050 — Lógica proposicional, predicados e inferencia](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md).

## Por qué importa

La clase donde se define, [SE-050 — Lógica proposicional, predicados e inferencia](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md), existe con este propósito: la clase existe para usar lógica para comprobar validez de inferencias y hacer visibles supuestos.

## Cómo funciona

Según [SE-050 — Lógica proposicional, predicados e inferencia](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md):

Un predicado depende de variables: `responde(host, prueba)`. `para todo` exige cubrir el dominio declarado; `existe` se demuestra con un testigo. Pasar de «falló en un cliente» a «falla para todos» cambia el cuantificador sin evidencia.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-050 — Lógica proposicional, predicados e inferencia](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md):

Las reglas del modelo de decisión diagnóstica no disparan acciones destructivas. Una conclusión incluye las premisas usadas, su vigencia y nivel de evidencia. Si falta una premisa, propone una prueba; si dos reglas concluyen estados incompatibles, eleva el conflicto en lugar de escoger silenciosamente.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-050 — Lógica proposicional, predicados e inferencia](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md)) son:

- **Se concluye «si no resuelve, falla DNS»** — causa: se invirtió la implicación (recíproca). Corrección: usar la contrapositiva y buscar una prueba que separe causas.
- **Una regla «todas pasan» se cumple sin ejecutar nada** — causa: verdad vacía sobre un conjunto vacío. Corrección: comprobar que el conjunto no es vacío antes de afirmar.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Pasar de «falló en un cliente» a «falla para todos» cambia el cuantificador sin evidencia. ([SE-050](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Dominio](../d/dominio.md), [Sobre](../s/sobre.md), [Estrategia](../e/estrategia.md), [Implicación](../i/implicacion.md), [Inferencia](../i/inferencia.md), [Predicado](../p/predicado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-050 — Lógica proposicional, predicados e inferencia](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md), [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.

---

[↑ Glosario](../../README.md) · [← CTO / Dirección de Tecnología](./cto-direccion-de-tecnologia.md) · [Cuantización →](./cuantizacion.md)
