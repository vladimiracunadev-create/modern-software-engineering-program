# Singleton

[↑ Glosario](../../README.md) · [← Simulado](./simulado.md) · [Síntesis →](./sintesis.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Patrón que garantiza una única instancia con acceso global, con el costo del estado compartido.

Definición de trabajo de [SE-304 — Patrones creacionales, estructurales y conductuales](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-314 — GoF creacionales: Factory, Builder, Singleton y Prototype](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md): Garantía de una instancia con acceso global; en este curso se separa de la unicidad.

## Por qué importa

La clase donde se define, [SE-304 — Patrones creacionales, estructurales y conductuales](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md), existe con este propósito: la clase existe para que uses los patrones de diseño como vocabulario de problemas recurrentes y no como plantillas que se instalan: sabrás nombrar el problema que un patrón resuelve, el costo que trae y la prueba que lo vuelve visible, y reconocerás cuándo el patrón solo añade estructura.

## Cómo funciona

Según [SE-304 — Patrones creacionales, estructurales y conductuales](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md):

Responden a quién crea los objetos y cuántos hay. La fábrica oculta qué clase concreta se crea; el constructor por pasos (builder) ordena la creación de objetos con muchas opciones; el singleton garantiza una sola instancia y un punto de acceso global. El singleton es el más usado y el que más cuesta: el estado global acopla a todos los módulos y vuelve las pruebas dependientes del orden. La alternativa suele ser crear la instancia una vez y pasarla a quien la necesita (inyección).

Según [SE-304 — Patrones creacionales, estructurales y conductuales](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md):

Reproduce el fallo clásico de la clase: **una suite que pasa en el orden en que se escribió y falla al reordenarla**. Ejecuta las doce pruebas del singleton con las cuatro escritoras primero.

## Ejemplo

Caso medido en la sección «Un singleton y el orden de las pruebas» de [SE-304 — Patrones creacionales, estructurales y conductuales](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md):

La configuración es una clase con una instancia global (`Config.get()`) con un campo `recargo`. Doce pruebas: ocho leen el valor por defecto y esperan 100 al calcular un precio base de 100, cuatro lo cambian a 0,1. Se ejecutan 5000 órdenes aleatorios de semilla fija con tres variantes: el singleton sin reinicio, el singleton reiniciado antes de cada prueba y una configuración pasada como parámetro.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La suite pasa en un orden y falla en otro** — causa: estado global compartido (singleton). Corrección: inyectar la dependencia y ejecutar en orden aleatorio con semilla. ([SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Se ejecutan 5000 órdenes aleatorios de semilla fija con tres variantes: el singleton sin reinicio, el singleton reiniciado antes de cada prueba y una configuración pasada como parámetro. ([SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-303](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Costo](../c/costo.md), [Estado](../e/estado.md), [Garantía](../g/garantia.md), [Instancia](../i/instancia.md), [Adaptador](../a/adaptador.md), [Builder](../b/builder.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-304 — Patrones creacionales, estructurales y conductuales](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-314 — GoF creacionales: Factory, Builder, Singleton y Prototype](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-324](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md), [SE-068](../../../classes/part-05-fundamentos-de-programacion/se-068-modulos-interfaces-y-separacion-de-responsabilidades/README.md), [SE-074](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md), [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Gamma, Helm, Johnson y Vlissides, «Design Patterns» (1994)](https://www.informit.com/store/design-patterns-elements-of-reusable-object-oriented-9780201633610) — catálogo de patrones; autoridad: los autores (Addison-Wesley).
- [Fowler, «Inversion of Control Containers and the Dependency Injection pattern»](https://martinfowler.com/articles/injection.html) — inyección de dependencias frente a localizador; autoridad: Martin Fowler.
- [Luo et al., «An empirical analysis of flaky tests» (FSE, 2014)](https://doi.org/10.1145/2635868.2635920) — pruebas intermitentes y dependencia del orden; autoridad: ACM SIGSOFT FSE.
- [Python: sentencia `for`](https://docs.python.org/3/reference/compound_stmts.html) — advertencia sobre modificar la secuencia que se recorre; autoridad: documentación de Python.
- [Python: `ast`](https://docs.python.org/3/library/ast.html) — análisis sintáctico usado para la huella de cada patrón; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Simulado](./simulado.md) · [Síntesis →](./sintesis.md)
