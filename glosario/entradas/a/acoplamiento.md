# Acoplamiento

[↑ Glosario](../../README.md) · [← ACL](./acl.md) · [Acoplamiento temporal →](./acoplamiento-temporal.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

El **acoplamiento** es el grado en que un módulo necesita conocer a otro para funcionar o para cambiar ([SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md)). [SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md) lo concreta para clases como el grado en que una clase depende de otras. El sentido del programa no es «dependencia mala»: es una propiedad con tres dimensiones que se pueden observar y contar.

## Por qué importa

Cada dependencia es un lugar más por el que un cambio se propaga: cuanto más acoplado está un módulo, más cosas hay que tocar y revisar cuando algo cambia. Por eso [SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md) lo ata a una pregunta práctica (cuántos lugares hay que editar para una decisión) y no a una opinión sobre el código.

## Cómo funciona

[SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md) pide mirar tres dimensiones, no solo contar dependencias:

- **Dirección:** quién conoce a quién.
- **Cantidad:** cuántos módulos conoce.
- **Naturaleza:** qué conoce: un nombre, un tipo, un orden de llamadas o una representación interna.

Cuanto más se conoce de la implementación del otro, más cambios se propagan. Un módulo de precio que usa una zona geográfica depende de ella por una razón del dominio: ese acoplamiento no es un defecto. El problema aparece cuando el módulo conoce la representación interna del otro.

Los ciclos de dependencias son el caso extremo: los módulos del ciclo no se pueden entender, probar ni desplegar por separado. [SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md) observa que aparecen sin mala intención, cuando cada persona añade la dependencia que le conviene, y que una regla de sentido (las capas altas pueden depender de las bajas, nunca al revés) elimina los ciclos por construcción. [SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md) agrega que el bajo acoplamiento y la alta cohesión tiran en direcciones opuestas y deben leerse juntos.

## Ejemplo

En [SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md), un cambio de unidad del peso obliga a tocar muchos archivos porque los clientes leen el dato y calculan por su cuenta: están acoplados a la representación. Exponer comportamiento en vez de datos (`Precio.costo_por_peso()`) esconde la representación y la unidad, y el cambio queda local.

## Errores y confusiones comunes

- **Condenar todo acoplamiento.** Un módulo de precio que usa una zona geográfica depende de ella por una razón del dominio; lo que importa es la dirección, la cantidad y la naturaleza de la dependencia ([SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md)).
- **Creer que es una opinión de estilo.** Es una propiedad observable en cuántos lugares hay que tocar ([SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md)).
- **Resolver un ciclo con un parche local.** Sin una regla de sentido, los ciclos reaparecen; la inversión de dependencias que trata [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md) es la herramienta cuando una capa baja necesita avisar a una alta.

## Límites y cuándo no aplica

Contar dependencias aproxima el acoplamiento, no lo agota: [SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md) advierte que el conteo de sitios a editar depende de qué cambio se imagine, y un número bajo puede coexistir con un mal diseño. El acoplamiento por razones del dominio es legítimo. Y los criterios de [SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md) (bajo acoplamiento, alta cohesión, indirección, variaciones protegidas) se solapan y dos autores pueden agruparlos distinto: son una elección didáctica del curso.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Módulo](../m/modulo.md), [Ciclo de dependencias](../c/ciclo-de-dependencias.md), [Cohesión](../c/cohesion.md), [Controlador](../c/controlador.md), [Creador](../c/creador.md), [Encapsulación](../e/encapsulacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-301 — Cohesión, acoplamiento y encapsulación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (33 clases más lo mencionan; las que más):

[SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), [SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md), [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md), [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), [SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md), [SE-543](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md).

**Aparece en los casos de estudio:** [Caída global de Meta](../../../casos/fallo/meta-2021.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Stevens, Myers y Constantine, «Structured design» (IBM Systems Journal, 1974)](https://doi.org/10.1147/sj.132.0115) — cohesión y acoplamiento; autoridad: IBM Systems Journal.
- [Chidamber y Kemerer, «A metrics suite for object oriented design» (IEEE TSE, 1994)](https://doi.org/10.1109/32.295895) — métricas de cohesión y acoplamiento; autoridad: IEEE Transactions on Software Engineering.
- [Parnas, «On the criteria to be used in decomposing systems into modules» (CACM, 1972)](https://doi.org/10.1145/361598.361623) — descomposición por decisiones ocultas; autoridad: Communications of the ACM.
- [Python: `ast`](https://docs.python.org/3/library/ast.html) — análisis del árbol sintáctico usado para medir; autoridad: documentación de Python.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla para las simulaciones; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← ACL](./acl.md) · [Acoplamiento temporal →](./acoplamiento-temporal.md)
