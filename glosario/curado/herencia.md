# Herencia

## Definición

La **herencia** es el mecanismo por el que una clase reutiliza la implementación y la interfaz de otra y puede sustituirla (`SE-303`). Hace que la subclase *sea* su base. Es una forma de reutilización de código y de polimorfismo, no la única: la composición es la alternativa que el programa contrasta.

## Por qué importa

Es la forma más corta de compartir código y, a cambio, la más intrusiva (`SE-303`): la subclase ve los métodos protegidos, el orden en que la base llama a sus propios métodos y los atributos. Eso acopla a la subclase con detalles internos de la base: cambia una decisión de diseño frecuente, la de «heredo o compongo».

## Cómo funciona

La subclase hereda atributos y métodos y puede sobrescribirlos. La causa de los problemas es que sobrescribir un método supone saber cómo lo usa la base. `SE-303` muestra el caso: una subclase de un contenedor cuenta elementos sobrescribiendo `agregar` y `agregar_todos`; con la base V1, `agregar_todos` llama internamente a `agregar`, así que cada elemento se cuenta dos veces. La herencia falla siempre con esa base, incluso con lotes de un solo elemento. Si la base cambia un detalle interno, la subclase se rompe sin que nadie la toque (clase base frágil).

Funciona bien cuando se cumplen tres condiciones: la relación es de verdad «es un» (sustituible, `SE-302`), la base está pensada para extenderse y ambas evolucionan juntas, por ejemplo dentro del mismo paquete y con las mismas personas.

## Ejemplo

```python
class Contador(Lista):
    def agregar(self, x): self.n += 1; super().agregar(x)
    def agregar_todos(self, xs): self.n += len(xs); super().agregar_todos(xs)   # base llama a agregar: cuenta doble
```

La alternativa de `SE-303`: componer y reenviar solo lo prometido, de modo que la clase envuelva a la lista y no dependa de sus llamadas internas.

## Errores y confusiones comunes

- **Un contador cuenta doble tras un cambio interno de la base.** Causa: herencia que sobrescribe métodos que la base también usa; corrección: componer y reenviar solo lo prometido (`SE-303`).
- **Cada nueva opción duplica las subclases.** Causa: herencia por combinación; corrección: componer con decoradores o una lista de recargos (`SE-303`).
- **Heredar solo para reutilizar código.** Si no es «es un», la sustituibilidad falla.

## Límites y cuándo no aplica

No conviene entre clases de módulos distintos que evolucionan por separado ni cuando la base no documenta cómo se extiende. En lenguajes con herencia múltiple, el orden de resolución añade complejidad. El ejemplo de `SE-303` es una construcción didáctica, no una medición sobre proyectos reales.
