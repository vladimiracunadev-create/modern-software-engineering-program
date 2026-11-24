# Punto de extensión

## Definición

Un **punto de extensión** es un lugar declarado de un sistema donde se pueden **añadir variantes o complementos sin editar el código existente**. El programa lo define de tres maneras que coinciden: `SE-115` lo describe como una interfaz con ciclo de vida, errores y compatibilidad definidos; `SE-302`, como el lugar donde se pueden añadir variantes sin editar el código existente (la idea de «abierto a la extensión» de SOLID); `SE-338`, como el lugar declarado donde un complemento puede engancharse. Lo esencial es que está **declarado**: el sistema promete aceptar extensiones allí y en ningún otro sitio.

## Por qué importa

Una cadena de condicionales que crece con cada regla nueva obliga a reabrir la misma función cada vez, con el riesgo de romper lo existente. Un punto de extensión mueve esa variabilidad a un lugar estable. `SE-302` documenta el síntoma: cada regla nueva reabre la misma función por una cadena de condicionales sin punto de extensión; la corrección es registrar reglas y escribir la política de combinación en un solo sitio. La decisión que cambia es dónde se paga el costo de añadir una variante: con el punto de extensión, en el archivo nuevo; sin él, en el núcleo.

## Cómo funciona

Un punto de extensión define cuatro cosas (`SE-115`):

- **Interfaz:** qué debe ofrecer un complemento (qué funciones, qué datos).
- **Ciclo de vida:** cuándo se crea, se activa, se usa y se cierra.
- **Errores:** qué ocurre si el complemento falla o lanza una excepción, sin derribar al anfitrión.
- **Compatibilidad:** qué versión del contrato soporta cada complemento y cuál es la política de cambios.

Es **más estrecho que exponer los internos**: en lugar de dejar que los complementos modifiquen cualquier parte del sistema, se les da una superficie pequeña y estable. Esa estrechez es lo que permite evolucionar el sistema sin romper complementos. `SE-115` advierte que los *hooks* (ganchos) **sin orden o reentrancia documentada producen interacciones invisibles entre plugins**: si dos complementos se enganchan al mismo evento, el orden en que se ejecutan y si uno puede disparar al otro cambian el resultado, y nadie lo sabe.

## Ejemplo

El SDK del programa expone `choose_next` y un punto de extensión para reglas de prioridad. Un registro de reglas:

```python
REGLAS = []

def regla(f):
    REGLAS.append(f)          # punto de extensión: registrar una regla
    return f

def combinar(casos):          # política de combinación: un solo sitio
    puntaje = {c["id"]: 0 for c in casos}
    for r in REGLAS:
        for c in casos:
            puntaje[c["id"]] += r(c)
    return max(casos, key=lambda c: puntaje[c["id"]])
```

Añadir una regla de descuento no toca `combinar`. `SE-302` agrega la salvedad: para «añadir una regla» se puede cerrar el cálculo detrás de este punto, pero para «cambiar cómo se combinan las reglas» ese mismo punto no ayuda: la extensión protege solo contra la variación que se previó.

## Errores y confusiones comunes

- **Exponer internos como si fueran un punto de extensión.** Cualquier cambio posterior rompe complementos.
- **Ganchos sin orden documentado.** Interacciones impredecibles entre plugins.
- **Sin manejo de errores.** Un complemento roto derriba al anfitrión.
- **Prever la extensión equivocada.** El punto no ayuda con la variación que no anticipó.

## Límites y cuándo no aplica

Con dos o tres variantes previsibles y un solo equipo, un condicional o una interfaz con implementaciones en el mismo repositorio es más simple que un mecanismo de extensión (`SE-338`). Cada punto de extensión es una API pública que hay que mantener, documentar y versionar. Si nadie ajeno va a extender el sistema, es complejidad sin retorno.
