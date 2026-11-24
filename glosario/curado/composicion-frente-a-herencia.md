# Composición frente a herencia

## Definición

**Composición frente a herencia** es el criterio de diseño que `SE-075` formula así: la **herencia** reutiliza un contrato y un comportamiento bajo una relación de **sustitución** (un subtipo puede usarse donde se espera el tipo base), mientras que la **composición** ensambla **colaboradores**: un objeto contiene a otros y les delega trabajo. No dice «nunca heredar»: dice que heredar solo para compartir código es una mala razón, y que la herencia queda reservada para tipos realmente sustituibles.

## Por qué importa

Quien hereda se acopla a la clase base: a sus métodos protegidos, a su orden de inicialización y a cualquier cambio futuro. Una jerarquía profunda hace que modificar la base afecte a todos sus descendientes, y que entender un método obligue a leer varios niveles. La composición mueve esa dependencia a una interfaz estrecha. La decisión que cambia es cómo se reutiliza código: en lugar de «extiendo la clase que ya hace algo parecido», se pregunta «¿es esto realmente un caso del tipo base, o solo quiero usar su código?».

## Cómo funciona

La prueba de herencia es de **sustitución**: si en cualquier lugar que usa el tipo base se puede poner el subtipo sin que cambie lo que el código espera, la herencia expresa una relación verdadera. Si el subtipo debe rechazar operaciones de la base, o cambiarle el significado, no es sustituible y la herencia miente.

La composición, en cambio, permite:

- **Cambiar el colaborador en ejecución** o por configuración (una política distinta, un repositorio distinto), cosa que una jerarquía fija en compilación.
- **Combinar capacidades** sin explosión de subclases: tres comportamientos independientes son tres colaboradores, no ocho subclases.
- **Probar por separado**, sustituyendo cada colaborador por un doble.

El motor de reglas comparado de `SE-075` hace esto: **compone políticas y repositorios** y reserva la herencia para tipos sustituibles. Un coste de la herencia múltiple, que `SE-075` ilustra, es el orden de resolución: llamar `A.m(self)` en lugar de `super().m()` ejecuta un método de la base dos veces o nunca en un diamante.

## Ejemplo

Se necesita que un servicio de recomendación aplique una política y guarde resultados. Con herencia, se crea `ServicioConPoliticaYRepositorio` extendiendo clases que ya hacen partes de esto. Con composición:

```python
class Servicio:
    def __init__(self, politica, repositorio):
        self.politica = politica
        self.repositorio = repositorio

    def recomendar(self, caso):
        r = self.politica.evaluar(caso)
        self.repositorio.guardar(caso, r)
        return r
```

Cambiar la política o el repositorio no toca `Servicio`. La herencia sigue siendo válida para algo como `ReglaPorUmbral(Regla)` si cualquier `Regla` se puede sustituir por ella sin sorpresas.

## Errores y confusiones comunes

- **Heredar para ahorrar líneas.** Crea acoplamiento a detalles internos de la base y jerarquías frágiles.
- **Creer que composición es «no usar clases base».** Las interfaces o clases abstractas pueden seguir existiendo; lo que cambia es que la reutilización ocurre por delegación.
- **`A.m(self)` en lugar de `super().m()`.** En herencia múltiple, el método de la base se ejecuta dos veces o nunca; hay que usar `super()` en todas las clases del diamante (`SE-075`).
- **Confiar en la privacidad por convención.** Un atributo con guion bajo no impide asignarle un valor inválido; hay que validar en el método que escribe o usar una propiedad con setter.

## Límites y cuándo no aplica

Los objetos reducen estados inválidos solo si sus fronteras son reales (`SE-075`). La composición no es gratuita: añade indirección y a veces obliga a escribir métodos que solo delegan. Cuando la relación es genuinamente «es un» con sustitución completa y estable, la herencia es más simple y legítima. En lenguajes con interfaces o rasgos, parte de la discusión se resuelve distinto, y en el estilo funcional, la reutilización se hace componiendo funciones y no objetos.
