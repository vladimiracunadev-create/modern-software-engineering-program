# Medida

[↑ Glosario](../../README.md) · [← Medición de campo](./medicion-de-campo.md) · [Medida de contrapeso →](./medida-de-contrapeso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Cantidad bien fundada que disminuye.

Definición de trabajo de [SE-053 — Recursión, inducción y razonamiento estructural](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md).

## Por qué importa

La clase donde se define, [SE-053 — Recursión, inducción y razonamiento estructural](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md), existe con este propósito: la clase existe para relacionar definición recursiva, caso base, progreso e inducción.

## Cómo funciona

Según [SE-053 — Recursión, inducción y razonamiento estructural](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md):

Para demostrar una propiedad P(n), se prueba base y paso desde la hipótesis para un tamaño menor. La inducción fuerte permite asumir todos los tamaños anteriores. Elegir n exige una medida que refleje la estructura: cantidad de nodos restantes, no valor de un ID.

Según [SE-053 — Recursión, inducción y razonamiento estructural](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md):

Elimina el caso base o llama recursivamente con el mismo nodo. Observa no terminación controlada por límite; identifica qué medida dejó de disminuir y repara el contrato.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-053 — Recursión, inducción y razonamiento estructural](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md):

El modelo de decisión diagnóstica recorre el grafo de hipótesis con una pila explícita, límite de profundidad y conjunto de visitados. La especificación explica que un ciclo es error del modelo; no se oculta devolviendo silenciosamente una lista parcial.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El caso base no se alcanza nunca** — causa: el argumento no se acerca al base. Corrección: definir la medida que decrece. ([SE-053](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Elegir n exige una medida que refleje la estructura: cantidad de nodos restantes, no valor de un ID. ([SE-053](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md))
- Observa no terminación controlada por límite; identifica qué medida dejó de disminuir y repara el contrato. ([SE-053](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Caso base](../c/caso-base.md), [Dominio](../d/dominio.md), [Estrategia](../e/estrategia.md), [Hipótesis inductiva](../h/hipotesis-inductiva.md), [Memoización](./memoizacion.md), [Recursión](../r/recursion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-053 — Recursión, inducción y razonamiento estructural](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.

**También se usa en** (354 clases más lo mencionan; las que más):

[SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), [SE-490](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md), [SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md), [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md), [SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md), [Airbnb](../../../casos/exito/airbnb.md), [Slack](../../../casos/exito/slack.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.
- [MIT 6.006 — Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — aporta definiciones, invariantes y análisis de estructuras y algoritmos usados en la clase.

---

[↑ Glosario](../../README.md) · [← Medición de campo](./medicion-de-campo.md) · [Medida de contrapeso →](./medida-de-contrapeso.md)
