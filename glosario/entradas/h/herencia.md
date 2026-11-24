# Herencia

[↑ Glosario](../../README.md) · [← Heisenbug y costo de pausa](./heisenbug-y-costo-de-pausa.md) · [Herencia de prioridad →](./herencia-de-prioridad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

La **herencia** es el mecanismo por el que una clase reutiliza la implementación y la interfaz de otra y puede sustituirla ([SE-303](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md)). Hace que la subclase *sea* su base. Es una forma de reutilización de código y de polimorfismo, no la única: la composición es la alternativa que el programa contrasta.

## Por qué importa

Es la forma más corta de compartir código y, a cambio, la más intrusiva ([SE-303](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md)): la subclase ve los métodos protegidos, el orden en que la base llama a sus propios métodos y los atributos. Eso acopla a la subclase con detalles internos de la base: cambia una decisión de diseño frecuente, la de «heredo o compongo».

## Cómo funciona

La subclase hereda atributos y métodos y puede sobrescribirlos. La causa de los problemas es que sobrescribir un método supone saber cómo lo usa la base. [SE-303](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md) muestra el caso: una subclase de un contenedor cuenta elementos sobrescribiendo `agregar` y `agregar_todos`; con la base V1, `agregar_todos` llama internamente a `agregar`, así que cada elemento se cuenta dos veces. La herencia falla siempre con esa base, incluso con lotes de un solo elemento. Si la base cambia un detalle interno, la subclase se rompe sin que nadie la toque (clase base frágil).

Funciona bien cuando se cumplen tres condiciones: la relación es de verdad «es un» (sustituible, [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md)), la base está pensada para extenderse y ambas evolucionan juntas, por ejemplo dentro del mismo paquete y con las mismas personas.

## Ejemplo

```python
class Contador(Lista):
    def agregar(self, x): self.n += 1; super().agregar(x)
    def agregar_todos(self, xs): self.n += len(xs); super().agregar_todos(xs)   # base llama a agregar: cuenta doble
```

La alternativa de [SE-303](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md): componer y reenviar solo lo prometido, de modo que la clase envuelva a la lista y no dependa de sus llamadas internas.

## Errores y confusiones comunes

- **Un contador cuenta doble tras un cambio interno de la base.** Causa: herencia que sobrescribe métodos que la base también usa; corrección: componer y reenviar solo lo prometido ([SE-303](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md)).
- **Cada nueva opción duplica las subclases.** Causa: herencia por combinación; corrección: componer con decoradores o una lista de recargos ([SE-303](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md)).
- **Heredar solo para reutilizar código.** Si no es «es un», la sustituibilidad falla.

## Límites y cuándo no aplica

No conviene entre clases de módulos distintos que evolucionan por separado ni cuando la base no documenta cómo se extiende. En lenguajes con herencia múltiple, el orden de resolución añade complejidad. El ejemplo de [SE-303](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md) es una construcción didáctica, no una medición sobre proyectos reales.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-030](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-030-powershell-bash-y-portabilidad-de-scripts/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Interfaz](../i/interfaz.md), [Mecanismo](../m/mecanismo.md), [Clase base frágil](../c/clase-base-fragil.md), [Composición](../c/composicion.md), [Configuración efectiva](../c/configuracion-efectiva.md), [Delegación](../d/delegacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-031 — Variables de entorno, configuración y secretos](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-031-variables-de-entorno-configuracion-y-secretos/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-303 — Composición, herencia y delegación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

**También se usa en** (12 clases más lo mencionan; las que más):

[SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md), [SE-075](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md), [SE-451](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md), [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md), [SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md), [SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md), [SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md), [SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Gamma, Helm, Johnson y Vlissides, «Design Patterns» (1994)](https://www.informit.com/store/design-patterns-elements-of-reusable-object-oriented-9780201633610) — composición frente a herencia de clases; autoridad: los autores (Addison-Wesley).
- [Fowler, «Replace Superclass with Delegate»](https://refactoring.com/catalog/replaceSuperclassWithDelegate.html) — paso de herencia a delegación; autoridad: Martin Fowler.
- [Python: «The Python 2.3 Method Resolution Order»](https://docs.python.org/3/howto/mro.html) — linealización de bases en Python; autoridad: documentación de Python.
- [Fowler, «Replace Subclass with Delegate»](https://refactoring.com/catalog/replaceSubclassWithDelegate.html) — subclases sustituidas por un colaborador; autoridad: Martin Fowler.
- [Liskov y Wing (1994)](https://doi.org/10.1145/197320.197383) — subtipos que preservan el comportamiento; autoridad: ACM TOPLAS.

---

[↑ Glosario](../../README.md) · [← Heisenbug y costo de pausa](./heisenbug-y-costo-de-pausa.md) · [Herencia de prioridad →](./herencia-de-prioridad.md)
