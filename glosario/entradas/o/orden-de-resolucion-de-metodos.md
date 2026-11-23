# Orden de resolución de métodos

[↑ Glosario](../../README.md) · [← Orden de foco](./orden-de-foco.md) · [Orden e iteración →](./orden-e-iteracion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Orden lineal en que el lenguaje busca un método entre una clase y sus bases.

Definición de trabajo de [SE-303 — Composición, herencia y delegación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md).

## Por qué importa

La clase donde se define, [SE-303 — Composición, herencia y delegación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md), existe con este propósito: la clase existe para que elijas entre heredar, componer y delegar por lo que cada mecanismo promete cuando la base cambia, cuando las opciones se combinan y cuando varias jerarquías se cruzan, y no por la costumbre de «favorecer la composición» ni por la comodidad de heredar.

## Cómo funciona

Según [SE-303 — Composición, herencia y delegación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md):

La herencia múltiple añade el problema del rombo: si dos bases definen el mismo método, ¿cuál se ejecuta? Python linealiza las bases (MRO). Hay órdenes de bases imposibles, que se rechazan al crear la clase, y órdenes posibles en los que **el orden en que se escriben las bases cambia el programa**. Por eso suele reservarse a mixins sin estado y sin métodos con el mismo nombre.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-303 — Composición, herencia y delegación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md):

El equipo decide opción por opción. `Fragil`, `Seguro`, `Urgente` y `Refrigerado` se vuelven decoradores de un `CalculadoraEnvio` con la interfaz `costo(envio)`, y el orden se fija por una regla escrita: primero los recargos fijos, después los porcentuales. Una prueba recorre los 24 órdenes y comprueba que solo el orden de la regla es válido. La colección contadora se reescribe por composición. Se deja la herencia para `EnvioInternacional(Envio)`, que sí es un «es un» sustituible, vive en el mismo paquete y comparte el contrato de `SE-302`.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-303 — Composición, herencia y delegación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md)) son:

- **Un contador cuenta doble tras un cambio interno de la base** — causa: herencia que sobrescribe métodos que la base también usa. Corrección: componer y reenviar solo lo prometido.
- **Cada nueva opción duplica las subclases** — causa: herencia por combinación. Corrección: componer con decoradores o con una lista de recargos.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-303 — Composición, herencia y delegación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md)) son: Las definiciones son operativas para `tarifas`. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la bibliografía enlazada al final. Se ejecutaron tres análisis con clases reales de Python y datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ninguna base de código real; las colecciones, los recargos y las jerarquías aleatorias son construcciones del autor. La siguiente clase nombra patrones que combinan herencia, composición y delegación y examina cuándo describen un problema que existe.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Base](../b/base.md), [Clase base frágil](../c/clase-base-fragil.md), [Composición](../c/composicion.md), [Delegación](../d/delegacion.md), [Herencia](../h/herencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-303 — Composición, herencia y delegación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-075](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «MRO».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Gamma, Helm, Johnson y Vlissides, «Design Patterns» (1994)](https://www.informit.com/store/design-patterns-elements-of-reusable-object-oriented-9780201633610) — composición frente a herencia de clases; autoridad: los autores (Addison-Wesley).
- [Python: «The Python 2.3 Method Resolution Order»](https://docs.python.org/3/howto/mro.html) — linealización de bases en Python; autoridad: documentación de Python.
- [Fowler, «Replace Superclass with Delegate»](https://refactoring.com/catalog/replaceSuperclassWithDelegate.html) — paso de herencia a delegación; autoridad: Martin Fowler.
- [Fowler, «Replace Subclass with Delegate»](https://refactoring.com/catalog/replaceSubclassWithDelegate.html) — subclases sustituidas por un colaborador; autoridad: Martin Fowler.
- [Liskov y Wing (1994)](https://doi.org/10.1145/197320.197383) — subtipos que preservan el comportamiento; autoridad: ACM TOPLAS.

---

[↑ Glosario](../../README.md) · [← Orden de foco](./orden-de-foco.md) · [Orden e iteración →](./orden-e-iteracion.md)
