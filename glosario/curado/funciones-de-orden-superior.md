# Funciones de orden superior

## Definición

Una **función de orden superior** es una función que **recibe otras funciones como argumento o las devuelve como resultado**. En `SE-076`, el uso central es **pasar una regla como valor**: en lugar de escribir condicionales que decidan qué regla aplicar, se entrega la regla como argumento y se **parametriza la evaluación**. `map`, `filter` y `reduce` son los ejemplos clásicos: reciben una función y la aplican a una colección. Es un concepto de la programación funcional, pero está presente en la mayoría de los lenguajes modernos.

## Por qué importa

Muchas variaciones de un procedimiento no cambian su estructura, solo un criterio: qué se filtra, cómo se ordena, qué regla se evalúa. Sin funciones como valores, cada variante exige una copia del procedimiento o una cadena de condicionales globales que crece con cada caso. La decisión que cambia es dónde vive la parte variable: como un argumento que el llamador elige, y no como una rama dentro del procedimiento. Así se agregan reglas sin tocar el código que las ejecuta.

## Cómo funciona

El mecanismo es que las funciones son **valores** de primera clase: se guardan en variables, estructuras de datos y se pasan por parámetro. Con eso:

- **`map(f, xs)`** aplica `f` a cada elemento; **`filter(p, xs)`** conserva los que cumplen `p`; **`reduce(g, xs)`** combina los elementos con `g`.
- Una función puede **construir** otra: recibe un parámetro y devuelve una función que lo recuerda (un **cierre**, que captura variables del entorno donde se creó).
- Se pueden **componer** funciones pequeñas en una transformación mayor.

`SE-076` marca dos precauciones. Una cadena larga de `map`/`filter`/`reduce` puede **ocultar orden, errores o complejidad**: cuántas pasadas se hacen, en qué orden, dónde falla. La forma debe servir al modelo, no demostrar virtuosismo sintáctico. Y los cierres tienen una trampa conocida: **capturan la variable, no su valor**.

## Ejemplo

Una regla se pasa como valor al evaluador:

```python
def evaluar(casos, regla):
    return [c for c in casos if regla(c)]

urgentes = evaluar(casos, lambda c: c["prioridad"] <= 2)
grandes  = evaluar(casos, lambda c: c["monto"] > 1000)
```

El síntoma que `SE-076` documenta es el siguiente: todas las funciones de una lista devuelven el **último** valor, porque el cierre captura la variable del bucle y no su valor en cada vuelta.

```python
fs = [lambda: i for i in range(3)]
[f() for f in fs]                 # [2, 2, 2], no [0, 1, 2]
fs = [lambda i=i: i for i in range(3)]       # captura por argumento por defecto
```

La corrección es capturar el valor con un argumento por defecto o con `functools.partial`.

## Errores y confusiones comunes

- **Cierres que capturan la variable del bucle.** Todas ven el último valor.
- **Cadenas excesivas.** Ocultan el orden de evaluación, dónde se produce un error y el costo real.
- **Creer que «inmutable» es automático.** Una tupla puede contener un objeto mutable que cambia (`SE-076`); se usan contenidos inmutables o se copia al construir.
- **Usar `reduce` cuando un bucle o una función con nombre es más claro.** La concisión no es el objetivo.

## Límites y cuándo no aplica

Pureza y composición no resuelven automáticamente interacción, latencia ni grandes flujos de datos (`SE-076`). Pasar funciones como argumento puede dificultar la depuración (trazas con funciones anónimas) y la serialización (no se pueden enviar sin más por red). Cuando solo hay dos variantes estables, un condicional simple es más directo que una abstracción por funciones.
