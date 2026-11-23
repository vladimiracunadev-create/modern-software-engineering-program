# Clase base frágil

[↑ Glosario](../../README.md) · [← Clarificación](./clarificacion.md) · [Clase de cambio →](./clase-de-cambio.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Situación en que un cambio interno de la base, sin cambiar su interfaz, rompe a sus subclases.

Definición de trabajo de [SE-303 — Composición, herencia y delegación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md).

## Por qué importa

En [SE-303 — Composición, herencia y delegación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md), el tema «Clase base frágil» importa porque la subclase falla cuando la base cambia sin cambiar su interfaz.

## Cómo funciona

Según [SE-303 — Composición, herencia y delegación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md), en la sección «Clase base frágil»:

El problema aparece cuando la base cambia **sin cambiar su interfaz**. Un caso clásico: una colección implementa `agregar_todos` llamando a su propio `agregar`. Una subclase que cuenta los elementos sobrescribe `agregar` y `agregar_todos` y suma en ambos: con esa implementación de la base cuenta el doble. Si la base cambia a un `extend` interno, la subclase pasa a contar bien. Ninguna de las dos bases rompe su documentación, y la subclase depende del detalle. Quien hereda asume el compromiso de seguir a la base.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-303 — Composición, herencia y delegación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md):

El equipo decide opción por opción. `Fragil`, `Seguro`, `Urgente` y `Refrigerado` se vuelven decoradores de un `CalculadoraEnvio` con la interfaz `costo(envio)`, y el orden se fija por una regla escrita: primero los recargos fijos, después los porcentuales. Una prueba recorre los 24 órdenes y comprueba que solo el orden de la regla es válido. La colección contadora se reescribe por composición. Se deja la herencia para `EnvioInternacional(Envio)`, que sí es un «es un» sustituible, vive en el mismo paquete y comparte el contrato de `SE-302`.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-303 — Composición, herencia y delegación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md)) son:

- **Un contador cuenta doble tras un cambio interno de la base** — causa: herencia que sobrescribe métodos que la base también usa. Corrección: componer y reenviar solo lo prometido.
- **Cada nueva opción duplica las subclases** — causa: herencia por combinación. Corrección: componer con decoradores o con una lista de recargos.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-303 — Composición, herencia y delegación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md)) son: Las definiciones son operativas para `tarifas`. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la bibliografía enlazada al final. Se ejecutaron tres análisis con clases reales de Python y datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ninguna base de código real; las colecciones, los recargos y las jerarquías aleatorias son construcciones del autor. La siguiente clase nombra patrones que combinan herencia, composición y delegación y examina cuándo describen un problema que existe.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Base](../b/base.md), [Interfaz](../i/interfaz.md), [Composición](./composicion.md), [Delegación](../d/delegacion.md), [Herencia](../h/herencia.md), [Orden de resolución de métodos](../o/orden-de-resolucion-de-metodos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-303 — Composición, herencia y delegación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Gamma, Helm, Johnson y Vlissides, «Design Patterns» (1994)](https://www.informit.com/store/design-patterns-elements-of-reusable-object-oriented-9780201633610) — composición frente a herencia de clases; autoridad: los autores (Addison-Wesley).
- [Python: «The Python 2.3 Method Resolution Order»](https://docs.python.org/3/howto/mro.html) — linealización de bases en Python; autoridad: documentación de Python.
- [Fowler, «Replace Superclass with Delegate»](https://refactoring.com/catalog/replaceSuperclassWithDelegate.html) — paso de herencia a delegación; autoridad: Martin Fowler.
- [Fowler, «Replace Subclass with Delegate»](https://refactoring.com/catalog/replaceSubclassWithDelegate.html) — subclases sustituidas por un colaborador; autoridad: Martin Fowler.
- [Liskov y Wing (1994)](https://doi.org/10.1145/197320.197383) — subtipos que preservan el comportamiento; autoridad: ACM TOPLAS.

---

[↑ Glosario](../../README.md) · [← Clarificación](./clarificacion.md) · [Clase de cambio →](./clase-de-cambio.md)
