# Ciclo de dependencias

[↑ Glosario](../../README.md) · [← Ciclo](./ciclo.md) · [Ciclo de trabajo →](./ciclo-de-trabajo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Conjunto de módulos que dependen unos de otros, directa o indirectamente.

Definición de trabajo de [SE-301 — Cohesión, acoplamiento y encapsulación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md).

## Por qué importa

En [SE-322 — Antipatrones y deuda de diseño](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md), el tema «Ciclos de dependencia» importa porque impiden probar y desplegar por separado

## Cómo funciona

Según [SE-322 — Antipatrones y deuda de diseño](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md), en la sección «Ciclos de dependencias»:

Cuando `avisos` importa `cursos`, `cursos` importa `usuarios` y `usuarios` importa `cursos` y `avisos`, ningún módulo del grupo se puede probar, entender ni desplegar sin los otros. El análisis de **componentes fuertemente conexos** (el algoritmo de Tarjan) los detecta: en el grafo del experimento devuelve un componente de tamaño tres, `['avisos', 'cursos', 'usuarios']`. Se rompe **extrayendo lo compartido** a un módulo del que todos dependan (`dominio`), no moviendo la importación de un lado a otro: con tres módulos que dependen de `dominio` y ninguno de los otros, el análisis devuelve **cero** ciclos.

**Cómo leer la figura.** La primera fila es el grafo con ciclo y el resultado del análisis; la segunda, el grafo corregido y su resultado. **Dónde deja de valer:** los grafos son de cuatro módulos escritos a mano; un sistema real tiene cientos de módulos, ciclos entre paquetes y dependencias dinámicas que el análisis estático no ve (importaciones en tiempo de ejecución, inyección por configuración). Un análisis real debe incorporarse al CI para que un ciclo nuevo falle la integración.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-322 — Antipatrones y deuda de diseño](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-322 — Antipatrones y deuda de diseño](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md)) son: Las clases, los grafos y el modelo de deuda son del autor; las métricas son aproximaciones y el interés es una ilustración. No se midió ningún equipo ni su historial real de cambios. El siguiente paso, `SE-323`, toma un punto doloroso concreto y lo refactoriza con un patrón con un maestro dorado, midiendo antes y después y decidiendo si el patrón se queda.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](./conjunto.md), [Módulo](../m/modulo.md), [Acoplamiento](../a/acoplamiento.md), [Antipatrón](../a/antipatron.md), [Clase de dios](./clase-de-dios.md), [Cohesión](./cohesion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-301 — Cohesión, acoplamiento y encapsulación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-322 — Antipatrones y deuda de diseño](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-051](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md), [SE-060](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-060-proyecto-especificacion-y-solucion-contrastable/README.md), [SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Ciclos de dependencia».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Parnas, «On the criteria to be used in decomposing systems into modules» (CACM, 1972)](https://doi.org/10.1145/361598.361623) — descomposición por decisiones ocultas; autoridad: Communications of the ACM.
- [Stevens, Myers y Constantine, «Structured design» (IBM Systems Journal, 1974)](https://doi.org/10.1147/sj.132.0115) — cohesión y acoplamiento; autoridad: IBM Systems Journal.
- [Chidamber y Kemerer, «A metrics suite for object oriented design» (IEEE TSE, 1994)](https://doi.org/10.1109/32.295895) — métricas de cohesión y acoplamiento; autoridad: IEEE Transactions on Software Engineering.
- [Python: `ast`](https://docs.python.org/3/library/ast.html) — análisis del árbol sintáctico usado para medir; autoridad: documentación de Python.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla para las simulaciones; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Ciclo](./ciclo.md) · [Ciclo de trabajo →](./ciclo-de-trabajo.md)
