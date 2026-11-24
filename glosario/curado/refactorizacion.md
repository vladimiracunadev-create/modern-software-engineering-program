# Refactorización

## Definición

La **refactorización** es un **cambio de la estructura interna del código que no altera su comportamiento observable** (`SE-070`, `SE-307`). Martin Fowler la define así y la apoya en pruebas que comprueban que el comportamiento se conserva (`SE-559`). Dos palabras son decisivas: *estructura interna*, porque lo que cambia es cómo está organizado el código (nombres, funciones, clases), y *observable*, porque lo que debe permanecer es lo que perciben quienes lo usan (resultados, errores, efectos). Un cambio que corrige un defecto o añade una función **no es** una refactorización, aunque se haga en el mismo archivo.

## Por qué importa

El código que se entiende mal se cambia con miedo y se rompe con facilidad. Refactorizar es la forma de pagar deuda técnica de manera segura: se mejora la legibilidad y la estructura para que el próximo cambio sea barato. La decisión que cambia es cómo se organiza el trabajo: **un cambio por propósito**. Si una refactorización y un arreglo van en el mismo cambio, no se puede saber, al aparecer un fallo, cuál de los dos lo causó; `SE-559` lo documenta como error frecuente y su corrección es un cambio por propósito, cada uno con su revisión.

## Cómo funciona

La seguridad de una refactorización descansa en tres prácticas:

- **Pasos pequeños.** Cada paso (renombrar, extraer una función, mover un método) es tan pequeño que, si algo se rompe, la causa se localiza en el último.
- **Pruebas que fijan el comportamiento antes.** Cuando no hay pruebas, se escriben **pruebas de caracterización** (`SE-519`) que registran lo que el código **hace**, no lo que debería hacer; sirven de red de seguridad.
- **Comparación diferencial.** La versión original y la refactorizada se ejecutan sobre muchas entradas, incluidas las fronteras, y se comparan los resultados.

Con asistentes automáticos, `SE-559` advierte de que la parte que se pierde es la **comprobación**: el asistente devuelve una versión más corta o más clara con total seguridad y el comportamiento puede haber cambiado en un caso (el orden, un valor límite, una nota igual a cero). «Parece igual» no es «se comprobó». Por eso la clase propone un procedimiento verificable: comparación diferencial con miles de entradas generadas con fronteras, ejecución de pruebas de caracterización y un *diff* acotado, sin cambios de estilo mezclados.

## Ejemplo

Un cálculo con una condición anidada se refactoriza extrayendo una función, sin cambiar su resultado:

```python
# antes
def total(items):
    t = 0
    for i in items:
        if i["activo"] and i["precio"] > 0:
            t += i["precio"] * i["cantidad"]
    return t

# después (misma conducta, mejor estructura)
def _vale(item): return item["activo"] and item["precio"] > 0
def total(items):
    return sum(i["precio"] * i["cantidad"] for i in items if _vale(i))

# comprobación diferencial
for caso in generar_casos(5000):
    assert total_antes(caso) == total_despues(caso)
```

El generador incluye listas vacías, precios cero y cantidades extremas, que son los lugares donde las refactorizaciones suelen cambiar la conducta.

## Errores y confusiones comunes

- **Mezclar refactorización y arreglo.** Se pierde la capacidad de localizar la causa de un fallo.
- **Comprobar solo con ejemplos.** La refactorización cambia el orden o un valor límite sin que nadie lo note; se usa comparación diferencial con generador enriquecido.
- **Llamar refactorización a cualquier reescritura.** Si cambia el comportamiento, es otra cosa.
- **Confiar en la pulcritud de la salida de un asistente.** Hay que comprobar.

## Límites y cuándo no aplica

Las pruebas de caracterización fijan lo que el código hace, incluidos sus errores: pueden consagrar un defecto (`SE-559`). La refactorización sin ninguna red de pruebas es una apuesta, y en código sin pruebas el primer paso es construirlas. Y si el comportamiento observable incluye rendimiento o uso de memoria, «no cambia el comportamiento» exige medirlos también; una estructura distinta puede cambiar el costo sin cambiar el resultado.
