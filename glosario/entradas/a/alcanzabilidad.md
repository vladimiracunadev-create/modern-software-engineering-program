# Alcanzabilidad

[↑ Glosario](../../README.md) · [← Alcance de un cambio](./alcance-de-un-cambio.md) · [Alerta de varias ventanas →](./alerta-de-varias-ventanas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Existencia de un camino entre vértices.

Definición de trabajo de [SE-051 — Conjuntos, relaciones, funciones y grafos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md).

## Por qué importa

La clase donde se define, [SE-051 — Conjuntos, relaciones, funciones y grafos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md), existe con este propósito: la clase existe para elegir conjuntos, relaciones, funciones y grafos según la estructura que deben preservar.

## Cómo funciona

Según [SE-051 — Conjuntos, relaciones, funciones y grafos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md):

Vértices representan estados o tareas y aristas dependencias o transiciones. Dirección, peso y etiqueta tienen significado distinto. Alcanzabilidad responde si existe camino; un orden topológico solo existe en grafos dirigidos acíclicos y no decide prioridad por sí mismo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-051 — Conjuntos, relaciones, funciones y grafos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md):

El modelo de decisión diagnóstica usa un grafo dirigido acíclico para prerequisitos y una relación aparte para evidencia. Antes de ejecutar, valida que toda hipótesis terminal tenga al menos una prueba autorizada y que no existan ciclos de prerrequisitos. Un orden topológico genera una secuencia válida, no necesariamente óptima.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-051 — Conjuntos, relaciones, funciones y grafos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md)) son:

- **El recorrido no termina** — causa: no hay conjunto de visitados o medida decreciente. Corrección: registrar los nodos visitados y acotar los pasos.
- **El orden de construcción cambia entre ejecuciones** — causa: se fijó una prueba al orden de vecinos. Corrección: comprobar solo las propiedades exigidas por el contrato.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Alcanzabilidad responde si existe camino; un orden topológico solo existe en grafos dirigidos acíclicos y no decide prioridad por sí mismo. ([SE-051](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Conjunto](../c/conjunto.md), [Dominio](../d/dominio.md), [Estrategia](../e/estrategia.md), [Función](../f/funcion.md), [Grafo](../g/grafo.md), [Relación](../r/relacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-051 — Conjuntos, relaciones, funciones y grafos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-089](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-089-grafos-y-recorridos/README.md), [SE-471](../../../classes/part-39-build-release-y-cadena-de-suministro/se-471-dependencias-directas-transitivas-y-vendorizacion/README.md), [SE-021](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md), [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md), [SE-039](../../../classes/part-03-redes-internet-y-protocolos/se-039-ipv4-ipv6-subredes-rutas-y-nat/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.
- [MIT 6.006 — Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — aporta definiciones, invariantes y análisis de estructuras y algoritmos usados en la clase.

---

[↑ Glosario](../../README.md) · [← Alcance de un cambio](./alcance-de-un-cambio.md) · [Alerta de varias ventanas →](./alerta-de-varias-ventanas.md)
