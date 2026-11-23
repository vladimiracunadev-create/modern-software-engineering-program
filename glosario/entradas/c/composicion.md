# Composición

[↑ Glosario](../../README.md) · [← Componentes y alcanzabilidad](./componentes-y-alcanzabilidad.md) · [Composición frente a herencia →](./composicion-frente-a-herencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Diseño en que un objeto contiene a otros y los usa para cumplir su trabajo.

Definición de trabajo de [SE-303 — Composición, herencia y delegación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-052 — Invariantes, precondiciones y poscondiciones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md): Encadenamiento donde garantías alimentan requisitos.

## Por qué importa

En [SE-303 — Composición, herencia y delegación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md), el tema «Composición y delegación» importa porque dependen solo de lo prometido y obligan a escribir el reenvío.

## Cómo funciona

Según [SE-303 — Composición, herencia y delegación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md):

En composición, el objeto contiene a otro y le reenvía lo que necesita (delegación). Depende solo de lo que el contenido promete en su interfaz. Cuesta escribir el reenvío y decidir qué parte de la interfaz se expone. Gana en dos cosas: la implementación interna puede cambiar sin que lo note quien contiene, y el contenido se puede sustituir en ejecución (un doble de prueba, otra estrategia).

Según [SE-303 — Composición, herencia y delegación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md):

El equipo decide opción por opción. `Fragil`, `Seguro`, `Urgente` y `Refrigerado` se vuelven decoradores de un `CalculadoraEnvio` con la interfaz `costo(envio)`, y el orden se fija por una regla escrita: primero los recargos fijos, después los porcentuales. Una prueba recorre los 24 órdenes y comprueba que solo el orden de la regla es válido. La colección contadora se reescribe por composición. Se deja la herencia para `EnvioInternacional(Envio)`, que sí es un «es un» sustituible, vive en el mismo paquete y comparte el contrato de `SE-302`.

## Ejemplo

Ejemplo de [SE-303 — Composición, herencia y delegación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md) (sección «Ejemplo profesional»):

El equipo decide opción por opción. `Fragil`, `Seguro`, `Urgente` y `Refrigerado` se vuelven decoradores de un `CalculadoraEnvio` con la interfaz `costo(envio)`, y el orden se fija por una regla escrita: primero los recargos fijos, después los porcentuales. Una prueba recorre los 24 órdenes y comprueba que solo el orden de la regla es válido. La colección contadora se reescribe por composición. Se deja la herencia para `EnvioInternacional(Envio)`, que sí es un «es un» sustituible, vive en el mismo paquete y comparte el contrato de `SE-302`.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **`TypeError` al definir una clase con varias bases** — causa: orden de resolución inconsistente. Corrección: revisar el orden de las bases o reducir a una base con composición. ([SE-303](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La composición con decoradores crece como n, pero introduce el **orden** como parte del diseño: un recargo fijo antes de un porcentaje no da lo mismo que después. ([SE-303](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md))
- «Favorecer» la composición es una inclinación por defecto, no una regla. ([SE-303](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Garantía](../g/garantia.md), [Objeto](../o/objeto.md), [Trabajo](../t/trabajo.md), [Clase base frágil](./clase-base-fragil.md), [Delegación](../d/delegacion.md), [Dominio](../d/dominio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-052 — Invariantes, precondiciones y poscondiciones](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-303 — Composición, herencia y delegación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

**También se usa en** (45 clases más lo mencionan; las que más):

[SE-076](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md), [SE-075](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md), [SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md), [SE-539](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-539-taller-conducir-una-revision-de-decision-dificil/README.md), [SE-029](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-029-terminales-shells-y-composicion-de-comandos/README.md), [SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md), [SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md), [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md).

**Aparece en los casos de estudio:** [Caída global de Meta](../../../casos/fallo/meta-2021.md).

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

[↑ Glosario](../../README.md) · [← Componentes y alcanzabilidad](./componentes-y-alcanzabilidad.md) · [Composición frente a herencia →](./composicion-frente-a-herencia.md)
