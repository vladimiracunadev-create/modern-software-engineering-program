# Reducción por dimensiones

## Definición

La **reducción por dimensiones** es la técnica de `SE-105` para obtener un **caso mínimo** de un fallo: se minimizan **por separado** los **datos, el código, la configuración, el tiempo y el entorno**. Cada una es una dimensión independiente sobre la que se puede quitar algo mientras se verifica que el fallo persista. El resultado es el artefacto más pequeño que aún reproduce el problema, útil para entenderlo, para comunicarlo y como base de la prueba de regresión. Se emparenta con el *delta debugging*.

## Por qué importa

Un fallo observado en producción o en un sistema grande viene envuelto en miles de líneas, datos voluminosos y configuración heredada. Diagnosticar ahí es lento y las explicaciones se pierden entre el ruido. Un caso mínimo hace visible la causa, es fácil de compartir y de automatizar como prueba. La decisión que cambia es qué se entrega al reportar un fallo: no «falla en producción», sino «falla con este archivo de 3 líneas, esta opción y esta versión». Además, `SE-105` señala que **el artefacto mínimo sigue explicando el dominio**: reducir no es destruir el sentido.

## Cómo funciona

El procedimiento recorre cada dimensión por separado:

- **Datos:** quitar registros o campos, partiendo la entrada por mitades, y comprobar si el fallo persiste.
- **Código:** quitar funciones, ramas y dependencias hasta que quede lo imprescindible.
- **Configuración:** devolver cada opción a su valor por defecto mientras el fallo siga.
- **Tiempo:** acortar esperas, repeticiones y la duración de la ejecución.
- **Entorno:** quitar variables, paquetes y servicios.

Quitar **la mitad** y conservar el fallo acelera la búsqueda de forma logarítmica. Pero hay dependencias entre elementos: quitar dos cosas por separado puede conservar el fallo y quitarlas juntas hacerlo desaparecer. Por eso, **cada paso se vuelve a comprobar**. Dos síntomas documentados en la clase: la reducción devuelve resultados distintos porque la prueba es intermitente (se repite cada decisión y se fijan las semillas), y la bisección de *commits* señala un *commit* inocente porque hay dos defectos o una prueba inestable (se estabiliza la prueba y se comprueba el *commit* señalado).

## Ejemplo

Un procesamiento falla con un archivo de 50 000 filas. Reducción por datos, por mitades (el *delta debugging* completo también prueba los complementos y trozos más finos):

```python
def falla(filas):                      # True si reproduce el fallo
    return procesar(filas) == "ERROR"

def reducir(filas):                    # versión mínima: solo prueba cada mitad
    avanzo = True
    while avanzo and len(filas) > 1:
        avanzo = False
        mitad = len(filas) // 2
        for candidato in (filas[:mitad], filas[mitad:]):
            if falla(candidato):        # el fallo persiste con solo esa mitad
                filas, avanzo = candidato, True
                break
    return filas
```

Si tras reducir queda un puñado de filas, la causa se vuelve visible (por ejemplo, una fecha sin zona horaria en una de ellas). Esa entrada pequeña se convierte en la prueba de regresión, con los datos sintéticos.

## Errores y confusiones comunes

- **Reducir una sola dimensión.** Un fallo puede depender de la configuración y no de los datos.
- **No repetir cada comprobación.** Las dependencias entre elementos o la intermitencia engañan.
- **Reducir hasta perder el sentido.** El caso mínimo debe seguir explicando el dominio.
- **Reducir sin reproducir primero.** Sin fallo determinista, la reducción no converge.

## Límites y cuándo no aplica

El caso mínimo aún debe poder ejecutarlo otra persona con modalidades distintas (`SE-105`): un fallo que depende del hardware, del tráfico o de la concurrencia puede no reducirse a un archivo. Para fallos intermitentes sin forma de volverlos deterministas, la reducción no converge. Si el fallo ya es evidente y pequeño, reducir más es esfuerzo innecesario.
