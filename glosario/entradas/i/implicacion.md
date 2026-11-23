# Implicación

[↑ Glosario](../../README.md) · [← Implementaciones idiomáticas](./implementaciones-idiomaticas.md) · [Importación →](./importacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Relación lógica que excluye antecedente verdadero y consecuente falso.

Definición de trabajo de [SE-050 — Lógica proposicional, predicados e inferencia](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md).

## Por qué importa

La clase donde se define, [SE-050 — Lógica proposicional, predicados e inferencia](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md), existe con este propósito: la clase existe para usar lógica para comprobar validez de inferencias y hacer visibles supuestos.

## Cómo funciona

Según [SE-050 — Lógica proposicional, predicados e inferencia](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md):

Conjunción exige ambas condiciones; disyunción inclusiva acepta una o ambas; implicación `P → Q` solo excluye P verdadera con Q falsa. La implicación no afirma causalidad. Su contraposición es equivalente; su conversa no lo es.

Según [SE-050 — Lógica proposicional, predicados e inferencia](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md):

Refuta la implicación solo si la prueba cumple la premisa p y no se cumple q. Si la premisa no se cumple, la implicación sigue siendo verdadera; la prueba no dice nada sobre ella.

## Ejemplo

Ejemplo de [SE-050 — Lógica proposicional, predicados e inferencia](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md) (sección «Preguntas frecuentes»):

Refuta la implicación solo si la prueba cumple la premisa p y no se cumple q. Si la premisa no se cumple, la implicación sigue siendo verdadera; la prueba no dice nada sobre ella.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se concluye «si no resuelve, falla DNS»** — causa: se invirtió la implicación (recíproca). Corrección: usar la contrapositiva y buscar una prueba que separe causas. ([SE-050](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Conjunción exige ambas condiciones; disyunción inclusiva acepta una o ambas; implicación `P → Q` solo excluye P verdadera con Q falsa. ([SE-050](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Relación](../r/relacion.md), [Cuantificador](../c/cuantificador.md), [Dominio](../d/dominio.md), [Estrategia](../e/estrategia.md), [Inferencia](./inferencia.md), [Predicado](../p/predicado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-050 — Lógica proposicional, predicados e inferencia](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-050-logica-proposicional-predicados-e-inferencia/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-501](../../../classes/part-41-observabilidad-sre-e-incidentes/se-501-postmortems-sin-culpa-y-aprendizaje/README.md), [SE-060](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-060-proyecto-especificacion-y-solucion-contrastable/README.md), [SE-215](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md).

**Aparece en los casos de estudio:** [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.

---

[↑ Glosario](../../README.md) · [← Implementaciones idiomáticas](./implementaciones-idiomaticas.md) · [Importación →](./importacion.md)
