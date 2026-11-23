# Componente fuertemente conexo

[↑ Glosario](../../README.md) · [← Componente](./componente.md) · [Componentes y alcanzabilidad →](./componentes-y-alcanzabilidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Grupo de módulos que se alcanzan entre sí.

Definición de trabajo de [SE-322 — Antipatrones y deuda de diseño](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md).

## Por qué importa

La clase donde se define, [SE-322 — Antipatrones y deuda de diseño](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md), existe con este propósito: la clase existe para que reconozcas un diseño que se ha vuelto caro de cambiar **con una medida y no con una impresión**, y para que distingas entre un antipatrón (una estructura recurrente que produce daño), un olor de código (una señal que merece revisión) y una incomodidad (algo que molesta pero no cuesta).

## Cómo funciona

Según [SE-322 — Antipatrones y deuda de diseño](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md):

Cuando `avisos` importa `cursos`, `cursos` importa `usuarios` y `usuarios` importa `cursos` y `avisos`, ningún módulo del grupo se puede probar, entender ni desplegar sin los otros. El análisis de **componentes fuertemente conexos** (el algoritmo de Tarjan) los detecta: en el grafo del experimento devuelve un componente de tamaño tres, `['avisos', 'cursos', 'usuarios']`. Se rompe **extrayendo lo compartido** a un módulo del que todos dependan (`dominio`), no moviendo la importación de un lado a otro: con tres módulos que dependen de `dominio` y ninguno de los otros, el análisis devuelve **cero** ciclos.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-322 — Antipatrones y deuda de diseño](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-322 — Antipatrones y deuda de diseño](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md)) son: Las clases, los grafos y el modelo de deuda son del autor; las métricas son aproximaciones y el interés es una ilustración. No se midió ningún equipo ni su historial real de cambios. El siguiente paso, `SE-323`, toma un punto doloroso concreto y lo refactoriza con un patrón con un maestro dorado, midiendo antes y después y decidiendo si el patrón se queda.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Módulo](../m/modulo.md), [Antipatrón](../a/antipatron.md), [Ciclo de dependencias](./ciclo-de-dependencias.md), [Clase de dios](./clase-de-dios.md), [Cohesión](./cohesion.md), [Deuda de diseño](../d/deuda-de-diseno.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-322 — Antipatrones y deuda de diseño](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-348](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Componente](./componente.md) · [Componentes y alcanzabilidad →](./componentes-y-alcanzabilidad.md)
