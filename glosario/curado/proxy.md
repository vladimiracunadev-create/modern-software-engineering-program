# Proxy

## Definición

Un **proxy** es un sustituto con la misma interfaz que controla el acceso al objeto real (`SE-315`). Es uno de los patrones estructurales: el cliente cree hablar con el objeto verdadero, pero el proxy decide si, cuándo y cómo el acceso llega. En `SE-280` aparece otra acepción, la de un **proxy de medición**: una medida sobre un sustituto accesible que muestra la forma de un efecto sin su magnitud. Esta entrada trata el patrón.

## Por qué importa

Permite añadir control (carga diferida, permisos, acceso remoto) sin cambiar a los clientes. Y obliga a distinguirlo de patrones vecinos con los que comparte estructura. `SE-315` insiste en que la estructura es la misma para varios y lo que los separa es la intención; confundirla produce una prueba equivocada.

## Cómo funciona

Los cinco patrones de `SE-315` comparten una estructura: un objeto que **contiene o envuelve** a otro. La intención diferencia:

- **Adapter:** cambia la interfaz a la que el cliente espera.
- **Facade:** ofrece una interfaz simple a un subsistema.
- **Proxy:** controla el acceso a un objeto con *su misma* interfaz (perezoso, remoto, con permisos).
- **Composite:** trata un grupo de objetos como uno solo.
- **Decorator:** añade comportamiento conservando la interfaz.

Proxy y Decorator pueden ser estructuralmente idénticos, y un mismo objeto puede ser ambos: el Decorator añade comportamiento (registro, reintento); el Proxy controla el acceso (perezoso, permisos, remoto). Cada intención tiene su propio modo de estropearse y su propia prueba: la del proxy perezoso es que el objeto real no se cree hasta el primer uso y que el resultado sea el mismo.

## Ejemplo

```python
class ImagenProxy:
    def __init__(self, ruta): self._ruta, self._real = ruta, None
    def mostrar(self):
        if self._real is None:          # carga diferida
            self._real = Imagen(self._ruta)
        return self._real.mostrar()
```

Un proxy de permisos haría lo análogo comprobando la identidad antes de delegar.

## Errores y confusiones comunes

- **Confundir proxy con Decorator.** La estructura es igual; lo que cambia es la intención (`SE-315`).
- **Proxy que cambia el resultado.** Si altera lo que devuelve, ya no es transparente para el cliente.
- **Confundirlo con un servidor proxy de red.** Comparte el nombre y la idea de intermediario, pero `SE-315` trata el patrón de objetos.

## Límites y cuándo no aplica

El proxy es adecuado cuando la construcción es cara y el uso es raro; si casi todos los objetos se usan, solo suma una indirección (`SE-315`). Un proxy remoto oculta la red, pero no sus fallos: latencia y errores parciales siguen existiendo y el cliente debe contemplarlos. Y el proxy de medición de `SE-280` es otra cosa: un indicador accesible que sustituye a uno inaccesible.
