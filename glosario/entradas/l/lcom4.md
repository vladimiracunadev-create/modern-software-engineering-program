# LCOM4

[↑ Glosario](../../README.md) · [← Latencia de un evento](./latencia-de-un-evento.md) · [Lead time →](./lead-time.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Número de componentes conectados que forman los métodos de una clase según los atributos que comparten o las llamadas entre sí.

Definición de trabajo de [SE-301 — Cohesión, acoplamiento y encapsulación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md).

## Por qué importa

La clase donde se define, [SE-301 — Cohesión, acoplamiento y encapsulación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md), existe con este propósito: la clase existe para que puedas decir qué agrupa un módulo, de qué depende y qué esconde, y para que conviertas esas tres preguntas en números que se pueden contrastar con un cambio real, no en adjetivos como «limpio» o «desacoplado».

## Cómo funciona

Según [SE-301 — Cohesión, acoplamiento y encapsulación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md):

Un módulo es cohesivo cuando sus partes cambian juntas y se entienden juntas. En una clase, una forma operativa de mirarlo es ver qué métodos comparten atributos o se llaman entre sí: si forman un solo grupo conectado, la clase cuenta una sola historia; si forman varios, son varias clases con un nombre común. LCOM4 cuenta esos grupos conectados. La cohesión no pide clases pequeñas: pide que lo que se agrupa tenga un motivo común de cambio.

Según [SE-301 — Cohesión, acoplamiento y encapsulación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md):

El equipo separa `Envio` en `Precio`, `Aviso` y `Bitacora` y deja a `Envio` como una fachada fina que los compone. Antes de moverlos, escribe el cambio que quiere hacer más barato: «cambiar la plantilla del aviso sin releer el cálculo». Después de mover, comprueba tres cosas: LCOM4 de cada clase, los sitios que hay que editar para el cambio de unidad del peso (con `Precio.costo_por_peso()` expuesto como comportamiento) y que el grafo de importaciones no creó un ciclo. Documenta qué decisión esconde cada módulo en una tabla de tres columnas.

## Ejemplo

Ejemplo de [SE-301 — Cohesión, acoplamiento y encapsulación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md) (sección «Ejemplo mínimo»):

`a` y `b` comparten `x`; `c` usa `y` solo: son dos componentes, LCOM4 = 2. Registra versión, comando y salida; añade a `c` una llamada a `a` y predice el nuevo valor.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Cambiar una plantilla obliga a releer el cálculo del costo** — causa: una clase mezcla responsabilidades con distinto motivo de cambio. Corrección: separar por decisión y comprobar con LCOM4 y con el cambio previsto. ([SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md))
- **LCOM4 = 1 y la clase sigue siendo un cajón de sastre** — causa: un atributo común (`self.datos`) conecta todo. Corrección: revisar los motivos de cambio y no confiar solo en la métrica. ([SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- LCOM4 no distingue una clase con tres responsabilidades de una clase con tres métodos sencillos que simplemente no comparten atributos, y sube o baja con la densidad de uso de los atributos. ([SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md))
- No necesariamente: una clase de dos métodos que no se tocan es pequeña y tiene LCOM4 = 2. ([SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Atributo](../a/atributo.md), [Componente](../c/componente.md), [Acoplamiento](../a/acoplamiento.md), [Ciclo de dependencias](../c/ciclo-de-dependencias.md), [Cohesión](../c/cohesion.md), [Encapsulación](../e/encapsulacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-301 — Cohesión, acoplamiento y encapsulación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Parnas, «On the criteria to be used in decomposing systems into modules» (CACM, 1972)](https://doi.org/10.1145/361598.361623) — descomposición por decisiones ocultas; autoridad: Communications of the ACM.
- [Stevens, Myers y Constantine, «Structured design» (IBM Systems Journal, 1974)](https://doi.org/10.1147/sj.132.0115) — cohesión y acoplamiento; autoridad: IBM Systems Journal.
- [Chidamber y Kemerer, «A metrics suite for object oriented design» (IEEE TSE, 1994)](https://doi.org/10.1109/32.295895) — métricas de cohesión y acoplamiento; autoridad: IEEE Transactions on Software Engineering.
- [Python: `ast`](https://docs.python.org/3/library/ast.html) — análisis del árbol sintáctico usado para medir; autoridad: documentación de Python.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla para las simulaciones; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Latencia de un evento](./latencia-de-un-evento.md) · [Lead time →](./lead-time.md)
